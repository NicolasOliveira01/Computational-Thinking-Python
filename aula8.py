"""
senha="1234"
senha_usuario=input("Diga sua senha: ")
tentativas = 1
while not senha_usuario == senha and tentativas<3:
    print("errou")
    senha_usuario=input("Diga sua senha: ")
    tentativas += 1
# foi uma maneira maias facil de fazer, o codigo so vai pro if ou else se ele acertar a senha ou se a tentivas for igual a 3, vai perguntar ate o tentativas for menor
# que 3

if senha == senha_usuario:
    print("Acesso liberado")
else:
    print("sai hacker")
"""

"""
for i in range(3):
   senha_usuario=input("Diga sua senha: ")
   if senha == senha_usuario:
       print("acesso liberado")
       break
"""

"""
lista=["danilo", "allen", "cordeiro", "israel", "francisco"]

if "danilo" in lista: #verifica se a string "danilo" esta na lista
    print(True)
    print(lista.index("cordeiro")) # a funcao .index() para obter o indice 

i=0
for nome in lista:
    if nome == "danilo":
        print(f"Encontrei no {i}")
    i+=1
# essa seria outra forma de conseguir o indice. Comeca com o i que vai ser o valor do indice com 0 antes do for e toda vez que o if for falso o i vai aumentar 1 
"""

"""
def acha_maior(valores): #valores vai ser qualquer lista de numeros
    indice_maior=0
    maior=valores[0]
    for i in range(len(valores)):
        if valores[i]>maior:
            maior=valores[i]
            indice_maior=i
    return indice_maior  #se colocar o return dentro do for vai retornar a funcao da primeira iteracao do loop, pois assim logo depois de atender o if ele vai atender
#o return que vai retornar o indice_maior que neste caso sempre vai ser o primeiro da lista. Quando o return estiver fora do for, ele vai retornar realmente o indice_maior
    
carro=["up", "KA", "celta", "uno", "combi"]
precos=[50, 100, 100000, 200, 300]
local_maior=acha_maior(precos) # precisa de uma variavel para chamar a funcao e depois passar o seu parametro que neste caso e uma lista 
print(f"O carro mais caro e o {carro[local_maior]} e vale R${precos[local_maior]}") # ele achou o indice do elemento mais caro da lista precos e com esse indice ele 
# falou o carro
teste=[1,2,3,4,5]
local_maior_teste=acha_maior(teste)
print(local_maior_teste)
"""

"""
def interseccao(lista1, lista2):
    comuns=[]
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            #print(f"estou verificando se {lista1[i]}=={lista2[j]}")
            if lista1[i] == lista2[j]:
                #print("achei")
                comuns.append(lista2[j])
    return comuns

lista1=["guilherme", "nicolas", "matheus", "henrique", "bruno", "paulo", "gabriel"]
lista2=["nicolas", "joao", "tiago", "matheus", "guilherme", "rafael", "enzo"]
intersect = interseccao(lista1, lista2)
print(intersect)
# nao colocar mesmo nome de uma variavel igual a de um parametro de uma funcao
"""

"""
#para inverter valores

a=2
b=3
c=a
a=b
b=c
"""

"""
def inverte_lista(lista):
    ultimo=len(lista)-1 # ele pega o ultimo numero da lista, pois len(lista) e o tamanho total da lista e o -1 pois ela comeca no 0
    for i in range(len(lista)//2): #// significa dividir um numero e arredondar ele para o menor(7//2=3), justamente porque para inverter precisa da metade e caso
# for impar vai precisar da metade e arredondar para o menor
        aux = lista[i] # aux e somente uma variavel para ajudar e aux vai armazenar o primeiro elemento da lista
        lista[i]=lista[ultimo-i] # o primeiro elemento da lista vai ser agora o ultimo(o tamanho da lista -1 - i) elemento da lista
        lista[ultimo-i] = aux # esse numero vai ser o aux agora
    return lista

numeros=[1,2,3,4,5,6,7,8,9]
teste=inverte_lista(numeros)
teste2=["danilo", "banana", True, "mandioca", "baseball bat"]
teste2=inverte_lista(teste2)
print(teste)
"""

"""
matriz = [[1,2,3,4], [4,5,6,7], [7,8,9,10]]
# lista de lista, vetor de vetores
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
# tambem funcionaria sem o 0, mas se colocar mais um elemento ele n vai printar
        print(matriz[i][j])
"""

"""
import numpy as np 

matriz = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if j<i:
            matriz[i][j] = 1
            
matriz = np.array(matriz)
print(matriz)
"""
