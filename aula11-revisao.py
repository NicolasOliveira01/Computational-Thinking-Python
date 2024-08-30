#funcao para achar o maior numero
def acha_maior(lista):
    indice_maior=0
    maior=lista[0]
    for i in range(len(lista)):
        if lista[i]>maior:
            maior=lista[i]
            indice_maior=i
    return indice_maior

#exercicio usando a funcao acha_maior

carros=["1", "2", "3", "4", "5"]
precos=[200, 1, 50, 35, 750]
local_maior=acha_maior(precos)
print(f"O carro mais caro e o {carros[local_maior]} e ele custa {precos[local_maior]}")


# as variaveis que estao dentro da funcao so existem dentro da funcao
# acha_maior(precos) vai achar o indice_maior da lista de precos e esse indice vai estar na variavel local_maior
# {carros[local_maior]} e o elemento da lista carros com o indice do indice_maior da lista precos

# Achar o que tem em comum entre duas listas
def intersecao(lista1, lista2):
    comuns=[]
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i]==lista2[j]:
                comuns.append(lista1[i])
    return comuns

radial=["nicolas", "matheus", "guilherme", "henrique", "bruno"]
fiap=["nicolas", "guilherme", "joao", "tiago", "matheus"]
comum = intersecao(radial, fiap)
print(comum)


# um for para cada lista
# quando for fazer o append pode colocar tanto o lista1[i] quanto lista2[j] pois so entraram se forem iguais

# Como inverter valores

a=1
b=2
c=a
a=b
b=c

# declara a outra variavel como a no comeca para que no final essa variavel troque com o b

#Como inverter os elementos de uma lista
def inverte_lista(lista):
    ultimo=len(lista)-1
    for i in range(len(lista)//2):
        aux = lista[i]
        lista[i] = lista[ultimo-i]
        lista[ultimo-i] = aux
    return lista


numeros = [1, 2, 3, 4, 5, 6]
inverte_lista(numeros)
print(numeros)


# len() e usado para determinar o comprimento de alguma coisa
# lista[1,2,3,4,5] -> len(lista) = 5
# range() gera um sequencia de numero em um intervalo especifico
# range(inicio, fim, passo)
# for i in range(1, 6) -> 1 2 3 4 5
# range(len(lista)) -> índices para acessar cada elemento da lista iniciada por 0 (se a lista tiver 3 -> elem1:0 elem2:1 elem3:2)
# ultimo vai servir como indice, len(lista) vai pogar o tamanho da lista e vai subtrair 1 pois ultimo vai ser usado como indice
# o for vai ate a metade da lista (se for impar vai simplicar para o menor) i = 0 1 2

# Mostra os elementos de todas as listas da matriz

matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        #print(matriz[i][j])

# i itera atraves dos indices das linhas da matriz -> 0 1 2
# j itera atraves dos indices das colunas da matriz -> 0 1 2 3
# neste caso precisa do matriz[0] pois o numero de listas da matriz e diferentes do numero de colunas

# Como mostrar os elementos de uma matriz e mostrar qual a sua linha e a sua coluna
def printa_elementos(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f"matriz[{i}][{j}] = {matriz[i][j]}")
    return

m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
printa_elementos(m)

# i vai do 0 ate o numero de linhas -1
# j vai do 0 ate o numero de colunas -1

def mostra_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return

m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
mostra_matriz(m)


#Como criar matriz determinando o numero de linhas e colunas
def cria_matriz(linhas, colunas):
    matriz=[]
    for i in range(linhas):
        matriz.append([])
        for j in range(colunas):
            matriz[i].append(0)
    return matriz

m = cria_matriz(10, 10)
mostra_matriz(m)

# comeca criando uma matriz vazia []
# matriz.append([]) serve para colocar as listas dentro da matriz que vao representar as linhas da matriz
# neste caso nao precisa colocar o len no for pois linhas e colunas ja e um numero
# matriz[i].append(0) serve para acessar as linhas da matriz
# como matriz[i].append(0) esta dentro do for j, ele acessa todas as colunas das linhas e preenche com 0
# se nao colocar [i] ele vai tentar acessar diretamente a matriz e nao as linhas da matriz

# Como mudar as linhas pares para terem 1

matriz = cria_matriz(10, 10)
for i in range(10):
    for j in range(10):
        if i%2==0:
            matriz[i][j]=1
mostra_matriz(matriz)

# matriz vai receber a matriz que foi criada
# se a linha for par vai colocar 1 nas colunas

# Como mudar as colunas pares para terem 1

matriz=cria_matriz(10, 10)
for i in range(10):
    for j in range(10):
        if j%2==0:
            matriz[i][j]=1
mostra_matriz(matriz)

# Como somar duas matrizes de mesmo tamanhos
def soma_matriz(m1, m2):
    if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                m1[i][j]+=m2[i][j]
        return m1
    else:
        print("nao tem com o somar duas matrizes de tamanhos diferentes")
        return

matriz1 = [[1,2,3], [4,5,6], [7,8,9]]
matriz2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
soma = soma_matriz(matriz1, matriz2)
mostra_matriz(soma)

# o verifica se as duas matrizes possuem o mesmo tamanho usando o len, tanto as linhas quanto as colunas
# m1[i][j] vai armazenar todos os valores das somas das duas matrizes
# a funcao vai retornar a m1
# o return no else vai retornar none, em uma função, geralmente todos os possíveis caminhos de execução da função tem algum tipo de valor de retorno.

# Como fazer dois triangulos em uma matriz por 0 e 1

triangular = cria_matriz(5, 5)
for i in range(len(triangular)):
    for j in range(len(triangular)):
        if i>j:
            triangular[i][j]=1
mostra_matriz(triangular)

#Como fazer o xadrez com 0 e 1

xadrez = cria_matriz(8, 8)
for i in range(len(xadrez)):
    for j in range(len(xadrez[0])):
        if i%2==j%2:
            xadrez[i][j]=1
        else:
            xadrez[i][j]=0
mostra_matriz(xadrez)

# Como inverter o i com o j em uma matriz
matriz=[[1,2,3], [4,5,6], [7,8,9]]
mostra_matriz(matriz)
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        aux = matriz[i][j]
        matriz[j][i] = matriz[i][j]
        matriz[i][j] = aux
mostra_matriz(matriz)

# Como printar todos os elementos das listas e suas linhas e colunas
def printar_elementos(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f"matriz[{i}][{j}] = {matriz[i][j]}")
    return

matriz=[[1,2,3], [4,5,6], [7,8,9]]
printar_elementos(matriz)

#Como mostrar a matriz com uma linha embaixo da outra
def mostra_matriz2(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return

m=[[1,2,3], [4,5,6], [7,8,9]]
mostra_matriz2(m)


#Como criar uma matriz com 0
def cria_matriz2(linhas, colunas):
    matriz=[]
    for i in range(linhas):
        matriz.append([])
        for j in range(colunas):
            matriz[i].append(0)
    return matriz

m=cria_matriz2(10, 10)
mostra_matriz2(m)


#Media ponderada
notas_alunos=[[5,10,3], [2,7,4], [10,2,7], [6,3,10], [10,10,10]]
mostra_matriz(notas_alunos)
pesos=[1,2,3,2,1]
soma_pesos = 9
media = []
for j in range(len(notas_alunos[0])):
    soma = 0
    for i in range(len(pesos)):
        soma+=pesos[i]*notas_alunos[i][j]
    media=soma/soma_pesos
    matriz.append(media)
print(matriz)

# alunos       1  2  3
#prova1        5  10 3 (x1)
#prova2        2  7  4 (x2)
#prova3        10 2  7 (x3)
#prova4        6  3  10 (x2)
#prova5        10 10 10 (x1)
# ele comeca pelo j pois ele comeca pelas colunas, pois as colunas representam os alunos e as linhas representam as notas dos alunos
# comecando pelo j ele analisa as notas do primeiro aluno e as multiplica pelos seus pesos correspondentes
# como tem 5 pesos as matriz nao pode aumentar os i dele e sim somente o j que seria a quantidade de alunos
# entao len(pesos) serviria tanto para os pesos quanto para as notas_alunos pois a quantidade e a mesma
# len(notas_alunos[0])) -> 0 1 2
# len(pesos)) -> 0 1 2 3 4
