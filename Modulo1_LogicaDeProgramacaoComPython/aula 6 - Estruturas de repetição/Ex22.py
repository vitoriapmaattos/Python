"""
Escreva um programa que solicite ao usuário um número inteiro positivo e
exiba o fatorial desse número.
"""
numero = int(input("Digite um número: "))

fatorial = 1
for i in range(2, numero + 1):
    fatorial *= i

print(fatorial)