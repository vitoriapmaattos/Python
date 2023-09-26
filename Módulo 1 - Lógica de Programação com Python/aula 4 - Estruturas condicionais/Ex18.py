"""
Faça um algoritmo que simule uma calculadora. Para isso, o algoritmo
deverá solicitar dois números e a operação matemática que deve ser
executada. O algoritmo deve permitir as operações de adição, subtração,
multiplicação e divisão
"""


numero_a = int(input("Escreva o primeiro número: "))
numero_b = int(input("Escreva o segundo número: "))
operacao = input("Escreva a operação desejada ( +, -, *, / ): ")

match operacao:
    case "+":
        print(f" O resultado é {numero_a + numero_b}")
    case "-":
        print(f" O resultado é {numero_a - numero_b}")
    case "*":
        print(f" O resultado é {numero_a * numero_b}")
    case "/":
        print(f" O resultado é {numero_a / numero_b}")
    case _:
        print("Operação inválida")

