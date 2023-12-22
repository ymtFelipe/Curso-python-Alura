from model.cardapio.itemCardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao) -> None:
        super().__init__(nome, preco)
        self.descricao = descricao

    def __str__(self) -> str:
        return f'{self._nome}'
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)