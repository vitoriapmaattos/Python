"""
Faça um programa que representa um algoritmo que leia um ano e verifique
se ele é bissexto. Para determinar se uma ano é bissexto execute as seguintes
etapas:
Se o ano for uniformemente divisível por 4, vá para a etapa 2. Caso contrário,
vá para a etapa 5.
Se o ano for uniformemente divisível por 100, vá para a etapa 3. Caso
contrário, vá para a etapa 4.
Se o ano for uniformemente divisível por 400, vá para a etapa 4. Caso
contrário, vá para a etapa 5.
O ano é bissexto (tem 366 dias).
O ano não é um ano bissexto (tem 365 dias).
"""

ano = int(input("Digite um ano: "))

if ano % 4 == 0 and ano % 100 != 0:
        print(f"{ano} é um ano bissexto")

elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
        print(f"{ano} é um ano bissexto")

else:
    print(f"{ano} não é um ano bissexto.")

