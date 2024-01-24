"""
Faça um algoritmo que solicite ao usuário um valor n simbolizando o número de
degraus e mostre na tela uma escada conforme o exemplo abaixo:
"""

n = int(input("Digite o número de degraus: "))

symbol = "#"

for i in range (1, n+1):
    print(symbol * i)