import pandas as pd
import matplotlib.pyplot as plt

# carregar dados do arquivo CSV para um DataFrame
tabela2 = pd.read_csv('src\\csvs\\summaryTOP20.csv')

# criar um gráfico de barras com a contagem de cada projeto
plt.bar(tabela2['Linguagem'], tabela2['quartile_99'])
plt.xlabel('Language')
plt.xticks(rotation=75)
plt.tight_layout()
plt.ylabel('Quantile 99')
plt.title('Quantile 99 x Language')
plt.show()
