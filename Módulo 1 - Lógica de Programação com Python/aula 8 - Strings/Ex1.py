"""
aça um programa que então leia uma string e a imprima. Caso o valor digitado
não seja um valor textual (ex.: 12345), uma mensagem deve ser mostrada para o
usuário e o valor deve continuar sendo solicitado até que o mesmo seja válido.
"""

while True:
    valor_textual = input("Digite um valor")
    if str.isdigit(valor_textual):
        print("É um número, tente novamente!")

    else:
        print("É um texto!")
        break
