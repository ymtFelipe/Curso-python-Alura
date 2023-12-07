import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException



chrome_options = Options()
#chrome_options.add_argument("--headless")  # Habilitando o modo headless modo invisível
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)


# abrindo a pagina. obs: irei trocar para que a pessoa escolha qual a opção.
driver.get("https://www.vivareal.com.br/venda/sp/santos/casa_residencial/3-quartos/#banheiros=2&onde=Brasil,S%C3%A3o%20Paulo,Santos,,,,,,BR%3ESao%20Paulo%3ENULL%3ESantos,,,&ordenar-por=preco:ASC&preco-ate=500000&quartos=3&vagas=1")




# while True:
#     # fazendo isso para que o site carregue com o número correto de total de casas encontradas. obs: o site as vezes pode demorar para carregar.
#     # as vezes o site carrega com ex: 4.500 total de casas e após 3seg ele carrega novamente com um total de 40 casas.


#     # criando uma variável para pegar o primeiro total de casas
#     total_casas = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/section/header/div/div/div[1]/div/h1/strong')))
#     total_casas_text = total_casas.text
#     time.sleep(5)


#     # criando uma variável para pegar o numero de total de casas após 3seg
#     total_casas_atualizado = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/section/header/div/div/div[1]/div/h1/strong')))
#     total_casas_atualizado_text = total_casas_atualizado.text


#     # fazendo uma verificação para saber se o valor total de casas está correto.
#     if total_casas_atualizado_text != total_casas_text: # se for diferente quer dizer que o site está funcionando normalmente.
#         break
#     else: # se não, irei recarregar.
#         print('Site com lentidão, irei recarregar.')
#         driver.refresh()
    

# lista para todos os links
links = []

articles = []

# para pegar os articles

time.sleep(3)
# loop para passar de pagina

while True:
      # Aceitar os cookies se o aviso estiver presente
    try:
        cookie_notification = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p.cookie-notifier__paragraph')))
        if cookie_notification.is_displayed():
            driver.find_element(By.CSS_SELECTOR, 'button.cookie-notifier__cta').click()
    except TimeoutException:
        pass  # Se não houver aviso de cookies, continue normalmente

    # Clicar no botão de próxima página
    driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/section/div[2]/div[2]/div/ul/li[4]/button'))

    articles = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'article.property-card__container.js-property-card')))
    driver.find_element(By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/section/div[2]/div[2]/div/ul/li[4]/button').click()
    time.sleep(2)
    break












# procurando os links dentro do article
for article in articles:
    # Encontrar o primeiro link dentro de cada 'article'
    link_element = article.find_element(By.CSS_SELECTOR, 'a')
    link = link_element.get_attribute('href')
    # Adicionar o link à lista de links
    links.append(link)


# abrindo o openpyxl
book = openpyxl.Workbook()

# creando uma aba nova
book.create_sheet('Casas')

# colocando na aba 'Sheet'
casas = book['Sheet']
# primeira linha da planilha
casas.append(['Valor', 'Endereço', 'Area', 'Quartos', 'Banheiros', 'Garagem', 'Link'])

print(len(links))
if links:
    for link in links:
        # abrindo o link
        driver.get(link)

        time.sleep(1.3)# sleep para que o site não trave com repetição de refresh
        # pegando o valor da casa/apartamento
        valor = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="js-site-main"]/div[2]/div[2]/div[1]/div/div[1]/div/h3')))

        # pegando o endereço
        endereco = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/div[1]/section/div/div/p')))

        # pegando a area da casa/apartamento
        area = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/div[4]/ul/li[1]')))

        # total de quartos
        quartos = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/div[4]/ul/li[2]')))

        # total de banheiros/suits
        banheiros = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/div[4]/ul/li[3]')))

        # total de garagem
        garagem = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/div[4]/ul/li[4]')))

        # colocando valor, endereço, area, quartos, banheiros e garagem dentro de uma planilha.
        casas.append([valor.text, endereco.text, area.text, quartos.text, banheiros.text, garagem.text, link])
        print(valor.text, endereco.text, area.text, quartos.text, banheiros.text, garagem.text, link)

else:
    print("Não foi possível encontrar divs")

# salvando a planilha
book.save('teste.xlsx')

# fechando o driver
driver.quit()
