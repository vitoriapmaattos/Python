"""
Escreva um programa que solicite ao usuário um número inteiro positivo e exiba
a soma dos dígitos desse número.
"""

numero = input("Digite um número inteiro positivo: ")

soma = 0
for digito in numero:
    soma += int(digito)

print(f"A soma dos digitos do número é: {soma}")