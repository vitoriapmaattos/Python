"""
Escreva um programa que receba uma lista como entrada e remova todas as
duplicatas, retornando uma nova lista com os elementos únicos em sua ordem
original.
"""
lista = []
listaunica = []

lista = input("Digite um lista de itens:")

for i in lista:
    if i not in listaunica:
        listaunica.append(i)

print(listaunica)