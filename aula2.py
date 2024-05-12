'''
resposta = input("Você quer adquirir conhecimento ??? (s/n): ")
while not (resposta == "s" or resposta == "n"): #while resposta != "s" and respota != "n"
    resposta = input("Mano tem que ser (s/n) ")#se a resposta for s ou n não vai entrar no while not e pula para o if
if resposta == "s":
    print("Parabens voce nao é boboca, bem vindo à calculadora!")
    while True:
        #para ele continuar dentro da calculadora, para repetir, ou seja vai perguntar para o usuário novamente "diga o primeiro número: ", so vai parar de perguntar se o usuário digitar sair
        num1 = input("diga o primeiro número: ") # não pode colocar a nota como float pois se o usuário digitar uma letra vai dar errado
        num2 = input("diga o segundo número: ")
        while not (num1.isnumeric() and num2.isnumeric()):#while (num1.isnumeric() == Flase and num2.isnumeric() == Flase)
            #nesse caso é and porque tanto o num1 quanto o num2 precisam ser um número
            num1 = input("tem que ser um número seu animal: ")
            num2 = input("O segundo tb: ")
            #mesmo o usuário não digitando um número num1 e num2 vão se tornar int
        num1 = int(num1)
        num2 = int(num2)
        opcao = input("Qual operações você quer fazer? soma, subtração, divisão, multipliacação ou sair?: ")
        while not (opcao == "soma" or opcao == "subtração" or opcao == "divisão" or opcao == "multiplicação" or opcao == "sair"):
            opcao = input("Qual operações você quer fazer? soma, subtração, divisão, multipliacação ou sair?")
        if opcao == "soma":
            resultado = num1 + num2
            print(f"O resultado da {opcao} entre {num1} e {num2} é {resultado}")
        elif opcao == "subtração":
            resultado = num1 - num2
            print(f"O resultado da {opcao} entre {num1} e {num2} é {resultado}")
        elif opcao == "subtração":
            resultado = num1/num2
            print(f"O resultado da {opcao} entre {num1} e {num2} é {resultado}")
        elif opcao == "multiplicação":
            resultado = num1*num2
            print(f"O resultado da {opcao} entre {num1} e {num2} é {resultado}")
        else:
            print("Tchau")
            break
else:
    print("seu boboca")
'''
'''
exercicio 1 
while True:
    nota = input("Diga sua nota de 0 a 10: ") # não pode colocar a nota como float pois se o usuário digitar uma letra vai dar erro
    if nota.isnumeric(): #se nota.isnuemric for True
        nota_convertida = int(nota) #vai converter o valor da nota para int
        if nota_convertida < 0 or nota_convertida > 10:
            continue
            #se a nota for menor que 0 maior que 10, vai dar um continue que vai voltar, nesse caso no nota = input("Diga sua nota de 0 a 10: ")
        else:  
            print("digitou corretamente")
            break # se a nota for entre 0 e 10 vai printar esse valor e parar(break)
    else:
        continue # se o usuário não digitar um número, vai dar um continue e voltar para o nota = input("Diga sua nota de 0 a 10: ")
# O usuário vai digitar um número, se for uma letra vai cair no else e ir no continue(voltando para a pergunta do começo), se ele digitar um número ele vai ser transformado em
# um float e se for menor que 0 e maior que 10 vai perguntar de novo
'''
'''
exemplo continue
i=0
while i < 20: # vai testar 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19
    if i>= 5 and i <15: # se o número testado for maior ou igual a 5 e menor que 15 (5,6,7,8,9,10,11,12,13,14)
        i+=1
        continue
        print("oi") #não printou o oi pois ou ele voltar para o if por causa do continue ou ele pula o if direto para o print(i)
    print(i) #aqui vão printar todos os números que não estão i>= 5 and i <15, pois o if vai dar False e esse valor do i testado não vai entrar no if  pular direto para o print(i), se o if for True ele vai voltar para o if
    # por causa do continue
    i+=1
'''
'''
exercicio 2
nome = input("Diga seu nome: ")
while len(nome) < 3:
    #ve com comprimento 
    nome = input("Diga seu nome:")

idade = int(input("Diga sua idade"))    
while idade<0 and idade >150:
    idade = input("Diga sua idade")

salario = int(input("Diga seu salario"))
while salario < 0:
    salario = input("Diga seu nome:")

sexo = input("Diga seu sexo")
while not (sexo == "f" or sexo == "m"):
    sexo = input("Diga seu nome:")

estado_civil = input("Diga seu estado civil: ")
while not (estado_civil == "s" or estado_civil == "c" or estado_civil == "v" or estado_civil == "d"):
    estado_civil = input("Diga seu estado civil: ")
'''
'''
exercicio 3
a = 80000
b = 200000
t = 0 # variável usada para guardar a quantidade de vezes que precisou fazer as operações
while a < b: # o while vai fazer a verificação com os novos valores de a e b até a ser maior que b
    a *= 1.03
    b *= 1.015
    t+=1
print(t) # se ele estiver dentro do while vai imprimir todos os números até o resultado final, se ele estiver fora do while vai imprimir somente o número final 
'''
'''
soma = 0
i=1
while i <= 5:
    numeros = int(input(f"Diga o {i}° número: "))
    i+=1
    soma+=numeros # todos os 5 valores estão dentro da variável numeros e soma vai ser o valor do 1° i, depois soma(1°) vai somar a 2° i e assim por diante
    media=soma/i # soma é a soma de todos os números digitados e i vai ser 5 que é a quantidade de vezes que o usuário digitou um número
print(f"A média é {media} e a soma é {soma}")
'''
'''
exercicio 5 
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
if num1 < num2:
    while num1 < num2:
        print(f"{num1}")
        num1 += 1
else:
    while num2 > num2:
        print(f"{num2}")
        num2 +=1
'''
'''
exercicio 8
a = 1
b = 1
n = int(input("Digite até qual ordem você quer saber da sequência de fibonacci: "))
i=0
while i < n:
    c = a + b
    a = b
    b = c
    i+=1
    print(f"{c}")
'''



