"""
Neste desafio, você e sua equipe irão construir um sistema básico para gerenciar livros em uma biblioteca. Os livros serão armazenados em um dicionário, onde cada chave é um ID único do livro (um número inteiro) e o valor é outro dicionário contendo informações sobre o livro.
Especificações
Informações do Livro:
Título
Autor
Ano de publicação
Gênero
Avaliações
Status (Emprestado ou Disponível)

Funções requeridas:
adicionar_livro(id, titulo, autor, ano, genero): Adiciona um livro ao sistema.
remover_livro(id): Remove um livro do sistema usando o ID.
emprestar_livro(id): Altera o status do livro para “Emprestado”.
devolver_livro(id): Altera o status do livro para “Disponível”.
listar_livros(): Retorna uma lista de todos os livros e suas informações.
buscar_livro(titulo): Busca um livro pelo título e retorna as suas informações.
livros_por_autor(autor): Retorna uma lista de todos os livros de um determinado autor.
livros_por_genero(genero): Retorna uma lista de todos os livros de um determinado gênero.
livros_emprestados(): Lista todos os livros que estão emprestados.
avaliar_livro(id): Permite adicionar uma avaliação para o livro (1 a 5 estrelas).
obter_media_avaliacoes(id): Retorna a média de avaliações de um livro.

Regras adicionais:
Não é possível adicionar um livro com um ID que já existe.
Não é possível remover ou emprestar um livro que não existe.
Não é possível emprestar um livro que já foi emprestado.
Não é possível devolver um livro que já está disponível.

Alunos: Alexandre Coimbra, Vitoria Mattos, Yuri Campos, Igor Faggiani e Mateus Hennich

"""


identidade = []
dicionario = {}


def mostrar_menu() -> None:
    """Exibe o menu da aplicação."""
    print("""\n--- Gerenciamento de livros ---
1: Adicionar Livro
2: Remover Livro
3: Emprestar Livro
4: Devolver Livro
5: Listar Livros
6: Buscar Livro
7: Livros por Autor
8: Livros por Gênero
9: Livros Emprestados
10: Avaliar Livro
11: Obter Média das Avaliações
12: Sair
""")


def adicionar_livro(identificador: int, livro: str, autor: str, ano_publicacao: int, genero: str) -> None:  # Case 1
    """Adiciona um livro no sistema."""
    for livro_info in dicionario.values():
        if livro == livro_info['Título']:
            print("O livro já consta no sistema.")
            return
    avaliacoes = []
    status = input("Digite 'E' caso o livro esteja emprestado ou 'D' caso o livro esteja disponível: ").lower()
    if status == "d":
        status = "Disponível"
    elif status == "e":
        status = "Emprestado"
    else:
        print("Dado incorreto, tente novamente.")
        return
    dicionario[identificador] = {"Título": livro, "Autor": autor,
                                 "Ano de Publicação": ano_publicacao, "Gênero": genero, "Avaliações": avaliacoes,
                                 "Status": status}
    print("Livro adicionado com sucesso!")


def remover_livro(identificador: int) -> None:  # Case 2
    """Remove um livro da biblioteca usando o Id."""
    if identificador in dicionario:
        print(f"O livro {dicionario[identificador]['Título']}, com o id {identificador}, foi removido")
        del (dicionario[identificador])
        identidade.remove(identificador)
    else:
        print(f"Id {identificador} não encontrado.")


def emprestar_livro(identificador: int) -> None:  # Case 3
    """Faz o empréstimo de um livro"""
    if identificador in dicionario:
        if dicionario[identificador]['Status'] == "Emprestado":
            print("O livro ja está emprestado.")
        else:
            dicionario[identificador]['Status'] = "Emprestado"
            print(f"O livro {dicionario[identificador]['Título']} está agora emprestado. ")
    else:
        print(f"Id {identificador} não encontrado.")


def devolver_livro(identificador: int) -> None:  # Case 4
    """Faz a devolução de um livro"""
    if identificador in dicionario:
        if dicionario[identificador]['Status'] == "Disponível":
            print("O livro já está disponível.")
        else:
            dicionario[identificador]['Status'] = "Disponível"
            print(f"O livro {dicionario[identificador]['Título']} está agora disponível. ")
    else:
        print(f"Id {identificador} não encontrado.")


def listar_livros() -> None:  # Case 5
    """Lista todos os livros registrados e suas informações."""
    print("\nLista de livros: ")
    for identificador in dicionario:
        print(
            f"ID: {identificador} | Título: {dicionario[identificador]['Título']} | "
            f"Autor: {dicionario[identificador]['Autor']} | "
            f"Ano de publicação: {dicionario[identificador]['Ano de Publicação']} |"
            f" Gênero: {dicionario[identificador]['Gênero']} | "
            f"Avaliações: {(dicionario[identificador]['Avaliações'])} |"
            f" Status: {dicionario[identificador]['Status']}")


def buscar_livro(titulo: str) -> None:  # Case 6
    """Exibe as informações de um livro."""
    achou = False
    for i in dicionario:
        if titulo == dicionario[i]["Título"]:
            achou = True
            print(
                f"Título: {dicionario[i]['Título']} | Autor: {dicionario[i]['Autor']} | "
                f"Ano de publicação: {dicionario[i]['Ano de Publicação']} |"
                f" Gênero: {dicionario[i]['Gênero']} | Avaliações: {dicionario[i]['Avaliações']} |"
                f" Status: {dicionario[i]['Status']}")
    if not achou:
        print("Livro não encontrado.")


def livro_autor(autor: str) -> None:  # Case 7
    """ Retorna uma lista de todos os livros de um determinado autor!"""
    print(f"\nLista de livros do autor {autor}: ")
    achou = False
    for i in dicionario:
        if autor == dicionario[i]["Autor"]:
            achou = True
            print(
                f"Título: {dicionario[i]['Título']} | Autor: {dicionario[i]['Autor']} | "
                f"Ano de publicação: {dicionario[i]['Ano de Publicação']} |"
                f" Gênero: {dicionario[i]['Gênero']} | Avaliações: {dicionario[i]['Avaliações']} |"
                f" Status: {dicionario[i]['Status']}")
    if not achou:
        print("Autor não encontrado")


def genero_livro(genero: str) -> None:  # Case 8
    """ Retorna uma lista de todos os livros de um determinado genero!"""
    print(f"\nLista de livros do gênero {genero}: ")
    achou = False
    for i in dicionario:
        if genero == dicionario[i]["Gênero"]:
            achou = True
            print(
                f"Título: {dicionario[i]['Título']} | Autor: {dicionario[i]['Autor']} | "
                f"Ano de publicação: {dicionario[i]['Ano de Publicação']} |"
                f" Gênero: {dicionario[i]['Gênero']} | Avaliações: {dicionario[i]['Avaliações']} |"
                f" Status: {dicionario[i]['Status']}")
    if not achou:
        print("Gênero não encontrado.")


def livros_emprestados() -> None:  # Case 9
    """ Retorna uma lista de todos os livros emprestados"""
    print(f"\nLista de livros emprestados: ")
    achou = False
    for i in dicionario:
        if dicionario[i]["Status"] == "Emprestado":
            achou = True
            print(f"Título: {dicionario[i]['Título']} | Autor: {dicionario[i]['Autor']} | "
                  f"Ano de publicação: {dicionario[i]['Ano de Publicação']} | "
                  f"Gênero: {dicionario[i]['Gênero']} | Avaliações: {dicionario[i]['Avaliações']} | "
                  f"status: {dicionario[i]['Status']}")
    if not achou:
        print("Não há livros emprestados.")


def avaliar_livro(identificador: int) -> None:  # Case 10
    """ Adiciona uma avaliação a um livro."""
    if identificador in dicionario:
        if dicionario[identificador]['Status'] == "Emprestado":
            print("Não é possível avaliar um livro que está emprestado.")
        else:
            avaliacao = int(input("Informe a avaliação, de 1 a 5: "))
            if avaliacao < 1 or avaliacao > 5:
                print("Valor incorreto, tente novamente.")
            else:
                dicionario[identificador]['Avaliações'].append(avaliacao)
    else:
        print("Livro não encontrado!")


def obter_media_avaliacoes(identificador: int) -> None:  # Case 11
    """ Obtém a média de avaliação de um livro"""
    if identificador in dicionario:
        avaliacoes = dicionario[identificador]['Avaliações']
        if not avaliacoes:
            print("O livro ainda não foi avaliado.")
        else:
            soma = sum(avaliacoes)
            media = soma / len(avaliacoes)
            print(f"A média das avaliações do livro é {media:.2f}.")
    else:
        print("Id não encontrado no sistema.")


# Menu para interação
while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            identificador = int(input("Informe o ID do livro. "
                                      "Ele não pode já estar sendo utilizado, tem que ser um novo: "))
            if identificador in identidade:
                print("O ID já está sendo utilizado, tente novamente.")
                continue
            else:
                identidade.append(identificador)
            livro = input("Digite o nome do Livro: ")
            autor = input("Digite o Autor do livro: ")
            ano_publicacao = int(input("Digite o ano de publicação do livro: "))
            genero = input("Digite o gênero do livro: ")
            adicionar_livro(identificador, livro, autor, ano_publicacao, genero)
        case "2":
            identificador = int(input("Digite o id do livro a ser removido: "))
            remover_livro(identificador)
        case "3":
            identificador = int(input("Digite o id do livro a ser emprestado: "))
            emprestar_livro(identificador)
        case "4":
            identificador = int(input("Digite o id do livro a ser devolvido: "))
            devolver_livro(identificador)
        case "5":
            listar_livros()
        case "6":
            titulo = input("Digite o nome do livro: ")
            buscar_livro(titulo)
        case "7":
            autor = input("Informe um autor: ")
            livro_autor(autor)
        case "8":
            genero = input("Informe um gênero de livro: ")
            genero_livro(genero)
        case "9":
            livros_emprestados()
        case "10":
            identificador = int(input("Informe o id do livro: "))
            avaliar_livro(identificador)
        case "11":
            identificador = int(input("Informe o id do livro: "))
            obter_media_avaliacoes(identificador)
        case "12":
            print("Encerrando.")
            break
        case _:
            print("Opção inválida!")