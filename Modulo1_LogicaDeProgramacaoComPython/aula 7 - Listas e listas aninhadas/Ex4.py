"""
Escreva um programa que receba duas listas e retorne uma nova lista que
contenha apenas os elementos em comum entre as duas listas.
"""

lista_a = []
lista_b = []

for i in range(3):
    lista_a.append(input(f"Digite o {i + 1}º número inteiro da lista A: "))
for i in range(3):
    lista_b.append(input(f"Digite o {i + 1}º número inteiro da lista B: "))

lista_c = list(set(lista_a) & set(lista_b))
print(lista_c)