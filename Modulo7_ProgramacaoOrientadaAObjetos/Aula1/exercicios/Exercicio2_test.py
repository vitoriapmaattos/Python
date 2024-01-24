import pytest

from Exercicio2 import Student

def test_student_creation ():
    student = Student("Willian", [10, 10, 10]) # Criando um aluno, dando um nome e suas notas.

    # Verifica se todas as propridades estão corretas
    assert student.name == "Willian"
    assert student.grades == [10, 10, 10]
    assert 1 <= student.registration <= 100_000 # Conferindo se o valor aleatório esta dentro do intervalo pré estabelecido

def test_get_average():
    student1 = Student("Ana", [8, 9, 10]) # Criando um aluno, dando um nome e suas notas.
    student2 = Student("Willian", [10, 10, 10]) # Criando outro aluno, dando um nome e suas notas.


    assert student1.get_average() == 9
    assert student2.get_average() == 10

def test_get_average_without_grades():
    student = Student("Willian", []) # Criando um aluno, dando um nome e suas notas.

    assert student.get_average() == 0

def test_get_situation():
    student1 = Student("Ana", [3, 3, 3]) # Criando um aluno, dando um nome e suas notas.
    student2 = Student("Willian", [5, 5, 5]) # Criando outro aluno, dando um nome e suas notas.
    student3 = Student("Vitória", [10, 10, 10]) # Criando outro aluno, dando um nome e suas notas.

    assert student1.get_situation() == "Reprovado"
    assert student2.get_situation() == "Recuperação"
    assert student3.get_situation() == "Aprovado"

def test_get_situation_without_grades():

    student1 = Student("Ana", []) # Criando um aluno, dando um nome e suas notas.

    assert student1.get_situation() == "Notas não cadastradas"
