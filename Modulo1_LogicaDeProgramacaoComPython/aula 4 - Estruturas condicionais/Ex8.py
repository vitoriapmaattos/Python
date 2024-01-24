"""
 Desenvolva um programa que recebe do usuário o placar de um jogo de
 futebol (os gols de cada time) e informe se o resultado foi um empate,
 a vitória do primeiro time ou do segundo time.
"""

gols_A = int(input("Quantos gols o time A fez?"))
gols_B = int(input("Quantos gols o time B fez?"))

if gols_A > gols_B:
    print("Time A venceu")

elif gols_A == gols_B:
    print("Empate")

else:
    print("time B venceu")