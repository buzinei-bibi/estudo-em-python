# chatbot com ia
import os
from langchain_groq import ChatGroq

os.environ["GROQ_API_KEY"] = "GROQ_API_KEY"
# criar um modelo de ia llama 3
chat = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# classificação de intenção
CLASSIFICACAO_PROMPT = """classifique a intenção da frase com base nas áreas abaixo e retorne APENAS o número da categoria:

1- suporte técnico
2- vendas
3- financeiro
4- recursos humanos
5- futebol
5- outros
frase: {frase}
"""

# dicionário para mapear intenção e gerar resposta contextual
RESPOSTAS_CONTEXTUAIS = {
    "1": "obrigado por entrar em contato com nosso suporte técnico. para que eu possa te ajudar melhor, qual é o problema que você está enfrentando?",
    "2": "que ótimo que você está interessado(a) em nossos produtos! nossa equipe de vendas ficará feliz em te atender. qual produto ou serviço despertou seu interesse?",
    "3": "entendi, sua solicitação é sobre o financeiro. posso te ajudar com faturas, pagamentos ou informações de conta? por favor, detalhe sua necessidade.",
    "4": "seja bem-vindo(a) à área de recursos humanos. você gostaria de falar sobre vagas, benefícios, ou informações internas? estou à disposição para ajudar.",
    "5": "certo, sua pergunta se encaixa em 'outros'. para direcionar você corretamente, poderia me dar mais detalhes sobre o que precisa? obrigado pela sua paciência."
}

# --- função original (renomeada para o propósito de classificação) ---
def classificar_intencao(pergunta):
    """invoca o modelo para obter APENAS o número da intenção."""
    resposta = chat.invoke([
        ("system", "você é um assistente que classifica intenção e retorna APENAS o número."),
        ("human", CLASSIFICACAO_PROMPT.format(frase=pergunta))
    ])
    # tenta limpar e retornar apenas o dígito (ex: "1", "2")
    return resposta.content.strip()

# --- função ---
def conversar_com_chatbot(pergunta):
    """
    classifica a intenção e usa um dicionário para retornar uma resposta
    leve, educada e contextualizada.
    """
    # 1. classifica a intenção (retorna "1", "2", "3", etc.)
    codigo_intencao = classificar_intencao(pergunta)

    # 2. usa o dicionário para buscar a resposta contextual
    # .get() é usado para evitar erro se o código for inválido, retornando um valor padrão
    resposta_contextual = RESPOSTAS_CONTEXTUAIS.get(
        codigo_intencao,
        "olá! não consegui classificar sua solicitação com precisão ( por favor, reformule sua pergunta para que eu possa te ajudar melhor. agradeço a compreensão.".format(erro=codigo_intencao)
    )

    return resposta_contextual

# --- loop principal do chatbot ---
print("🤖 chatbot de intenção ativado. digite 'sair' para encerrar.")

while True:
    pergunta = input("\nVocê: ")
    if pergunta.lower() == "sair":
        print("🤖 encerrando o chatbot. até mais!")
        break

    resposta = conversar_com_chatbot(pergunta)
    print("chatbot:", resposta)

    