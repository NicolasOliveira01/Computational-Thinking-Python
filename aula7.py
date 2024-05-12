"""num=2
def par_ou_impar(numero):
    print(numero)
    if num % 2==0:
        print(f"{num} e par")
    else:
        print(f"{num} e impar")
    return
par_ou_impar(5)
print(numero)#vai dar erro pq a var numero so existe dentro da fução
"""

"""def vogal_ou_n(letras):
    qtd_vogais=0
    for letra in letras:
        if letra in ["a","e","i","o","u"]:
            qtd_vogais +=1
            print(f"{letra} é uma vogal")
        else:
            print(f"{letra} é uma consoante")
    return qtd_vogais

#sequencia_de_letras = "hello"
#total_vogais = vogal_ou_n(sequencia_de_letras)
#print(f"Total de vogais encontradas: {total_vogais}")
# o valor retornado pela função (ou seja, o número total de vogais) é atribuído à variável total_vogais

qtd = vogal_ou_n("danilo")
print(qtd)
#print(qtd_vogais) da erro pq ela so existe dentro da função
"""

"""def soma(num1, num2):
    return num1+num2
def subtracao(num1, num2):
    return num1-num2
def divisao(num1, num2):
    return num1/num2
def multiplicacao(num1, num2):
    return num1*num2

#divisao(10, 2) somente assim nao vai

res = soma(2,3)
print(res)
res = subtracao(2,3)
print(res)
res = divisao(2,3)
print(res)
res = multiplicacao(2,3)
print(res)"""

"""def soma(num1, num2):
    return num1+num2

def subtracao(num1, num2):
    return num1-num2

def divisao(num1, num2):
    return num1/num2

def multiplicacao(num1, num2):
    return num1*num2

def meu_input_numerico(frase):
    num1=input(frase)
    while not num1.isnumeric():
        num1 = input(frase)
    num1=int(num1)
    return num1

def checa_opcoes(frase,opcoes_cadastradas):
# frase é uma mensagem a ser exibida ao usuário para solicitar sua escolha e opcoes_cadastradas é uma lista contendo as opções válidas que o usuário pode escolher
    operacao = input(frase)
    while not operacao in opcoes_cadastradas:
# verifica se a escolha do usuário (operacao) está presente na lista de (opcoes_cadastradas)
        operacao = input(frase)
    return operacao

msg = "o que vc deseja fazer? soma, subtração, divisão, multiplicação: "
lista_operacoes=["soma", "subtracao", "divisao", "multiplicacao"]
operacao=checa_opcoes(msg, lista_operacoes)
num1=meu_input_numerico("Me diga um número: ")
num2=meu_input_numerico("Me diga um número: ")

if operacao =="soma":
    res=soma(num1, num2)
    print(res)
elif operacao =="subtracao":
    res=subtracao(num1, num2)
    print(res)
elif operacao =="divisao":
    res=divisao(num1, num2)
    print(res)
else:
    res = multiplicacao(num1, num2)
    print(res)

#lista_de_vinhos=["tinto", "rose", "branco"]
#msg = "Qual vinho vc quer ? (tinto, rose, branco)"
#vinho = checa_opcoes(msg, lista_de_vinhos)
"""

"""def checa_opcoes(frase,opcoes_cadastradas):
# frase é uma mensagem a ser exibida ao usuário para solicitar sua escolha e opcoes_cadastradas é uma lista contendo as opções válidas que o usuário pode escolher
    operacao = input(frase)
    while not operacao in opcoes_cadastradas:
# verifica se a escolha do usuário (operacao) está presente na lista de (opcoes_cadastradas)
        operacao = input(frase)
    return operacao

def acha_maior(valores, nomes):
    maior=valores[0]
    local_maior=0
    for i in range(len(valores)):
        #print(f"Agora testo se {valores[i]} > {maior}")
        if valores[i] > maior:
            #print(f"troquei o maior de {maior} para {valores}")
            maior=valores[i]
            local_maior=i
    return nomes[local_maior]

def acha_menor(valores, nomes):
    menor=valores[0]
    local_menor=0
    for i in range(len(valores)):
        if valores[i]<menor:
            menor=valores[i]
            local_menor=i
        return nomes[local_menor]

vinhos=["tinto", "rose", "branco", "suave", "fedido", "cheiroso"]
precos=[100, 200, 150, 75, 237, 50]

def acha_media(valores):
    soma=0
    for valor in valores:
        soma+=valor
    return soma/len(valores)

vinho_mais_caro = acha_maior(precos,vinhos)
vinho_mais_barato = acha_menor(precos,vinhos)


opcao= checa_opcoes("Voce quer saber o maior ou o menor?: ", ["maior","menor"])
if opcao=="maior":
    print(vinho_mais_caro)
else:
    print(vinho_mais_barato)
"""