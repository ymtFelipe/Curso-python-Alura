class ContaBancaria:
    def __init__(self, titular='', saldo=0) -> None:
        self.titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self) -> str:
        return f'Titular: {self.titular}, Saldo: {self._saldo}, {self._ativo}'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = 'Ativado' if not conta._ativo else 'Desativado'

    @property
    def criar_atributo(self, atributo):
        self.atributo = atributo

conta1 = ContaBancaria('Felipe', 2300)
conta2 = ContaBancaria('Jhon', 1500)
print(conta1)
print(conta2)

conta3 = ContaBancaria("Carlos", 200)
print(f"Antes de ativar: Conta ativa? {conta3._ativo}")
ContaBancaria.ativar_conta(conta3)
print(f"Depois de ativar: Conta ativa? {conta3._ativo}")


class ContaBancariaPythonica:
    def __init__(self, titular, saldo) -> None:
        self._titular = titular
        self._saldo = saldo
        self._ativo = True
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo
    
conta4 = ContaBancariaPythonica('Felipe', 2300)
print(conta4._titular)


class ClienteBanco:
    def __init__(self, titular='', idade=0, endereco='', cpf='', profissao=0, saldo=0) -> None:
        self._titular = titular
        self._idade = idade
        self._endereco = endereco
        self._cpf = cpf
        self._profissao = profissao
        self._saldo = saldo

    @property
    def saldo(self, valor):
        self._saldo += valor

cliente1 = ClienteBanco("Ana", 30, "Rua A", "123.456.789-01", "Backend")
cliente2 = ClienteBanco("Luiza", 25, "Rua B", "987.654.321-01", "Estudante")
cliente3 = ClienteBanco("Vinny Neves", 40, "Rua C", "111.222.333-44", "Frontend")
cliente1.saldo(1200)
print(cliente1._saldo)