"""
Faça um algoritmo que leia um número e, se ele for positivo, mostre na tela
o seu inverso; caso contrário, mostre o valor absoluto do número.
"""

numero = int(input("Insira um número de quatro digitos: "))

if numero > 0:

    digito1 = numero % 10
    digito2 = numero // 10 % 10
    digito3 = numero // 100 % 10
    digito4 = numero // 1000

    numero_inverso = digito1 * 1000 + digito2 * 100 + digito3 * 10 + digito4

    print(f"O numero inverso de {numero} é {numero_inverso}")

else:
    modulo = numero * -1
    abs(numero)
    print(f"O módulo do número é {modulo}")