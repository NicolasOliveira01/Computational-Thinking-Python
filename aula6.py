print("Bem vindo a vinheria!!!")
endereco=input("Diga seu endereço: ")
ano=input("Diga seu ano de nascimento : ")
while not ano.isnumeric():
    ano=input("Seu ano de nascimento deve ser um número: ")
ano=int(ano)
if 2023-ano<18:
    print("Que feio não pode")
else:
    valor=0
    qtd_tinto = 0
    qtd_suave = 0
    qtd_rose = 0

    while True:
        opcao=input("Qual vinho você quer? (tinto, suave, rosé): ")
        while not(opcao=="tinto" or opcao=="suave" or opcao=="rosé"):
            opcao=input("Tem quer ser uma dessas: ")

        qtd=input(f"Quantas garrafas de {opcao} você quer? ")
        while not qtd.isnumeric():
            qtd=input(f"Quantas garrafas de {opcao} você quer? ")
        qtd=int(qtd)

        if opcao=="tinto":
            valor+=30*qtd
            qtd_tinto+=qtd
        elif opcao=="suave":
            valor+=40*qtd
            qtd_suave+=qtd
        else:
            valor+=50*qtd
            qtd_rose+=qtd
        pergunta=input("Você quer continuar comprando? (s/n): ")
        while not (pergunta=="s" or pergunta=="n"):
            pergunta=input("Você quer continuar comprando? (s/n): ")
        if pergunta=="s":
            continue
        else:
            break
    if valor>500:
        print("Você recebeu frete grátis!")
    else:
        valor+=10
    print(f"Valeu, você gastou R${valor}, com {qtd_suave} suave, {qtd_tinto} tinto e {qtd_rose} rosé e será entregue em {endereco}")


# Descobrir se um número é impar ou par de uma lista


#por indice
numeros=[234,546,567,523467,2343,54234]
indice=0
for numero in numeros:
    if numero%2==0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é impar")
#por elememto
numeros=[234,546,567,523467,2343,54234]
for i in range(len(numeros)):
    if numeros[i]%2==0:
        print(f"{numeros[i]} é par")
    else:
        print(f"{numeros[i]} é impar")

# Somar os numeros de mesmo indice das duas listas

num1=[1,2,3,4,5,6,7,8,9,10]
num2=[11,12,13,14,15,16,17,18,19,20]
num3=[]
for i in range(len(num1)):
    soma=num1[i]+num2[i]
    num3.append(soma)
print(num3)

# Conte a quatidade de vogais na lista

letras=["a","b","c","d","i","o","h"]
vogais=0
for i in range(len(letras)):
    if letras[i]=="a" or letras[i]=="e" or letras[i]=="i" or letras[i]=="o" or letras[i]=="u":
        vogais+=1
print(vogais)


# ve se o elemento está na lista e diga seu indice

while True:
    profs=["allen","israel","danilo","yan","luciano","ana","cordeiro"]
    teste=input("Diga um nome: ")
    ta_ou_n=False
    for i in range(len(profs)):
        if teste==profs[i]:
            ta_ou_n=True
            indice_elemento=i
    if ta_ou_n:
        print(f"{teste} está na posição {indice_elemento}")
    else:
        print(f"{teste} não está na lista")
    continue

# Mudar todos os elementos de uma lista

numeros=[0,0,0,0,0,0,0]
for i in range(len(numeros)):
    numeros[i]=1
print(numeros)

# saber qual é o carro mais caro pela lista de preços

carros=["ka","celta","golf","fusca",]
preco=[10,100,200,5]

indice_maior=0
maior=preco[0]
for i in range(len(preco)):
    if preco[i]>maior:
        maior=preco[i]
        indice_maior=i

indice_menor=0
menor=preco[0]
for i in range(len(preco)):
    if preco[i]<menor:
        menor=preco[i]
        indice_menor=i

print(f"O carro mais caro é o {carros[indice_maior]} e o carro mais barato é o {carros[indice_menor]})




