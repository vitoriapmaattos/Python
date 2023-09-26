"""
Faça um programa que pergunte em que turno você estuda. Peça para digitar
M - Matutino, V - Vespertino ou N - Noturno. Imprima a mensagem "Bom Dia!",
"Boa Tarde!", "Boa Noite!" ou "Valor Inválido!" de acordo com o turno
escolhido.
"""

turno = (input("Digite o turno que você estuda (M - Matutino, V - Vespertino ou N - Noturno):"))

match turno:
    case "M":
        print("bom dia!")
    case "V":
        print("boa tarde!")
    case "N":
        print("boa noite!")
    case _:
        print("Valor Inválido!")