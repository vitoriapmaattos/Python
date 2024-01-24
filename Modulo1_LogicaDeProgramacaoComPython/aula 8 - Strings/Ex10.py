"""
Escreva um algoritmo que retorne o número de palavras únicas em um texto.
Ignore a diferenciação entre maiúsculas e minúsculas.
"""
strings = input("Digite uma frase: ").upper().split(" ")

valores = []
repetidos = set()

for string in strings:
    if string not in valores:
        valores.append(string)
    else:
        repetidos.add(string)

for letra in valores:
    if letra in valores:
        strings.count(letra)

print(f"Únicos = {valores}.")
