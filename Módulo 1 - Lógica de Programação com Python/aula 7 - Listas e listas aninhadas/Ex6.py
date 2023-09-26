"""
Crie um programa que receba uma lista de números e retorne a média dos
números pares.
"""
lista = []

for i in range(5):
    lista.append(int(input(f"Digite os valores inteiros: ")))

pares = []
qtdpares = 0
soma = 0
impares = []

for c in lista:
    if c % 2 == 0:
        pares.append(c)
        qtdpares += 1
        soma += c
    else:
        impares.append(c)

media = soma / qtdpares

print(f"A média dos números pares é: {media}")