from biblioteca import Biblioteca
from livro import GeneroLivro
from usuario import Usuario


biblioteca = Biblioteca()

while True:
    print("\n========== Sistema de Biblioteca ==========")
    print("1. Adicionar Livro")
    print("2. Buscar Livro")
    print("3. Listar Livros Disponíveis")
    print("4. Adicionar Usuário")
    print("5. Listar Usuários")
    print("6. Emprestar Livro")
    print("7. Devolver Livro")
    print("8. Sair")
    print("============================================")
    
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite um número válido!")
        continue
    
    if opcao == 1:
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        isbn = input("Digite o ISBN do livro: ")
        genero = input("Digite o gênero do livro: ")
        livro = GeneroLivro(titulo, autor, isbn, genero)
        biblioteca.adicionarLivro(livro)
        print("Livro adicionado com sucesso!")
        
    elif opcao == 2:
        titulo = input("Digite o título do livro que deseja buscar: ")
        biblioteca.buscarLivro(titulo)
    
    elif opcao == 3:
        biblioteca.listarLivrosDisponiveis()
            
    elif opcao == 4:
        nome = input("Digite o nome do usuário: ")
        id = input("Digite o ID do usuário: ")
        usuario = Usuario(nome, id)
        biblioteca.adicionarUsuario(usuario)
        print("Usuário adicionado com sucesso!")
    
    elif opcao == 5:
        biblioteca.listarUsuarios()
        
    elif opcao == 6:
        id_usuario = input("Digite o ID do usuário: ")
        titulo_livro = input("Digite o título do livro a ser emprestado: ")
        usuario = next((u for u in biblioteca.usuarios if u.id == id_usuario), None)
        livro = next((l for l in biblioteca.livros if l.titulo == titulo_livro), None)
        if usuario and livro:
            biblioteca.emprestimo(usuario, livro)
            print("Empréstimo realizado com sucesso!")
        else:
            print("Usuário ou livro não encontrado.")
            
    elif opcao == 7:
        id_usuario = input("Digite o ID do usuário: ")
        titulo_livro = input("Digite o título do livro a ser devolvido: ")
        usuario = next((u for u in biblioteca.usuarios if u.id == id_usuario), None)
        livro = next((l for l in biblioteca.livros if l.titulo == titulo_livro), None)
        if usuario and livro:
            biblioteca.devolucao(usuario, livro)
            print("Devolução realizada com sucesso!")
        else:
            print("Usuário ou livro não encontrado.")
            
    elif opcao == 8:
        print("Saindo do sistema...")
        break
        
    else:
        print("Opção inválida. Tente novamente.")