class Restaurante:
    resturantes = []
    def __init__(self, nome, categoria):
        self._nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.resturantes.append(self)
    
    
    def __str__(self):
        return f'{self._nome} | {self.categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}')
        for restaurante in cls.resturantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'Ativado' if self._ativo else 'Desativado'

    def altenar_estado(self):
        self._ativo = not self._ativo


    

    
restaurante1 = Restaurante('pushi', 'japonesa')
restaurante2 = Restaurante('pizza Express', 'Italiana')
restaurante2.altenar_estado()

Restaurante.listar_restaurantes()
