"""
Escreva um programa que pergunte a quantidade de km percorridos por um carro
alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi
alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia
e R$ 0,15 por km rodado.
"""

kmpercorridos = float(input("Quantos km foram percorridos com o carro alugado? "))
diasutilizados = int(input("Por quantos dias utilizaram o carro alugado? "))

precodiaria = diasutilizados * 60
precokm = kmpercorridos * 0.15

precoapagar = precodiaria + precokm

print(f"O valor total a pagar é: R$ {precoapagar:.2f}")