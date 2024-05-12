def forca_opcao(msg,lista_opcoes):
    resposta=input(msg)
    while not resposta in lista_opcoes:
        print("Digite uma opcao cadastrada: ")
        resposta=input(msg)
    return resposta

#forca_opcao(f"Você é cliente ou funcionário ? (c/f)", ['c','f'])

# while nor resposta == lista_opcoes (esta errado)
# neste caso vai verificar se resposta e extamente igual a lista_opcoes, o que nunca vai acontecer pq resposta e uma string e lista_opcoes e uma lista
# entao ele nunca vai dar como resposta certa
# o certo e usar o in lista_opcoes pois vai verificar se o input de resposta vai ser igual a alguma string da lista lista_opcoes

whiskeys = {
    'tipo' : ['bourbon','blended','scotch','single malt','double malt'],
    '%alcoolico' : [41,50,35,62,37],
    'volume (ml)' : [1000,750,50,100,800,2000],
    'idade' : [15,12,8,8,10],
    'preco' : [14,23,541,65,999,],
    'marca' : ['jack Daniels','White Horse','Passport','Johnie Walker','Chanceler'],
}

#whiskeys e um dicionario que contem varias chaves (tipo,%alcoolico,volume(ml),idade,preco,marca) e suas listas

compra = {
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

# valor_total e uma chave que comeca com o valor 0
# garrafas e um dicionario vazia
# endereco e um dicionario e dentro dele possui a suas sub-chaves


cliente_funcionario=forca_opcao("Voce e cliente ou funcionario? (c/f): ", ['c','f'])
if cliente_funcionario == 'c':
    nome=input("Digite seu nome: ")
    compra['nome']=nome
    for key in compra['endereco'].keys():
        info = input(f"Digite seu {key}: ")
        compra['endereco'][key]=info
    print(f"Seja bem vindo/a {nome}!")
    while True:
        print("Essas sao nossas opcoes de whiskeys: ")
        for i in range(len(whiskeys['tipo'])):
            print(f"{i} : {whiskeys['tipo'][i]}")
        opcao=int(forca_opcao("Qual deles voce mais gostou? [0,1,2,3,4]: ", ['0','1','2','3','4']))
        for key in whiskeys.keys():
            print(f"{key} : {whiskeys[key][opcao]}")
        comprar = forca_opcao("Voce vai levar ? (s/n)", ["s", "n"])
        if comprar == 's':
            compra['valor_total'] += whiskeys['preco'][opcao]
            marca = whiskeys['marca'][opcao]
            if marca not in compra['garrafas']:
                compra['garrafas'][marca] = 1
            else:
                compra['garrafas'][marca] += 1
        continuar = forca_opcao('Voce quer comprar mais whiskeys ? (s/n)', ['s', 'n'])
        if continuar == 'n':
            print("Resumo do seu pedido : ")
            for key in compra.keys():
                if type(compra[key]) is dict:
                    for key2 in compra[key].keys():
                        print(f"{key2} : {compra[key][key2]}")
                        # Isso é ganbiarra, tem que fazer uma function
                else:
                    print(f"{key} : {compra[key]}")
            break



# compra e o dicionario e o ['nome'] e a chave e o input nome vai estar dentro da chave nome

# compra['endereco'][key]=info serve para que as informacoes sejam registradas nas chaves da compra['endereco'], caso ela n estiver no final nao vai mostrar o que o usuario digitou nas chaves

# .keys() vai retornar todas as chaves do dicionario endereco, que esta detro do dicionario compra
#  for key in itera por todas as chaves do dicionario compra['endereco']
#  rua, numero, cep, bairro, cidade
# em um dicionario nao tem como acessar os elementos por indice como uma lista

# precisa do int na opcao pois ele esperava um numerico porem as listas so aceitam strings
# as entradas do usuario sao lidas como string quando usa o input

# print(f"{key} : {whiskeys[key][opcao]}") o porque de usar o [key]
# neste caso o dicionario precisa analisar uma chave e o dicionario precisa de um parametro para colocar essas chaves
# como key percorre pelas chaves do dicionario whiskyes ele foi usado como parametro


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
}

# primeiro vai perguntar se é cliente ou funcionario
# se for cliente perguntar o nome
# mostrar todas as informoções sobre o endereço
# fazer um loop infinito mostrando as opcoes de whiskeys com numera pra cada um
# mostrar todas as informções sobre esse whiskey escolhido
# perguntar se ele vai levar e se sim colocar o preco no dicionario
# colocar somente no dicionario os whiskeys comprados ou adicionar se ja estiver um



