
lista=[4,5,6,7,9]
while True:
    try:
        i = int(input("Diga um número: "))
        print(lista[i])
    except ValueError:
        print("Você não digitou um inteiro")
    except IndexError:
        print(f"Deve ser entre 0 e {len(lista)}")
    except Exception as e:
        print(e)
    else:
        print("Operação realizada com sucesso!")
        break
    finally:
        print("Não sirvo para muito coisa")


# o usuario vai digitar um numero e o código vai retornar o número com esse índice na lista
# porém, existem vários erros que podem acontecer, o usuário não digitar um número, digitar um índice que não existe
# ValueError é quando o usuário não digitar um número inteiro, como uma string
# IndexError é quando o usuário digita um índice inválido
# Exception as e é só quando não for um ValueError ou um IndexError, o programa vai imprimir a mensagem de erro associada a essa exceção específica
# exception (e) vai ser outro erro que não tem no except
# o break no else é para sair do loop while
# finally sempre vai printar mesmo quando der certo ou errado


while True:
    try:
        flag = "primeiro"
        a = int(input("Diga o primeiro numero : "))
        flag = "segundo"
        b = int(input("Diga o segundo numero : "))
        resultado = b/a
    except ValueError:
        print(f"O {flag} numero está errado")
    except ZeroDivisionError:
        print("O primeiro número não pode ser zero!")
    else:
        print(resultado)
        break


# quando o usuário for digitar para o 'a' e o 'b', se não for um número inteiro logo vai entrar o ValueError
# antes de pedir a e b a variável flag é atualizada
# o erro ZeroDivisionError vai ocorrer mais tarde, ou seja, mesmo que o 'a' for igual a 0 ele ainda vai perguntar o input 'b' ocorre devido à natureza da
# exceção ZeroDivisionError
# se o a for igual a zero ele vai entrar no ZeroDivisionError porque qualquer número dividido por 0 da erro

times = {
    'são paulo' : 'campeão',
    'corinthians' : 'sem tite',
    'palmeiras' : 'sem mundial',
    'santos' : 'idoso rebaixado'
}


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

