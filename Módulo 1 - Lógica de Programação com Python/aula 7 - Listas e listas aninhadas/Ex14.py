"""
Crie um algoritmo que receba duas listas como parâmetros e retorne uma nova
lista contendo os elementos intercalados das duas listas. Por exemplo, se as
listas forem `[1, 2, 3]` e `[4, 5, 6]`, o algoritmo deve retornar
`[1, 2, 3, 4, 5, 6]`.
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
