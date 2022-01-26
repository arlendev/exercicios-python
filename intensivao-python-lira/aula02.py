# Passo 1: Importar a base de dados
import pandas as pd

tabela = pd.read_csv('telecom_users.csv')
print(tabela)

tabela = tabela.drop('Unnamed: 0', axis = 1)
print(tabela)
# Passo 2: Visualizar a base de dados
# - Entender quais as informações tão disponíveis
# - Descobrir as cagadas da base de dados