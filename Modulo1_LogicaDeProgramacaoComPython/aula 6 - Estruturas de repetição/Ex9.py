"""
Crie um algoritmo que solicite ao usuário o valor inicial e final de um
intervalo de números e mostre todos os números pares presente nesse
intervalo. Caso não haja nenhum número par o programa deve apresentar a
mensagem: “Não há números pares no intervalo”.
"""
inicio = int(input("Digite o valor inicial do intervalo: "))
fim = int(input("Digite o valor final do intervalo: "))
passo = int(input("Digite o passo do intervalo: "))


tem_par = False  # Variável flag
for i in range(inicio, fim + 1, passo):
    if i % 2 == 0:
        print(i, end=" ")
        tem_par = True

# print(bool(0))
if not tem_par:
    print("Não há números pares no intervalo")
