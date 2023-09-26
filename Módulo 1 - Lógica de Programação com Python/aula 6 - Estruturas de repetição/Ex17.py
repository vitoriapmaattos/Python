"""
Crie um algoritmo que solicite o nome do usuário e informe a quantidade de
vogais, quantidade de consoantes e o total de caracteres presentes no nome.
"""

nome = input("Digite um nome: ")

qtd_vogais = 0
total_carac = len(nome)

for letra in nome:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        qtd_vogais += 1

qtd_consoantes = total_carac - qtd_vogais
print(f"""
Quantide de vogais: {qtd_vogais}
Quantidade de consoantes: {qtd_consoantes}
Total de caracteres: {total_carac}""")