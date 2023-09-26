"""
Escreva um programa que calcule o produto da multiplicação de dois fatores.
O programa deve realizar os cálculos utilizando laços de repetição e adição.
"""
fator1 = int(input("Digite o primeiro fator: "))
fator2 = int(input("Digite o segundo fator: "))

soma = 0
for i in range(fator1):
    soma += fator2

print(f"O resultado é: {soma}")