class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    # tira os espaços da url
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""
    
    # verifica se a url está vazia
    def valida_url(self):
        if self.url == "":
            raise ValueError("A URL está vazia")
    
    # separa a url base
    def get_url_base(self):
        indice_interrogacao = self.url.find("?")
        url_base = self.url[:indice_interrogacao]
        return url_base
    
    # separa o paremetro
    def get_url_parametros(self):
        indice_interrogacao = self.url.find("?")
        url_parametro = self.url[indice_interrogacao + 1:]
        return url_parametro
    
    # busca o valor de um parametro
    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_comercial = self.get_url_parametros().find("&", indice_valor)
        if indice_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_comercial]
        return valor 
    

#extrator_url = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
extrator_url = ExtratorURL(None)
# extrator_url = ExtratorURL("  ")
valor_quantidade = extrator_url.get_valor_parametro("moedaOrigem")
print(valor_quantidade)