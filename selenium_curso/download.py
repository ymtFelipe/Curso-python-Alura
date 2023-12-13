from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\felip\Downloads",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=options)

driver.get("https://www.opera.com/pt-br/download")

spanBotao = driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div/span')
linkBotao = spanBotao.find_element(By.TAG_NAME, "a").click()
# link_download = linkBotao.get_attribute('href')

# driver.get(link_download)

sleep(10)

