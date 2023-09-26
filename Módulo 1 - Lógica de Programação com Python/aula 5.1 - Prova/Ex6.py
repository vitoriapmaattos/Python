"""
Faça um programa que receba 4 números inteiros e mostre eles ordenados na tela
de acordo com os exemplos:
"""

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))
numero3 = int(input("Digite um número: "))
numero4 = int(input("Digite um número: "))

if numero1 < numero3 and numero1 < numero2 and numero1 < numero4:
    if numero3 >= numero2 and numero3 < numero4 and numero3 > numero1:
        if numero2 > numero1 and numero2 <= numero3 and numero2 < numero4:
            print(numero1, numero3, numero2, numero4)

elif numero1 < numero3 and numero1 > numero2 and numero1 > numero4:
    if numero3 > numero2 and numero3 > numero4 and numero3 > numero1:
        if numero2 < numero1 and numero2 < numero3 and numero2 > numero4:
            print(numero4, numero1, numero2, numero3)

elif numero1 == numero3 and numero1 > numero2 and numero1 > numero4:
    if numero3 > numero2 and numero3 > numero4 and numero3 == numero1:
         if numero2 < numero4:
            print(numero2, numero3, numero4, numero1)

else:
    print("nada")