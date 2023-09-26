"""
Escreva um programa que pergunte a velocidade do carro de um usuário.
Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi
multado. Nesse caso, exiba o valor da multa, cobrando R$ 5,00 por km acima
de 80 km/h.
"""

velocidadeatual = int(input("Qual a velocidade do carro? "))

if velocidadeatual > 80:
    valormulta = ((velocidadeatual - 80)* 5)
    print(f"Você foi multado!  Valor da multa: R$ {valormulta:.2f}")

else:
    print("Velocidade permitida!")