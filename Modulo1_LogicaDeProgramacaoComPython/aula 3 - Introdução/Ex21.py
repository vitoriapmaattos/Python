"""
Escreva um programa que calcule o valor futuro de um investimento com base
no montante inicial, na taxa de juros e no período de tempo. Peça ao usuário
para inserir essas informações e exiba o valor futuro. Você pode utilizar a
fórmula de juros compostos para realizar o cálculo.
"""

montante = int(input("Digite o capital inicial: "))
taxa_juros = float(input("Digite a taxa de juros anual: "))
período = float(input("Digite o período em anos: "))

porcentagem = taxa_juros / 100
i = (1 + porcentagem)
tempo = i ** período
m = montante * tempo

valor_futuro = montante * tempo

print(f"O valor futuro é: {valor_futuro}")