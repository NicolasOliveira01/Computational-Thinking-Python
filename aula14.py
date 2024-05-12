import requests

"""
url = "https://pokeapi.co/api/v2/pokemon/pikachu"
response=requests.get(url)
print(response.json())
"""

# a biblioteca requests serve para fazer uma requisição HTTP a uma API da web
# a função get é usada para receber uma resposta do servidor web
# Isso envia uma solicitação HTTP para a API da Pokémon para obter informações sobre o Pokémon "Pikachu" e é armazenado na response
# .json converte os dados JSON recebidos da API em um dicionário Python

dic = {
    'data': {
         "languages": [
            {
                "code": "af",
                "name": "Afrikaans"
            },
        ]
    }
}

"""
dic1 = dic['data']['languages'][0]
print(dic1) # {'code': 'af', 'name': 'Afrikaans'}
nome=dic1['name']
sigla=dic1['code']
print(nome) # Afrikaans
print(sigla) # af
novo={}
novo[sigla]=nome
print(novo) # {'af': 'Afrikaans'}
lingua=input("para qual lingua vc deseja traduzir? ") # af
print(novo[lingua]) # afrikaans
"""

# dic1 vai receber o primeiro elemento da lista
# coloca o Afrikaans dentro da variavel nome
# coloca o af dentro da variavel sigla
# cria um dicionario vazio chamado novo e a chave dele e um dicionario que vai ser a sigla (af) e ela vai receber como valor o nome (afrikaans)
# imagine que voce tenha varias chaves dentro de languages que sao o code e o name de cada lingua. O que esta acontecendo e associar o code ao nome
# ou seja, se a pessoa digitar o code da lingua automaticamente vai retornar o name da lingua
# novo[sigla] = nome. Se a chave sigla ja existir no dicionario novo, ela substituira pelo novo valor nome
# se a chave sigla nao existir no dicionario novo uma nova entrada sera criada com a chave sigla e o valor nome

"""
times = {"São Paulo" : "vencedor"}
times['São Paulo'] = 'perdedor'
time = input("Pra que time vc torce ? ")
print(f"Você é um {times[time]}")
"""

# neste caso como a chave Sao paulo ja existe, ele substituiu o valor
# se nao existisse a chave sao paulo, criaria uma chave e atribuiria seu valor

linguas = {'data': {'languages': [{'code': 'af', 'name': 'Afrikaans'}, {'code': 'sq', 'name': 'Albanian'}, {'code': 'am', 'name': 'Amharic'}, {'code': 'ar', 'name': 'Arabic'}, {'code': 'hy', 'name': 'Armenian'}, {'code': 'az', 'name': 'Azerbaijani'}, {'code': 'eu', 'name': 'Basque'}, {'code': 'be', 'name': 'Belarusian'}, {'code': 'bn', 'name': 'Bengali'}, {'code': 'bs', 'name': 'Bosnian'}, {'code': 'bg', 'name': 'Bulgarian'}, {'code': 'ca', 'name': 'Catalan'}, {'code': 'ceb', 'name': 'Cebuano'}, {'code': 'ny', 'name': 'Chichewa'}, {'code': 'zh-CN', 'name': 'Chinese (Simplified)'}, {'code': 'zh-TW', 'name': 'Chinese (Traditional)'}, {'code': 'co', 'name': 'Corsican'}, {'code': 'hr', 'name': 'Croatian'}, {'code': 'cs', 'name': 'Czech'}, {'code': 'da', 'name': 'Danish'}, {'code': 'nl', 'name': 'Dutch'}, {'code': 'en', 'name': 'English'}, {'code': 'eo', 'name': 'Esperanto'}, {'code': 'et', 'name': 'Estonian'}, {'code': 'tl', 'name': 'Filipino'}, {'code': 'fi', 'name': 'Finnish'}, {'code': 'fr', 'name': 'French'}, {'code': 'fy', 'name': 'Frisian'}, {'code': 'gl', 'name': 'Galician'}, {'code': 'ka', 'name': 'Georgian'}, {'code': 'de', 'name': 'German'}, {'code': 'el', 'name': 'Greek'}, {'code': 'gu', 'name': 'Gujarati'}, {'code': 'ht', 'name': 'Haitian Creole'}, {'code': 'ha', 'name': 'Hausa'}, {'code': 'haw', 'name': 'Hawaiian'}, {'code': 'iw', 'name': 'Hebrew'}, {'code': 'hi', 'name': 'Hindi'}, {'code': 'hmn', 'name': 'Hmong'}, {'code': 'hu', 'name': 'Hungarian'}, {'code': 'is', 'name': 'Icelandic'}, {'code': 'ig', 'name': 'Igbo'}, {'code': 'id', 'name': 'Indonesian'}, {'code': 'ga', 'name': 'Irish'}, {'code': 'it', 'name': 'Italian'}, {'code': 'ja', 'name': 'Japanese'}, {'code': 'jw', 'name': 'Javanese'}, {'code': 'kn', 'name': 'Kannada'}, {'code': 'kk', 'name': 'Kazakh'}, {'code': 'km', 'name': 'Khmer'}, {'code': 'rw', 'name': 'Kinyarwanda'}, {'code': 'ko', 'name': 'Korean'}, {'code': 'ku', 'name': 'Kurdish (Kurmanji)'}, {'code': 'ky', 'name': 'Kyrgyz'}, {'code': 'lo', 'name': 'Lao'}, {'code': 'la', 'name': 'Latin'}, {'code': 'lv', 'name': 'Latvian'}, {'code': 'lt', 'name': 'Lithuanian'}, {'code': 'lb', 'name': 'Luxembourgish'}, {'code': 'mk', 'name': 'Macedonian'}, {'code': 'mg', 'name': 'Malagasy'}, {'code': 'ms', 'name': 'Malay'}, {'code': 'ml', 'name': 'Malayalam'}, {'code': 'mt', 'name': 'Maltese'}, {'code': 'mi', 'name': 'Maori'}, {'code': 'mr', 'name': 'Marathi'}, {'code': 'mn', 'name': 'Mongolian'}, {'code': 'my', 'name': 'Myanmar (Burmese)'}, {'code': 'ne', 'name': 'Nepali'}, {'code': 'no', 'name': 'Norwegian'}, {'code': 'or', 'name': 'Odia (Oriya)'}, {'code': 'ps', 'name': 'Pashto'}, {'code': 'fa', 'name': 'Persian'}, {'code': 'pl', 'name': 'Polish'}, {'code': 'pt', 'name': 'Portuguese'}, {'code': 'pa', 'name': 'Punjabi'}, {'code': 'ro', 'name': 'Romanian'}, {'code': 'ru', 'name': 'Russian'}, {'code': 'sm', 'name': 'Samoan'}, {'code': 'gd', 'name': 'Scots Gaelic'}, {'code': 'sr', 'name': 'Serbian'}, {'code': 'st', 'name': 'Sesotho'}, {'code': 'sn', 'name': 'Shona'}, {'code': 'sd', 'name': 'Sindhi'}, {'code': 'si', 'name': 'Sinhala'}, {'code': 'sk', 'name': 'Slovak'}, {'code': 'sl', 'name': 'Slovenian'}, {'code': 'so', 'name': 'Somali'}, {'code': 'es', 'name': 'Spanish'}, {'code': 'su', 'name': 'Sundanese'}, {'code': 'sw', 'name': 'Swahili'}, {'code': 'sv', 'name': 'Swedish'}, {'code': 'tg', 'name': 'Tajik'}, {'code': 'ta', 'name': 'Tamil'}, {'code': 'tt', 'name': 'Tatar'}, {'code': 'te', 'name': 'Telugu'}, {'code': 'th', 'name': 'Thai'}, {'code': 'tr', 'name': 'Turkish'}, {'code': 'tk', 'name': 'Turkmen'}, {'code': 'uk', 'name': 'Ukrainian'}, {'code': 'ur', 'name': 'Urdu'}, {'code': 'ug', 'name': 'Uyghur'}, {'code': 'uz', 'name': 'Uzbek'}, {'code': 'vi', 'name': 'Vietnamese'}, {'code': 'cy', 'name': 'Welsh'}, {'code': 'xh', 'name': 'Xhosa'}, {'code': 'yi', 'name': 'Yiddish'}, {'code': 'yo', 'name': 'Yoruba'}, {'code': 'zu', 'name': 'Zulu'}, {'code': 'he', 'name': 'Hebrew'}, {'code': 'zh', 'name': 'Chinese (Simplified)'}]}}

def get_languages():
	url = "https://text-translator2.p.rapidapi.com/getLanguages"
	headers = {
		"X-RapidAPI-Key": "d9ebb4af2amshe17ab90a1f24cebp11e7c9jsn147c38d73b9e",
		"X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
	}
	response = requests.get(url, headers=headers)
	print(response.json())
	response = response.json()
	return response

opcoes_linguas = {}
lista = linguas['data']['languages']
for dic in lista:
	nome = dic['name']
	codigo = dic['code']
	opcoes_linguas[nome] = codigo
print(opcoes_linguas)

target_language = input("Para que lingua vc deseja traduzir ? ")
texto = input("Digite o texto a ser traduzido: ")

url = "https://text-translator2.p.rapidapi.com/translate"
# define o endereco da API

payload = {
	"source_language": "pt",
	"target_language": opcoes_linguas[target_language],
	"text": texto
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "d9ebb4af2amshe17ab90a1f24cebp11e7c9jsn147c38d73b9e",
	"X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())

response = response.json()
texto_traduzido = response['data']['translatedText']
print(texto_traduzido)

