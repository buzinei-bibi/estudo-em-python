#chatbot com ia 
import os
from langchain_groq import ChatGroq 

os.environ["GROQ_API_KEY"] = "GROQ_API_KEY" 

#criar um modelo de ia llama 3 
chat= ChatGroq(
    model="llama-3.1-8b-instant",
 temperature=0) 

# classificação de intenção, mas pode aplicar engenharia de contexto 
prompt= """classifique a intenção da frase com base nas áreas abaixo: 

1- suporte técnico
2- vendas
3- financeiro
4- recursos humanos
5- outros 
frase: {frase} 
""" 

#função para interagir com o chatbot
def conversar_com_chatbot(pergunta):
    resposta = chat.invoke([
        ("system", "você é um assistente que classifica intenção."), 
        ("human", prompt.format(frase=pergunta))
    ])
    return resposta.content 

#loop do chatbot 
while True:
    pergunta = input("você: ")
    if pergunta.lower() == "sair" :
        print("encerrando o chatbot. até mais!")
        break


    resposta = conversar_com_chatbot(pergunta)
    print("chatbot:", resposta) 


