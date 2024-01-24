"""
Escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês
correspondente a este número. Isto é, Janeiro se for 1, Fevereiro se 2,
e assim por diante.
"""

mes = int(input("Digite um número entre 1 e 12:"))

match mes:
    case 1:
        print("janeiro")
    case 2:
        print("fevereiro")
    case 3:
        print("março")
    case 4:
        print("abril")
    case 5:
        print("maio")
    case 6:
        print("junho")
    case 7:
        print("julho")
    case 8:
        print("agosto")
    case 9:
        print("setembro")
    case 10:
        print("outubro")
    case 11:
        print("novembro")
    case 12:
        print("dezembro")
    case _:
        print("Dia inválido!")