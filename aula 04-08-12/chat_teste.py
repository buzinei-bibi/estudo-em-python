from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

# 1. configurar o modelo
# certifique-se de que o ollama esteja em execução e que o modelo "llama3.1:8b" esteja baixado.
# se você tiver outro modelo como "llama3:8b", use-o.
chat = ChatOllama(
    model="llama3.1:8b",
    temperature=0
)

# 2. função para interagir com o chatbot
def conversar_com_chatbot(pergunta: str) -> str:
    """
    invoca o modelo com a mensagem do sistema e a pergunta do usuário.
    """
    # é uma boa prática usar as classes específicas (systemmessage, humanmessage)
    # da LangChain para construir a lista de mensagens.
    mensagens = [
        SystemMessage(content="você é um assistente útil."),
        HumanMessage(content=pergunta)
    ]
    
    resposta = chat.invoke(mensagens)
    return resposta.content 

# 3. loop principal do chatbot
print("🤖 chatbot llama 3.1 iniciado. digite 'sair' para encerrar.")
print("---")

while True:
    pergunta = input("você: ")
    
    # condição de saída
    if pergunta.lower() == "sair":
        print("encerrando o chatbot. até mais!")
        break

    try:
        # chama a função para obter a resposta
        resposta = conversar_com_chatbot(pergunta)
        print("chatbot:", resposta)
    except Exception as e:
        # tratar erros, como se o ollama não estiver em execução
        print(f"❌ ocorreu um erro: {e}")
        print("verifique se o ollama está em execução e o modelo está disponível.")