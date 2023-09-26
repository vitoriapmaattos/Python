"""
Escreva um programa que receba uma lista como entrada e retorne uma nova lista
comprimida, onde elementos repetidos sejam substituídos por uma tupla contendo
o elemento e a quantidade de vezes que ele se repete. Por exemplo, para a
lista [1, 1, 1, 2, 3, 3, 4, 4, 4, 4], o programa deve retornar
[(1, 3), 2, (3, 2), (4, 4)].
"""

lista_a = []
lista_b = []
lista_c = []

lista_a = (input("Digite números para a lista A: "))
lista_b = (input("Digite números para a lista B: "))

for i in lista_a:
    lista_c.append(i)

for i in lista_b:
    lista_c.append(i)

    

print(lista_c)
