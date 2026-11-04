#chatbot com ia 
import os
from langchain_groq import ChatGroq 

os.environ["GROQ_API_KEY"] = "GROQ_API_KEY" 

#criar um modelo de ia llama 3 
chat_model = ChatGroq(
    model="llama3.1-8b-istant",  
    temperature=0)  

#função para interagir com o chatbot
def conversar_com_chatbot(pergunta): 
    resposta = chat_model.chat([{"role": "user", "content": pergunta}]) 
    return resposta['content']
#exemplo de uso
if __name__ == "__main__":
    pergunta = "qual é a capital da frança?" 
    resposta = conversar_com_chatbot(pergunta) 
    print("chatbot:", resposta)