import pandas as pd

tabela = pd.read_csv("advertising.csv")
print(tabela)

import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(tabela.corr(), annot=True, cmap="Wistia")
plt.show()
