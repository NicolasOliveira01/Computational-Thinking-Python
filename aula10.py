import random

def printa_elemento(matriz):
    for i in range(len(matriz)): # o len matriz neste caso é 3, porque tem 3 listas dentre da matriz
        for j in range(len(matriz[0])):
            print(f"matriz[{i}][{j}] = {matriz[i][j]}")
    return
# este caso ele pega todos as linhas e todas as as colunas da matriz e mostra todos os elementos dentros das listas

#matriz é uma lista dentro de listas

#m = [[1,2,3], [4,5,6], [7,8,9]]
#printa_elemento(m)


def printa_elemento_i(matriz):
    for i in matriz:
        print(i)
    return

#m = [[1,2,3], [4,5,6], [7,8,9]]
#printa_elemento_i(m)

# o range e muito usado no for pois ele tem o comeco, no fim e por quanto ele vai percorrer esse comeco e fim
# range(5) -> 0,1,2,3,4
# len e usado para pegar o comprimento de alguma coisa
# len nao comeca com 0 porem o range comeca com 0
# for i in matriz -> i vai percorrer todos os elementos da matriz


def mostra_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return

#m = [[1,2,3], [4,5,6], [7,8,9]]
#mostra_matriz(m)

# esse codigo vai percorrer os elementos da lista e no fim vai printar eles
# for i in range(len(matriz) -> 0,1,2
# 0 -> [1,2,3] 1 -> [4,5,6] 2 -> [7,8,9]

def cria_matriz(colunas, linhas):
    matriz=[]
    for i in range(linhas):
        matriz.append([]) # cria as listas da matriz
        for j in range(colunas):
            matriz[i].append(random.randint(0, 9)) # colocar o [j] neste caso n vai funcionar pois o matriz.append([]) esta vazio e nao possui colunas
    return matriz

# vai criar uma lista vazia e vai percorrer a quantidade de linhas

#m = cria_matriz(10, 10)
#mostra_matriz(m)

linhas=10
colunas=10
matriz = cria_matriz(linhas, colunas)
for i in range(linhas): # neste caso poderia usar o range(len(matriz)) e colocar o [0] no for do j
    for j in range(colunas):
        if i%2==0:
            matriz[i][j]=1
#mostra_matriz(matriz)

# vai percorrer as linhas e as colunas e se os indices das linhas forem pares vai colocar 1

matriz1=cria_matriz(10, 10)
for i in range(10):
    for j in range(10):
        if j%2==0:
            matriz1[i][j]=1
#mostra_matriz(matriz1)

xadrez=cria_matriz(8, 8)
for i in range(len(xadrez)):
    for j in range(len(xadrez[0])):
        if i%2==j%2:
            xadrez[i][j]=1
        else:
            xadrez[i][j]=0
#mostra_matriz(xadrez)

"""
alunos = 3
pesos = [1, 2, 3, 2, 1]
notas = cria_matriz(5, alunos)
soma_pesos = 9
media = []
mostra_matriz(notas)
print()

for j in range(len(notas)):
    soma = 0
    for i in range(len(pesos)):
        soma += pesos[i] * notas[j][i]  # Note a inversão de índices aqui
    media_aluno = soma / soma_pesos
    media.append(media_aluno)

print(media)
"""

materias=5
alunos=10
pesos = [1,2,3,2,1]
notas = cria_matriz(alunos,materias)
mostra_matriz(notas)
soma_pesos = 9
media = []
for j in range(len(notas[0])):
    soma = 0
    for i in range(len(pesos)):
        soma+=pesos[i]*notas[i][j]
    soma/=soma_pesos
    media.append(soma)
print(media)







