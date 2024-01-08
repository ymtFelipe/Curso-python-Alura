
# # # class Conta:
# # #     def __init__(self, codigo) -> None:
# # #         self._codigo = codigo
# # #         self._saldo = 0
    
# # #     def depostia(self, valor):
# # #         self._saldo += valor

# # #     def __str__(self) -> str:
# # #         return f'Codigo: {self._codigo} - Saldo: {self._saldo:.2f}'
    
# # # class ContaCorrente(Conta):
# # #     def passa_o_mes(self):
# # #         self._saldo -= 2
    
# # # class ContaPoupança(Conta):
# # #     def passa_o_mes(self):
# # #         self._saldo *= 1.01
# # #         self._saldo -= 3

# # # conta16 = ContaCorrente(16)
# # # conta16.depostia(1000)
# # # conta16.passa_o_mes()
# # # print(conta16)


# # # conta17 = ContaPoupança(17)
# # # conta17.depostia(1000)
# # # conta17.passa_o_mes()
# # # print(conta17)

# # # idades = [1, 3, 53, 64, 23, 94, 43, 10]

# # # for index in enumerate(idades):
# # #     print(index)
# # from functools import total_ordering
# # @total_ordering
# # class ContaSalario:
    
# #     def __init__(self, codigo):
# #         self._codigo = codigo
# #         self._saldo = 0
    
# #     def deposita(self, valor):
# #         self._saldo += valor

# #     def __lt__(self, outro): #lessthan
# #         if self._saldo != outro._saldo:
# #             return self._saldo < outro._saldo
# #         return self._codigo < outro._codigo

        
# #     def __str__(self):
# #         return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)
  
# # conta_do_guilherme = ContaSalario(17)
# # conta_do_guilherme.deposita(500)

# # conta_da_daniela = ContaSalario(3)
# # conta_da_daniela.deposita(500)

# # conta_do_paulo = ContaSalario(133)
# # conta_do_paulo.deposita(500)

# # contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

# # print(conta_do_paulo >= conta_do_paulo)

# # # from operator import attrgetter
# # for conta in sorted(contas):
# #   print(conta)

# aparicoes = {  "Guilherme" : 1,
#   "cachorro" : 1,
#   "nome" : 2,
#   "vindo" : 1}

# print(aparicoes.get("Teste", -1))
# print(aparicoes.get("cachorro", -1))

# aparicoes['Carlos'] =  2
# print(aparicoes)
# del aparicoes['Carlos']
# print(aparicoes)


# for chave, valor in aparicoes.items():
#     print(chave, valor)

# meu_texto = "Bem vindo meu nome é Felipe eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
# meu_texto = meu_texto.lower()

# aparicoes = {}
# for palavra in meu_texto.split():
#     ate_agora = aparicoes.get(palavra, 0)
#     aparicoes[palavra] = ate_agora + 1

# print(aparicoes)



# aparicoes = defaultdict(int)

# for palavra in meu_texto.split():
#     aparicoes[palavra] += 1
# print(aparicoes)


from collections import defaultdict
class Conta:
    def __init__(self) -> None:
        print('Criando uma conta')

contas = defaultdict(Conta)
contas[15]
print(contas)