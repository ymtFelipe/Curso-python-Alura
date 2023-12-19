from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\gusta\Documents\driver\chromedriver.exe")

driver.get("https://br.gearbest.com/celulares-c_11293/")

driver.implicitly_wait(3) # seconds

listaLinks = []

existePagina = True
primeiraPagina = True

while (existePagina):

    if(primeiraPagina):
        primeiraPagina = False
    else:
        try:
            driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/div/footer/div[2]/div/a[5]/i").click()
            driver.implicitly_wait(3) # seconds
        except:
            print("Acabaram as páginas")
            existePagina = False
            driver.close()

    for produtoAtual in driver.find_elements_by_class_name("gbGoodsItem_outBox"):
        link = produtoAtual.find_element_by_tag_name("a")
        listaLinks.append(link.get_attribute("href"))

    for linkAtual in listaLinks:
        driver.get(linkAtual)
        driver.implicitly_wait(3) # seconds
        nomeProduto = driver.find_element_by_class_name("goodsIntro_title").text
        preco = driver.find_element_by_id("js-panelIntroNormalPrice").find_element_by_tag_name("span").text
        try:
            avaliacao = driver.find_element_by_class_name("gbStarGrade_count").text
        except:
            avaliacao = "Sem avaliação"

        print(nomeProduto)
        print(preco)
        print(avaliacao)