"""
Escrever um programa que calcule o Índice de Massa Corporal (IMC) com base
no peso e altura inseridos pelo usuário. Em seguida, o programa deve
fornecer uma classificação de acordo com o resultado do cálculo do IMC.
Regras:
O programa deve solicitar ao usuário que insira seu peso em quilogramas (kg) e altura em metros (m).
O programa deve calcular o IMC usando a fórmula: IMC = peso / altura^2.
O programa deve arredondar o resultado do IMC para duas casas decimais.
O programa deve fornecer a seguinte classificação de acordo com o IMC
calculado:
IMC menor que 18.5: "Abaixo do peso"
IMC entre 18.5 e 24.9: "Peso normal"
IMC entre 25 e 29.9: "Sobrepeso"
IMC entre 30 e 34.9: "Obesidade grau 1"
IMC entre 35 e 39.9: "Obesidade grau 2"
IMC maior ou igual a 40: "Obesidade grau 3"
"""

peso = float(input("Qual o seu peso em quilogramas?"))
altura = float(input("Qual a sua altura em metros?"))

imc = peso / (altura ** 2)

if imc > 1 and imc < 18.5:
    print(f"IMC = {imc:.2f} \nAbaixo do peso")

elif imc >= 18.5 and imc <= 24.9:
    print(f"IMC = {imc:.2f} \nPeso normal")

elif imc >= 25 and imc <= 29.9:
    print(f"IMC = {imc:.2f} \nSobrepeso")

elif imc >= 30 and imc <= 34.9:
    print(f"IMC = {imc:.2f} \nObesidade grau 1")

elif imc >= 35 and imc <= 39.9:
    print(f"IMC = {imc:.2f} \nObesidade grau 2")

elif imc >= 40:
    print(f"IMC = {imc:.2f} \nObesidade grau 3")

else:
    print("Valores inválidos!")

