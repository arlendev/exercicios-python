import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

tabela = pd.read_csv("advertising.csv")
print(tabela)

mask = np.triu(np.ones_like(tabela.corr())) 
dataplot = sb.heatmap(tabela.corr(), cmap="Wistia", annot=True, mask=mask) 
plt.show() 

from sklearn.model_selection import train_test_split

y = tabela["Vendas"]
x = tabela.drop("Vendas", axis=1)

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1)