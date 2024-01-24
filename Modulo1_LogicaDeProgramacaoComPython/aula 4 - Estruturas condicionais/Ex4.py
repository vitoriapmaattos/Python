"""
Escreva um programa que receba um número, se esse número for par,
mostre na tela “O número é par” senão mostre “O número é ímpar”
"""

numero = int(input("Digite um número: "))

if numero % 2 == 0:
   print(f"O número é par")

else:
    print("O número é impar")
