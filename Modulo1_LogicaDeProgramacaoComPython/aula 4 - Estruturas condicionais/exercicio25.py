
import math

numero_a = int(input("Digite o valor A: "))

if numero_a == 0:
    print("A equação não é do segundo grau")
else:
    numero_b = int(input("Digite o valor B: "))
    numero_c = int(input("Digite o valor C: "))

    delta = numero_b ** 2 - 4 * numero_a * numero_c

    if delta < 0:
        print("A equação não tem raízes reais")
    elif delta == 0:
        raiz1 = -numero_b / (2 * numero_a)
        print(f"A raiz é {raiz1:.2f}")
    else:
        raiz1 = (-numero_b + math.sqrt(delta)) / (2 * numero_a)
        raiz2 = (-numero_b - math.sqrt(delta)) / (2 * numero_a)
        print(f"Primeira raiz é {raiz1:.2f}")
        print(f"Segunda raiz é {raiz2:.2f}")