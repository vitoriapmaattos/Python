"""
Escreva um programa que solicite ao usuário um número inteiro positivo e exiba
a tabuada desse número de 1 a 10 utilizando um loop for.
"""

numero = int(input("Escreva um número: "))

for i in range (1, 11):
    tabuada = numero * i
    print(tabuada, end = " ")