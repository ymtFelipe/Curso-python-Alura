from model.sabor_express import Restaurante
from model.cardapio.bebida import Bebida
from model.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('suco de melancia', 5.00, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('paozinho', 2.00, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()
# restaurante_mexicano = Restaurante('mexican food', 'Mexicana')
# restaurante_japones = Restaurante('Japa', 'Japonesa')
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
    restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()