"""
Dada uma lista de números inteiros, escreva um programa que encontre a soma
dos números consecutivos maiores do que zero. Por exemplo, para a lista
[ -2, 3, 4, 0, 7, -1], o programa deve retornar a soma 7 (3 + 4).
"""
numeros = []
soma = 0

while True:
    numero = int(input("Digite valores inteiros:\nPra finalizar digite 10." ))
    if numero < 10:
        numeros.append(numero)
        if numero >= 0:
            soma += numero
    else:
        break
print(f"A soma dos valores maiores que 0 é: {soma}")
