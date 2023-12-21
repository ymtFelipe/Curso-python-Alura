from model.sabor_express import Restaurante
from model.cardapio.bebida import Bebida
from model.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('suco de melancia', 5.00, 'grande')
prato_paozinho = Prato('paozinho', 2.00, 'O melhor pão da cidade')
# restaurante_mexicano = Restaurante('mexican food', 'Mexicana')
# restaurante_japones = Restaurante('Japa', 'Japonesa')
restaurante_praca.adicionar_bebida_no_cardapio(bebida_suco)
restaurante_praca.adicionar_prato_no_cardapio(prato_paozinho)

def main():
    print(bebida_suco)
    print(prato_paozinho)
    


if __name__ == '__main__':
    main()