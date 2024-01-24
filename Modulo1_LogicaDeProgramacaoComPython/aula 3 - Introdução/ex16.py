"""Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio R.
 A fórmula para calcular  volume é: (4/3) *  * R3."""
#pedi ajuda do chat gp para achar o código do pi
import math
raio = float(input("Digite o raio: "))
pi = (math.pi)
v = (4/3) * pi * raio ** 3
print("o volume é:", v)
