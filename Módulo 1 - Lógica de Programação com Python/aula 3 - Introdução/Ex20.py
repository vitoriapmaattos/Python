"""
Faça um programa que leia horas, minutos e segundos e
converta para segundos.
"""

hora = int(input(f"Digite a hora: "))
minutos = int(input(f"Digite os minutos: "))
segundos = int(input(f"Digite os segundos: "))

s1 = hora * 3600
s2 = minutos * 60
segundos_total = s1 + s2 + segundos

print(f"Total em segundos é: {segundos_total}")