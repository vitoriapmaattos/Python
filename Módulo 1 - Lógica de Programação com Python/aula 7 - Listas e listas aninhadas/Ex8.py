"""
Faça um programa que leia um vetor de 8 posições e, em seguida, leia também
dois valores X e Y quaisquer correspondentes a duas posições no vetor. Ao
final, seu programa deverá escrever a soma dos valores encontrados nas
respectivas posições X e Y. Se o usuário digitar valores inválidos para X ou
Y mostre uma mensagem de erro e peça novos valores até que ambos os valores
sejam válidos.
"""

lista = []

for i in range(8):
    lista.append(int(input(f"Digite os valores inteiros: ")))

x = None
while True:
    x = int(input("Digite o valor de X: "))

    if 0 <= x < len(lista):
        break

y = None
while True:
    y = int(input("Digite o valor de Y: "))

    if 0 <= y < len(lista) and y != x:
        break

soma = lista[x] + lista[y]

print(f"Soma: {lista[x]} + {lista[y]} = {soma}")

