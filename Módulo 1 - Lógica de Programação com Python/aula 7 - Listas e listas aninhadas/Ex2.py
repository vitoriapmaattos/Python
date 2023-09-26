"""
Escreva um programa que peça as três notas de um aluno armazenando-as em uma
lista e retorne a média das notas.
"""
lista_notas = []
notas = 0

for i in range (3):
    lista_notas.append(float(input(f"Digite a {i + 1}ª notas de um aluno: ")))
    notas += lista_notas[i]

media = notas / 3
print(f"A média do aluno é: {media:.2f}")
