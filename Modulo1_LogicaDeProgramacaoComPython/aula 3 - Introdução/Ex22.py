"""
Faça um programa que leia o nome de um livro, o tempo médio (em segundos)
que o usuário leva para ler uma página do livro, o tempo de leitura diário
(em segundos) e a quantidade de páginas de um livro. Ao final, o programa
deverá mostrar um relatório que mostre:
"""

livro = input(f"O nome do livro é: ")
tempo_medio = int(input(f"O tempo médio para ler uma página em segundos: "))
qtd_paginas = int(input(f"A qtd de páginas do livro: "))

horas_dia = 24
segundos_hora = 3600
dias_semana = 7

segundos_dia = horas_dia * segundos_hora
paginas_dia = segundos_dia / tempo_medio
dias_livro = qtd_paginas / paginas_dia
horas_livro = dias_livro * horas_dia
semana_livro = dias_livro / dias_semana


print(f"Quantidade de páginas lidas por dia: {paginas_dia}")
print(f"Quantidade de horas necessárias para ler o livro: {horas_livro}")
print(f"Quantidade de dias necessários para ler o livro: {dias_livro}")
print(f"Quantidade de semanas necessárias para ler o livro: {semana_livro}")