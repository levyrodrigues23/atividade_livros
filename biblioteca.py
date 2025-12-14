from livro import GeneroLivro
from usuario import Usuario



class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        
        
        
        
    def adicionarLivro(self, livro: GeneroLivro):
        if livro not in self.livros:
            self.livros.append(livro)
        else:
            print("livro ja existe na biblioteca")
            
    
    
    def adicionarUsuario(self, usuario: Usuario):
        if usuario not in self.usuarios:
            self.usuarios.append(usuario)
        else:
            print("usuario ja existe na biblioteca")
        
    
    def buscarLivro(self, titulo: str):
        for i in self.livros:
            if i.titulo == titulo:
                return print(f"Livro encontrado: {i.titulo} por {i.autor}")
    
    def listarLivrosDisponiveis(self):
        for i, x in enumerate(self.livros):
            if x.disponivel:
                print(f"Livro {i}: {x.titulo} por {x.autor}")
    def listarUsuarios(self):
        for i in self.usuarios:
            print(f"usuario:{i.nome}, ID: {i.id}")
            
    def emprestimo(self, usuario: Usuario, livro: GeneroLivro):
        if livro.disponivel:
            usuario.adicionarLivro(livro)
            
            
    def devolucao(self, usuario: Usuario, livro: GeneroLivro):
        if livro.disponivel == False:
            usuario.devolverLivro(livro)
            
    def __repr__(self):
        return f"({self.livros})"
           
    
    
if __name__ == "__main__":
    livro1 = GeneroLivro("1984", "George Orwell", "978-0451524935", "Distopia")
    livro2 = GeneroLivro("O Senhor dos Anéis", "J.R.R. Tolkien", "978-0544003415", "Fantasia")
    livro3 = GeneroLivro("Harry Potter", "J.K. Rowling", "978-8532530783", "Fantasia")
    livro4 = GeneroLivro("Dom Casmurro", "Machado de Assis", "978-8535910663", "Romance")
    livro5 = GeneroLivro("O Pequeno Príncipe", "Saint-Exupéry", "978-8522031450", "Fábula")
    biblioteca = Biblioteca()
    biblioteca.adicionarLivro(livro1)
    biblioteca.adicionarLivro(livro2)
    biblioteca.adicionarLivro(livro3)
    biblioteca.adicionarLivro(livro4)
    biblioteca.adicionarLivro(livro5)
    biblioteca.listarLivrosDisponiveis()
    
    

            
        
        
    