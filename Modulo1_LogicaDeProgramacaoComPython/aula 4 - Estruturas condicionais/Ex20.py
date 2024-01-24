"""
Faça um programa que leia três números e exiba se eles formam um
triângulo válido. Um triângulo é válido se a soma de dois lados for
maior que o terceiro lado.
"""

lado_1 = int(input("Insira o lado 1: "))
lado_2 = int(input("Insira o lado 2: "))
lado_3 = int(input("Insira o lado 3: "))

if lado_1 + lado_2 > lado_3 and lado_1 + lado_3 > lado_2 and lado_2 + lado_3 > lado_1:
    print("Triângulo válido")

else:
    print("Triângulo Inválido")