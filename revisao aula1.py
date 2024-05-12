'''exercicio 1

num1 = int(input("Escreva um numero: "))
num2 = int(input("Escreva outro numero: "))

if num1 > num2:
    print(f"O maior numero e o {num1}")
else:
    print(f"O maior numero e o {num2}")
'''

'''exercicio 2

nasc = int(input("Digite o ano que voce nasceu: "))
idade = 2023 - nasc

if idade < 16:
    print("Voce nao podera votar esse ano")
else:
    print("Voce podera votar esse ano")
'''

'''exercicio 3 

senha = int(input("Digite sua senha: "))

if senha == 1234:
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO")
'''

'''exercicio 4

quantidade = int(input("Digite o numero de macas que voce comprou: "))
preco = quantidade * 0.30

if quantidade < 6:
    print(f"O preco pago e de {preco}: ")
else:
    preco = quantidade * 0.25
    print(f"O preco pago e de {preco}: ")
'''

'''exercicio 5

num1 = float(input("Digite um numero: "))
num2 = float(input("Outro um numero: "))
num3 = float(input("Outro um numero: "))

if num1 > num2 and num1 > num3:
    print(f"O maior numero e o {num1}")
elif num2 > num3:
    print(f"O maior numero e o {num2}")
else:
    print(f"O maior numero e o {num3}")
'''

'''exercicio 6

sexo = int(input("Digite 1 para feminino e 2 para masculino: "))
altura = float(input("Digite sua altura: "))

if sexo == 1:
    peso1 = (62.1 * altura) - 44.7
    print(f"O seu peso ideal {peso1}")
elif sexo == 2:
    peso2 = (72.7 * altura) - 58
    print(f"O seu peso ideal {peso2}")
'''

'''exercicio 7 e 8

lados = int(input("Digite o numero de lados do poligono: "))

if lados < 3:
    print("Nao e um POLIGONO")
elif lados == 3:
    altura = float(input("Digite a altura do triangulo: "))
    base = float(input("Digite a base do triangulo: "))
    area = base * altura / 2
    print(f"Esse poligono e um TRIANGULO e sua e area e {area}")
elif lados == 4:
    area = lados * lados
    print(f"Esse poligono e um QUADRADO e sua area e {area}")
elif lados == 5:
    print("Esse poligono e um PENTAGONO")
else:
    print("POLIGONO nao identificado")
'''

'''exercicio 9 

num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))
num3 = float(input("Digite outro numero: "))

maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
print(f"O maior numero e o {maior}")
'''

'''exercicio 10

lado1 = float(input("Digite o valor de um lado do triangulo: "))
lado2 = float(input("Digite o valor de outro lado do triangulo: "))
lado3 = float(input("Digite o valor de outro lado do triangulo: "))

if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
    print("Esse trinagulo e equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Esse triangulo e isoscele")
else:
    print("Esse triangulo e escaleno")
'''

'''exercicio 11

angulo1 = float(input("Digite o valor de um angulo do triangulo: "))
angulo2 = float(input("Digite o valor de outro angulo do triangulo: "))
angulo3 = float(input("Digite o valor de outro angulo do triangulo: "))

if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
    print("Triangulo Retangulo")
elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
    print("Triangulo Obtusangulo")
elif angulo1 < 90 or angulo2 < 90 or angulo3 < 90:
    print("Triangulo Acutangulo")
'''
'''
escolha = input("Digite se o primeiro jogador escolheu par ou impar: ")
num1 = int(input("Digite o numero que o primeiro jogador escolheu: "))
num2 = int(input("Digite o numero que o segundo jogador escolheu: "))
soma = num1 + num2

if escolha == "par" and soma % 2 == 0:
    print("A soma deu um numero par e o jogador 1 escolheu par, portanto ele ganhou")
elif escolha == "impar" and soma % 2 == 1:
    print("A soma deu um numero impar e o jogador 1 escolheu impar, portanto ele ganhou")
elif escolha == "par" and soma % 2 == 1:
    print("A soma deu um numero impar e o jogador 2 escolheu impar, portanto ele ganhou")
else:
    print("A soma deu um numero par e o jogador 2 escolheu par, portanto ele ganhou")
'''

