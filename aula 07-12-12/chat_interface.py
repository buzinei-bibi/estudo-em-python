# chatbot com IA

import os
import streamlit as st
from langchain_groq import ChatGroq 

# o comando from importa a biblioteca somente a parte necessariam pois se usar o import sem o from será importado tudo

os.environ["GROQ_API_KEY"] = "GROQ_API_KEY" 

# criar o modelo de IA Llama 3
chat = ChatGroq(
                model="llama-3.1-8b-instant",
                temperature=0
                , max_tokens=50
                )
#configurar a interface do Streamlit
st.set_page_config(page_title="Chatbot com IA", page_icon="👽", layout="centered")
st.title("Chatbot com IA Llama 3 via Groq e Streamlit",width="content")

st.write("digite sua mensagem para a buzina.")

# função para interagir com o chat bot
def conversar_com_chatbot(pergunta):
    resposta = chat.invoke([("system", "você é um assistente útil."), ("human", pergunta)])
    return resposta.content

#histórico de conversas
if "historico" not in st.session_state:
    st.session_state.historico = []

# exibir o histórico de conversas
for entrada, resposta in st.session_state.historico:
    st.markdown(f"**você:** {entrada}")
    st.markdown(f"**chatbot:** {resposta}")

# campo de entrada para o usuário
entrada_usuario = st.text_input("Digite sua pergunta:", key="input")
if st.button("Enviar"):
    if entrada_usuario:
        resposta_chatbot = conversar_com_chatbot(entrada_usuario)
        st.session_state.historico.append((entrada_usuario, resposta_chatbot))
        st.rerun()