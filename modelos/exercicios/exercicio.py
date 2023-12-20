"""Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. 
Crie uma instância dessa classe e atribua valores aos seus atributos."""

"""Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. 
Instancie um restaurante e atribua valores aos seus atributos."""

"""Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como
parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor."""

"""Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, 
seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante."""

"""Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos 
desta classe e atribua valores aos seus atributos através de um método construtor."""

class Carro:
    def __init__(self, modelo, cor, ano) -> None:
        self.moledo = modelo
        self.cor = cor
        self.ano = ano

meu_carro = Carro(modelo='Fusca', cor='Azul', ano=1970)


class Restaurante:
    def __init__(self, nome, categoria, ativo=False, email=None, telefone=None, avaliacao=None):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.email = email
        self.telefone = telefone
        self.avaliacao = avaliacao

    def __str__(self) -> str:
        return f'{self.nome} | {self.categoria}'

restaurante_formatado = Restaurante(nome='Bom Sabor', categoria='Tradicional')
print(restaurante_formatado)
print()
class Cliente:
    def __init__(self, nome, email, senha, telefone) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone
        
    def __str__(self) -> str:
        return f'Nome: {self.nome} | Email: {self.email} | Telefone: {self.telefone}'


cliente1 = Cliente('Felipe', 'Felipe.A@gmail.com', '1234@#%maf', '4002-8922')
cliente2 = Cliente('Roberto', 'RobertoAugusto@gmail.com', 'adad123356#$f', '4002-8922')
cliente3 = Cliente('Jhon', 'JhonatanBR@gmail.com', '21312fff', '4002-8922')
print(cliente1)
print(cliente2)
print(cliente3)