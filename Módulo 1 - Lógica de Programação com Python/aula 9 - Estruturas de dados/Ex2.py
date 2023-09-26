"""
Escreva uma list comprehension que retorne uma lista dos quadrados dos números
de 1 a 10.
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrados = []
for numero in lista:
    quadrados.append(numero ** 2)
print(quadrados)