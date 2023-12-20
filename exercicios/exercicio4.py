class Livro:
    livros = []
    def __init__(self, titulo, autor, ano_publicacao) -> None:
        self.titulo = titulo.title()
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)

    def __str__(self) -> str:
        return f'{self.titulo} | {self.autor} | {self.ano_publicacao}'
    
    def emprestar(self):
        self.disponivel = False
        return f'O livro {self.titulo} está {"disponível" if  self.disponivel else "indisponível"}.'
    
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = []
        for livro in Livro.livros:
            if livro.ano_publicacao == ano and livro.disponivel:
                print(livro)
        
                



