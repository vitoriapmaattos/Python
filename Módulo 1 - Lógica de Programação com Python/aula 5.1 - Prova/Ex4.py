"""
Uma empresa deseja calcular o bônus salarial de seus funcionários com base no
desempenho deles ao longo do ano. O bônus é calculado da seguinte forma:

Se o funcionário atingir todas as metas de vendas, o bônus é de 20% do salário
anual.
Se o funcionário atingir pelo menos metade das metas de vendas, o bônus é de
10% do salário anual.
Caso contrário, o funcionário não receberá bônus.

Escreva um que solicite ao usuário o salário mensal, o valor das metas de
desempenho atingidas pelo funcionário e o valor total das metas de venda do
funcionário. Com base nas regras acima, o programa deve calcular e exibir o
valor do bônus que o funcionário receberá.
"""
''
salario = float(input("Qual o salário do funcionário?"))
meta = float(input("Qual a meta de venda?"))
vendido = float(input("Qual o valor vendido?"))

salarioanual = salario * 12
porcatingida = vendido / meta

if porcatingida >= 1:
    receber = salarioanual * 0.2
    print(f"O funcionário receberá de bônus R$ {receber:.2f}")

elif porcatingida >= 0.5:
    receber = salarioanual * 0.1
    print(f"O funcionário receberá de bônus R$ {receber:.2f}.")

else:
    print("O funcionário não esta apto a receber o bônus.")