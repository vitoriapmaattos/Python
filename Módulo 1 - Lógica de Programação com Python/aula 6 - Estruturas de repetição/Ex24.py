"""
Desenvolva um programa que compare diferentes tipos de investimentos. Peça ao
usuário para informar o valor inicial a ser investido, a taxa de retorno anual
e o período de investimento. O programa deve calcular o valor final para
diferentes tipos de investimentos (poupança, renda fixa e ações) e mostrar a
diferença de retorno entre eles.
"""

valor_inicial = float(input("Digite o valor inicial: "))
taxa_poupanca = int(input("Digite o valor da taxa de retorno anual (Poupança): "))
taxa_rendafixa = int(input("Digite o valor da taxa de retorno anual (Renda Fixa): "))
taxa_acoes = int(input("Digite o valor da taxa de retorno anual (Ações): "))
periodo = int(input("Digite o período de investimento: (ano) "))

taxa_poupanca2 = taxa_poupanca / 100
taxa_rendafixa2 = taxa_rendafixa / 100
taxa_acoes2 = taxa_acoes / 100

juros_total_poupanca = 0
juros_total_acoes = 0
juros_total_rendafixa = 0

#Poupança
for tempo in range (periodo):
    juros_poupanca = valor_inicial * taxa_poupanca2
    juros_total_poupanca += juros_poupanca

retorno_poupanca = valor_inicial + juros_total_poupanca

#Ações
for tempo in range (periodo):
    juros_acoes = valor_inicial * taxa_acoes2
    juros_total_acoes += juros_acoes

retorno_acoes = valor_inicial + juros_total_acoes

#Renda fixa
for tempo in range (periodo):
    juros_rendafixa = valor_inicial * taxa_rendafixa2
    juros_total_rendafixa += juros_rendafixa

retorno_rendafixa = valor_inicial + juros_total_rendafixa

print(f"""
Valor investido: R$ {valor_inicial:.2f}

POUPANÇA
Taxa de retorno {taxa_poupanca}%
Retorno = R$ {retorno_poupanca:.2f}

RENDA FIXA
Taxa de retorno {taxa_rendafixa}%
Retorno = R$ {retorno_rendafixa:.2f}

AÇOES
Taxa de retorno {taxa_acoes}%
Retorno = R$ {retorno_acoes:.2f}
""")