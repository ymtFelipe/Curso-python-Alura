from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.common.exceptions import NoSuchElementException, TimeoutException

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 3)

#driver.get('https://www.vivareal.com.br/venda/sp/santos/casa_residencial/3-quartos/#banheiros=2&onde=Brasil,S%C3%A3o%20Paulo,Santos,,,,,,BR%3ESao%20Paulo%3ENULL%3ESantos,,,&ordenar-por=preco:ASC&preco-ate=500000&quartos=3&vagas=1')
driver.get('https://www.vivareal.com.br/venda/?itl_id=1000177&itl_name=vivareal_-_link-header_comprar_to_vivareal_resultado-pesquisa')

# variável para todos os links
links = []
n = 0

while n != 2:
     # Aceitar os cookies se o aviso estiver presente
    try:
        cookie_notification = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p.cookie-notifier__paragraph')))
        if cookie_notification.is_displayed():
            driver.find_element(By.CSS_SELECTOR, 'button.cookie-notifier__cta').click()
    except TimeoutException:
        pass  # Se não houver aviso de cookies, continue normalmente

    try:
        
        articles = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'article.property-card__container.js-property-card')))
        print('passei pelo try/articles get')
        
    except:
        print('Deu erro')
        break

    sleep(1)
    # procurando os links dentro do article
    for article in articles:
        # Encontrar o primeiro link dentro de cada 'article'
        link_element = article.find_element(By.CSS_SELECTOR, 'a')
        link = link_element.get_attribute('href')
        
        #Adicionar o link à lista de links

        if link in links:
            
            print('Um link repetido', link)
            continue

        if link not in links:
                
            links.append(link)
        else:
            print('Deu erro no if link')
            break

    sleep(5)

    elements = driver.find_elements(By.CSS_SELECTOR, 'ul.pagination__wrapper > li.pagination__item')
    ultimo_li = elements[-1]
    botao = ultimo_li.find_element(By.CSS_SELECTOR, 'button.js-change-page')
    botao.click()  
    n += 1  
   


driver.quit()