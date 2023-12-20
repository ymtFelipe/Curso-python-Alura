# class Banco:
#     def __init__(self, nome, endereco) -> None:
#         self._nome = nome
#         self._endereco = endereco

# class Agencia(Banco):
#     def __init__(self, nome, endereco, numero) -> None:
#         super().__init__(nome, endereco)
#         self._numero = numero

class Veiculo:
    def __init__(self, marca, modelo) -> None:
        self.marca = marca.title()
        self.modelo = modelo
        self._ligado = False

    def __str__(self) -> str:
        return f'{self.marca} | {self.modelo} | {self.verificando_estado_carro}'
    
    @property
    def verificando_estado_carro(self):
        return f"{'Ligado' if self._ligado else 'Desligado'}"


class Carro(Veiculo):
    def __init__(self, marca, modelo, portas) -> None:
        super().__init__(marca, modelo)
        self.portas = portas

    def __str__(self) -> str:
        return super().__str__() + f' | {self.portas}'



class Moto(Veiculo):
    def __init__(self, marca, modelo, esportiva_ou_casual) -> None:
        super().__init__(marca, modelo)
        self.esportiva_ou_casual = esportiva_ou_casual

    def __str__(self) -> str:
        return super().__str__() + f' | {self.esportiva_ou_casual}'
    

