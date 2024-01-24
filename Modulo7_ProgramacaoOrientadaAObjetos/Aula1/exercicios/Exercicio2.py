# Importanto módulo de números aleatórios para utilizar na matrícula
from random import randint

# Importando as tipagens do python
from typing import List

class Student:
    """ Student representa um aluno.

    Attributes:
        name (str): Nome do aluno.
        grades (List[float]): Notas do aluno.    
    - Não listamos a matrícula pois é um atributo privado -
    """

    # Método Construtor
    def __init__(self, name: str, grades: List[float]):
        self.__registration = randint(1, 100_000) # Criando a matrícula aleatoriamente
        self.name = name
        self.grades = grades

    @property # Criando o getter para visualizar a matrícula que é privada
    def registration(self):
        """(int): Número da matrícula do aluno."""
        return self.__registration
    
    # Método para calcular a média
    def get_average(self) -> float: #setinha float significa que o resultado final é um float
        """Calcula a média do aluno baseado nas notas"""

        """Caso não tenha nenhuma nota lançada, a média será 0"""
        if not self.grades:
            return 0
        
        return sum(self.grades) / len(self.grades) 
        """soma as notas em grades, conta o número/tamanho(len) de notas em 
        grades e divide a soma por esse valor."""

    # Método para verificar a situação do aluno
    def get_situation(self) -> str:
        """Retorna a situação do aluno com base na média.
        
        Returns:
            A situação do aluno ("Aprovado", "Recuperação", "Reprovado")
        """
            
        """Caso não tenha nenhuma nota lançada, aparecerá um aviso de notas não cadastradas"""
        if not self.grades:
            return "Notas não cadastradas"
        
        media = self.get_average()

        if 0 <= media <= 4:
            return "Reprovado"
        
        if 4 <= media <= 6:
            return "Recuperação"
        
        return "Aprovado"
