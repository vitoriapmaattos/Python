"""
Crie um algoritmo que solicite ao usuário um número e mostre todos os
divisores desse número.
"""
i = 1

numero = int(input("Digite um numero: "))

for i in range(i, numero+1):
    if numero % i == 0:
        print(f"Os divisores deste número:", i)