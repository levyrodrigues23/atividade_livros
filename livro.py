class Livro:
    def __init__(self, titulo, autor, isbn):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._disponivel = True
    
    @property    
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, valor):
        self._titulo = valor
        
    @property    
    def autor(self):
        return self._autor
    
    @autor.setter
    def autor(self, valor):
        self._autor = valor
        
    @property    
    def isbn(self):
        return self._isbn
    
    @isbn.setter
    def isbn(self, valor):
        self._isbn = valor
        
    @property    
    def disponivel(self):
        return self._disponivel
    
    @disponivel.setter
    def disponivel(self, valor):
        self._disponivel = valor
        
    
    def emprestar(self):
        print(f"O livro {self.titulo} foi emprestado.")
        self.disponivel = False
         
    def devolver(self):
        print(f"O livro {self.titulo} de {self.autor} foi devolvido.")
        self.disponivel = True
        
    def __repr__(self):
        return f"Livro('{self.titulo}', '{self.autor}', '{self.isbn}')"
    
    
class GeneroLivro(Livro):
    def __init__(self, titulo, autor, isbn, genero):
        super().__init__(titulo, autor, isbn)
        self.genero = genero

    def __repr__(self):
        return f"Livro('{self.titulo}', '{self.autor}', '{self.isbn}', '{self.genero}')"
    
    def __str__(self):
        return f"{self.titulo} por {self.autor} - Gênero: {self.genero}"

if __name__ == "__main__":  
    livro = Livro("1984", "George Orwell", "1234567890")
    print(livro.titulo)
    print(livro.autor)
    print(livro.isbn)
    livro.emprestar()
    livro.devolver()
            
    livro2 = GeneroLivro("O Senhor dos Anéis", "J.R.R. Tolkien", "0987654321", "Fantasia")
    print(livro2.titulo) # funciona porque eu tenho herança da classe Livro
    print(livro2.genero)

    # a verificação de instancia abaixo funciona porque livro2 é uma instancia de genero livro que herda de livro
    if isinstance(livro2, Livro):
        print(f"{livro2.titulo} é uma instância de Livro")

    # nesse caso aqui, livro é uma instancia de livro, mas não de generolivro, por isso ele roda o else.
    if isinstance(livro, GeneroLivro):
        print(f"{livro.titulo} é uma instância de GeneroLivro")
    else:
        print(f"{livro.titulo} não é uma instância de GeneroLivro")





