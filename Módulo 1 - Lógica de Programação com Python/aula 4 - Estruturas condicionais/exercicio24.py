"""
Faça um programa que leia três números e mostre-os em ordem decrescente.
"""

numero_a = int(input("Escreva o primeiro número: "))
numero_b = int(input("Escreva o segundo número: "))
numero_c = int(input("Escreva o terceiro número: "))

if numero_a > numero_b:
    numero_a, numero_b = numero_b, numero_a

if numero_b > numero_c:
    numero_b, numero_c = numero_c, numero_b

if numero_a > numero_b:
    numero_a, numero_b = numero_b, numero_a

print(numero_c, numero_b, numero_a)