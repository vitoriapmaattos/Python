"""
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
O programa deve perguntar o valor da casa a comprar, o salário e a quantidade
de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do
salário. Calcule o valor da prestação como sendo o valor da casa a comprar
dividido pelo número de meses a pagar.
"""

valorcasa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salario? "))
qtdanos = int(input("Qual a quantidade de anos a pagar? "))

qtdmeses = qtdanos * 12 #tempo em meses
prestacao = valorcasa / qtdmeses #valor prestação

if salario * 0.3 > prestacao:
    print(f"Empréstimo autorizado. Valor prestação R$ {prestacao:.2f}")

else:
    print(f"Empréstimo negado! Valor da prestação R$ {prestacao:.2f} maior que 30% do salário.")

