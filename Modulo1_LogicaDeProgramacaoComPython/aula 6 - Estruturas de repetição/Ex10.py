"""
Crie um algoritmo que realize a leitura de 5 números inteiros e ao final
mostre qual é o maior e o menor número lido. Suponha que nem todos os números
serão positivos.
"""
from math import inf

numeros = []
for i in range(5):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

maior_numero = -inf
menor_numero = inf

for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero
for numero in numeros:
    if numero < menor_numero:
        menor_numero = numero

print(f"O maior número é {maior_numero} e o menor número é {menor_numero}")



