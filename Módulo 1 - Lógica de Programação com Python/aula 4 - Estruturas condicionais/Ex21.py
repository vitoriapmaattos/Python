"""
Faça um programa que leia a idade de uma pessoa e exiba se ela é criança
(até 12 anos), adolescente (13 a 17 anos), adulto (18 a 59 anos) ou idoso
(maiores de 60 anos)
"""

idade = int(input("Qual a sua idade: "))

if idade <= 12:
    print("É criança")

elif idade >= 13 and idade <= 17:
    print("É adolescente")

elif idade >= 18 and idade <= 59:
    print("É adulto")

else:
    print("É idoso")