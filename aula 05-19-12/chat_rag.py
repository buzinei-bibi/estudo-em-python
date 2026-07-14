#chat com rag (geração aumentada por recuperação)

# pip install langchain langchain-groq langachain-community pypdf faiss-cpu

import os
from langchain_groq import ChatGroq 

#loaders e vectorstores
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings 

#slitters atualizados
from langchain_text_splitters import RecursiveCharacterTextSplitter 

#cadeia de rag atualizada
from langchain_classic.chains.retrieval_qa.base import RetrievalQA  

#configurar a chave da groq
os.environ["GROQ_API_KEY"] = "GROQ_API_KEY" 

#criar um modelo de ia llama 3 

chat= ChatGroq(
    model="llama-3.1-8b-instant",
 temperature=0)

#carregar o documento pdf
loader = PyPDFLoader("documento.pdf")
pages = loader.load_and_split(
    RecursiveCharacterTextSplitter(chunk_size=1000,
                                   chunk_overlap=200)
) 

#criar embeddings e armazenar em faiss 
# embedding são vetores que representam o conteúdo dos documentos 
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(pages, embeddings) 
retriever = vectorstore.as_retriever() 

#criar a cadeia de rag 

rag_chain = RetrievalQA.from_chain_type(
    llm=chat,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

#função para interagir com o chatbot
def conversar_com_chatbot(pergunta):
    resposta = rag_chain.invoke ({"query": pergunta})
    return resposta["result"]

#loop do chatbot 
while True:
    pergunta = input("você: ")
    if pergunta.lower() == "sair" :
        print("encerrando o chatbot. até mais!")
        break

    resposta = conversar_com_chatbot(pergunta)
    print("chatbot:", resposta) 

    