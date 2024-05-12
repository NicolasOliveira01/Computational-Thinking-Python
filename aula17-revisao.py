"""
frase = "A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha."
frase = frase.replace(".", "") # vai trocar o . por nada, ou seja, vai tirar o ponto
print(frase)
frase = frase.lower() # vai deixar todo o texto em letra minuscula
print(frase)
frase = frase.split(" ") # coloca todo a frase em uma lista e cada palavra da frase vai virar um valor da lista
print(frase)
# lista nao tem chave e sim valor

dic={}
for palavra in frase:
    if palavra not in dic.keys():
        dic[palavra] = 1
    else:
        dic[palavra] += 1
print(dic)
"""

# vai iterar sobre os valores da frase e nao usa .keys() porque frase e uma lista e neste caso cada palavra e um valor
# se a palavra nao estiver dentro do dicionario, ou seja, se a palavra nao for uma chave do dicionario ainda
# vai criar uma chave com o nome da palavra e o seu valor vai ser 1
# se essa palavra ja for uma chave do dicionario vai acrescentar 1
# neste exemplo precisou tirar o . porque ele esta junto com outras palavras e para o python aranha. e diferente de aranha
# mesma coisa com letras maiusculas, para o python A e diferentes de a, porem na contagem de palavras e igual
# se nao fazer um split na frase, vai contar a quatidade de letras na frase e nao a quantidade de palavras

"""
lista = [10,20,30,40]
print(lista)
lista.remove(30) # .remove vai remover o valor da lista diretamente
lista.pop(2) # .pop vai remover o valor da lista atraves do seu indice
print(lista)
"""

# função para forçar resposta
def forca_opcao(msg,lista_opcoes):
    resposta=input(msg)
    while not resposta in lista_opcoes:
        print("Digite uma opcao cadastrada: ")
        resposta=input(msg)
    return resposta

# precisa ser in no while not e nao ==
# precisa dar um return resposta

def printa_dic(dic):
    for key in dic.keys():
        if type(dic[key]) is dict:
            printa_dic(dic[key])
        else:
            print(f"{key} : {dic[key]}")
    return

# precisa de um for para iterar sobre as chaves do dicionario, pois quer printar a chave e o seu valor correspondente
# no type precisa do dic[key] e nao somente key, pois para falar da chave do dicionario precisa falar qual o seu dicionario
# se a chave do dicionario for um dicionario volta para o comeco da funcao chamando ela, e nao pode ter um return
# se ele nao for um dicionario vai printar as chaves do dicionario

def checa_estoque(opcao):
    if whiskeys1['estoque'][opcao] == 0:
        return False
    whiskeys1['estoque'][opcao] -= 1
    return True

# esse codigo vai verificar se tem disponivel o whiskey que o usuario quis
# se a quantidade no estoque de whiskey que ele pediu whiskeys1['estoque'][opcao] for igual a 0 vai retornar false
# se a quantidade no estoque de whiskey que ele pediu whiskeys1['estoque'][opcao] for maior que 0 ele vai descontar 1 e vai retornar True
# esta retornando false ou true para ficar mais facil usar essa funcao

def cadastrar():
    for key in whiskeys1.keys():
        novo=input(f"Me diga o {key} desse whiskey: ")
        whiskeys1[key].append(novo)
    return

# essa funcao vai colocar um whiskey, e colocando mais um precisa colocar todas as informacoes sobre ele
# por isso tem que ter um for iterando sobre as chaves do dicionario
# novo vai ser a nova informacao sobre esse whiskey
# o novo vai ser o novo valor da chave que foi adicionado

"""
def alterar(preco_ou_estoque):
    for i in range(len(whiskeys1[preco_ou_estoque])):
        print(f"{i} : {whiskeys1[preco_ou_estoque][i]}")
    escolha=forca_opcao(f"Qual o {preco_ou_estoque} voce quer alterar? (0,1,2,3,4): ", ('0','1','2','3','4'))
    novo=int(input("Digite o novo valor: "))
    whiskeys1[preco_ou_estoque][escolha].append(novo)
    return
"""

def alterar(preco_estoque):
    for i in range(len(whiskeys1['tipo'])):
        print(f"{i} - {whiskeys1['tipo'][i]}")
    qual = int(forca_opcao(f"De que whiskey vc irá alterar o {preco_estoque}?", ('0','1','2','3','4')))
    novo = input(f"Diga o novo {preco_estoque}")
    whiskeys1[preco_estoque][qual] = novo
    return

# esse codigo serve para trocar o valor do preco ou do estoque de um determinado whiskey
# precisa de um range(len) pois tem o i que vai ser o indice de cada chave da lista tipo
# no primeiro for nao precisa usar um .keys() pois ele normalmente e usado para iterar sobre as chaves de um dicionario
# neste caso, e preciso iterar sobre os valores de uma chave do dicionario e usar o [''] ja e suficiente
# no primeiro print precisa ter um [i] para printar somente uma chave da lista e nao a lista tipo inteira
# i vai percorrer o tamanho da lista tipo e cada chave vai ter seu indice
# qual, novo e whiskeys[preco_estoque][qual] precisam estar fora do for, senao ele vai mostrar o primeiro whiskey e depois fazer as perguntas
# porem precisa mostrar todos os whiskeys primeiro para depois ir para as perguntas
# neste caso so vai alterar o preco ou o estoque, entao o parametro nao vai ser qualquer chave do dicionario e sim o preco_ou_estoque
# para alterar os valores, nao precisa colocar um pop e um append, basta colocar whiskeys[preco_estoque][qual] = novo em que preco_estoque vai ser qual chave quer alterar, qual vai ser o
# indice do valor daquela chave e o novo vai ser o novo valor

def remover():
    for i in range(len(whiskeys['tipo'])):
        print(f"{i} - {whiskeys['tipo'][i]}")
    qual = int(obriga_opcao(f"Qual será removido ?",opcoes))
    for key in whiskeys.keys():
        whiskeys[key].pop(qual)
    return

compra1 = {
    'valor_total': 0,
    'garrafas' : {},
    'endereco' : {'rua' : '',
                  'numero': '',
                  'cep' : '',
                  'bairro' : '',
                  'cidade' : '',
    },
    'nome' : '',
}

whiskeys1 = {
    'tipo' : ['bourbon','blended','scotch','single malt','double malt'],
    '%alcoolico' : [41,50,35,62,37],
    'volume (ml)' : [1000,750,50,100,800],
    'idade' : [15,12,8,8,10],
    'preco' : [14,23,541,65,999],
    'marca' : ['jack Daniels','White Horse','Passport','Johnie Walker','Chanceler'],
    'estoque' : [1,34,54,12,11],
}

# primeiro vai perguntar se é cliente ou funcionario
# se for cliente perguntar o nome
# mostrar todas as informoções sobre o endereço
# fazer um loop infinito mostrando as opcoes de whiskeys com numera pra cada um
# mostrar todas as informções sobre esse whiskey escolhido
# perguntar se ele vai levar e se sim colocar o preco no dicionario
# colocar somente no dicionario os whiskeys comprados ou adicionar se ja estiver um
# vai peguntar se ele quer continuar e se nao mostra o resumo do pedido
# cadastrar(), alterar(preço, estoque), remover()


opcoes=['0', '1', '2', '3', '4']
cliente_ou_funcionario = forca_opcao("Voce e cliente ou funcionario? (c/f): ", ("c", "f"))
if cliente_ou_funcionario == "c":
    nome=input("Digite seu nome: ")
    compra1['nome'] = nome
    print(f"Bem vindo {nome}")
    for key in compra1['endereco'].keys():
        info=input(f"Digite sua/o {key}: ")
        compra1['endereco'][key] = info
    while True:
        print("Essas sao nossas opcoes de whiskey: ")
        for i in range(len(whiskeys1['tipo'])):
            print(f"{i} : {whiskeys1['tipo'][i]}")
        escolha=int(forca_opcao("Qual whiskey voce esta interessado? (0,1,2,3,4): ", opcoes))
        print("Essas sao as informacoes sobre esse whiskey: ")
        for key in whiskeys1.keys():
            print(f"{key} : {whiskeys1[key][escolha]}")

# nome vai armazenar o nome que o usuario digitou
# compra1['nome']=nome vai colocar o nome que o usuarioi digitou na chave nome do dicionario compra1
# endereco e um dicionario que tem 5 chaves e que esta dentro de um dicionario e esse for serve para iterar sobre as chaves do dicionario endereco
# key vai ser cada chave do dicionario e info vai ser a resposta sobre cada chave do dicionario e compra1['endereco'][key] vai colocar cada resposta como valor de cada chave
# em compra1['endereco'][key] precisa desse [key] pois ele vai dizer em qual chave vai colocar aquela informacao
# o while True serve para sempre voltar desde o comeco caso o usuario nao querer levar o whiskey
# o for vai iterar sobre a quantidade de tipos de whiskey em whiskeys1['tipo'] que neste caso e 5
# vai printar cada valor referente a cada ao tipo de whiskey e {whiskeys1['tipo'][i]} precisa do [i] para mostrar em qual tipo ele esta iterando
# precisa do int na opcao pois ele esperava um numerico porem as listas so aceitam strings e as entradas do usuario sao lidas como string quando usa o input
# o for vai iterar sobre as chaves de whiskeys1 e vai printar todas as informacoes de cada chave no indice que o usuario escolheu
# {whiskeys1[key][opcao]} [key] sao todas as chaves do dicionario
# perguntar se o cliente vai querer levar e se for n vai voltar para o comeco por causa do while True
# uma das chaves do dicionario compra e valor_total que ja recebe o valor 0 e whiskeys['preco'][opcao] vai ser o preco do whiskey que o usuario escolheu
# marca vai armazenar qual a marca que o usuario escolheu whiskeys1['marca'][opcao]
# compra1['garrafas'] e um dicionario, entao ele tem uma chave e um valor, a chave vai ser a marca e o valor a quantidade que o usuario escolheu
# se a marca que o usuario escolheu nao estiver dentro de compra1['garrafas'] vai crirar uma chave dentro dele com a marca e o seu valor vai ser 1
# se aquele chave ja existir que no caso seria se o usuario ja escolheu aquele whiskey vai adicionar 1 ao valor da chave

'''
1º Exercício:
	- tirar pontuação de frase
	- deixar tudo minúsculo
	- adicionar as palavras separadamente nas chaves de um dicionário
	'''

frase_qualquer = "~Olá! Você está bem? Espero que sim. O @céu está lindo hoje! #Vamos celebrar &festejar. Ei, você! Sim, você! 12345, 6789. Palavras?! Sim, palavras: 'alegria', 'amor', 'paz'. %$#@! Agora é ^hora de partir. Adeus!"

#função para retirar caracteres especiais e deixar minúsculo
def formatar(frase):
    for char_especial in '!@#~$%&*()_.,><?-/"':
        frase = frase.replace(char_especial, '')
    frase = frase.lower()
    return frase

 # função para remover acentos das palavras de uma frase e transformar cada palavra em um valor da lista
 def acentos(frase):
    letras_acentuadas = {"ãàáâ": "a", "éêè": "e", "íîì": "i", "óôõò": "o", "úù": "u"}
    for vogais_acentuadas in letras_acentuadas.keys(): #percurso pelas chaves do dicionário
         for vogal_acentuada in vogais_acentuadas: #percorre cada vogal de cada chave de vogais
             frase = frase.replace(vogal_acentuada, letras_acentuadas[vogais_acentuadas])
    frase = frase.split(" ")
    return frase


def formatacao(frase):
    dicionario_zuadas = {"ãàáâ": "a", "éêè": "e", "íîì": "i", "óôõò": "o", "úù": "u"} #dicionário com vogais acentudadas a serem substituídas por voagsi sem acento
    for char_especial in '!@#~$%&*()_.^,><?-/"': #loop nos caracteres especiais
        frase = frase.replace(char_especial, '') #cada caracter especiais sendo substituído por nada a cada loop
    frase = frase.lower() #transforma em minúsculo
    for chave_zuada in dicionario_zuadas.keys(): #percurso pelas chaves do dicionário
        for vogal_zuada in chave_zuada: #percorre cada vogal acentuada de cada chave de vogais
            frase = frase.replace(vogal_zuada, dicionario_zuadas[chave_zuada]) #substitui cada vogal zuada pelo valor de cada chave, que são as vogais sem acento
    frase = frase.split(" ") #transforma em uma lista
    return frase

print(frase_qualquer)
print(formatacao(frase_qualquer))
lista_de_palavras_formatadas = formatacao(frase_qualquer)

#- contar quantas tem de cada palavra nos valores das chaves

def contar(lista):
    contagem = {}
    for palavra in lista:
        if palavra not in contagem.keys(): #aqui "contagem" pode ser sem o método .keys(), mas é boas práticas colocá-lo para especificar que estamos percorrendo as chaves dele
            contagem[palavra] = 1
        else:
            contagem[palavra] += 1
    return contagem

def print_dic(dic): #declara a função que printa as chaves do dicionário e seus valores
    for key in dic.keys(): #percorre as chaves do dicionário
        if type(dic[key]) is dict: #verifica se o valor da chave do dicionário é um dicionário
            print_dic(dic[key]) #caso o valor da chave do dicionário for um dicionário, vai chamar a função novamente repetindo o ciclo
        else: #caso o valor da chave do dicionário não for um dicionário
            print(f"{key} : {dic[key]}") #vai printar a chave com seu respectivo valor
    return #essa função não retorna nada, porque a saída de dados printando o dicionário ja acontece nos prints do else

print(print_dic(contar(lista_de_palavras_formatadas)))

'''
2º Exercício:
	Documento com especificações de carros
	- função que acha o carro com maior potencia
	- trazer todas as informações do carro que tem a maior potência
	- adicionar a funcionalidade de poder cadastrar um carro com todas as informações
	- adicionar a funcionalidade de poder excluir um carro cadastrado
'''
carros = {
    "marca": ["hb20", "polo", "celta", "fusca"],
    "potencia": [200, 1000, 100, 8000],
    "preco": [50, 100, 125, 15000],
    "ano": [1990, 2000, 2010, 1940],
    "montadora": ["hyundai", "wolks", "chevrolet", "wolkswagen"]
}

# - função que acha o carro com maior potencia
def acha_maior_potencia():
    maior = carros["potencia"][0]
    indice_do_maior = 0
    for i in range(len(carros["potencia"])):
        if carros["potencia"][i] > maior:
            indice_do_maior = i
    return indice_do_maior

#- trazer todas as informações do carro que tem a maior potência
for key in carros.keys():
    print(f"{key} : {carros[key][acha_maior_potencia()]}")

# - adicionar a funcionalidade de poder cadastrar um carro com todas as informações
def cadastrar():
    print("Bem vindo ao cadastro de carros")
    for key in carros.keys():
        info = input(f"Digite o/a {key} do carro")
        carros[key].append(info)
    return

#- adicionar a funcionalidade de poder excluir um carro cadastrado
def excluir():
    print("Você está excluindo um carro")
    opcao = int(forca_opcao("Qual carro deseja excluir? 1-hb20 2-polo 3-celta 4-fusca", ["0","1","2","3"]))
    for key in carros.keys():
        carros[key].pop(opcao)
    return

