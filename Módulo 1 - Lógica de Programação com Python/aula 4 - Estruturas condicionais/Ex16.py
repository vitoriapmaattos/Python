"""
Escreva um algoritmo que peça o salário bruto de uma pessoa e imprima o
salário líquido, segunda a tabela a seguir:
"""

salario = float(input("Insire o salário bruto: "))

if salario <= 0:
    print((f"O salário é inválido."))

elif salario <= 600:
    print(f"O salário líquido é: {salario:.2f} (Isento)")

elif salario <= 1200:
    salario_liquido = salario * 0.8
    print(f"O salário líquido é: {salario_liquido:.2f} (20%)")

elif salario <= 2000:
    salario_liquido = salario * 0.75
    print(f"O salário líquido é: {salario_liquido:.2f} (25%)")

else:
    salario_liquido = salario * 0.7
    print(f"O salário líquido é: {salario_liquido:.2f} (30%)")