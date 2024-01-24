"""
Escreva um algoritmo para validar se uma string é um endereço de e-mail
válido.
"""

import re

email = input("Digite o e-mail: ")

padrao = r"^\w+@\w+\.\w+$"  # Verifica se o email está em um formato válido
valido = re.match(padrao, email)
if valido:
    print("O email é válido.")
else:
    print("O email é inválido.")