travalinguas = "A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha"
#palavras = {'a' : 8 , 'palavra' : 'numero de ocorrencias da palavra'}
#for char in travalinguas:
    # print(char) -> problema

#nome = 'Danilo'
#nome = nome.lower() # deixa minusculo
#print(nome)
#nome[0] = 'd' # nao e igual uma lista, vai dar erro
#print(nome[2].append('.')) # vai dar erro

"""
print(travalinguas)
travalinguas = travalinguas.replace('.','')
print(travalinguas)
travalinguas = travalinguas.lower()
print(travalinguas)
travalinguas = travalinguas.split(" ") # split
print(travalinguas)
#print('aranha' == 'aranha.') # vai dar falso
"""

"""
palavras = {}
for palavra in travalinguas:
    if palavra not in palavras.keys():
        palavras[palavra] = 1
    else:
        palavras[palavra] += 1
    print(palavras)
"""
# se nao estiver com o split vai mostrar a quantidade de letras e nao de palavras

def conta_palavras(travalingua):
    for char in '!@#$%^&*()_.,:<>?/':
            travalingua = travalingua.replace(char, '') # se nao estiver nao vai dar erro
    travalingua = travalingua.lower()
    travalingua = travalingua.split(" ")
    palavras = {}
    for palavra in travalingua:
        if palavra not in palavras.keys():
            palavras[palavra] = 1
        else:
            palavras[palavra] += 1
    return palavras

"""
travalingua2 = "Se percebeste, percebeste. Se não percebeste, faz que percebeste para que eu perceba que tu percebeste. Percebeste?"
print(conta_palavras(travalingua2))
"""

"""
nome = "danilo é humilde, esse danilo"
nome = nome.capitalize()
print(nome)
"""

"""
nome = "danilo é humilde, esse danilo"
sentenca = ''
for palavra in nome.replace(',','').split(" "):
    if palavra != 'danilo':
        sentenca+=palavra + ' '
    else:
        palavra = palavra.replace("d", "D")
        sentenca += palavra + ' '
print(sentenca)
"""


frase = "não é íntegro ômegra três no último mês"
letras_zuadas = {'ãáàâ' : 'a', 'éêè' : 'e', 'íîì' : 'i', 'óòõô' : 'o', 'úû' : 'u'}
for letra_zuada in letras_zuadas.keys():
    for letra in letra_zuada:
        frase.replace(letra, letras_zuadas[letra_zuada])
print(frase)


"""
import pandas as pd
dados = pd.read_csv("dado_mg.csv")
print(dados.columns)
print(dados.columns[0].split(";"))
print(dados.columns[0][0].split(";"))
print(dados.columns[1][0].split(";"))

def teste(dados):
    dados_processados = {}
    j=0
    for key in dados.columns[0].split(";"):
        for i in range(len(dados)):
            dados_processados[key] = []
            for dado in dados.values[i][0].split(";"):
                dados_processados[key].append(dados.values[i][0].split(";")[0])
            j+=1
    return dados_processados
dados_processados = teste(dados)
dados_processados = pd.DataFrame(dados_processados)
print(dados_processados)
"""


lista=['a','b', 'c']
while True:
    try:
        i = int(input("Diga um numero: "))
        letra = lista[i]
        #print(1+'3')
    except ValueError:
        print("seu bobao era pra ser um numero")
        raise ValueError("Vc e mt bobao")
    except IndexError:
        print(f"Tem que ser entre 0 e {len(lista)}")
    except NameError:
        print("Alguma variavel nao foi definida")
    except Exception as e:
        print(e)
    else:
        print(letra)
        print("Operacao realizada com sucesso ")
        break
    finally:
        print("Sou printado sempre e nao sirvo pra muito coisa")
# try except nao e if e else
# tudo que pode dar erro dando try


"""
num = input("Diga um numero: ")
while not num.isnumeric():
    num = input("Diga um numero: ")
num = int(num)
print(num)
"""

while True:
    try:
        num1 = float(input("Diga um numero: "))
        num2 = float(input("Diga o segundo numero: "))
        print(num2/num1)
    except ZeroDivisionError:
        print("n pode dividir por zero bobao")
    except ValueError:
        print("Tem que ser numero mano")
    else:
        print("Voce nao e tao bobao")
        break

