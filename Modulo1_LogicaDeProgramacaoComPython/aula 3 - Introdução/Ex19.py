"""
Faça um programa que leia o nome de um vendedor, o seu salário fixo e o
total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este
vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o
total a receber no final do mês, com duas casas decimais.
"""

nome = (input("Digite o nome do vendedor: "))
salario_fixo = float(input("Digite o salário do vendedor: "))
vendas_efetuadas = float(input("Digite o valor das vendas efetuadas: "))
porcentagem = 0.15

comissao = vendas_efetuadas * porcentagem
total_receber = salario_fixo + comissao

print(f"Vendedor: {nome}")
print(f"Salário: {salario_fixo}")
print(f"Valor vendido : {vendas_efetuadas}")
print(f"Comissão : {comissao}")
print(f"Total a receber : {total_receber}")
