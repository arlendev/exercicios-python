from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# para rodar o chrome em 2º plano
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.headless = True 
# navegador = webdriver.Chrome(options=chrome_options)

# abrir um navegador
navegador = webdriver.Chrome("chromedriver.exe")

navegador.get("https://www.google.com/")

# Passo 1: Pegar a cotação do Dólar
navegador.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")

navegador.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element(By.XPATH,
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value") 
print(cotacao_dolar)

# Passo 2: Visualizar a base de dados

# Passo 3: Tratamento de dados

# Passo 5: Análise Mais completa

# etapa 1: criar o gráfico
