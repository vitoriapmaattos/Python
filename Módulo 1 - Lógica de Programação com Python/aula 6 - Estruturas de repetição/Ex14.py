"""
Escreva um programa que calcule e mostre o valor de x elevado a n.
O programa deverá fazer o cálculo da potenciação utilizando laços de
repetição (Não usar o operador de exponenciação).
"""
x = int(input("Digite o valor de x: "))
n = int(input("Digite o valor de n: "))

soma = 1

for i in range(1, n + 1):
    soma *= x

print(soma)