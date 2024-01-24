"""
Escreva um programa que peça 5 números inteiros e armazene-os em uma lista.
Ao final, o programa deve mostrar o menor e o maior número da lista.
"""

lista = []

for i in range (5):
    lista.append(float(input(f"Digite o {i + 1}º número inteiro: ")))

print(f"O menor valor da lista é {min(lista)} e o maior é {max(lista)}.")