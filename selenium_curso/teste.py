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

driver.get('https://www.vivareal.com.br/venda/sp/santos/casa_residencial/3-quartos/#banheiros=2&onde=Brasil,S%C3%A3o%20Paulo,Santos,,,,,,BR%3ESao%20Paulo%3ENULL%3ESantos,,,&ordenar-por=preco:ASC&preco-ate=500000&quartos=3&vagas=1')
while True:
     # Aceitar os cookies se o aviso estiver presente
    try:
        cookie_notification = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p.cookie-notifier__paragraph')))
        if cookie_notification.is_displayed():
            driver.find_element(By.CSS_SELECTOR, 'button.cookie-notifier__cta').click()
    except TimeoutException:
        pass  # Se não houver aviso de cookies, continue normalmente




    button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/section/div[2]/div[2]/div/ul/li[9]/button')))
    button.click()
    sleep(1)