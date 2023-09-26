"""
Construa um programa que receba um texto e uma palavra como entrada e indique
se a palavra está presente ou não no texto. Se a palavra estiver presente no
texto, diga quantas vezes ela aparece.
"""

string = input("Digite uma frase: ")
palavra = input("Digite uma palavra: ")


if palavra not in string:
    print("A palavra não esta no texto.")

elif palavra in string:
    string.count(palavra)
    print(f"A {palavra} aparece {string.count(palavra)} vezes.")