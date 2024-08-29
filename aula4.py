
a=1
b=1
qtd=2
while qtd<100:
    c=a+b
    a=b
    b=c
    i=2
    while i<c:
        #print(f"{c}%{i}={c%i}")
        if c%i==0:
            print(f"{c} não é primo pois é divisível por {i}")
            break
        elif i>=c**(1/2): #outra forma de ver se o número é primo, indo até sua raiz
            print(f"{c} é primo")
            break
        i+=1
    qtd+=1

for i in range(10, -10, -2): 
        #numero que começa, ordem que termina e qual a sequencia
    print(i)

for i in range (1, 11):
    for j in range (1, 11):
        print(f"{i} * {j} = {i*j}")
        #faz a tabuada

soma = 0
for i in range (1, 11):
    num=int(input("Digite um número: "))
    soma=soma+num
    media=soma/i
print(soma)
print(media)

usuario = "nicolas"
senha = "1234"
for i in range (1, 3):
    user = input("Digite seu nome de usuario: ")
    password = input("Digite sua senha: ")
    if user==usuario and password==senha:
        print("Acesso liberado")
        break
    user = input("Digite seu nome de usuario: ")
    password = input("Digite sua senha: ")

usuario = "nicolas"
senha = "1234"
for i in range (1, 3):
    user = input("Digite seu nome de usuario: ")
    password = input("Digite sua senha: ")
    if user==usuario and password==senha:
        print("Acesso liberado")
        break
    else:
        continue
print("Voce perdeu suas 3 tentativas")

for i in range(5):
    print(i)
    continue
    print("Nao vai printar")

nomes = ["ana","cordeiro", "danilo", "yan", "luciano", "israel", "eduardo"]
for i in range(len(nomes)):
    if nomes[i] == "danilo":
        print(f"o {nomes[i]} é o melhor professor")
        indice_do_danilo = i
    else:
        print(f"o professor {nomes[i]} é paia")
print(f"o indice do danilo é {indice_do_danilo}")
