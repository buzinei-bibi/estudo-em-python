matriz=[]
for i in range(3):
    linha=[]
    for j in range(3):
        linha.append(int(input(f"digite o elemento [{i},{j}]: ")))
    matriz.append(linha)
print("matriz 3x3:")
for linha in matriz:
    print(linha)
soma=0
for i in range(3):
    for j in range(3):
        if i==j:
            soma+=matriz[i][j]
print(f"soma dos elementos da diagonal principal: {soma}")

#código para criar uma matriz 3x3, preencher com valores do usuário e calcular a soma da diagonal principal.