"""
Escreva um programa que receba uma lista como entrada e remova todas as
duplicatas, retornando uma nova lista com os elementos únicos em sua ordem
original.
"""
lista = []

for i in range(5):
    lista.append(int(input(f"Digite os valores inteiros: ")))

unique_list = list(set(lista))

print(unique_list)