"""
Escreva um programa que solicite ao usuário um número inteiro positivo e
verifique se ele é um número primo.
"""


numero = int(input("Digite o número: "))

for i in range(2, numero):
    if numero % i == 0:
        print("O número não é primo")
        break
else:
    print("O número é primo")