"""
Crie um algoritmo que leia o nome e as três
notas de 5 alunos e mostre a média de cada um
deles. Ao final mostre a média da turma.
"""
alunos=int(input("Quantos alunos tem na turma: ") )
provas=int(input("Quantas provas foram feitas: ") )

media_turma = 0

for aluno in range(alunos):
    print(f"Aluno {aluno+1}:")

    media_aluno = 0
    for prova in range(provas):
        print(f"Digite a nota de prova {prova+1}: ")
        nota = float(input())
        media_aluno += nota

    media_aluno /= provas
    print(f"Média do Aluno {aluno+1}: {media_aluno}")

    media_turma += media_aluno

media_turma /= alunos
print(f"Média da turma: {media_turma}")