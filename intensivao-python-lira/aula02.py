# Passo 1: Importar a base de dados
import pandas as pd

tabela = pd.read_csv("telecom_users.csv")

# Passo 2: Visualizar a base de dados
tabela = tabela.drop("Unnamed: 0", axis=1)
display(tabela)
# - Entender quais as informações tão disponíveis
# - Descobrir as cagadas da base de dados