# Importando as pessoas no exercício 1
from Exercicio1 import Person

class PhoneBook:
    """PhoneBook representa uma agenda de contatos.
    
    Attributes:
        name (str): Nome do contato.
    """

    # Método Construtor
    def __init__(self, name: str):
        self.name = name
        self.__people = []


    # Getter para poder acessar o atributo privado
    @property
    def people(self):
        """(List[Person]): Lista de peddoas na agenda"""
        return self.__people
    
    # Método para adicionar as pessoas na agenda
    def add_person(self, name: str, phone: str):
        """Adiciona uma pessoa na agenda.
        
        Args:
            person (Person): Pessoa que será adicionada na agenda."""
        
        person = Person(name, phone)

        if len(self.__people) < 10:
            self.__people.append(person)
        else:
            print("Agenda Lotada.")

    # Método para remover a pessoa pelo nome

    def remove_person(self, name: str):
        """Remove um passo da agenda pelo nome
        Args:
            name (str): Nome da pessoa que será removida."""
        
        for person in self.__people:
            if person.name == name:
                self.__people.remove(person)
                return

        print("Pessoa não encontrada na agenda")

    # Método para pesquisar pelo nome

    def search_person(self, name: str):
        """Pesquisa uma pessoa pelo nome.
        Args:
            name (str): Nome da pessoa pesquisada.
        """

        for person in self.__people:
            if person.name == name:
                print(person)
                return
            
        print("Pessoa não encontrada na agenda")

    # def list_person(self):


