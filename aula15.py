#URL: viacep.com.br/ws/01001000/json/
# essa url e a url da api de cep, e o 01001000 e o argumento de consulta que e o cep que vc deseja consultar, neste caso e um cep ficticio

import requests
# fazer requisições HTTP, solicitações de página web, envio de dados para um servidor

#requests.get(url)
# chama a funcao get da biblioteca requests, e a funcao get solicita um recurso que neste caso e a api de cep

#response = requests.get(url)
# normalmente atribui o valor para response porque seria a resposta que a requesicao esta dando e com ela faz a manipulacao de dados


#.response.json()
# vai transformar o response em um dicionario vazio


cep = input("Diga seu cep: ")
url = f"https://viacep.com.br/ws/{cep}/json/"
response = requests.get(url)
data = response.json()
print(data)


# pede o cep
# a url recebe o endereco da api do cep e ela vai consultar o que foi digitado na variavel cep
# chama a api do cep e coloca ela na variavel response
# response.json() vai transformar a resposta da api em um dicionario e suas chaves vao ser as informacoes relacionadas ao cep (cep, logradouro, complemente) e o valor dessas chaves
# vao ser relacionadas ao cep digitado

def cep():
    while True:
        cep = input("Diga seu cep: ")
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)
        if response.status_code == 200:
            response = response.json()
            printa_dic(response)
            s_ou_n = obriga_opcao("Essas informações estão corretas (s/n) ", ["s", "n"])
            if s_ou_n == "s":
                num = input("diga o numero de sua residência: ")
                complemento = input("Diga um complemento: ")
                response['número'] = num
                response['complento'] = complemento
                compra['Endereço de entrega'] = response
                break
        else:
            print("Digite um cep válido")
    return

# comeca pedindo para o usuario escrever o cep dele e com o requests.get(url) a api vai fazer uma busca daquele cep
# porem pode acontecer do cep ser invalido, por isso usa o response.status_code pois o response esta armazenando a resposta da api, se encontrar vai mostrar todos os dados referente
# aquele cep, caso nao encontra ou nao exista vai dar um erro no codigo e .status_code ve qual erro deu ou se deu certo
# neste caso ele esta com == 200 que seria caso de certo, ou seja, se a api conseguiu encontrar aquele cep
# a variavel data serve neste caso para transformar o response (os dados do cep) em um dicionario (response.json())
# print_dic tem como parametro o data e serve para printar cada chave e o seu valor de uma vez

compra = {
    'endereço' : {},
    'valor total' : 0,
    'garrafas' : {}
          }

def obriga_opcao(msg,lista_opcoes):
    resposta = input(msg)
    if resposta not in lista_opcoes:
        print("Digite uma opção cadastrada!")
        return obriga_opcao(msg,lista_opcoes)
    return resposta
def printa_dic(dic):
    for key in dic.keys():
        if type(dic[key]) is dict:
            printa_dic(dic[key])
        else:
            print(f"{key} : {dic[key]}")
    return

response = {'data': {'languages': [{'code': 'af', 'name': 'Afrikaans'}, {'code': 'sq', 'name': 'Albanian'}, {'code': 'am', 'name': 'Amharic'}, {'code': 'ar', 'name': 'Arabic'}, {'code': 'hy', 'name': 'Armenian'}, {'code': 'az', 'name': 'Azerbaijani'}, {'code': 'eu', 'name': 'Basque'}, {'code': 'be', 'name': 'Belarusian'}, {'code': 'bn', 'name': 'Bengali'}, {'code': 'bs', 'name': 'Bosnian'}, {'code': 'bg', 'name': 'Bulgarian'}, {'code': 'ca', 'name': 'Catalan'}, {'code': 'ceb', 'name': 'Cebuano'}, {'code': 'ny', 'name': 'Chichewa'}, {'code': 'zh-CN', 'name': 'Chinese (Simplified)'}, {'code': 'zh-TW', 'name': 'Chinese (Traditional)'}, {'code': 'co', 'name': 'Corsican'}, {'code': 'hr', 'name': 'Croatian'}, {'code': 'cs', 'name': 'Czech'}, {'code': 'da', 'name': 'Danish'}, {'code': 'nl', 'name': 'Dutch'}, {'code': 'en', 'name': 'English'}, {'code': 'eo', 'name': 'Esperanto'}, {'code': 'et', 'name': 'Estonian'}, {'code': 'tl', 'name': 'Filipino'}, {'code': 'fi', 'name': 'Finnish'}, {'code': 'fr', 'name': 'French'}, {'code': 'fy', 'name': 'Frisian'}, {'code': 'gl', 'name': 'Galician'}, {'code': 'ka', 'name': 'Georgian'}, {'code': 'de', 'name': 'German'}, {'code': 'el', 'name': 'Greek'}, {'code': 'gu', 'name': 'Gujarati'}, {'code': 'ht', 'name': 'Haitian Creole'}, {'code': 'ha', 'name': 'Hausa'}, {'code': 'haw', 'name': 'Hawaiian'}, {'code': 'iw', 'name': 'Hebrew'}, {'code': 'hi', 'name': 'Hindi'}, {'code': 'hmn', 'name': 'Hmong'}, {'code': 'hu', 'name': 'Hungarian'}, {'code': 'is', 'name': 'Icelandic'}, {'code': 'ig', 'name': 'Igbo'}, {'code': 'id', 'name': 'Indonesian'}, {'code': 'ga', 'name': 'Irish'}, {'code': 'it', 'name': 'Italian'}, {'code': 'ja', 'name': 'Japanese'}, {'code': 'jw', 'name': 'Javanese'}, {'code': 'kn', 'name': 'Kannada'}, {'code': 'kk', 'name': 'Kazakh'}, {'code': 'km', 'name': 'Khmer'}, {'code': 'rw', 'name': 'Kinyarwanda'}, {'code': 'ko', 'name': 'Korean'}, {'code': 'ku', 'name': 'Kurdish (Kurmanji)'}, {'code': 'ky', 'name': 'Kyrgyz'}, {'code': 'lo', 'name': 'Lao'}, {'code': 'la', 'name': 'Latin'}, {'code': 'lv', 'name': 'Latvian'}, {'code': 'lt', 'name': 'Lithuanian'}, {'code': 'lb', 'name': 'Luxembourgish'}, {'code': 'mk', 'name': 'Macedonian'}, {'code': 'mg', 'name': 'Malagasy'}, {'code': 'ms', 'name': 'Malay'}, {'code': 'ml', 'name': 'Malayalam'}, {'code': 'mt', 'name': 'Maltese'}, {'code': 'mi', 'name': 'Maori'}, {'code': 'mr', 'name': 'Marathi'}, {'code': 'mn', 'name': 'Mongolian'}, {'code': 'my', 'name': 'Myanmar (Burmese)'}, {'code': 'ne', 'name': 'Nepali'}, {'code': 'no', 'name': 'Norwegian'}, {'code': 'or', 'name': 'Odia (Oriya)'}, {'code': 'ps', 'name': 'Pashto'}, {'code': 'fa', 'name': 'Persian'}, {'code': 'pl', 'name': 'Polish'}, {'code': 'pt', 'name': 'Portuguese'}, {'code': 'pa', 'name': 'Punjabi'}, {'code': 'ro', 'name': 'Romanian'}, {'code': 'ru', 'name': 'Russian'}, {'code': 'sm', 'name': 'Samoan'}, {'code': 'gd', 'name': 'Scots Gaelic'}, {'code': 'sr', 'name': 'Serbian'}, {'code': 'st', 'name': 'Sesotho'}, {'code': 'sn', 'name': 'Shona'}, {'code': 'sd', 'name': 'Sindhi'}, {'code': 'si', 'name': 'Sinhala'}, {'code': 'sk', 'name': 'Slovak'}, {'code': 'sl', 'name': 'Slovenian'}, {'code': 'so', 'name': 'Somali'}, {'code': 'es', 'name': 'Spanish'}, {'code': 'su', 'name': 'Sundanese'}, {'code': 'sw', 'name': 'Swahili'}, {'code': 'sv', 'name': 'Swedish'}, {'code': 'tg', 'name': 'Tajik'}, {'code': 'ta', 'name': 'Tamil'}, {'code': 'tt', 'name': 'Tatar'}, {'code': 'te', 'name': 'Telugu'}, {'code': 'th', 'name': 'Thai'}, {'code': 'tr', 'name': 'Turkish'}, {'code': 'tk', 'name': 'Turkmen'}, {'code': 'uk', 'name': 'Ukrainian'}, {'code': 'ur', 'name': 'Urdu'}, {'code': 'ug', 'name': 'Uyghur'}, {'code': 'uz', 'name': 'Uzbek'}, {'code': 'vi', 'name': 'Vietnamese'}, {'code': 'cy', 'name': 'Welsh'}, {'code': 'xh', 'name': 'Xhosa'}, {'code': 'yi', 'name': 'Yiddish'}, {'code': 'yo', 'name': 'Yoruba'}, {'code': 'zu', 'name': 'Zulu'}, {'code': 'he', 'name': 'Hebrew'}, {'code': 'zh', 'name': 'Chinese (Simplified)'}]}}

def opcoes_linguas():
    url = "https://text-translator2.p.rapidapi.com/translate"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "24f1673f5bmsh152c9863a970d4fp166efcjsn98c7e6968156",
        "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
    }

    response = requests.post(url, headers=headers)
    response = response.json()
    return response

def traduzir(texto,alvo,origem = 'en'):
    if alvo == origem:
        return texto
    # para quando quer traduzir o nome da lingua para aquela lingua
    url = "https://text-translator2.p.rapidapi.com/translate"
    payload = {
        "source_language": origem,
        "target_language": alvo,
        "text": texto
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "24f1673f5bmsh152c9863a970d4fp166efcjsn98c7e6968156",
        "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)
    response = response.json()
    return response['data']['translatedText']

print(response['data']['languages'][0]['name'])
lista = response['data']["languages"]
opcoes = {}
for i in range(len(lista)):
    codigo = response['data']['languages'][i]['code']
    nome = response['data']['languages'][i]['name']
    nome = traduzir(nome, codigo) #'pt'
    opcoes[nome] = codigo
print(opcoes)
