import os
import streamlit as st
from langchain_groq import ChatGroq

os.environ["GROQ_API_KEY"] = "GROQ_API_KEY" 


# ======================================================
# MODELO DE IA
# ======================================================
chat = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3,
    max_tokens=180
)

# ======================================================
# INTERFACE STREAMLIT
# ======================================================
st.set_page_config(
    page_title="chatbot de futebol ⚽",
    page_icon="⚽",
    layout="centered"
)

st.title("⚽ chatbot de futebol")
st.caption("especialista em futebol brasileiro e mundial")

# ======================================================
# SIDEBAR – CONFIGURAÇÕES
# ======================================================
st.sidebar.header("⚙️ configurações")

time_favorito = st.sidebar.text_input(
    "Seu time do coração",
    placeholder="ex: flamengo, são paulo, cruzeiro..."
)

modo_resposta = st.sidebar.radio(
    "modo de resposta",
    ["didático (explicativo)", "técnico (analista)"]
)

nivel_zoacao = st.sidebar.slider(
    "nível de zoação ⚽😄",
    0, 2, 1
)

# ======================================================
# FUNÇÃO DO CHATBOT
# ======================================================
def conversar_com_chatbot(pergunta: str) -> str:

    estilo = (
        "explique como se estivesse ensinando um iniciante."
        if "didático" in modo_resposta
        else "responda como um analista tático profissional."
    )

    torcedor = (
        f"você é levemente torcedor do {time_favorito}, "
        "mas sempre respeita os rivais."
        if time_favorito
        else "você é neutro em relação a clubes."
    )

    zoacao = [
        "seja totalmente respeitoso e neutro.",
        "use zoação leve e educada, sem ofensas.",
        "pode provocar de forma divertida e respeitosa."
    ][nivel_zoacao]

    prompt_sistema = f"""
você é um assistente especialista em futebol, educado, rápido e preciso.
foque principalmente em futebol brasileiro, mas conheça o futebol mundial.
{estilo}
{torcedor}
{zoacao}
evite respostas longas demais e seja claro.
"""

    resposta = chat.invoke([
        ("system", prompt_sistema),
        ("human", pergunta)
    ])

    return resposta.content

# ======================================================
# HISTÓRICO DE CONVERSAS
# ======================================================
if "historico" not in st.session_state:
    st.session_state.historico = []

for pergunta, resposta in st.session_state.historico:
    with st.chat_message("user"):
        st.write(pergunta)
    with st.chat_message("assistant"):
        st.write(resposta)

# ======================================================
# ENTRADA AUTOMÁTICA (RESPONDE SOZINHO)
# ======================================================
pergunta_usuario = st.chat_input("digite sua pergunta sobre futebol ⚽")

if pergunta_usuario:
    resposta = conversar_com_chatbot(pergunta_usuario)
    st.session_state.historico.append(
        (pergunta_usuario, resposta)
    )
    st.rerun()
