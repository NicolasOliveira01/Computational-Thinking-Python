# POR INDICE:

"""nomes=["dan", "allen", "israel", "luciano", "yan", "ana", "cordeiro"] # na lista os elementos começam com o indice 0
frase = "" # ela precisa ser declarada para poder printar depois, por isso está fazia
indice=0 # vai servir para indicar os indices do elementos da lista
for nome in nomes: # nome é uma variavel contadora da lista nomes, ou seja, irá assumir o valor de cada elemento da lista nomes, o for será executado para cada elemento da lista nomes
    if indice < len(nomes)-2: # o indice começa com 0 e a lista nomes possui 7 elementos. Nesse caso vai de 0 até 4, pois o indice tem que ser menor que 5 (7-2), então vai printar os
# 5 primeiros elementos da lista nomes
        frase += f"o {nome}, "
    elif indice == len(nomes)-2:# se o indice for igual a 5 (ana)
        frase += f"o {nome} e o "
    elif indice == len(nomes)-1:# se o indice for igual a 6 (codeiro)
        frase += f"{nome} são professores"
    indice+=1
print(frase)
"""

# POR ELEMENTO:

'''nomes=["dan", "allen", "israel", "luciano", "yan", "ana", "cordeiro"]
frase = ""
for i in range(len(nomes)): # i = 0,1,2,3,4,5,6, o i vai de 0 até len(nomes) - 1
    if i < len(nomes)-2: #len(nomes) é 7 e o i começa com 0,ou seja, quando o i for menor que 5
        frase += f"o {nomes[i]}, "# como ele faz a verificação apenas pelo indice dos elementos da lista precisa indicar qual o seu indice para printar
    elif i == len(nomes)-2:
        frase += f"o {nomes[i]} e o "
    else: 
        frase += f"{nomes[i]} são professores"
print(frase)
'''

"""nomes=["dan", "allen", "israel", "luciano", "yan", "ana", "cordeiro"]
ta_ou_n=False
teste = input("Diga um nome: ")
for i in range (len(nomes)):#o i vai de 0 até len(nomes) - 1
    if nomes[i] == teste: #verifica se o elemento atual da lista nomes (acessado por nomes[i]) é igual ao teste
        indice_teste = i # so vai entrar nesse if se o teste for igual a algum elemento da lista (nomes[i])
        ta_ou_n = True #ta_ou_n so vai ser verdadeiro se o teste for igual a algum elemento da lista (nomes[i]) 
if ta_ou_n:
    print(f"o {nomes[indice_teste]} está no {indice_teste}")
else:
    print("elemento não encontrado")"""
"""
numeros = [i for i in range(109,201,6)]
teste = numeros[:]#numeros[:] faz uma cópia da lista e atribui os valores para teste
teste[3] = "mdsjndsjvn" #troca os elemento 4 da lista numeros por "mdsjndsjvn"
print(numeros)
print(teste)
"""
"""
numeros = [] # lista vazia
num=int(input("diga um numero: "))
numeros.append(num) #vai adicionar num na lista numeros atraves do .append
print(numeros)
numeros.append("fjenfjkenfjfn") # depois vai adicionar "fjenfjkenfjfn" na lista 
print(numeros)
"""

"""lista=[]
qtd=int(input("Diga a quantidade de numeros que vc quer colocar: "))
for i in range(0,qtd):
    elem=int(input("Digite um número"))
    lista.append(elem)
print(lista)"""
