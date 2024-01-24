"""
A universidade Entra21 tem a seguinte política de classificação:
Cada estudante recebe uma nota no intervalo de 0 a 100.
Qualquer nota abaixo de 40 é uma classificação de reprovado.
William é um professor nessa universidade e gosta de arredondar as notas dos
alunos de acordo com os seguintes critérios:
Se a diferença entre a nota e o próximo múltiplo de 5 é menor do que 3, a n
ota é arredondada para o próximo múltiplo de 5.
Se o valor da nota for menor do que 38, nenhum arredondamento será aplicado
e a classificação será mantida como reprovado.
Exemplos:
nota = 84 -> 85 (85 - 84 < 3)
nota = 29 -> 29 (não arredonda, nota é mais baixa do que 40)
nota = 57 -> 57 (não arredonda, 60 - 57 >= 3)

Faça um programa que leia as notas de 5 alunos e mostre a nota arredondada,
a média da turma, a quantidade de alunos aprovados e a quantidade de alunos
reprovados.
"""

# Inicialização das variáveis de contagem
TOTAL_ALUNOS = 5
aprovados = 0
reprovados = 0
soma_notas = 0

# Loop para coletar notas e realizar os cálculos
for i in range(TOTAL_ALUNOS):
    nota = int(input(f"Digite a nota do aluno {i + 1}: "))

    nota_arredondada = nota
    # Calculando o arredondamento
    if nota >= 38:
        proximo_multiplo_5 = (nota + 4) // 5 * 5
        nota_arredondada = proximo_multiplo_5 if proximo_multiplo_5 - nota < 3 else nota

    print(f"Nota arredondada: {nota_arredondada}")

    if nota_arredondada >= 40:
        aprovados += 1
    else:
        reprovados += 1

    soma_notas += nota_arredondada

# Cálculo da média da turma
media_turma = soma_notas / TOTAL_ALUNOS

print("Média da turma:", media_turma)
print("Quantidade de alunos aprovados:", aprovados)
print("Quantidade de alunos reprovados:", reprovados)
