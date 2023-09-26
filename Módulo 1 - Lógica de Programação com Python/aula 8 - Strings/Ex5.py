"""
Escreva um algoritmo que checa se o texto de uma string é spam. Para ser
considerado spam a string deve conter as palavras “jequiti” ou “curso de
python”.
"""

texto = input("Digite uma frase: ")

palavra = "jequiti"
palavra2 = "curso de python"

if palavra not in texto and palavra2 not in texto:
    print("A frase não é Spam")

elif palavra in texto or palavra2 in texto:
    print("A frase é Spam")

