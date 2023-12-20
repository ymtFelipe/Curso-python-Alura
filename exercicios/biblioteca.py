from exercicio4 import Livro

livro1 = Livro('Harry Potter e a Pedra Filosofal', ' J. K. Rowling', 1997)
livro2 = Livro('Harry Potter e a Criança Amaldiçoada', ' J. K. Rowling, Jack Thorne e John Tiffany', 2016)
livro3 = Livro('Harry Potter e as Relíquias da Morte', ' J. K. Rowling', 2007)

print(livro1.emprestar())
# livro3.emprestar()
Livro.verificar_disponibilidade(2007)