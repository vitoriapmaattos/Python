"""Implementação da conta."""
from __future__ import annotations

#Criando a Classe
class Conta:
    """Conta representa uma conta bancária.

    Attributes:
        numero (str): Número identificador da conta.
        titular (str): Nome do titular da conta.
        saldo (float): Saldo da conta.
        limite (float): Limite da conta.
    """

    #Atributo estático -> Pertence a Classe não ao objeto.
    quantidade_contas = 0 

    # Self se utiliza sempre que estivermos acessando um atributo do objeto

    #Criando o objeto na classe
    def __init__(self, numero: str, titular: str):
        # Realizando a validação do número da conta
        if len(numero) != 9:
            raise AttributeError("Número da conta deve possuir 9 digitos.")
        
        #Encapsulamento dos dados
        self.__numero = numero
        self.titular = titular # Está usando o @titular.setter para definir valor e encapsular
        self.__limite = 100
        self.__saldo = 0

        #Incrementando a quantidade de contas no atributo estático da classe
        Conta.quantidade_contas += 1

    # Formata a saída de dados (print)
    def __str__(self):
        return f"Titular: {self.__titular} | Saldo: {self.__saldo} | Limite: {self.limite}"

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, novo_titular: str):
        self.__titular = novo_titular.title()

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite (self, novo_limite: float):
        self.__limite = novo_limite

    @property
    def saldo(self):
        return self.__saldo
    

    # Métodos para os objetos
    def depositar(self, valor: float) -> None:
        """Deposita um valor no saldo da conta.

        Args:
            Valor (float): Valor do depósito
        """
        self.__saldo += valor

    def sacar(self, valor: float) -> bool:
        """Saca um valor da conta se o saldo + limite for maior ou igual ao valor do saque
        Args:
            valor (float): Valor do saque.
        Returns:
            True se for bem sucedido, False caso contrário.
        """
        if (self.__saldo + self.__limite) < valor:
            print("Saldo indisponivel para realizar a operação")
            return False
        if self.__saldo < valor:
            self.__limite -= valor - self.__saldo
            self.__saldo = 0
        else:
            self.__saldo -= valor
        
        return True
    
    def transferir(self, valor: float, conta_destino: Conta) -> None:
        """Transfere o valor de uma conta para outra se o saldo + limite for > ou = ao valor da transferência

        Args:
            valor (float): Valor da transferência
            conta_destino (Conta): Conta de destino da transferência
        """
        if (self.sacar(valor)):
            conta_destino.depositar(valor)
            print("Transferência realizada com sucesso.")

    # Método para a classe
    @staticmethod
    def verifica_numero_conta(numero: str) -> bool:
        """Verificar se o número da conta é válido.
        
        Args:
            numero (str): Número da conta.
        
        Returns:
            True caso o número da conta seja válido, False caso contrário
        """
        return len(numero) == 9


if __name__ == "__main__":

    #Criando um objeto na classe conta
    conta_william = Conta("123456789", "wiliam cirico")

    #Informando os dados da conta
    print(f"Nome do titular quando foi criado: {conta_william.titular}")

    #Alterando o nome do titular
    conta_william.titular = "william cirico"

    #Informando o novo nome do titular
    print(f"Nome do titular quando foi modificado: {conta_william.titular}")

    #Informando o saldo inicial
    print(f"Saldo: {conta_william.saldo}")

    #Realizando um depósito
    conta_william.depositar(100_000_000)

    #Informando o valor depositado
    print(f"Valor após o depósito: {conta_william.saldo}")

    #Realizando um saque e informando o valor do saldo
    conta_william.sacar(100_000_101)
    print(f"Valor após o saque: {conta_william.saldo} | Limite {conta_william.limite}")

    #Realizando um saque e informando o valor do saldo
    conta_william.sacar(1000)
    print(f"Valor após o saque: {conta_william.saldo} | Limite {conta_william.limite}")

    #Realizando um saque e informando o valor do saldo
    conta_william.sacar(99999050)
    print(f"Valor após o saque: {conta_william.saldo} | Limite {conta_william.limite}")

    #Informando dados formatados pelo __str__
    print(conta_william)    

    #Criando um outro objeto na classe conta
    conta_marcos = Conta("123467282", "marcos silva")  
    print(conta_marcos)

    #Realizando a transferência e exibindo o resumo das contas
    conta_william.transferir(20, conta_marcos)
    print(conta_william)
    print(conta_marcos)

    #Acessando o atributo estático da classe
    print(Conta.quantidade_contas)

    #Testando o método da classe
    if (Conta.verifica_numero_conta("123183721")):
        print("Número da conta é válido!")
    else:
        print("Número da conta é inválido")


