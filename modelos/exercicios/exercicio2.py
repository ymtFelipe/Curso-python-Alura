class Livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade


# Agora é sua vez! Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__para imprimir 
# uma representação em string da pessoa. Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano.
# Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.
        
class Pessoa:
    def __init__(self, nome='', idade=0, profissao='') -> None:
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def __str__(self) -> str:
        return f'{self.nome}, {self.idade} anos, {self.profissao}'
    
    
    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}'
        else:
            return f'Olá, sou {self.nome}!'
        
# Criando 3 instâncias da classe Pessoa
pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22)

# Imprimindo informações iniciais
print("Informações Iniciais:")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

# Utilizando o método de instância aniversario para aumentar a idade de uma pessoa
pessoa1.aniversario()
pessoa3.aniversario()

# Imprimindo informações após aniversário
print("Informações após aniversário:")
print(pessoa1)
print(pessoa3)
print()

# Utilizando o método de classe saudacao para exibir mensagens personalizadas
print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)
