"""
Escreva um programa que dado um valor inteiro de reais, mostre a menor
quantidade possível de notas para aquele valor, levando em consideração
as seguintes notas:
100 reais
50 reais
10 reais
5 reais
2 reais
moeda de 1 real
"""
valor = int(input("Digite um valor: "))

n100 = valor // 100
a = valor % 100

n50 = a // 50
b = a % 50

n10 = b // 10
c = b % 10

n5 = c // 5
d = c % 5

n2 = d // 2
e = d % 2

n1 = e // 1

print(f"O valor: R$ {valor:.2f}\n{n100} notas de R$ 100,00\n{n50} notas de R$ 50,00\n{n10} notas de R$ 10,00\n{n5} notas de R$ 5,00\n{n2} notas de R$ 2,00\n{n1} moedas de R$ 1,00")
