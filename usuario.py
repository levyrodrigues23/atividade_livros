from livro import GeneroLivro

class Usuario:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        self.livros_emprestados = []
        
        
    def adicionarLivro(self, livro: GeneroLivro):
        if livro.disponivel:
            self.livros_emprestados.append(livro)
            livro.emprestar()
            
        
    
    def devolverLivro(self, livro: GeneroLivro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.devolver()
            



if __name__ == "__main__":
    usuario = Usuario("João", "001")
    print(usuario.nome)
    print(usuario.id)
    livro = GeneroLivro("O Código Da Vinci", "Dan Brown", "1122334455", "Mistério")
    livro2 = GeneroLivro("A Menina que Roubava Livros", "Markus Zusak", "5544332211", "Ficção Histórica")
    usuario.adicionarLivro(livro)
    print(usuario.livros_emprestados)
    usuario.adicionarLivro(livro2)
    print(usuario.livros_emprestados)
    usuario.devolverLivro(livro)
    print(usuario.livros_emprestados)
        
        
            
        
        
        