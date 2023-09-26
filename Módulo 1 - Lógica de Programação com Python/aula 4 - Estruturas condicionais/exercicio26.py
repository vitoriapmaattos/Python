"""
Crie um programa que auxilie no controle de gastos pessoais. Peça ao usuário para inserir suas despesas
mensais nas seguintes categorias:
Alimentação
Moradia
Transporte
Lazer
Saúde
TV / Internet / Telefone
Também peça ao usuário o seu salário mensal. O programa deve calcular o total de despesas,
mostrar o percentual de cada categoria em relação ao total e informar se as suas despesas excedem o salário.
"""

salario = float(input("Qual o salário? "))
alimentacao = float(input("Qual o gasto com alimentação: "))
moradia = float(input("Qual o gasto com moradia: "))
transporte = float(input("Qual o gasto com transporte: "))
lazer = float(input("Qual o gasto com lazer: "))
saude = float(input("Qual o gasto com saúde: "))
planos = float(input("Qual o gasto com planos: "))

soma_gastos = alimentacao + moradia + transporte + lazer + saude + planos

print(f"""O gasto total é R${soma_gastos:,.2f}!
As porcentagens dos gastos são:
alimentação - {alimentacao*100/soma_gastos:.2f}%
moradia - {moradia*100/soma_gastos:.2f}%
transporte - {transporte*100/soma_gastos:.2f}%
lazer - {lazer * 100/ soma_gastos:.2f}%
saúde - {saude * 100/ soma_gastos:.2f}%
planos - {planos * 100/ soma_gastos:.2f}%
""")

print("O valor NÃO excede o salário") if soma_gastos < salario else print("O valor excede o salário")