"""Construa um algoritmo que leia o preço de um produto, o percentual de desconto e calcule
o valor a pagar e o valor do desconto."""
import math

n1 = float(input("Digite o preço do produto: "))
n2 = float(input("Digite o percentual de desconto: "))
r1 = (n2 / 100) * n1
r2 = n1 - r1

print(f"Desconto: R${r1}")
print(f"Valor a pagar: R${r2}")


