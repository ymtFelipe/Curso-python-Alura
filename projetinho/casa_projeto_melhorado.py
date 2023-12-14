from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import openpyxl

chrom_options = Options()

#chrome_options.add_argument("--headless")  # Habilitando o modo headless modo invisível

# Para não fechar o chrome
chrom_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrom_options)

# wait para esperar o elemento aparecer na tela
wait = WebDriverWait(driver, 10)

# link da página
link = "https://www.vivareal.com.br/venda/sp/santos/casa_residencial/3-quartos/#banheiros=2&onde=,S%C3%A3o%20Paulo,Santos,,,,,city,BR%3ESao%20Paulo%3ENULL%3ESantos,,,&preco-ate=500000&quartos=3&vagas=1"

# abrindo o link
driver.get(link)

# váriavel para pegar todos os links
links = []

existe_pagina = True
primeira_pagina = True

while True:
    primeiro_valor_total_imoveis = driver.find_element(By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/section/header/div/div/div[1]/div/h1/strong').text
    sleep(5)
    segundo_valor_total_imoveis = driver.find_element(By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/section/header/div/div/div[1]/div/h1/strong').text 
    if primeiro_valor_total_imoveis == segundo_valor_total_imoveis:
        print('Site com lentidão.')
        driver.refresh()
        sleep(1)
    else:
        break
driver.fullscreen_window()





while existe_pagina:
    
    if primeira_pagina:
        primeira_pagina = False
    else:
        # Try para passar a pagina. ex: 1, 2, 3...
        try:
            # usa o scroll até o botão de pular a página, pois estava com problema em acessar a proxima página.
            # Encontre o elemento desejado pelo ID, classe, XPath, etc.
            elemento_desejado = driver.find_element(By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/section/div[2]/div[2]/div')  # Substitua pelo ID do elemento desejado

            # Role até o elemento desejado
            driver.execute_script("arguments[0].scrollIntoView();", elemento_desejado)

            # Obtém as dimensões da janela do navegador
            window_height = driver.execute_script("return window.innerHeight;")
            window_width = driver.execute_script("return window.innerWidth;")

            # Obtém as coordenadas do elemento
            element_location_y = elemento_desejado.location['y']
            element_location_x = elemento_desejado.location['x']

            # Calcula as coordenadas para centralizar o elemento na tela
            scroll_y = element_location_y - (window_height / 2)
            scroll_x = element_location_x - (window_width / 2)

            # Executa um novo script para rolar a página para centralizar o elemento na tela
            driver.execute_script(f"window.scrollTo({scroll_x}, {scroll_y});")
            # botão de próxima pagina.
            sleep(1)
            driver.find_elements(By.CLASS_NAME,'pagination__item')[-1].click()
              
        except:
            # caso não tenha mais o botão "próxima pagina" ativo, ele faz sair do loop while.
            existe_pagina = False
            print('Não existem mais páginas.')

    # pegando os articles da página para conseguir os links.
    sleep(1)
    articles = driver.find_element(By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/section/div[2]/div[1]').find_elements(By.CSS_SELECTOR, 'article.property-card__container.js-property-card')

    # for para pegar os links.
    for article in articles:
        # Encontrar o primeiro link dentro de cada 'article'
        link_element = article.find_element(By.CSS_SELECTOR, 'a')
        link_atual = link_element.get_attribute('href')
        print(link_atual)
        # caso não tenha um repetido.
        if link_atual not in links:
            links.append(link_element.get_attribute('href'))
          
    articles = ''
    sleep(1)
print(len(links))
# casas = []
# # abrindo o openpyxl
# book = openpyxl.Workbook()

# # colocando na aba 'Sheet'
# casas = book['Sheet']

# # primeira linha da planilha
# casas.append(['Valor', 'Endereço', 'Area', 'Quartos', 'Banheiros', 'Garagem', 'Link'])

# for link in links:
#     driver.get(link)

#     # pegando o tamanho da area.
#     area_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/div[4]/ul/li[1]')))
#     area_txt = area_element.text

#     # pegando quantos quartos.
#     bedroom_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/div[4]/ul/li[2]')))
#     bedroom_txt = bedroom_element.text

#     # pegando quantos banheiros.
#     bathroom_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/div[4]/ul/li[3]')))
#     bathroom_txt = bathroom_element.text

#     # pegando quantas vagas de carros.
#     vacancies_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/div[4]/ul/li[4]')))
#     vacancies_txt = vacancies_element.text

#     # pegando o valor.
#     price_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="js-site-main"]/div[2]/div[2]/div[1]/div/div[1]/div/h3')))
#     price_txt = price_element.text

#     # pegando o local do imóvel.
#     local_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/div[1]/section/div/div/p')))
#     local_text = local_element.text
#     casas.append([price_txt, local_text, area_txt, bedroom_txt, bathroom_txt, vacancies_txt, link])
#     sleep(1.3)

# book.save('casas.xlsx')