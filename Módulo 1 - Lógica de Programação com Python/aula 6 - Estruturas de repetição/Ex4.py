"""
Escreva um programa que solicite ao usuário uma sequência de números inteiros
positivos até que o usuário digite um número menor ou igual a 0. Ao final, o
programa deve mostrar a soma dos números lidos.
"""

soma = 0

while True:
    numero = int(input("Digite um número: "))

    if numero <= 0:
        break

    soma += numero

print(f"A soma dos números digitados: {soma}")
