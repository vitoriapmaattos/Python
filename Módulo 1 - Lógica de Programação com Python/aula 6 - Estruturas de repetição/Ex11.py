"""
Vamos criar um jogo de adivinhação de números! O programa irá gerar um número
aleatório entre 1 e 100, e o jogador terá que adivinhar qual é esse número.
O programa deve fornecer dicas ao jogador, informando se o número a ser
adivinhado é maior ou menor do que o número fornecido pelo jogador. O jogo
deve continuar até o jogador adivinhar corretamente o número.
"""

sorteado = gera()
while True :
tentativas += 1
palpite = int(input("DIGITE UM NÚMERO DE 1 À 100 "))
if palpite > sorteado :
print("SEU PALPITE FOI ALTO!")
elif palpite < sorteado :
print("SEU PALPITE FOI BAIXO!")
else:
print("PARABÉNS! VOCÊ ACERTOU COM O NÚMERO ", palpite, " COM ", tentativas, " TENTATIVAS!")
break