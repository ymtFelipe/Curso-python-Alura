from selenium import webdriver

driver = webdriver.Chrome()

#exemplo 1

# driver.get("https://www.e-crvsp.sp.gov.br")

# driver.implicitly_wait(3) # seconds

# framePagina = driver.find_elements_by_tag_name("frame")[1]

# driver.switch_to.frame(framePagina)

# driver.find_element_by_name("codigo").send_keys("informe um cpf válido")
# driver.find_element_by_name("senha").send_keys("123")

#exemplo 2

driver.get("https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/empresas-listadas.htm")

driver.implicitly_wait(3) # seconds

driver.switch_to.frame("bvmf_iframe")

botao = driver.find_element_by_css_selector("#accordionName > div > app-companies-home-filter-name > form > div > div:nth-child(4) > button")
botao.click()

dados = driver.find_elements_by_class_name("card-body")
sigla = dados[0].find_element_by_tag_name("h5").text
nome = dados[0].find_element_by_class_name("card-title").text
descricao = dados[0].find_element_by_class_name("card-text").text
print(sigla)
print(nome)
print(descricao)
