#faça um programa que verifique se uma letra digitada é "f" ou "m". 
# conforme a letra escrever: F - feminino, M - masculino, sexo inválido.

letra = input("digite uma letra (f/m): ")

if letra.lower() == "f":
    print("feminino")
elif letra.lower() == "m":
    print("masculino")
else:
    print("sexo inválido")
