"""
Escreva um programa que receba uma lista de palavras e retorne a palavra
mais longa.
"""

lista = []
tam_palavras = []

lista.append(input("Digite algumas palavras: ").split())
for palavra in lista:
    tam_palavras.append(len(palavra))
    print(f"A maior palavra é {max(palavra, key=len)}")
