"""
Escreva um programa que pergunte a distância que um passageiro deseja
percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para
viagens de até de 200km, e R$ 0,45 para viagens mais longas.
"""

kmviagem = float(input("Qual a distância que será percorrida? (km)"))

if kmviagem <= 200:
    preco = kmviagem * 0.50
    print(f"O preço da passagem é: R$ {preco:.2f}")

elif kmviagem > 200:
    preco = kmviagem * 0.45
    print(f"O preço da passagem é: R$ {preco:.2f}")

else:
    print("Distância invalida")