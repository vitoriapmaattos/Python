"""
Faça um programa que leia o salário de um trabalhador e o valor da prestação
 de um empréstimo. Se a prestação for maior que 20% do salário imprima:
  “empréstimo não concedido”, caso contrário imprima: “empréstimo concedido"
"""

salario = float(input("Digite o salário: "))
prestacao = float(input("Digite o valor da prestação: "))

if salario * 0.2 >= prestacao:
    print("emprestimo concedido")

else:
    print("emprestimo não concedido")