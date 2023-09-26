"""
Dada uma lista de nomes, crie uma nova lista que contenha apenas os nomes
que começam com a letra “A”.
"""


lista = ["ana lua", "branca", "antônio", "carlos", "eduarda"]
nomes_com_a = []

for nome in lista:
    if nome[0].upper() == "A": # .upper converte letra em maiusculo
        nomes_com_a.append(nome)

print(nomes_com_a)
