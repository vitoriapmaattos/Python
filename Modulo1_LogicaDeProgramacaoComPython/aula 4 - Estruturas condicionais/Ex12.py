"""
Escreva um programa que receba três valores: A, B e C.
Faça as comparações necessárias para exibir na tela o maior valor
entre os três.
"""

valor_A = int(input("Escreva o primeiro valor: "))
valor_B = int(input("Escreva o segundo valor: "))
valor_C = int(input("Escreva o segundo valor: "))

if valor_A > valor_B and valor_A >  valor_C:
    print(f"O primeiro valor é o maior")

elif (valor_B > valor_A and valor_B>  valor_C):
    print(f"O segundo valor é o maior")

elif (valor_C > valor_A and valor_C>  valor_B):
    print(f"O terceiro valor é o maior")

else:
    print(f"Os valores maiores são iguais")