"""
Faça um programa que leia a altura e o sexo (M ou F) de uma pessoa e calcule
o peso ideal. Para homens, o peso ideal é calculado pela fórmula:
(72.7 * altura) - 58. Para mulheres, o peso ideal é calculado pela fórmula:
(62.1 * altura) - 44.7.
"""

altura = float(input("Qual a sua altura? "))
sexo = input("Qual o seu genero? (M e F) ")

match sexo:
    case "F":
        peso_ideal = 62.1 * altura - 44.7
        print(f"O peso ideal é: {peso_ideal}")

    case "M":
        peso_ideal = 72.7 * altura - 58
        print(f"O peso ideal é: {peso_ideal}")

    case _:
        print("Genero inválido")

