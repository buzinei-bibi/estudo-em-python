import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, BaseMessage
from typing import List, Tuple, Optional, Callable

# --- configuração da API ---
# avariável de ambiente é definida aqui.
os.environ["GROQ_API_KEY"] = "GROQ_API_KEY"

# define o tipo para os handlers (métodos que retornam contexto e resposta)
IntentHandler = Callable[[str], Tuple[str, str]]

class ChatbotDeIntencao:
    """
    Chatbot que usa reflexão e histórico, sem usar if/else na lógica principal.
    """
    
    # --- configuração de intenções ---
    INTENCOES = {
        "1": "suporte técnico", "2": "vendas", "3": "financeiro",
        "4": "recursos humanos", "5": "outros" 
    }
    
    CLASSIFICACAO_PROMPT = """classifique a intenção da frase com base nas áreas abaixo e retorne APENAS o número da categoria.
    
    {categorias_formatadas}
    frase: {{frase}}
    """
    
    def __init__(self, model_name: str = "llama-3.1-8b-instant", temperature: float = 0):
        # o modelo é configurado para ser mais 'frio' (deterministic) na classificação de intenção
        self.chat = ChatGroq(model=model_name, temperature=temperature)
        self.historico: List[BaseMessage] = [] 
        self._formata_categorias()
        print(f"🤖 chatbot inicializado com modelo: {model_name}")

    def _formata_categorias(self):
        """Preenche o template do prompt de classificação."""
        categorias_str = "\n".join([f"{k}- {v}" for k, v in self.INTENCOES.items()])
        self.CLASSIFICACAO_PROMPT = self.CLASSIFICACAO_PROMPT.format(categorias_formatadas=categorias_str)

    def classificar_intencao(self, pergunta: str) -> str:
        """Invoca o modelo para obter APENAS o número da intenção."""
        # garante que a classificação use a entrada em minúsculas
        pergunta_lower = pergunta.lower()
        
        messages = [
            SystemMessage(content="você é um assistente que classifica intenção e retorna APENAS o número da categoria (1, 2, 3, 4 ou 5)."),
            HumanMessage(content=self.CLASSIFICACAO_PROMPT.format(frase=pergunta_lower))
        ]
        resposta = self.chat.invoke(messages)
        # O retorno da LLM é forçado a ser um número em str
        return resposta.content.strip()

    # --- Handlers de Intenção (Mantidos com contexto e resposta em minúsculas) ---
    def _handle_intent_1(self, pergunta: str) -> Tuple[str, str]:
        contexto = "você está atuando como um atendente de suporte técnico. sua tarefa é diagnosticar o problema."
        resposta = "obrigado por entrar em contato com nosso suporte técnico. qual é o problema que você está enfrentando?"
        return contexto.lower(), resposta.lower()

    def _handle_intent_2(self, pergunta: str) -> Tuple[str, str]:
        contexto = "você está atuando como um consultor de vendas. seu objetivo é recomendar produtos/serviços."
        resposta = "que ótimo que você está interessado(a) em nossos produtos! qual produto ou serviço despertou seu interesse?"
        return contexto.lower(), resposta.lower()
    
    def _handle_intent_3(self, pergunta: str) -> Tuple[str, str]:
        contexto = "você está atuando no setor financeiro. forneça informações precisas sobre faturas e pagamentos."
        resposta = "entendi, sua solicitação é sobre o financeiro. posso te ajudar com faturas, pagamentos ou informações de conta?"
        return contexto.lower(), resposta.lower()
    
    def _handle_intent_4(self, pergunta: str) -> Tuple[str, str]:
        contexto = "você está atuando no setor de recursos humanos. direcione questões sobre vagas, benefícios ou informações internas."
        resposta = "seja bem-vindo(a) à área de recursos humanos. você gostaria de falar sobre vagas, benefícios, ou informações internas?"
        return contexto.lower(), resposta.lower()

    def _handle_intent_5(self, pergunta: str) -> Tuple[str, str]:
        contexto = "você é um assistente geral que precisa direcionar o usuário para a área correta."
        resposta = "certo, sua pergunta se encaixa em 'outros'. poderia me dar mais detalhes sobre o que precisa?"
        return contexto.lower(), resposta.lower()
    
    # --- HANDLER DE FALLBACK (Padrão) ---
    def _handle_intent_fallback(self, pergunta: str) -> Tuple[str, str]:
        """handler padrão para intenções inválidas ou não mapeadas."""
        contexto_sistema = ("você é um assistente que falhou em classificar a intenção. peça ao usuário para reformular o pedido.")
        resposta_inicial = "olá! não consegui classificar sua solicitação com precisão. por favor, reformule sua pergunta para que eu possa te ajudar melhor."
        return contexto_sistema.lower(), resposta_inicial.lower()

    def _tratar_primeira_interacao(self, pergunta: str, handler: IntentHandler) -> str:
        """método auxiliar que define o contexto e retorna a resposta inicial."""
        contexto_sistema, resposta_inicial = handler(pergunta)
        
        # 1. engenharia de contexto
        self.historico.append(SystemMessage(content=contexto_sistema))
        
        # 2. primeira pergunta e resposta inicial
        # armazena a pergunta do usuário em minúsculas
        pergunta_lower = pergunta.lower()
        self.historico.append(HumanMessage(content=pergunta_lower))
        self.historico.append(AIMessage(content=resposta_inicial))
        
        return resposta_inicial

    def _tratar_interacoes_seguintes(self, pergunta: str) -> str:
        """método auxiliar que continua a conversa com o histórico existente."""
        
        # adiciona a nova pergunta do usuário ao histórico (em minúsculas)
        pergunta_lower = pergunta.lower()
        self.historico.append(HumanMessage(content=pergunta_lower))
        
        # o modelo responde com base no histórico completo
        resposta = self.chat.invoke(self.historico)
        
        # armazena a resposta do modelo em minúsculas e adiciona ao histórico
        resposta_content_lower = resposta.content.lower()
        self.historico.append(AIMessage(content=resposta_content_lower))
        
        return resposta_content_lower

    def conversar_com_chatbot(self, pergunta: str) -> str:
        """
        função principal limpa. despacha a lógica sem usar if/else.
        """
        
        # 1. se o histórico estiver vazio, classifique e use o handler para configurar o contexto.
        if not self.historico:
            # classifica a intenção
            codigo_intencao = self.classificar_intencao(pergunta)
            
            # reflexão: obtém o handler (com fallback garantido)
            handler_name = f"_handle_intent_{codigo_intencao}"
            handler = getattr(self, handler_name, self._handle_intent_fallback)
            
            # chama o método que trata a primeira interação
            return self._tratar_primeira_interacao(pergunta, handler)

        # 2. se o histórico não estiver vazio, trata a conversação contínua.
        return self._tratar_interacoes_seguintes(pergunta)
    
    def mostrar_historico(self):
        """imprime o histórico da conversa formatado."""
        print("\n*** histórico completo da conversa ***")
        for i, message in enumerate(self.historico):
            if isinstance(message, SystemMessage):
                print(f"[sistema]: {message.content}")
            elif isinstance(message, HumanMessage):
                print(f"[você]: {message.content}")
            elif isinstance(message, AIMessage):
                print(f"[chatbot]: {message.content}")
        print("************************************\n")


# --- loop principal do chatbot ---

bot = ChatbotDeIntencao()

print("\n🤖 chatbot de intenção (despacho com reflexão) ativado. digite 'sair' ou 'novo tópico'.")
print("💡 dica: sua primeira frase classifica a intenção e define o contexto da ia.")

while True:
    pergunta = input("\nvocê: ").lower() # converte a entrada do console para minúsculas
    
    if pergunta == "sair":
        bot.mostrar_historico() # imprime o histórico antes de sair
        print("🤖 encerrando o chatbot. até mais!")
        break
    
    if pergunta == "novo tópico":
        bot.historico = []
        print("\n--- contexto da conversa resetado. por favor, inicie um novo tópico. ---\n")
        continue

    resposta = bot.conversar_com_chatbot(pergunta)
    print("chatbot:", resposta)

    