"""
Faça um algoritmo que elimine as duplicatas da lista abaixo e ordene-as de
maneira decrescente:
"""

lista = [1, 1, 5, 3, 2, 10, 2, 5, 6, 11, 100, 1000, 900, 900, 10, 5, 534]


def remove_duplicados(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

lista = remove_duplicados(lista)
print(lista)
