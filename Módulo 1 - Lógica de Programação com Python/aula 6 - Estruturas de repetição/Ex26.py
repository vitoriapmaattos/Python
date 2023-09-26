"""
Você está coreografando um show de circo com vários animais. Para um ato,
você recebe dois cangurus em uma linha numérica prontos para pular em uma
direção positiva (ou seja, em direção ao infinito positivo).
O primeiro canguru inicia em uma posição x1 e se move a uma taxa v1 de metros
por salto.
O segundo canguru inicia em uma posição x2 e se move a uma taxa v2 de metros
por salto.
Você deve implementar um algoritmo que verifique se os dois cangurus vão
estar no mesmo local ao mesmo tempo durante o show. Se for possível mostre
na tela “SIM” e indique em qual salto os dois cangurus irão se encontrar,
caso contrário mostre “NÃO”
"""

x1 = int(input("Digite a posição inicial do canguru 1: "))
v1 = int(input("Digite a velocidade do canguru 1: "))
x2 = int(input("Digite a posição inicial do canguru 2: "))
v2 = int(input("Digite a velocidade do canguru 2: "))

ponto_de_encontro = int((x2 - x1) / (v1 - v2))

if ponto_de_encontro >= 0:
    print(f"SIM. Eles irão se encontrar no {ponto_de_encontro}º salto")
else:
    print(f"NÃO")