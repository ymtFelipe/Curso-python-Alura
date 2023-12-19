from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
#pip3 install xlsxwriter
import xlsxwriter

df = pd.read_excel (r'C:\Users\gusta\Downloads\correios\fretes.xlsx')

precos = []
prazos = []

driver = webdriver.Chrome(executable_path=r"C:\Users\gusta\Documents\driver\chromedriver.exe")

driver.get("https://www2.correios.com.br/sistemas/precosprazos/")

for index, row in df.iterrows():

  driver.find_element_by_name("cepOrigem").send_keys(str(row['origem']))

  sleep(1)

  driver.find_element_by_name("cepDestino").send_keys(str(row['destino']))

  sleep(1)

  Select(driver.find_element_by_name("servico")).select_by_index(15)

  sleep(1)

  Select(driver.find_element_by_name("embalagem1")).select_by_index(2)

  driver.find_element_by_name("Altura").send_keys(int(row['altura']))

  driver.find_element_by_name("Largura").send_keys(int(row['largura']))

  driver.find_element_by_name("Comprimento").send_keys(int(row['comprimento']))

  driver.find_element_by_name("peso").send_keys(int(row['peso']))

  driver.find_element_by_name("ckValorDeclarado").click()

  sleep(1)

  driver.find_element_by_name("valorDeclarado").send_keys(str(row['valor']))

  sleep(1)

  driver.find_element_by_name("Calcular").click()

  driver.switch_to.window(driver.window_handles[1])

  tempoEntrega = driver.find_elements_by_class_name("destaque")[0].find_element_by_tag_name("td").text

  preco = driver.find_elements_by_class_name("destaque")[1].find_element_by_tag_name("td").text

  prazos.append(tempoEntrega)
  precos.append(preco)

  sleep(2)

  driver.close()
  driver.switch_to.window(driver.window_handles[0])
  driver.refresh()


data = {'origem': df.iloc[:,0], 'destino': df.iloc[:,1], 'altura': df.iloc[:,2], 'largura': df.iloc[:,3], 'comprimento': df.iloc[:,4], 'peso': df.iloc[:,5], 'valor': df.iloc[:,6], 'prazo': prazos, 'precos': precos} 
df2 = pd.DataFrame(data)

df2.to_excel('output.xlsx', engine='xlsxwriter')  	
print(df2)