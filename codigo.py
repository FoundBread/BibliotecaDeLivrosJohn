# Dicionário para armazenar os livros
biblioteca = {}

# Função para adicionar um livro à biblioteca
def adicionar_livro(titulo, autor, ano_publicacao):
    if titulo in biblioteca:
        print(f"O livro '{titulo}' já está na biblioteca.")
    else:
        biblioteca[titulo] = {'autor': autor, 'ano_publicacao': ano_publicacao, 'disponivel': True}
        print(f"Livro '{titulo}' adicionado com sucesso.")

# Função para atualizar as informações de um livro existente na biblioteca
def atualizar_livro(titulo, autor=None, ano_publicacao=None, disponivel=None):
    if titulo in biblioteca:
        if autor:
            biblioteca[titulo]['autor'] = autor
        if ano_publicacao:
            biblioteca[titulo]['ano_publicacao'] = ano_publicacao
        if disponivel is not None:
            biblioteca[titulo]['disponivel'] = disponivel
        print(f"Informações do livro '{titulo}' atualizadas com sucesso.")
    else:
        print("Livro não encontrado na biblioteca.")

# Função para remover um livro da biblioteca
def remover_livro(titulo):
    if titulo in biblioteca:
        del biblioteca[titulo]
        print(f"Livro '{titulo}' removido com sucesso.")
    else:
        print("Livro não encontrado na biblioteca.")

# Função para consultar a disponibilidade de um livro específico
def consultar_disponibilidade(titulo):
    if titulo in biblioteca:
        if biblioteca[titulo]['disponivel']:
            print(f"Livro '{titulo}' está disponível.")
        else:
            print(f"Livro '{titulo}' está indisponível.")
    else:
        print("Livro não encontrado na biblioteca.")

# Função para listar todos os livros na biblioteca
def listar_livros():
    if biblioteca:
        print("Lista de livros na biblioteca:")
        for titulo, info in biblioteca.items():
            disponibilidade = "disponível" if info['disponivel'] else "indisponível"
            print(f"- {titulo} (Autor(a): {info['autor']}, Ano: {info['ano_publicacao']}, Disponibilidade: {disponibilidade})")
    else:
        print("A biblioteca está vazia.")

# Menu interativo
def menu():
    while True:
        print("\nGerenciamento de Biblioteca")
        print("1. Adicionar Livro")
        print("2. Atualizar Livro")
        print("3. Remover Livro")
        print("4. Consultar Disponibilidade")
        print("5. Listar Todos os Livros")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Título do livro: ")
            autor = input("Autor(a) do livro: ")
            ano_publicacao = input("Ano de publicação: ")
            adicionar_livro(titulo, autor, ano_publicacao)
        elif opcao == '2':
            titulo = input("Título do livro a ser atualizado: ")
            autor = input("Novo autor(a) (pressione Enter para manter o atual): ")
            ano_publicacao = input("Novo ano de publicação (pressione Enter para manter o atual): ")
            disponivel = input("Disponibilidade (True para disponível, False para indisponível, pressione Enter para manter o atual): ")
            if disponivel.lower() == 'true':
                disponivel = True
            elif disponivel.lower() == 'false':
                disponivel = False
            else:
                disponivel = None
            atualizar_livro(titulo, autor if autor else None, ano_publicacao if ano_publicacao else None, disponivel)
        elif opcao == '3':
            titulo = input("Título do livro a ser removido: ")
            remover_livro(titulo)
        elif opcao == '4':
            titulo = input("Título do livro para consultar a disponibilidade: ")
            consultar_disponibilidade(titulo)
        elif opcao == '5':
            listar_livros()
        elif opcao == '6':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()
