from model.avaliacao import Avaliacao
from model.cardapio.itemCardapio import ItemCardapio
class Restaurante:
    resturantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.resturantes.append(self)
    
    
    def __str__(self):
        return f'{self._nome} | {self.categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')
        for restaurante in cls.resturantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo.ljust(25)}')

    @property
    def ativo(self):
        return 'Ativado' if self._ativo else 'Desativado'

    def altenar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        else:
            return print('Somente nota de 0 à 5.')

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        else:
            soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
            quantidade_de_notas = len(self._avaliacao)
            media = round(soma_das_notas / quantidade_de_notas, 1)
            return media
    
    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    # código omitido

    @property
    def exibir_cardapio(self):
            print(f'Cardapio do restaurante {self._nome}:\n')
            for i,item in enumerate(self._cardapio,start=1):
                    if hasattr(item,'descricao'):
                            mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                            print(mensagem_prato)
                    else:
                            mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                            print(mensagem_bebida)

# código omitido
