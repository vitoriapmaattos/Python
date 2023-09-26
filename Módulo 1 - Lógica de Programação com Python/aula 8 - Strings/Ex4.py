"""
Faça um programa que abrevie o nome fornecido pelo usuário de acordo com os
exemplos fornecidos:
"""

nome_completo = (input("Por favor digite seu nome completo: ").split(" "))

if len(nome_completo) == 3:
    primeiro_nome = nome_completo[0]
    segundo_nome = nome_completo[1]
    terceiro_nome = nome_completo[-1]
    print(f"{primeiro_nome.capitalize()} {segundo_nome[0].capitalize()}. {terceiro_nome.capitalize()}")

if len(nome_completo) >= 4:
    primeiro_nome = nome_completo[0]
    segundo_nome = nome_completo[1]
    terceiro_nome = nome_completo[2]
    quarto_nome = nome_completo[-1]
    print(f"{primeiro_nome.capitalize()} {segundo_nome[0].capitalize()}. {terceiro_nome[0].capitalize()}. {quarto_nome.capitalize()}")

if len(nome_completo) == 2:
    primeiro_nome = nome_completo[0]
    segundo_nome = nome_completo[1]
    print(f"{primeiro_nome[0].capitalize()}{segundo_nome[0].capitalize()}")