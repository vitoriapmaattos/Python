"""
Utilizando os conceitos de matrizes e laços de repetição faça um jogo da velha
onde a cada rodada será pedido a posição onde o jogador X quer jogar e onde o
jogador O quer jogar. Caso seja informado uma posição já ocupada, informe que
a "posição já está ocupada" e peça por outra jogada. Quando o jogo acabar
mostrar quem ganhou o jogo, ou em caso de empate, a mensagem: "O jogo empatou".
"""

tabuleiro = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

contador_jogadas = 0
jogador_atual = 1 # 1 == 'X' | -1 == '0'
ganhou = False

while True:
    # Mostrar o tabuleiro
    for linha in tabuleiro:
        for valor in linha:
            if valor == 0:
                print("-", end=" ")
            elif valor == 1:
                print("X", end=" ")
            else:
                print("O", end=" ")
        print()

    # Verificar ganhadores
    if ganhou:
        print("O jogador O ganhou!") if jogador_atual == 1 else print("O jogador X ganhou!")
        break

    # Verificar Empate
    if contador_jogadas == 9:
        print("O jogo empatou")
        break

    # Mostrar o jogador atual
    print("Jogador Atual: X") if jogador_atual == 1 else print(("Jogador atual: O"))

    #Solicitar as posições da jogada
    linha_jogada = int(input("Digite a linha da jogada (0 - 2): "))
    coluna_jogada = int(input("Digite a coluna da jogada (0 - 2): "))

    # Verificar se a jogada é válida
    if tabuleiro[linha_jogada][coluna_jogada] != 0:
        input("Posição ja está ocupada")
        continue

    # Atribuir a jogada ao tabuleiro
    tabuleiro[linha_jogada][coluna_jogada] = jogador_atual

    # Checar se o jogador ganhou
    # Checando as linhas
    for i in range(3):
        soma = tabuleiro[i][0] + tabuleiro[1][i] + tabuleiro[2][i]
        if soma == 3 or soma == -3:
            ganhou = True

    # Checando as diagonais
    diagonal_principal = tabuleiro[0][0] + tabuleiro[1][1] + tabuleiro[2][2]
    diagonal_secundaria = tabuleiro[0][2] + tabuleiro[1][1] + tabuleiro[2][0]

    if diagonal_principal == 3 or diagonal_principal == -3 or diagonal_secundaria == 3 or diagonal_secundaria == -3:
        ganhou = True

    # Aumentar o número de jogadas
    contador_jogadas += 1

    # Trocar o jogado atual
    jogador_atual *= -1