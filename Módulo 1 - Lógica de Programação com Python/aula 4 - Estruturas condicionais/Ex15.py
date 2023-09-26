"""
Para doar sangue é necessário ter entre 18 e 67 anos. Faça um programa
que pergunte a idade de uma pessoa e diga se ela pode doar sangue ou não.
Para realizar essa questão utilize o operador lógico OU
"""

idade = int(input("Qual a sua idade? "))

if not (idade < 18 or idade > 67):
    print("Você pode ser doador: ")

else:
    print("Você não pode ser doador")