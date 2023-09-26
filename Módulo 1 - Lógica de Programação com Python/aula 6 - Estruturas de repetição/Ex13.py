"""
Escreva um programa que calcule o quociente da divisão de dois números.
O programa deve receber o dividendo e o divisor e realizar operações de
subtração com laços de repetição para chegar ao valor esperado.
"""

dividendo = float(input("Digite o dividendo: "))
divisor = float(input("Digite o divisor: "))
quociente = 0
x = dividendo

while x >= divisor:
    x = x - divisor
    quociente = quociente + 1

resto = x

print(f"O resto de {dividendo} / {divisor} é {resto}")