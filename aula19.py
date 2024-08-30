# REVISÃO DE PYTHON 07/11

# TRY EXCEPT


lista=[4,5,6,7,9]
while True:
    try:
        i = int(input("Diga um número: "))
        print(lista[i])
    except ValueError:
        print("Você não digitou um inteiro")
    except IndexError:
        print(f"Deve ser entre 0 e {len(lista)}")
    except NameError:
        print("Alguma variavel nao foi definida")
    except Exception as e:
        print(e)
    else:
        print("Operação realizada com sucesso!")
        break
    finally:
        print("Não sirvo para muito coisa")

# Neste exemplo tem uma lista com as str a,b e c; e ele pede para o usuário digitar um número que depois vai printar o elemento com esse índice na lista
# Porém, o usuário pode digitar alguma coisa que pode dar um erro, e esses excepts seriam os tipos de erros que seriam possíveis
# ValueError -> quando tenta converter uma string para um int, neste caso i vai ser obrigatóriamente transformado em int
# IndexError -> quando o usuário digita um índice que não existe, se o usuário digitar 4 vai dar esse erro
# NameError -> quando tenta acessar uma variável que não foi definida
# Exception as e -> quando tem outro tipo de expeption
# Finally -> sempre vai ser executado, mesmo quando ocorrer algum except ou não
# else vai ser executado quando não acontecer nenhum except e neste caso vai printar qual a letra e um print que deu certo, precisa do break por causa do while True


while True:
    try:
        num1 = float(input("Diga um numero: "))
        num2 = float(input("Diga o segundo numero: "))
        print(num1/num2)
    except ZeroDivisionError:
        print("n pode dividir por zero bobao")
    except ValueError:
        print("Tem que ser numero mano")
    else:
        print("Voce nao e tao bobao")
        break

# o código pede para o usuário digitar dois números e depois faz a divisão deles
# ZeroDivisionError -> quando tenta fazer uma divisão com o denominador com 0
# ValueError -> quando digita uma str neste caso

while True:
    try:
        flag = "primeiro"
        a = int(input("Diga o primeiro numero: "))
        flag = "segundo"
        b = int(input("Diga o segundo numero: "))
        resultado = b/a
    except ValueError:
        print(f"O {flag} numero está errado")
    except ZeroDivisionError:
        print("O primeiro número não pode ser zero!")
    else:
        print(resultado)
        break


# o código pede para o usuário digitar dois números e flag vai armazenar qual número não foi um int
# se a não for int logo vai aparecer o erro e vai aparecer o primeiro flag e a mesma coisa com o b
# ValueError -> quando o número neste caso não for um int, se o usuário digitar uma str
# ZeroDivisionError -> quando o denominador for 0

times = {
    'são paulo' : 'campeão',
    'corinthians' : 'sem tite',
    'palmeiras' : 'sem mundial',
    'santos' : 'idoso rebaixado'
}

# esse dicionário tem chaves que são times e cada chave tem seu valor
# se printar times e qualquer chave vai printar o valor dessa chave


while True:
    time = input("Diga seu time : ")
    try:
        print(f"Você é um {times[time]}")
        break
    except KeyError:
        print(f"Você deve digitar um desses: {times.keys()}")


# esse código pede primeiro para o usuário digitar um time
# o time que o usuário digitar vai mostrar o valor daquele time que é uma chave do dicionário
# KeyError -> quando tenta acessar uma chave que não existe
# times.keys() vai mostrar todas as chaves daquele dicionário


while True:
    time = input("Diga seu time : ")
    try:
        print(f"Você é um {times[time]}")
        break
    except KeyError:
        print(f"Você deve digitar um desses: {times.keys()}")


# o dicionário times tem suas chaves como nomes de times e cada um tem um valor específico
# time é um input e dentro do try vai mostrar o valor da chave que o usuário digitou
# KeyError é quando a chave não é encontrada
# times.keys() -> times é o dicionário,.keys() percorre pelas chaves do dicionario e fala que só pode escolher entre essas chaves

# FUNÇÕES IMPORTANTES PARA FAZER O MENU SEM TRY EXCEPT

#exemplo de dicionário
vinhos = {
    'tipo' : ['tinto', 'rosÃ©', 'seco', 'branco', 'suave'],
    '% alcólico' : [11,15,12,13,10],
    'safra' : [1958,1962,1970,1994,2002],
    'preço' : [100.0,130.0,20.0,25.0,50.0],
    'Nacionalidade' : ['chileno','argentino','franÃ§Ãªs','italiano','jundiaiense'],
    'estoque' : [1,20,30,40,50]
}

def acha_maior(lista):
    indice_maior=0
    maior=lista[0]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior=lista[i]
            indice_maior=i
    return indice_maior

# para funcionar para o menor basta trocar os nomes de maiores para menores e trocar o sinal de > para <
# esse código começa falando que o primeiro da lista é o maior elemento
# depois ele itera sobre todos os elementos da lista e se o número analisado for > que o maior atual, ele se torna o maior e pega o índice desse número

def acha_menor(lista):
    indice_menor=0
    menor=lista[0]
    for i in range(len(lista)):
        if lista[i]<menor:
            menor=lista[i]
            indice_menor=i
    return indice_menor

def cadastrar():
    for key in vinhos.keys():
        info=input(f'Digite o novo {key}: ')
        vinhos[key].append(info)
    return

# esse código cadastra um novo vinho, por causa disso ele itera sobre todas as chaves do dicionário e pede para o usuário digitar o novo key
# como ele quer cadastrar ele precisa usar o .append(info) pois ele está adicionando um novo valor para cada chave
# neste caso não pode usar vinhos[key] = info pois ele deixará de ser uma lista

def obriga_opcao(msg, lista):
    resposta=input(msg)
    while not resposta in lista:
        print('Você só pode responder as opções disponíveis!')
        resposta=input(msg)
    return resposta


# essa função vai obrigar ao usuário a digitar sempre as opções disponíveis e ela tem como parâmetro a mensagem e a lista de opções disponíveis
# resposta precisa ser um input
# pode ser while not resposta in lista ou while resposta not in lista
# essa função precisa retornar a resposta para ser usado posteriormente

def remover():
    for i in range(len(vinhos['tipo'])):
        print(f"{i} : {vinhos['tipo'][i]}")
    opcao=int(obriga_opcao('Quais das opções você vai querer remover? ([0,1,2,3,4])', ['0','1','2','3','4']))
    for key in vinhos.keys():
        vinhos[key].pop(opcao)

# esse código remove todas as informações de um vinhos específico do dicionário
# ele coloca índices para cada tipo de vinho e pede para o usuário escolher 1 e guarda em opcao
# itera sobre as chaves do dicionário e para todas as chaves ele remove através da função .pop com o índice opcao que foi o índice que o usuário escolheu

def obriga_opcao_tentativas(msg, lista_opcoes, max_tentativas=None):
    resposta=input(msg)
    tentativas=1
    while resposta not in lista_opcoes:
        print('Você só pode responder entre a lista de opções!')
        resposta=input(msg)
        if max_tentativas:
            if tentativas>=max_tentativas-1:
                print('Sai hacker')
                return False
        tentativas+=1
    return resposta
# max_tentativas = none significa que se o usuário não colocar um parâmetro para max_tentativas as tentativas vão ser infinitas
# if max_tentativas é para ver justamente se o max_tentativas foi declarado
# precisa ser >= e ter o -1 no max_tentativas e dentro desse if precisa retornar false
# tentativas+=1 pode ter a identação de qualquer if

def login():
    usuario=obriga_opcao_tentativas('Digite seu usuário: ', ['Nicolas'], 3)
    if usuario:
        senha=obriga_opcao_tentativas('Digite sua senha: ', ['1234'], 3)
    else:
        return false
    return senha and usuario

# essa função pede para o usuário digitar o seu usuário e sua senha
# primeiro ele usa a função obriga_opcao_tentativas e ele só vai escrever a senha se ele passar na parte do usuário
# caso ele não consiga passar na parte do usuário e a senha cai no else e essa função retorna false
# se ele conseguiu passar pelo usuário e senha vai retornar elas

def printa_dicionario(dic):
    for key in dic.keys():
        if type(dic[key]) is dict:
            printa_dicionario(dic[key])
        else:
            print(f'{key} : {dic[key]}')
    return

# essa função mostra o dicionário de uma forma bonita
# porém um dicionário pode ter como chave um outro dicionário
# por isso ele começa iterando sobre as chaves do dicionário e se a chave for um dicionário ele volta para a função
# porém precisa passar o dic[key] e não somente key
# se não for um dicionário fazer um print(f'{key} : {dic[key]}') para mostrar bonitinho

# FAZENDO AS FUNÇÕES DE ALTERAR E CADASTRAR UM NOVO VINHO

# quando for cadastrar ou alterar o vinho não pode simplesmente colocar o novo vinho como str para todas as chaves do dicionário, porque nem sempre todas elas vão
# ser str, elas podem ter str, int e float, portanto é necessário verificar o tipo do primeiro elemento da lista para converter o novo vinho para esse tipo, por
# isso usa o try except

# dicionário de exemplo
vinhos1 = {
    'tipo' : ['tinto', 'rosÃ©', 'seco', 'branco', 'suave'],
    '% alcólico' : [11,15,12,13,10],
    'safra' : [1958,1962,1970,1994,2002],
    'preço' : [100.0,130.0,20.0,25.0,50.0],
    'Nacionalidade' : ['chileno','argentino','franÃ§Ãªs','italiano','jundiaiense'],
    'estoque' : [1,20,30,40,50]
}

def cadastrar_produto():
    for key in vinhos1.keys():
        if type(vinhos1[key][0]) is not str:
            if type(vinhos[key][0]) is float:
                while True:
                    try:
                        info=float(input(f'Digite o/a novo/a {key}: '))
                        vinhos1[key].append(info)
                        break
                    except:
                        print('Você precisa digitar um float')
            else:
                while True:
                    try:
                        info=int(input(f'Digite o/a novo/a {key}: '))
                        vinhos1[key].append(info)
                        break
                    except:
                        print('Você precisa digitar um int')
        else:
            info=input(f'Digite o/a novo/a {key}: ')
            vinhos1[key].append(info)
    return

# esse código cadastra um produto no dicionário, então ele pergunta qual será o novo key para o usuário
# e esse código já faz a conversão do tipo de elemento dentro da lista quando for perguntar ao usuário
# primeiro ele itera sobre as chaves do dicionário
# ele basicamente ve se é str, se não for ele pode ser float ou int e já faz a conversão
# para colocar no dicionário não precisa de um else, basta colocar no try e depois um break porque está no while true

lista_opcoes = ['0','1','2','3','4']

def altera_preco():
    for i in range(len(vinhos1['tipo'])):
        print(f"{i} - {vinhos1['tipo'][i]}")
    opcao = int(obriga_opcao("De que vinho vc vai alterar ? ",lista_opcoes))
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
            vinhos1['preço'][opcao] = preco
            print("Operação realizada com sucesso")
            break
    return

# esse código altera somente a lista de preços do dicionário vinhos1, então ele coloca um índice para cada tipo e pede para o usuário escolher
# usa um try except porque o tipo dentro da lista preço é float e também não pode ser negativo
# o raise força a cair na except que tem um print falando que não pode ser negativo
# se der certo, o preço do vinho que o usuário escolheu vai ser trocado
# break precisa der um break porque está dentro de um while true



# MENU DO CLIENTE E FUNCIONÁRIO

# primeiro verifica se é cliente ou funcionário
# se for cliente peça para o usuário digitiar as informações do endereço
# de as opções de vinhos e pergunte qual deles ele se interessou
# mostre todas as informações sobre esse vinho
# pergunte se quer comprar, se sim verifique se tem no estoque e se tiver tire 1 do estoque desse vinho, coloque o preço no valor_total e crie ou acrescente uma
# chave com o nome do vinho e seu valor com a quantidade que o usuário escolheu
# pergunte se quer continuar e se não mostre o resultado total
# se for funcionário peça para ele fazer login e depois ele escolhe se ele quer alterar, remover, cadastrar, sair

vinhos2 = {
    'tipo' : ['tinto', 'rosê', 'seco', 'branco', 'suave'],
    '% alcólico' : [11,15,12,13,10],
    'safra' : [1958,1962,1970,1994,2002],
    'preço' : [100.0,130.0,20.0,25.0,50.0],
    'Nacionalidade' : ['chileno','argentino','franÃ§Ãªs','italiano','jundiaiense'],
    'estoque' : [1,20,30,40,50]
}

compra2 = {
    'valor_total' : 0,
    'endereço' : {
        'cep' : '',
        'numero' : '',
    },
    'vinhos' : {}
}


c_f=obriga_opcao('Você é um cliente ou um funcionário? (c/f): ', ['c','f'])
lista_opcoes1= ['0','1','2','3','4',]
if c_f=='c':
    print('Bem vindo a loja de vinhos')
    for key in compra2['endereço'].keys():
        info=input(f'Digite seu {key}: ')
        compra2['endereço'][key]=info
    for i in range(len(vinhos2['tipo'])):
        print(f'{i} : {vinhos2["tipo"][i]}')
    opcao=int(obriga_opcao('Qual dos vinhos você mais se interessou? (0,1,2,3,4): ', lista_opcoes1))
    for key in vinhos2.keys():
        print(f'{key} : {vinhos2[key][opcao]}')
    comprar=obriga_opcao('Você vai querer comprar? (s/n): ', ['s','n'])
    if comprar=='s':
        if vinhos2['estoque'][opcao] == 0:
            print(f'Desculpa mas nós não temos mais {vinhos2["tipo"][opcao]} no estoque')
        else:
            vinhos2['estoque'][opcao] -= 1
        compra2['valor_total'] += vinhos2['preço'][opcao]
        nome = vinhos['tipo'][opcao]
        if nome not in compra2['vinhos'].keys():
            compra2['vinhos'][nome] = 1
        else:
            compra2['vinhos'][nome] += 1
    continuar=obriga_opcao('Você quer continuar? (s/n): ', ['s','n'])
    if continuar == 'n':
        printa_dicionario(compra2)
        print('Obrigado por vir')
    else:
        print('é funcionario')
else:
    if login():
        while True:
            operacao = obriga_opcao("Qual operacao vc deseja realizar ?\n0-Alterar preÃ§o"
                                    "\n1-Remover produto\n2-Cadastrar produto"
                                    "\n3-Sair\n-> ", ['0', '1', '2', '3'])
            if operacao == '0':
                altera_preco()
            elif operacao == '1':
                remover()
            elif operacao == '2':
                cadastrar()
            else:
                print("OperaÃ§Ã£o realizada com sucesso!")
                break
    else:
        print("Encerrando programa!")


# Na parte do endereço precisa do .keys() no compra2['endereço'].keys() e também precisa do [key] em compra2['endereço'][key], além de ser = info não .append(info)
# a opcao precisa ser um int
# quando for tirar do estoque o vinho só essa parte precisa estar dentro do else e resto é com mesma identação
# precisa colocar qual o tipo de vinho que ele comprou em uma variável nome = vinhos['tipo'][opcao]
# quando for verificar se essa variavel for ou não uma chave de compra2['vinhos'] precisa do .keys()
# precisa do not in para ver se a variável que armazena a escolha do vinho é uma chave do dicionário compra2['vinhos']

def acha_maior_lista(lista):
    msg='Deve ser uma lista com números int ou float'
    if type(lista) is not list:
        raise ValueError(msg)
    for elem in lista:
        if type(elem) is not [float, int]:
            raise TypeError(msg)
    else:
        indice_maior=0
        maior=lista[0]
        for i in range(len(lista)):
            if lista[i] > maior:
                maior=lista[í]
                indice_maior=i
    return indice_maior

# esse código ve qual é o maior da lista, porém antes ele verifica se a lista é realmente uma lista e se os elementos detro dela são int ou float
# raise é para forçar um erro e ValueError é quando você quer converter uma str em int por exemplo
# TypeError quando quer somar por exemplo 5 + '10'
# defini o maior como o primeiro da lista e passa por todos os outros elementos da lista e se algum for maior ele se torna a variável maior e guarda seu índice

# COMO ORDENAR UMA LISTA

lista=[4,2,5,7,6,1,3]

def selection_sort_pior(lista):
    ordenada=[]
    #for i in range(len(lista)):
    while lista:
        indice=acha_menor(lista)
        menor=lista.pop(indice)
        ordenada.append(menor)
        print(lista)
        print(ordenada)
        print()
    return ordenada

# while lista significa enquando a lista estiver elemento
# esse código tem uma lista não ordenada e uma lista vazia
# acha o menor da lista e chama de indice
# tira o indice da lista e guarda esse número em um variável
# coloca o menor na lista na lista ordenada que é uma lista vazia
# esse código é uma maneira de ordenar a lista mas é uma maneira ruim de fazer isso


lista1=[4,2,5,7,6,1,3]
#print(lista1[3:]) # começa a partir do indice 3

def selection_sort_ruim(lista):
    for i in range(len(lista)):
        indice_sublista=acha_menor(lista[i:])
        indice_lista=indice_sublista+i
        print(f"O numero {lista[indice_lista]}, na sublista {lista[i:]} está no índice {indice_sublista}, porém na lista original {lista}, está no {indice_lista}")
        aux = lista[i]
        lista[i] = lista[indice_lista]
        lista[indice_lista] = aux
        print(lista)
    return lista

#selection_sort_ruim(lista1)

# indice_sublista é o índice do menor número na lista completa, pois ele chama a função acha_menor e seu parãmetro é a lista e a cada iteração ela diminui um número
# (lista[i:]) significa que a cada iteração do for a lista vai começar a partir daquele i (índice analisado no momento), ou seja, a lista vai diminuir 1 da esqueda
# para a direita a cada iteração. a sublista sempre vai ser a lista da lista completa dos números que não estão ordenados
# indice_lista é o índice do menor número na lista completa, pois ele é o índice do menor número da lista mais o i do for. Exemplo:
# a sublista é [6, 7, 5] e a lista é [1, 2, 3, 4, 6, 7, 5]. i do for está no valor 4, o indice_sublista neste caso é 2 (indice do 5) e o indice_lista é 6, ou seja,
# indice_sublista (2) + i (4) = indice_lista (6)
# neste caso não poderia simplesmente colocar em uma variável o menor da lista porque sempre ia achar o mesmo número, por isso precisa da sublista e é por isso que
# usa o lista[i:], pois vai tirando os números que já estão ordenados e acha o menor dessa lista sem esses números
# indice_sublista é uma maneira que vai servir para encontrar o menor da lista completa e não vai usar diretamente essa variável no final
# depois de encontrar o indice_lista, precisa trocar o primeiro, segundo, terceiro ... até ordenar a lista e para fazer isso precisa de outra variável que no caso
# vai ser a veriável aux


lista3=[4,2,5,7,6,1,3]

def bubble_sort(lista):
    for i in range(len(lista)):
        trocou = False
        print(f"{i + 1}º passo : ")
        for j in range(len(lista)-i-1):
            if lista[j]>lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
                trocou = True
                print(lista)
        print()
        if not trocou:
            return lista

#bubble_sort(lista3)

# esse código vai analisar dois números da lista e ver se o primeiro número é maior que o do seu lado, se for maior ele vai trocar os dois de lugar e se não for
# quer dizer que esses números já estão ordenados e esse código sempre vai ficar colocando o maior número no final e vai ordenando a lista
# Tudo que está dentro do for ele vai executar a cada iteração e quando chega no for j ele executa tudo que está dentro para depois ir no if not trocou
# quando tem um range(len(lista)) em um for significa que ele vai começar do 0 e vai até o tamanho da lista -1 e (len(lista)) é o número do tamanho da lista
# então o range(len()) dentro de um for diz que o número vai começar do 0 e vai até um certo número e neste caso a partir que o i vai aumentando o j vai diminuindo,
# ou seja, o j vai ter menos iterações.
# range(len(lista3) -i - 1 -> quando o i for igual a 4, vai ser 7 - 4 - 1 - 1 = 1, ou seja, quando o i for 4 o j vai de 0 a 1 fazendo 2 iterações
# se o número analisado for maior que o seu do lado ele vai trocar e o trocou = true vai ser só uma forma de printar somente quando a lista ja estiver ordenada

#exemplo para entender um for dentro de um for

for i in range(len(lista3)): #0,1,2,3,4,5,6
    print(f'para i={i}')
    for j in range(len(lista3)-i -1):
        print(j)
    print()
'''
'''
para i=0
j -> 0,1,2,3,4,5
para i=1
j -> 0,1,2,3,4
para i=2
j -> 0,1,2,3
para i=3
j -> 0,1,2
para i=4
j -> 0,1
para i=5
j -> 0
para i=6

