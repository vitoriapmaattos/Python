"""
Escreva um programa para calcular a redução do tempo de vida de um fumante.
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
Considere que um fumante perde 11 minutos de vida a cada cigarro, calcule
quantos dias de vida um fumante perderá. Exiba o total em dias.
"""

qtdcigarros = int(input("Quantos cigarros fumandos por dia? "))
qtdanos = int(input("Fuma a quantos anos? "))

minutosperdido = qtdcigarros * 11 #minutos gastos por dia

tempodias = qtdanos * 365 #total de dias fumando

tempoperdido = tempodias * minutosperdido #total minutos perdidos fumando

diasperdidos = tempoperdido / 1440 #total em dias perdidos fumando

print(f"{diasperdidos:.0f} dias perdidos fumando.")