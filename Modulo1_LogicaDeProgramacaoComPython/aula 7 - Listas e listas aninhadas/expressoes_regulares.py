"""
Expressões regulares - são sequências de caracteres que definem um padrão
em uma string.
"""
import re

texto  = """Phyton é uma olinguagem de programação poderosa.
Javascript e Phyton são linguagem similares.
"""

padrao = r"\bp\w+"

palavras_encontradas = re.findall(padrao, texto, flags=re.I | re.S)
print(palavras_encontradas)


#Validação de dados
email = "exemplo@email.com"

padrao = r"^\w+@\w+\.\w+$"
if re.match(padrao,email):
    print("E-mail válido!")
else:
    print("E-mail inválido!")
"""
# Substituicão de padrões
texto = "Eu amo programação com JavaScript!"

padrao = r"javascript"
texto = re.sub(padrao, repl= "Python", texto, flags=re.I)
print(texto)
"""

#Extraindo informação
telefones = """ (47) 9 9999-9999
47 99999-9999
"""

padrao = r"\((\d+)\) 9 \d{4}-\d{4}"

telefone_encontrado = re.search(padrao, telefones)
if telefone_encontrado:
    print(f"DDD: {telefone_encontrado.group(1)}")

