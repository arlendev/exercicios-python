import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

# Passo 1: Entrar no sistema (no nosso caso, entrar no link)
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

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

# Passo 4: Calcular o faturamento e quantidade de produtos vendidos (os indicadores)
import pandas as pd

tabela = pd.read_excel
tabela = pd.read_excel(r'C:\Users\......') # caminho do xlsx
print(tabela)
faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()

print(f'O faturamento totao foi R${faturamento:,.2f}')
print(f'A quantidade de produtos vendidos foi {quantidade}')

# Passo 5: Entrar no email
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://mail.google.com/mail/u/0/#inbox')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(5)

# Passo 6: Enviar por e-mail o resultado
pyautogui.click(x=109, y=183)

pyautogui.write('xyz@gmail.com') # colocar o e-mail de destino
pyautogui.press('tab') # seleciona o email
# escreve outro email
# tab
# escreve outro email
# tab
pyautogui.press('tab') # pula pro campo de assunto
pyperclip.copy('Relatório de Vendas')
pyautogui.hotkey('ctrl', 'v') # escrever o assunto
pyautogui.press('tab') #pular pro corpo do email

texto = f'''
Prezados, bom dia

O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos foi de: {quantidade:,}

Abs
Arlen Possamai'''

pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')

# clicar no botão enviar

# apertar Ctrl Enter
pyautogui.hotkey('ctrl', 'enter')