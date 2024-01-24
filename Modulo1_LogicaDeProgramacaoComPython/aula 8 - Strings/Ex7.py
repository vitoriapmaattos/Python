"""
Escreva um algoritmo que encontre todas as ocorrências de números em uma
string e os retorne em uma lista.
"""
import re
numero = []

texto = input("Digite um texto: ")

padrao = r"\d"
numero.append(re.findall(padrao, texto))

print(numero)






