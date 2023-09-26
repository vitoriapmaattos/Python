"""
Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é
Equilátero, Isósceles ou Escaleno.

Sendo que:
Triângulo Equilátero: possui os 3 lados iguais.
Triângulo Isósceles: possui 2 lados iguais.
Triângulo Escaleno: possui 3 lados diferentes.
"""

lado_A = int(input("Escreva o primeiro lado: "))
lado_B = int(input("Escreva o segundo lado: "))
lado_C = int(input("Escreva o segundo lado: "))

if lado_A == lado_B and lado_A == lado_C:
    print(f"Equilátero")

elif lado_A != lado_B and lado_A != lado_C and lado_B != lado_C:
    print(f"Escaleno")

else:
    print(f"Isósceles")