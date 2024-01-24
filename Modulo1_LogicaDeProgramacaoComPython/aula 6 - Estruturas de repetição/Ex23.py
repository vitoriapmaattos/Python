"""
Crie um programa que simule um empréstimo bancário. Peça ao usuário para
inserir o valor do empréstimo, a taxa de juros e o período de pagamento. O
programa deve calcular as parcelas mensais, mostrando o valor total do
empréstimo com os juros inclusos e o valor de cada parcela.
"""
juros_total = 0

valor = float(input("Digite o valor do empréstimo: "))
taxa = int(input("Digite o valor da taxa de juros (mensal): "))
pagamento = int(input("Digite o período de pagamento (meses): "))

taxa_corrigida = taxa / 100

for tempo in range (pagamento):
    juros = valor * taxa_corrigida
    juros_total += juros

montante = valor + juros_total
parcelas = montante / pagamento

print(f"""
Valor inicial: R$ {valor:.2f}
Parcelas Mensais: R$ {parcelas:.2f}
Valor total do empréstimo: R$ {montante:.2f}
""")