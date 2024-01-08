idades = [39,19,27]

idades.insert(0, 20)
print(idades)
idades.extend([30, 19])
print(idades)
idades_no_ano_que_vem = [idade + 1 for idade in idades]
print(idades_no_ano_que_vem)
idades_no_ano_que_vem = [idade for idade in idades if idade >= 20]
print(idades_no_ano_que_vem)

