"""
Faça um algoritmo para calcular o IMC de uma pessoa
com base no seu peso e altura.
"""

peso = int(input("Digite o peso em kg: "))
altura = float(input("Digite o altura em cm: "))

altura_quadrado = altura * altura
imc = peso / altura_quadrado
print(f"O IMC é: {imc:.2f} ")
