"""
Escreva uma função chamada compressao_string, que receba uma string como
parâmetro e retorne a versão comprimida da mesma.

Exemplo:
Entrada: “AAABBBCCCCAA”
Saída: “A3B3C4A2”
"""

strings = list(input("Digite uma string: "))
qtd = []

valores = []
repetidos = set()

for string in strings:
    if string not in valores:
        valores.append(string)
    else:
        repetidos.add(string)

    for s in string:
        qtd = strings.count(s)

print(valores)
print(qtd)




