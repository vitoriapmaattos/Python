"""
Escreva um programa que receba um número, se esse número for ímpar, mostre
na tela o quadrado do número digitado. No final do programa mostre na tela
a mensagem: “Programa finalizado…
"""

numero = int(input("Digite um número: "))

if numero % 2 != 0:
   print(f"O quadrado do número digitado é: {numero ** 2}")

print("Programa finalizado")