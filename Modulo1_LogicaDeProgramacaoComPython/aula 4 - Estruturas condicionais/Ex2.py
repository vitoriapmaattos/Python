"""
Escreva um programa que receba um número, se esse número for par,
mostre na tela a metade do número digitado. No final do programa
mostre na tela a mensagem: “Programa finalizado…
"""

numero = int(input("Digite um número: "))

if numero % 2 == 0:
   print(f"A metade do número digitado é: {numero / 2}")

print("Programa finalizado")