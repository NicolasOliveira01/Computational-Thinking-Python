
frase = "A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha."
frase = frase.replace(".",'')
frase = frase.lower()
print(frase)
print("a" == "A")
frase = frase.split(" ")
print(frase)

#.replace() serve para trocar uma string pela outra, neste caso ester substituindo o "." por nada ""
#.lower() serve para deixar todas as letras minusculas
# esta fazendo isso porque A e diferente a e aranha. e diferente de aranha
# .split() serve neste caso para colocar a frase em uma lista e cada palavra representa um elemento da lista ['A', 'aranha', 'arranha' ...]

dic = {}
for palavra in frase:
    if palavra not in dic.keys():
        dic[palavra] = 1
    else:
        dic[palavra] += 1
print(dic)

# cria um dicionario vazio para poder colocar alguma coisa dentro dele
# todas as palavras dentro da frase sao consideradas como chaves por isso .keys()


#pergunte ao usuário se ele é cliente ou funcionário
#se for cliente, de as opções de vinhos da casa e pergunte seu endereço
#pergunte informações a respeito de qual ele quer ver
#pergunte se ele vai comprar o vinho escolhido no item anterior
#caso queira, adicione ao carrinho dele o vinho e seu preço
#se for funcionário pergunte qual operação ele deseja realizar
#1-Cadastrar um novo whiskey
#2-Atualizar o preço de um whiskey
#3-Atualizar o estoque de um whiskey
#4-Deletar um whiskey da tabela


lista = [10,20,30,40]
print(lista)
lista.remove(30)
lista.pop(2)
print(lista)

#.pop serve para tirar um elemento da lista de acordo com o seu indice
# .remove vai tirar um elemento especifico da lista


def obriga_opcao(msg, opcoes):
    resposta=input(msg)
    while not resposta in opcoes:
        print("Digite uma opção cadastrada!")
        resposta=msg
    return resposta


obriga_opcao("Diga qual a sua cor? ", ['azul', 'vermelho'])


# precisa do input na primeira resposta
# precisa retornar resposta no final porque a funcao precisa saber qual foi a resposta do usuario


def printa_dic(dic):
    for key in dic.keys():
        if type(dic[key]) is dict:
            printa_dic(dic[key])
        else:
            print(f"{key} : {dic[key]}")
    return

my_dict = {
    'nome': 'Alice',
    'idade': 30,
    'endereco': {
        'rua': '123 Main Street',
        'cidade': 'Cidade Exemplo',
        'cep': '12345-678'
    },
    'telefones': {
        'casa': '555-1234',
        'trabalho': '555-5678'
    }
}
printa_dic(my_dict)


# serve para colocar as chaves e os seus valores um embaixo do outro
# ele primeiro vai percorrer pelas chaves do dicionario
# se a chave do dicionario for um dicionario ele volta para o comeco da funcao
# depois disso ele nao vai ser mais um dicionario e vai ter chaves dentro dele e vai cair no else
# dic[key] vai ser o valor que esta dentro da chave e nao a chave em si
# quando a funcao if type(dic[key]) is dict: chega no endereco vai ver se o valor de endereco e um dicionario
# e o valor de endereco realmente e um dicionario
# nao pode colocar um return depois do if, preciso colocar o printa_dic(dic[key]) para ele voltar para o comeco da funcao

def checa_estoque(opcao):
    if whiskeys['estoque'][opcao] == 0:
        return False
    whiskeys['estoque'][opcao] -= 1
    return True

# cada whiskeys possui uma quantidade e essa funcao verifica se tem whiskeys disponiveis
# opcao vai ser o indice whiskey que o usuario escolheu
# essa funcao vai analisar o estoque do whiskey escolhido pelo usuario
# precisa retornar false ou true porque depois ela vai ser usado em um if
# if checa_estoque(opcao) ou seja, so vai entrar nesse if se for verdadeiro
# nao pode colocar um else para ver se ele tem pelo menos 1 quantidade disponivel, porque essa funcao precisa tirar 1 quantidade do whiskey

def cadastrar():
    for key in whiskeys.keys():
        info = input(f"Diga o/a novo/a {key} : ")
        whiskeys[key].append(info)
    return

# coloca mais um whiskey no dicionario whiskeys porem e necessario colocar as informacoes de cada chave
# vai percorrer as chaves do dicionario whiskeys
# vai perguntar todas as novas chaves e esses valores vao ser armazenados em info
# info vai ser adicionado ao valor de cada chave dentro do dicionario
# para colocar cada nova informacao (novo) precisa colocar um append(info) e nao apenas o infoe tambem [key] nao precisa de ''

def alterar(preco_estoque):
    for i in range(len(whiskeys['tipo'])):
        print(f"{i} - {whiskeys['tipo'][i]}")
    qual = int(obriga_opcao(f"De que whiskey vc irá alterar o {preco_estoque}?",opcoes))
    novo = input(f"Diga o novo {preco_estoque}")
    whiskeys[preco_estoque][qual] = novo
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

# esse codigo serve para tirar alguma chave dentro das listas do dicionario whiskeys
# o primeiro for serve para ele indicar qual o indice do valor de todas as chaves que ele quer remover
# esse indice vai ser armazenado em qual e precisa de outro for para iterar sobre todas as chaves do dicionario whiskeys, porque precisa tirar todos os valores com o indice qual
# whiskeys[key].pop(qual) vai tirar todos os valores com o indice qual de todas as chaves do dicionario

whiskeys = {
    'tipo' : ['bourbon', 'blended', 'scotch', 'single malt', 'double malt'],
    '% alcoólico' : [11,15,12,13,10],
    'safra' : [1958,1962,1970,1994,2002],
    'preço' : [100,130,20,25,50],
    'Nacionalidade' : ['chileno','argentino','françês','italiano','jundiaiense'],
    'estoque' : [1,34,54,12,11]
}
compra = {
    'endereço' : {
        'Rua' : '',
        'Cep' : '',
        'Número': ''},
    'valor total' : 0,
    'garrafas' : {}
          }
opcoes = [str(i) for i in range(len(whiskeys['tipo']))] # ['0', '1', '2', '3', '4']
papel=obriga_opcao("Voce e um cliente ou um funcionario? (c/f): ", ['c', 'f'])
if papel == 'c':
    print("Seja bem vindo!")
    for key in compra['endereço'].keys():
        info = input(f"Diga seu/a {key}")
        compra['endereço'][key] = info
# nao precisa colocar um compra['endereco'][key] dentro do input pois voce ja esta acessando as chaves do dicionario endereco atraves do for
    while True:
        print("Essas são nossas opções de whiskeys : ")
        for i in range(len(whiskeys['tipo'])):
            print(f"{i} : {whiskeys['tipo'][i]}") # no segundo print precisa do [i] para ele printar somente um whiskeys
        opcao = int(obriga_opcao("Qual vinho lhe interessou mais ? ",opcoes))
        print("Essas sao as informacoes sobre esse vinho: ")  # esse print precisa estar fora do for
        for key in whiskeys.keys():
            print(f"{key} : {whiskeys[key][opcao]}")
        comprar = obriga_opcao("Vai levar ? (s/n) ",['s','n'])
        if comprar == 's' and checa_estoque(opcao):
            compra['valor total'] += whiskeys['preço'][opcao] # vai colocar o preco do whiskey comprado na chave valor_total
            qual = whiskeys['tipo'][opcao] # armazena qual o tipo de whiskey que foi comprado
            if qual not in compra['garrafas'].keys(): # se o tipo de whiskey nao estiver em garrafas
                compra['garrafas'][qual] = 1 # dentro da chave garrafas vai aparecer o tipo de whiskeys (qual)
            else:
                compra['garrafas'][qual] += 1
            # maneira mais facil de mostrar somente as garrafas que foram compradas e adicionar as que ja foram
        elif comprar != 'n':
            print(f"Desculpe, infelizmente não há mais estoque de {whiskeys['tipo'][opcao]}")
        continuar = obriga_opcao("Quer ver mais opceos ? ", ['s', 'n'])
        if continuar == 'n':
            print("Obrigado por comprar conosco!\nEsse é o resumo de sua compra")
            printa_dic(compra)
            break
else:
    while True:
        operacao = obriga_opcao("Qual operação vc deseja realizar:\n"
                                    "1-Cadastrar novo produto\n"
                                    "2-Alterar preço\n"
                                    "3-Alterar estoque\n"
                                    "4-Remover Produto\n"
                                    "5-sair", ['1', '2', '3', '4', '5'])
        if operacao == '1':
            cadastrar()
        elif operacao == '2':
            alterar('preço')
        elif operacao == '3':
            alterar('estoque')
            print(pd.DataFrame(whiskeys))
        elif operacao == '4':
            remover()
        continuar=obriga_opcao("Quer realizar mais operacoes? (s/n): ", ("s", "n"))


