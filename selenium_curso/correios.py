from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome(executable_path=r"C:\Users\gusta\Documents\driver\chromedriver.exe")

driver.get("https://www2.correios.com.br/sistemas/precosprazos/")

driver.find_element_by_name("cepOrigem").send_keys("31630900")

sleep(1)

driver.find_element_by_name("cepDestino").send_keys("35400000")

sleep(1)

#pac
Select(driver.find_element_by_name("servico")).select_by_value()

sleep(1)

Select(driver.find_element_by_name("embalagem1")).select_by_index(2)

driver.find_element_by_name("Altura").send_keys("10")

driver.find_element_by_name("Largura").send_keys("10")

driver.find_element_by_name("Comprimento").send_keys("15")

driver.find_element_by_name("peso").send_keys("3")

driver.find_element_by_name("ckValorDeclarado").click()

sleep(1)

driver.find_element_by_name("valorDeclarado").send_keys("300000")

sleep(1)

driver.find_element_by_name("Calcular").click()

driver.switch_to.window(driver.window_handles[1])

tempoEntrega = driver.find_elements_by_class_name("destaque")[0].find_element_by_tag_name("td").text

print(tempoEntrega)

preco = driver.find_elements_by_class_name("destaque")[1].find_element_by_tag_name("td").text

print(preco)