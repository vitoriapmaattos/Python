"""
Crie um algoritmo que mostre os números de 1 a 100 e ao final mostre a soma de
todos eles.
"""

soma = 0

for i in range (0, 101):
    print(i, end = " ")
    soma += i
print()
print(f"A soma dos números digitados: {soma}")