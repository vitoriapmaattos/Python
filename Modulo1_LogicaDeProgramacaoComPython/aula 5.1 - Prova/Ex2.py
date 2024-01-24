"""
Faça um algoritmo que simule uma calculadora. Para isso, o algoritmo deverá
solicitar a operação matemática que deve ser executada e os números
necessários para cada operação. O algoritmo deve permitir as operações
de adição, subtração, multiplicação, divisão, porcentagem
(ex.: 20% de 100 = 20) e logaritmo (ex.: log636 = 2).
"""
import math
numero1 = float(input("Qual o primeiro número da operação? "))
operacao = input("Qual a operação? (+, -, /, *, %, log) ")
numero2 = float(input("Qual o segundo número da operação? \nEm caso de log: preencher a base "))

match operacao:
    case "+":
        resultado = numero1 + numero2
        print(f"O resultado é {resultado}")
    case "-":
        resultado = numero1 - numero2
        print(f"O resultado é {resultado}")
    case "/":
        resultado = numero1 / numero2
        print(f"O resultado é {resultado}")
    case "*":
        resultado = numero1 * numero2
        print(f"O resultado é {resultado}")
    case "%":
        resultado = numero1 / numero2 * 100
        print(f"O resultado é {resultado}")
    case "log":
        print(f"O resultado é {math.log(numero1,numero2)}")
    case _:
        print("Operação inválida")

