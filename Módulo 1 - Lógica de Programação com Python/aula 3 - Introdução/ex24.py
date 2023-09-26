"""Crie um algoritmo para efetuar o cálculo da quantidade de litros de combustível gastos em uma viagem,
sabendo-se que o carro faz 12 km com um litro. Deverão ser fornecidos o tempo gasto na viagem e a velocidade
média. O algoritmo deverá apresentar os valores da velocidade média, tempo gasto na viagem, distância percorrida
e a quantidade de litros utilizados na viagem."""
# 1l = 12km
# x    y
litros = 12
D = float(input("quantos km tu quer viajar? "))
R = D * 12
print(f"tu precisa de {R}Lt de combustível.")
