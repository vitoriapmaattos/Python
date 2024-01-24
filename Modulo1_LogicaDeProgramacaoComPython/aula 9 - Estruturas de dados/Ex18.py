"""
Escreva um programa para armazenar uma agenda de telefones em um dicionário.
Cada pessoa pode ter um ou mais telefones e a chave do dicionário é o nome da
pessoa. Seu programa deve ter as seguintes funções:

Adicionar contato: acrescenta um novo nome na agenda com um ou mais telefones.

Adicionar telefone: acrescenta um novo telefone em um nome já existente na
agenda. Caso o nome não exista na agenda, você deve perguntar se a pessoa
deseja incluí-lo.

Excluir telefone: remove o telefone de uma pessoa que já está cadastrada na
agenda.

Excluir contato: remove o nome de uma pessoa da agenda.

Consultar contato: obtém as informações de contato de uma pessoa pelo nome.

Listar contatos: listar todos os contatos (nome e telefones) presentes na
agenda.

"""

lista = {}

while True:
    print("""
--- Agenda Telefônica ---
1) Adicionar Contato:
2) Adicionar Telefone:
3) Excluir Telefone:
4) Excluir Contato:
5) Consultar Contato:
6) Listar Contatos:
0) Sair: """)

    opcao = int(input("Digite uma opção [0 - 6]: "))



    match opcao:

        case "1": #Adicionar contato
            nome = input("Digite o nome do contato: ")
            telefones = input("Digite o telefones separados por virgula: ").split(" , ")
            lista[nome] = telefones
            print(f"{nome} foi adicionado.")


        case "2": #Adicionar telefone
            nome = input("Digite o nome do contato que adicionar um telefone: ")
            telefone = input("Digite o telefone do contato: ")
            if nome in lista:
                lista[nome].append(contato)

            else:
                resposta = input(f"O nome {nome} não esta na agenda. Deseja inclui-lo (s/n): ").lower()
                if resposta == "s":
                    lista[nome] = telefone

        case "3": #Excluir telefone
            nome = input("Digite o nome do contato que deseja remover o telefone: ")
            if nome in lista:
                for indice, telefone in enumerate(lista[nome]):
                    print(f"{indice+1}) {telefone}")

                indice_telefone = int(input("Selecione o telefone para ser removido")) - 1

                if indice_telefone not in range(len(agenda[nome])):
                    print("O índice selecionado não existe.")

                else:
                    lista[nome].pop(indice_telefone)

            else:
                print(f"{nome} não encontrado na agenda.")

        case "4": #Excluir contato
            nome = input("Digite o nome do contato que deseja remover: ")
            if nome in lista:
                del lista[nome]
            else:
                print(f"{nome} não encontrado.")

        case "5": #Consultar contato

            nome = input("Digite o nome que deseja consultar:")
            if nome in lista:
                print(f"Nome: {nome} | Telefones: {', '.join(lista[nome])}")
            else:
                print("Nome não foi encontrado na agenda.")

        case "6": #mostrar contatos
            for nome, telefones in lista.items():
                print(f"Nome: {nome} | Telefones: {', '.join(lista[nome])}")

        case "0": #Sair
            break

        case _: #opção inválida
            print("Opção inválida!")