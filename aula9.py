
def printa_elementos(matriz): #matriz e somente uma referencia
    for i in range(len(matriz)): # neste caso ele pega a quantidade de listas (0,1,2)
        for j in range(len(matriz[i])): # se nao colocar o [0] ou [i] ele nao vai printar o ultimo elemento quando a quantidade de colunas for maior do que a de linhas
            print(f"matriz[{i}][{j}] = {matriz[i][j]}")
    return


#m1 = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
#printa_elementos(m1)


def mostra_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return

# ele vai repetir a quantidade de listas que tem dentro da matriz e vai printar a matriz nos seus i matriz[i] = [1,2,3,4]

#m1 = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
#mostra_matriz(m1)

def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        matriz.append([]) # adiciona uma nova linha para colocar os novos elementos
        for j in range(colunas):
            matriz[i].append(0) # vao ter mais de uma matriz e o i seria a matriz que esta sendo analisado
    return matriz

#Neste exemplo entede o porque i e para linhas e j e para colunas

#matriz1=cria_matriz(10,10)
#mostra_matriz(matriz1)

"""
matriz1 = cria_matriz(10,10)
for i in range(len(matriz1)):
    for j in range(len(matriz1[0])):
        if i%2==0:
            matriz1[i][j]=1 # aqui precisa ser [i][j] porque todos os 1 possuem a sua linha e a sua coluna
mostra_matriz(matriz1)
"""

# i sao as linhas da matriz e todos os elementos das linhas pares vao ser trocados por 1

"""
matriz2 = cria_matriz(10,10)
for i in range(len(matriz2)):
    for j in range(len(matriz2[0])):
        if j%2==0:
            matriz2[i][j]=2
mostra_matriz(matriz2)
"""

"""
m1=[[1,2,3,4], [5,6,7,8], [9,10,11,12]]
mostra_matriz(m1)
print()
m2=cria_matriz(3,4)
mostra_matriz(m2)
print()
"""

def soma_matriz(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]): # verifica se tem o mesmo numero de linhas e de colunas, m1[0] verifica a qtd de elementos da linha para ver a coluna
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                m1[i][j]+=m2[i][j]
        return m1
    else:
        print("impossível somar matrizes de tamanhos distintos!")
        return # se nao tiver esse return a funcao continuara executando mesmo apos a mensagem de erro, retornando none

#matriz1 = [[1,2,3], [4,5,6], [7,8,9]]
#matriz2 = [[10,20,30], [40,50,60], [70,80,90]]
#soma_matriz(matriz1, matriz2)
#mostra_matriz(matriz1)

"""
triangular = cria_matriz(5,5)
for i in range(len(triangular)):
    for j in range(len(triangular[0])):
        if i>j:
            triangular[i][j] = 1
mostra_matriz(triangular)
"""

"""
   j 0  1  2  3  4
i
0   [0, 0, 0, 0, 0]
1   [1, 0, 0, 0, 0]
2   [1, 1, 0, 0, 0]
3   [1, 1, 1, 0, 0]
4   [1, 1, 1, 1, 0]
"""

"""
xadrez = cria_matriz(8,8)
for i in range(len(xadrez)):
    for j in range(len(xadrez)):
        if i%2==0:
            if j%2==0:
                xadrez[i][j]=0
            else:
                xadrez[i][j]=1
        else:
            if j%2==0:
                xadrez[i][j]=1
            else:
                xadrez[i][j]=0
mostra_matriz(xadrez)
"""

# no xadrez as linhas pares as colunas pares e igual a 0 e as colunas impares e igual a 1 e nas linhas impares e ao contrario

#if j%2==i%2==0:
#   xadrez[i][j]=0
#else:
#   xadrez[i][j]=1

"""
i  j 0  1  2  3  4  5  6  7
0   [0, 1, 0, 1, 0, 1, 0, 1]
1   [1, 0, 1, 0, 1, 0, 1, 0]
2   [0, 1, 0, 1, 0, 1, 0, 1]
3   [1, 0, 1, 0, 1, 0, 1, 0]
4   [0, 1, 0, 1, 0, 1, 0, 1]
5   [1, 0, 1, 0, 1, 0, 1, 0]
6   [0, 1, 0, 1, 0, 1, 0, 1]
7   [1, 0, 1, 0, 1, 0, 1, 0]
"""

"""
matriz=[[1,2,3], [4,5,6], [7,8,9]]
mostra_matriz(matriz)
for i in range(len(matriz)):
    for j in range(i):
        aux=matriz[i][j]
        matriz[i][j]=matriz[j][i]
        matriz[j][i]=aux
mostra_matriz(matriz)
"""

# esse codigo troca as linhas com as colunas usando outra variavel para trocar
#a=1
#b=2
#c=a
#a=b
#b=c