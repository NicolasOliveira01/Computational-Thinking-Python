import random

"""
jogo = {'são paulo' : 'vencedor', 'corinthians' : 'perdedor'} # sao paulo e corinthians sao as chaves do dicionario
jogo['palmeiras'] = 'sem mundial' # adiciona mais uma chave ao dicionario jogo
jogo['são paulo'] = 'trimundial' # atualiza a chave sao paulo
time=input("Pra que time vc torce? ")
print(f"Voce é um {jogo[time]}") # jogo e o dicionario e time e a pergunta
"""

"""
saudacoes = {
            'oi' : ['olá', 'salve', 'e ai', 'fmz'],
            'tchau' : ['e o pix?', 'flw', 'tmj', 'vaza']
            }
print(saudacoes.keys()) # printa as chaves do dicionario
while True:
    resposta=input('Diga oi ou tchau: ')
    if resposta in saudacoes.keys(): # resposta e a pergunta e ele verifica se e a chave do dicionario saudacoes
        print(random.choice(saudacoes[resposta])) # escolhe uma resposta aleatoria 
    elif resposta == 'sair':
        break
    else:
        print('fala dnv')
"""

"""
parentes = {} # dicionario
parentes['pai'] = 'João'
parentes['mãe'] = 'Maria'
parentes['irmão'] = 'José'
parentes['primo'] = 'lucas'
for key in parentes.keys():
    print(f"O nome do/a seu/sua {key} é {parentes[key]}")

#  parentes ['pai'] = 'Joao'
#dicionario  chave    entrada
"""

"""
carros = {'modelo': ['up', 'ka', 'fox', 'celta', 'gol'], 'preco': [10, 20, 15, 50, 30]}
maior = carros['preco'][0]
indice_maior = 0
for i in range(len(carros['preco'])):
    if carros['preco'][i] > maior:
        indice_maior = i
        maior = carros['preco'][i]
print(f"O carro mais caro é o {carros['modelo'][indice_maior]} e custa {carros['preco'][indice_maior]}")
carros['potencia'] = [10, 20, 30, 100000, 10]
print(f"A potência do carro mais caro é {carros['potencia'][indice_maior]}")
"""

"""
jogo = {'sao paulo' : 'vencedor', 'corinthians' : 'perdedor'}
jogo['palmeiras'] = 'sem mundial'
print(jogo)
jogo['sao paulo'] =[jogo['sao paulo']] # esta transformando as entradas da chave em uma lista
print(jogo)

jogo['sao paulo'].append('trimundial') # colocando entradas na chave
print(jogo)
print(type(jogo['sao paulo'])) # o tipo de chave
jogo['vasco'] = {'rebaixamento' : 'certeza', 'campeao' : 'serie B'}
print(jogo)
"""

"""
selecao = {
    'Nome' : 'Brasil',
    'titulos mundiais' : 5,
    'anos e títulos' : [1958,1962,1970,1994,2002],
    'melhor jogador em cada título' : ['pelé', 'garrincha', 'pele', 'romario', 'ronaldo'],
    'rivais' : ['argentina','franca','alemanha'],
    'nunca ganhou' : 'Noruega'
}

# print(selecao)

for key in selecao.keys():
    print(f"{key} : {selecao[key]}")
"""

"""
jogo = {'sao paulo' : 'vencedor', 'corinthians' : 'perdedor'}
jogo['palmeiras'] = 'sem mundial'
for key in jogo.keys():
    print(f"Voce torce para o {key} então voce é um {jogo[key]}")
"""

"""
numeros={"pares" : [], "impares" : []}
for i in range(11):
    if i%2==0:
        numeros['pares'].append(i)
    else:
        numeros['impares'].append(i)
print(numeros)
"""

"""
def forca_resposta(msg,lista_opcoes):
    resposta = input(msg)
    while resposta not in lista_opcoes:
        resposta = input(msg)
    return resposta

carros ={"modelos" : ['celta','ka','up'], 'precos' : [10,20,30]}
while True:
    pergunta = forca_resposta("Voce quer cadastrar um carro? (s/n): ", ['s', 'n'])
    if pergunta == 's':
        for key in carros.keys():
            info = input(f"Diga a/o {key} : ")
            carros[key].append(info)
    else:
        print("Cadastro finalizado")
        break

print(carros)
"""