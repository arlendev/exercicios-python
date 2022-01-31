from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui
import time

# #para rodar o chrome em 2º plano
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.headless = True 
# navegador = webdriver.Chrome(options=chrome_options)

# abrir um navegador
navegador = webdriver.Chrome()

navegador.get("https://www.google.com/")
pyautogui.click(x=804, y=923, clicks=1)

# Passo 1: Pegar a cotação do Dólar
navegador.get("https://www.melhorcambio.com/dolar-hoje")

cotacao_dolar = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute("value")
cotacao_dolar = cotacao_dolar.replace(",", ".") # troca virgula por ponto
print(cotacao_dolar)

# Passo 2: Pegar a cotação do Euro
navegador.get("https://www.melhorcambio.com/euro-hoje")

cotacao_euro = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute("value")
cotacao_euro = cotacao_euro.replace(",", ".") # troca virgula por ponto
print(cotacao_euro)

# Passo 3: Pegar a cotação do Ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")

cotacao_ouro = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute("value")
cotacao_ouro = cotacao_ouro.replace(",", ".") # troca virgula por ponto
print(cotacao_ouro)

navegador.quit()

# Passo 4: Importar a lista de produtos
import pandas as pd

tabela = pd.read_excel("Produtos.xlsx")
print(tabela)

# Passo 5: Recalcular o preço de cada produto
# atualizar a cotação
# nas linhas onde na coluna "Moeda" = Dólar
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)

# atualizar o preço base reais (preço base original * cotação)
tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]

# atualizar o preço final (preço base reais * Margem)
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

# tabela["Preço de Venda"] = tabela["Preço de Venda"].map("R${:.2f}".format)
print('-=' *45)
print('Impressão da tabela com os dados atualizados dentro do python - não atualizado na base')
print(tabela)

# Passo 6: Salvar os novos preços dos produtos
tabela.to_excel("Produtos Novo.xlsx", index=False)

# etapa 1: criar o gráfico
 