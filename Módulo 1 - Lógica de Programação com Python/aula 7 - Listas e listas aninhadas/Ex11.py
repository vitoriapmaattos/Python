"""
Faça um programa que receba uma lista de números inteiros e retorne uma nova
lista com os elementos em ordem crescente.
"""
lista = []

for i in range(5):
    lista.append(int(input(f"Digite os valores inteiros: ")))

print(sorted(lista))