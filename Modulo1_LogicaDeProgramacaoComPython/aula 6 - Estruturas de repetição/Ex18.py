"""
Crie um algoritmo que receba uma palavra e informe se ela é ou não um
palíndromo
"""
palavra = input("Digite um palavra: ")
tamanho = len(palavra)

for i in range(tamanho // 2):
    if palavra[i] != palavra[tamanho - 1 - i]:
        print("A palavra não é um palíndromo")
        break
else:
    print("A palavra é um palíndromo")