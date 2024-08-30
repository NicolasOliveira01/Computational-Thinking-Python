
frase = "Concluímos que chegamos à conclusão que não concluímos nada. Por isso, conclui-se que a conclusão será concluída quando todas tiverem concluído que já é tempo de concluir uma conclusão."
frase = frase.lower() # letra minúscula
frase = frase.replace(".",'') # troca . por nada
frase = frase.replace(",",'') # troca , por nada
frase = frase.split(" ") # coloca toda a frase dentro de uma lista e toda palavra se torna um item da lista, como se fosse uma chave
palavras = {}
for palavra in frase: # vai iterar sobre cada elemento da lista frase
    if palavra in palavras.keys(): # se a palavra em análise já for um dicionário vai acrescentar 1 no valor
        palavras[palavra] += 1
    else:
        palavras[palavra] = 1 # vai transformar a palavra em análise em uma chave do dicionário palavras, pois ele ainda não existe


carros = {
    "model": ["Mazda RX4", "Mazda RX4 Wag", "Datsun 710", "Hornet 4 Drive", "Hornet Sportabout", "Valiant", "Duster 360", "Merc 240D", "Merc 230", "Merc 280", "Merc 280C", "Merc 450SE", "Merc 450SL", "Merc 450SLC", "Cadillac Fleetwood", "Lincoln Continental", "Chrysler Imperial", "Fiat 128", "Honda Civic", "Toyota Corolla", "Toyota Corona", "Dodge Challenger", "AMC Javelin", "Camaro Z28", "Pontiac Firebird", "Fiat X1-9", "Porsche 914-2", "Lotus Europa", "Ford Pantera L", "Ferrari Dino", "Maserati Bora", "Volvo 142E"],
    "mpg": [21.0, 21.0, 22.8, 21.4, 18.7, 18.1, 14.3, 24.4, 22.8, 19.2, 17.8, 16.4, 17.3, 15.2, 10.4, 10.4, 14.7, 32.4, 30.4, 33.9, 21.5, 15.5, 15.2, 13.3, 19.2, 27.3, 26.0, 30.4, 15.8, 19.7, 15.0, 21.4],
    "cyl": [6, 6, 4, 6, 8, 6, 8, 4, 4, 6, 6, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 8, 8, 8, 8, 4, 4, 4, 8, 6, 8, 4],
    "disp": [160.0, 160.0, 108.0, 258.0, 360.0, 225.0, 360.0, 146.7, 140.8, 167.6, 167.6, 275.8, 275.8, 275.8, 472.0, 460.0, 440.0, 78.7, 75.7, 71.1, 120.1, 318.0, 304.0, 350.0, 400.0, 79.0, 120.3, 95.1, 351.0, 145.0, 301.0, 121.0],
    "hp": [110, 110, 93, 110, 175, 105, 245, 62, 95, 123, 123, 180, 180, 180, 205, 215, 230, 66, 52, 65, 97, 150, 150, 245, 175, 66, 91, 113, 264, 175, 335, 109],
    "drat": [3.9, 3.9, 3.85, 3.08, 3.15, 2.76, 3.21, 3.69, 3.92, 3.92, 3.92, 3.07, 3.07, 3.07, 2.93, 3.0, 3.23, 4.08, 4.93, 4.22, 3.7, 2.76, 3.15, 3.73, 3.08, 4.08, 4.43, 3.77, 4.22, 3.62, 3.54, 4.11],
    "wt": [2.62, 2.875, 2.32, 3.215, 3.44, 3.46, 3.57, 3.19, 3.15, 3.44, 3.44, 4.07, 3.73, 3.78, 5.25, 5.424, 5.345, 2.2, 1.615, 1.835, 2.465, 3.52, 3.435, 3.84, 3.845, 1.935, 2.14, 1.513, 3.17, 2.77, 3.57, 2.78],
    "qsec": [16.46, 17.02, 18.61, 19.44, 17.02, 20.22, 15.84, 20.0, 22.9, 18.3, 18.9, 17.4, 17.6, 18.0, 17.98, 17.82, 17.42, 19.47, 18.52, 19.9, 20.01, 16.87, 17.3, 15.41, 17.05, 18.9, 16.7, 16.9, 14.5, 15.5, 14.6, 18.6],
    "vs": [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    "am": [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    "gear": [4, 4, 4, 3, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 4, 4, 4, 3, 3, 3, 3, 3, 4, 5, 5, 5, 5, 5, 4],
    "carb": [4, 4, 1, 1, 2, 1, 4, 2, 2, 4, 4, 3, 3, 3, 4, 4, 4, 1, 2, 1, 1, 2, 2, 4, 2, 1, 2, 2, 4, 6, 8, 2]
}


for key in carros.keys():
    print(key)

# vai printar todas as chaves e somente o nome das chaves


for value in carros['hp']:
    print(value)

# vai printar todos os valores de carros na chave 'hp'


def acha_maior(lista):
    indice_maior = 0
    maior = lista[indice_maior]
    for i in range(len(lista)):
        candidato = lista[i]
        if candidato > maior:
            maior = candidato
            indice_maior = i
    return indice_maior

# começa falando que o maior é o primeiro da lista e depois vai passar por todos os items para ver se esse elemente é maior
# candidato vai ser somente uma forma de ver se outro elemento da lista é maior que a variável maior no momento
# se o candidato for maior que o maior elemento (maior) ele vai se tornar o maior
# so vai entrar no if se candidato for maior que o maior, então o índice maior vai ser o índice do maior elemento no momento
# essa função vai retornar o indice_maior

def acha_menor(lista):
    indice_menor = 0
    menor = lista[indice_menor]
    for i in range(len(lista)):
        candidato = lista[i]
        if candidato < menor:
            menor = candidato
            indice_menor = i
    return indice_menor

# tem a mesma lógica do def acha_maior porém com o menor número

def cadastrar():
    for key in carros.keys():
        info = input(f"Diga o novo {key} : ")
        carros[key].append(info)
    return

# quando vai cadastrar é preciso passar para todas as chaves do dicionario, pois precisa passar todas as informações
# então primeiro percorre todas as chaves do dicionario com o for
# info vai ser o novo valor que vai ser adicionado para cada chave
# no final é adicionado o info naquela chave analisada com o append

def obriga_opcao(msg,dicionario_opcoes):
    resposta = input(msg)
    while resposta not in dicionario_opcoes.keys():
        for key in dicionario_opcoes.keys():
            print(f"{key} : {dicionario_opcoes[key]}")
        resposta = input(msg)
    return resposta

# esse código serve para obrigar o usuário a responder alguma chave de algum dicionário
# se a resposta não for nenhuma chave do dicionário ele vai printar a todas as chaves (key) com todos os seus valores (dicionario_opcoes[key]) até que a resposta
# seja uma chave do dicionário

def remover():
    dic = {}
    for i in range(len(carros['model'])):
        dic[str(i)] = carros['model'][i]
    opcao = int(obriga_opcao("Qual carro você deseja remover ? ",dic))
    for key in carros.keys():
        carros[key].pop(opcao)
    return

# esse código vai remover todos item reverentes à aquele item do 'model'
# o primeiro for vai iterar sobre os valores da chave 'model' por índice
# depois vai transformar todos os índices em strings e também em chaves e seus valores vão ser o nome do carro naquele índice
# opcao vai armazenar o índice do carro e obriga_opcao faz com que o usuário tenha que digitar a chave de dic, pois cada chave é um índice de um carro
# pop vai remover aquele elemento de acordo com aquele índice
# o segundo for vai iterar sobre as chaves do dicionário carros e para cada chave vai remover um item com o índice escolhido (opcao)


while True:
    opcoes = ['sair','cadastrar','remover','mais potente','menos potente']
    dic = {str(i) : opcoes[i] for i in range(len(opcoes))}
    opcao = int(obriga_opcao("O que voce deseja fazer ? ",dic))
    if opcao == 0:
        print("Tchau")
        break
    elif opcao == 1:
        cadastrar()
    elif opcao == 2:
        remover()
    elif opcao == 3:
        indice = acha_maior(carros['hp'])
        for key in carros.keys():
            print(f"{key} : {carros[key][indice]}")
    elif opcao == 3:
        indice = acha_menor(carros['hp'])
        for key in carros.keys():
            print(f"{key} : {carros[key][indice]}")

# dic transforma todos os elementos de opcoes em valores de chaves e cada chave representa o indice desse elemento
# while true para sempre ficar perguntando e tem um opcao para sair com um break
# cada opcao vai chamar um função diferente


#pergunte ao usuÃ¡rio se ele é cliente ou funcionÃ¡rio
#se for cliente, de as opÃ§Ãµes de vinhos da casa e pergunte seu endereÃ§o
#pergunte informaÃ§Ãµes a respeito de qual ele quer ver
#pergunte se ele vai comprar o vinho escolhido no item anterior
#caso queira, adicione ao carrinho dele o vinho e seu preÃ§o

def obriga_opcao2(msg,lista_opcoes,max_tentativas = None):
    resposta = input(msg)
    tentativas = 1
    while resposta not in lista_opcoes:
        print("Digite uma opção válida! ")
        resposta = input(msg)
        if max_tentativas:
            if tentativas>=max_tentativas-1:
                print("Sai Hacker")
                return False
            tentativas +=1
    return resposta

# max_tentativas limita o número de tentativas que o usuário vai escolher, mas ele recebe o valor none, ou seja, se não for declarado um valor ele será nulo
# por isso é usado if max_tentativas, para ver se ele foi declarado
# return false é para encerrar a função, uma vez que só vai encerrar quando exceder o número de tentativas
# supondo que o max_tentivas seja 3, a função já vai fazer 1 primeira pergunta e tentivas é igual a 1
# se errar faz a pergunta de novo e tentativas é igual a 2 e se errar de novo, faz a pergunta novamente e tentivas fica igual a 3 o que cairia no segundo if

def login():
    usuario = obriga_opcao2("Diga seu usuario : ",["Danilo"],3)
    if usuario:
        senha = obriga_opcao2("Diga sua senha : ",['1234'],3)
    else:
        return False
    return senha and usuario

# essa função pede para o usuário fazer o login com o usuário e senha e ele vai ter somente 3 tentativas
# essa função usa a função obriga_opcao2 para a msg, o lista de opções e a tentativas
# o usuário só vai digitar a senha se ele digitar o usuário certo
# essa função precisa retornar false caso o usuário exceda o número de tentativas tanto no usuario como na senha

vinhos = {
    'tipo' : ['tinto', 'rosÃ©', 'seco', 'branco', 'suave'],
    '% alcólico' : [11,15,12,13,10],
    'safra' : [1958,1962,1970,1994,2002],
    'preço' : [100.0,130.0,20.0,25.0,50.0],
    'Nacionalidade' : ['chileno','argentino','franÃ§Ãªs','italiano','jundiaiense'],
    'estoque' : [1,20,30,40,50]
}

compra = {
    'valor total' : 0,
    'endereço' : {
        'cep' : '',
        'numero' : ''
    },
    'vinhos' : {}
}


lista_vinhos = [str(i) for i in range(len(vinhos['tipo']))]
# lista_opcoes = []
# for i in range(len(vinhos['tipo'])):
#    lista_opcoes.append(str(i))
# ['0', '1', '2', '3', '4']

def altera_preco():
    for i in range(len(vinhos['tipo'])):
        print(f"{i} - {vinhos['tipo'][i]}")
    vinho = int(obriga_opcao2("De que vinho vc vai alterar ? ",lista_vinhos))
    while True:
        try:
            preco = float(input("Diga o novo preço : "))
            if preco<0:
                raise
        except ValueError:
            print("Voce deve digitar um número com ponto ao invés de vírgula")
        except:
            print("Não pode ser negativo")
        else:
            vinhos['preço'][vinho] = preco
            print("Operação realizada com sucesso")
            break
    return

# esse código começa printando todos os vinhos com um índice
# lista_vinhos é uma maneira automatizada de sempre atualizar a quantidade de vinhos na lista com os índices
# raise é usado para gerar um excessão, para sinalizar um erro ou capturada pelo except
# quando digitar um número negativo vai aparecer "Não pode ser negativo", pois o raise sem especificar o tipo de exceção gera uma exceção genérica
# valueError é quando se tem um argumento do tipo inesperado, esperando uma float e for um int ou uma string
# se não tiver nenhum erro o preco vai alterar o preco no dicionário vinhos, na chave preço e no índice vinho que foi o que o usuário escolheu

def remove_produto():
    for i in range(len(vinhos['tipo'])):
        print(f"{i} - {vinhos['tipo'][i]}")
    vinho = int(obriga_opcao2("Qual vinho vc vai remover ? ",lista_vinhos))
    for key in vinhos.keys():
        vinhos[key].pop(vinho)
    return

# primeiro ele mostra todos os tipos de vinhos com índices
# o usuário é obrigado a digitar um índice que tem na lista
# o segundo for vai iterar sobre todas as chaves do dicionario vinhos
# vai remover atraves do pop todos os items com o índice de vinho que foi o que o usuário escolheu

#maneira 1 de fazer

def cadastra_produto():
    for key in vinhos.keys():
        if type(vinhos[key][0]) is not str:
            if type(vinhos[key][0]) is float:
                while True:
                    try:
                        info = float(input(f"Diga o/a novo/a {key} : "))
                        vinhos[key].append(info)
                        break
                    except:
                        print("precisa ser um numero com ponto")
            else:
                while True:
                    try:
                        info = int(input(f"Diga o/a novo/a {key} : "))
                        vinhos[key].append(info)
                        break
                    except:
                        print("precisa ser um numero inteiro")
        else:
            info = input(f"Diga o/a novo/a {key} : ")
            vinhos[key].append(info)
    return


# quando for cadastrar um item em um dicionário precisa dizer se ele é float, str ou int, pois dentro de um dicionário vc pode ter chaves que os valores delas sejam str, int ou float
# esse código verifica qual tipo o valor da chave é, para que quando for fazer a pergunta já converter
# primeiro é iterar sobre as chaves do dicionário
# depois ele faz a verificação se o primeiro valor da chave em análise é uma str, se for, vai fazer um input normal e ele vai sair como str
# se não for str, ele pode ser float e se não for float ele é um int
# quando for usar o try except usa o while true

tipos = {key : type(vinhos[key][0]) for key in vinhos.keys()}
#tipos1={}
#for key in vinhos.keys():
#    tipos1[key]=type(vinhos[key][0])
#print(tipos)


# maneira 2
def cadastra_produto1():
    for key in vinhos.keys():
        if vinhos[key] is not str:
            while True:
                info = float(input(f"Diga o/a novo/a {key} : "))
                try:
                    flag = 'Tem que ser um numero'
                    if tipos[key] is int:
                        info = int(info)
                    else:
                        flag += 'com ponto'
                        info = float(info)
                except ValueError:
                    print(flag)
                else:
                    vinhos[key].append(info)
                    break
        else:
            info = input(f"Diga o novo {key}")
            vinhos[key].append(info)
    return


# tipos é um dicionário que itera sobre todas as chaves do dicionário vinhos e para cada chave o valor vai ser o tipo do primeiro elemento daquela chave
# essa função itera sobre todas as chaves do dicionário vinhos e se for str ele faz um input normal e pede para o usuário escrever o novo elemento da chave
# se não for ele vai declarar o input do usuário como float e armazenar dentro de info
# se o valor da chave em análise for um número inteiro vai transformar ele em int, senão ele vai continuar sendo float
# flag é um str que vai ser

def printa_dicionarios(dic):
    for key in dic.keys():
        if type(dic[key]) is dict:
            printa_dicionarios(dic[key])
        else:
            print(f"{key} : {dic[key]}")
    return

# itera sobre as chaves do dicionário
# se a chave for um dicionario ele volta para o comeco da função
# senão printa a chave e os valores

vinhos1 = {
    'tipo' : ['tinto', 'rosê', 'seco', 'branco', 'suave'],
    '% alcólico' : [11,15,12,13,10],
    'safra' : [1958,1962,1970,1994,2002],
    'preço' : [100.0,130.0,20.0,25.0,50.0],
    'Nacionalidade' : ['chileno','argentino','franÃ§Ãªs','italiano','jundiaiense'],
    'estoque' : [1,20,30,40,50]
}

compra1 = {
    'valor total' : 0,
    'endereço' : {
        'cep' : '',
        'numero' : ''
    },
    'vinhos' : {}
}

c_f = obriga_opcao2("Voce é cliente ou funcionário ? (c/f): ",['c','f'])
lista_vinhos1 = [str(i) for i in range(len(vinhos['tipo']))]

if c_f == 'c':
    for key in compra['endereço'].keys():
        info = input(f"Diga seu {key} : ")
        compra['endereço'][key] = info
    while True:
        print("Essas são nossas opções de vinhos: ")
        for i in range(len(vinhos1['tipo'])):
            print(f"{i} - {vinhos1['tipo'][i]}")
        opcao = int(obriga_opcao2("Por qual vc se interesou ?", lista_vinhos1))
        for key in vinhos1.keys():
            print(f"{key} : {vinhos1[key][opcao]}")
        comprar = obriga_opcao2("Voce quer levar ?(s/n)", ['s','n'])
        if comprar == 's':
            if vinhos['estoque'][opcao] == 0:
                print(f"Desculpa, não temos mais estoque de {vinhos['tipo'][opcao]}")
                continue
            else:
                vinhos['estoque'][opcao] -= 1
            compra['valor total'] += vinhos['preço'][opcao]
            nome = vinhos['tipo'][opcao]
            if nome not in compra['vinhos'].keys():
                compra['vinhos'][nome] = 1
            else:
                compra['vinhos'][nome] += 1
        continuar = obriga_opcao2("Vc quer ver mais vinhos?(s/n) ", ['s', 'n'])
        if continuar == 'n':
            print("Obrigado pela sua compra:")
            printa_dicionarios(compra)
            break
