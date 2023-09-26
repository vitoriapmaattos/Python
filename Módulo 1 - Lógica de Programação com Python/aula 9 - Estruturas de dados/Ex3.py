"""
Implemente um algoritmo que declare uma lista de strings e retorne uma tupla
contendo a quantidade de palavras em cada string.
"""
resultados = []

str1 = input().split(" ")
str2 = input().split(" ")
str3 = input().split(" ")
str4 = input().split(" ")
str5 = input().split(" ")
lista = [str1, str2, str3, str4, str5]

qtdstring = [(len(str1)), (len(str2)), (len(str3)), (len(str4)), (len(str5))]

for i in range(5):
    tupla = (lista[i],qtdstring[i])
    resultados.append(tupla)
print(resultados)