"""
Escreva um programa que receba uma lista de números e retorne apenas os
números que são únicos, ou seja, sem duplicatas.
"""
lista = []

for i in range(5):
    lista.append(int(input(f"Digite os valores inteiros: ")))

unique_list = list(set(lista))
print(unique_list)
    