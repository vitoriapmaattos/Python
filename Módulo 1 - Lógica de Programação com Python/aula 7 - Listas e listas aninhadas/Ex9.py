"""
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e
armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor
foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para
gerar números aleatórios, simulando os lançamentos dos dados.
"""

from random import randint #gera numeros inteiros aleatórios

resultado = [0] * 7  # posição 0 não será usada.
for i in range(100):
    x = randint(1, 6)
    resultado[x] += 1

for i in range(1, 7):
    print(i, ": ", resultado[i])