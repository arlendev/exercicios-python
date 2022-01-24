import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

# Passo 1: Entrar no sistema (no nosso caso, entrar no link)
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(5)

# Passo 2: Navegar até o local do relatório (entrar na pasta Exportar)
pyautogui.click(x=374, y=303, clicks=2)
time.sleep(2)
pyautogui.click(x=384, y=311, clicks=2)
time.sleep(2)

# Passo 3: Fazer o download do relatório
pyautogui.click(x=96, y=148, clicks=1)
time.sleep(2)
pyautogui.click(x=163, y=425, clicks=1)
time.sleep(2)
pyautogui.click(x=460, y=430, clicks=1)

time.sleep(5) # Esperar o download

# Passo 4: Calcular os indicadores
import pandas as pd

tabela = pd.read_excel(r"C://Users/alonp/Downloads/Vendas - Dez.xlsx")
display(tabela)
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()
