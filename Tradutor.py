
from googletrans import Translator

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='0202',
    database='tradutor'
)
cursor = conexao.cursor()

res = input(' DIGITE UMA PALAVRA OU TEXTO A SER TRADUZIDO: \n')
translator = Translator()
translations = translator.translate(res, dest='en', src='pt')
textinho = translations.text
# adicionando o item de pesquisa no banco de dados
comando = f'INSERT INTO historico_traducoes (item_pesquisa , trad_item) VALUES ("{res}", "{textinho}")'
cursor.execute(comando)
conexao.commit()  # edita o banco de dados
print(translations.text)









