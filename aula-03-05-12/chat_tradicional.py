#criação de um chat tradicional 

def responder(mensagem):
    mensagem_lower = mensagem.lower() 
    if "olá" in mensagem_lower or "oi" in mensagem_lower: 
        return "olá! como posso ajudar você hoje?" 
    elif "tchau" in mensagem_lower or "até logo" in mensagem_lower: 
        return "tchau! tenha um ótimo dia!" 
    else: 
        return "desculpe, não entendi sua mensagem. você pode reformular?" 

histórico = [] 
#estrutura de repetição 
while True: #loop infinito while - enquanto verdadadeiro
    msg_user = input("você: se quiser sair, digite 'sair', 'encerrar' ou 'tchau' . \n ")    

    if msg_user.lower() in ["sair", "encerrar", "tchau"]:  
        print("chat encerrado. até logo!") 
        break 

    histórico.append({"usuário": msg_user}) 
    resposta = responder(msg_user) 
    histórico.append({"chatbot": resposta}) 
    print("chatbot:",  resposta)   