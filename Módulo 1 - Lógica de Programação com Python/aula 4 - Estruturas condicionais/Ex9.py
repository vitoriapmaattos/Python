"""
Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da
semana correspondente a este número. Isto é, domingo se for 1, segunda-feira
se for 2, e assim por diante.
"""

dia = int(input("Digite um número entre 1 e 7:"))

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-Feira")
    case 3:
        print("Terça-Feira")
    case 4:
        print("Quarta-Feira")
    case 5:
        print("Quinta-Feira")
    case 6:
        print("Sexta-Feira")
    case 7:
        print("Sabado")
    case _:
        print("Dia inválido!")