"""
Escreva um programa que calcule o preço a pagar pelo fornecimento de energia
elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R
para residências, I para indústrias e C para comércios. Calcule o preço a
pagar de acordo com a tabela a seguir.
"""

faixakwh = float(input("Qual a quantidade de kWh consumida: "))
tipoinstalacao = input("Qual o tipo de instalação:\nResidencia = R\nIndústrias = I\nComércios = C\n")

match tipoinstalacao:
    case "R":
        if faixakwh <= 500:
            print(f"Preço a pagar é: R$ {faixakwh * 0.40:.2f}")
        else:
            print(f"Preço a pagar é: R$ {faixakwh * 0.65:.2f}")
    case "C":
        if faixakwh <= 1000:
            print(f"Preço a pagar é: R$ {faixakwh * 0.55:.2f}")
        else:
            print(f"Preço a pagar é: R$ {faixakwh * 0.60:.2f}")
    case "I":
        if faixakwh <= 5000:
            print(f"Preço a pagar é: R$ {faixakwh * 0.55:.2f}")
        else:
            print(f"Preço a pagar é: R$ {faixakwh * 0.60:.2f}")
    case _:
        print("Tipo de residência inválido!")
