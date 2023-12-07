from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome

#Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# opts = ChromeOptions()
# #esta opcao serve para nao fechar o navegador apos a execucao do script
# opts.add_experimental_option("detach", True)
# servico = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=servico, options=opts)
# opts = ChromeOptions()
# opts.add_experimental_option("detach", True)
# 
# 

# driver.get("https://www.infomoney.com.br/")

# dados1 = driver.find_element(By.ID, "high").text
# dados2 = driver.find_elements(By.ID, "high")[0].text

# print(dados1)
# print('-'*10)
# print(dados2)

driver = webdriver.Chrome()
driver.get("https://www.vivareal.com.br/venda/sp/santos/casa_residencial/3-quartos/#banheiros=2&onde=Brasil,S%C3%A3o%20Paulo,Santos,,,,,,BR%3ESao%20Paulo%3ENULL%3ESantos,,,&ordenar-por=preco:ASC&preco-ate=500000&quartos=3&vagas=1")
sleep(2)

# Encontrar todos os elementos 'article' com a classe específica
articles = driver.find_elements(By.CSS_SELECTOR, 'article.property-card__container.js-property-card')

# Inicializar uma lista para armazenar os links
links = []

# Iterar sobre os elementos 'article'
for article in articles:
    # Encontrar o primeiro link dentro de cada 'article'
    link_element = article.find_element(By.CSS_SELECTOR, 'a')
    link = link_element.get_attribute('href')
    
    # Adicionar o link à lista de links
    links.append(link)

# Imprimir o primeiro link encontrado
c = 0
for link in links:
    print(f'{link} {c}')
    c += 1