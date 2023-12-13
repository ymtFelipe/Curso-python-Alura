from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://www.imdb.com/")
wait = WebDriverWait(driver, 10)

q = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#suggestion-search')))
q[0].send_keys("Titanic" + Keys.RETURN)

driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[1])
driver.close()
sleep(10)