#chatbot com ia localmente 

from langchain_community.chat_models import ChatOllama

#criar um modelo de ia llama 3 
chat= ChatOllama(
    model="llama3.1:8b",
    
    temperature=0)

#função para interagir com o chatbot
def conversar_com_chatbot(pergunta):
    resposta = chat.invoke([
        ("system", "você é um assistente útil."), 
        ("human", pergunta)
    ])
    return resposta.content 

#loop do chatbot 
while True:
    pergunta = input("você: ")
    if pergunta.lower() == "sair" :
        print("encerrando o chatbot. até mais!")
        break
