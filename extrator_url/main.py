url = "https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
# url = ""

# sanitização URL
url = url.strip()


# validação URL
if url == "":
    raise ValueError("A URL está vazia")


# separa base e os parametros 
indice_interrogacao = url.find("?")
url_base = url[:indice_interrogacao]
print(url_base)
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# busca o valor de um parametro
parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find("&", indice_valor)

# verificação
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
    print(valor)
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
    print(valor)