
resposta =  input("Voce quer cnhecer minha calculadora?(s/n): ")
while not (resposta == "s" or resposta == "n"):
    resposta = input("Mano é p falar (s/n): ")
print("acertou as opcões")

resposta = input("Voce quer conhecer minha calculadora? (s/n): ")
while resposta != "s" and resposta != "n":
    resposta = input("Mano é p falar (s/n: ")
print("acertou as opcões")

#Essa e uma forma de repetir a pergunta ao usuario caso ele digite o que nao foi pedido, seria enquanto a resposta for diferente de s ou n vai aparacer o input o "Mano é p falar (s/n):"


# print("danilo".isnumeric())
# print("1234".isnumeric())
# verifica se o que foi digitado e um numero ou nao


resposta = input("Digite um numero: ")
#while resposta.isnumeric() == false:
while not resposta.isnumeric():
    resposta = input("Vacilao, Diga um numero: ")
print("parabens voce acertou")
resposta = int(resposta)
# transformando a variavel em int 


num1 = input("Diga um numero: ")
num2 = input("Diga outro numero: ")
#while respota.isnumeric() == false:
while not num1.isnumeric() and not num2.isnumeric():
    num1 = input("Vacilao Diga um numero")
    num2 = input("Vacilao Diga um numero")
print(num1 + num2)
#ira juntar os numeros pois eles nao sao um int
num1 = int(num1)
num2 = int(num2)
#forma para transformar uma variavel em int
print(num1 + num2)
#ira somar os numeros pois eles sao um int

# mesmo que some dois numeros mas eles nao forem um int, forem uma string "" o que vai acontecer é de juntar os numeros, se eles
# forem uma int vai somar os numeros


# Desafio e perguntar ao usuario se ele quer conhecer a minha calculadora, depois pergunte ao usuario digitar dois numeros e depois peca
# para ele escolher qual operacao ele vai querer e opcao sair para sair, sempre faca a perguta novamente se a resposta do usuario nao
# for o que voce esta pedindo

pergunta = input("Voce quer conhecer a minha calculadora s/n:")
while not (pergunta == "s" or pergunta == "n"):
    input("Voce tem que digitar s/n")
if pergunta == "s":
    num1 = print("Escolha um numero: ")
    num2 = print("Escolha outro numero: ")
    while not num1.isnumeric() and not num2.isnumeric():
        print("Digite um numero")





