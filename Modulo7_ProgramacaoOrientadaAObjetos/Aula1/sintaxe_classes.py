"""
Classse - É um modelo para o objeto.
* Atributos - Caracteristicas do objeto.
* Meétodos - Ação do objeto.

Nomeclatura das classes - https://peps.python.org/pep-0008/#class-names
"""

class NomeClasse:
        """Docstring da classe."""

        #Método construtor: método utilizado para inicializar um objeto da classe.
        def __init__(self, parametro1: int) -> None:
                # self -> referência ao próprio objeto.
                self.atributo1 = parametro1
                

                # Declara um atributo privado/encapsulado.
                self.__atributo_privado = 0

        # Getters
        @property 
        #Adicionando um comportamento na função - para poder acessar os atributos privados.
        def atributo_privado(self):
            return self.__atributo_privado
    
        # Setters
        @atributo_privado.setter
        #Atualizando o valor do objeto privado
        def atributo_privado(self, novo_valor: int):
            self.__atributo_privado = novo_valor

        # Métodos do objeto
        def metodo1(self):
            """Docstring do método"""
            print("Chamando o método do objeto")

if __name__ == '__main__':
      # Sintaxe para criar um objeto
      objeto_teste = NomeClasse(20)

      # Acessando os atributos
      print(objeto_teste.atributo1)

      # Acessando métodos
      objeto_teste.metodo1()
            