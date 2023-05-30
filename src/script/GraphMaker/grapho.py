import pandas as pd
import matplotlib.pyplot as plt

# carregar dados do arquivo CSV para um DataFrame
tabela2 = pd.read_csv('src\\csvs\\javascript_count.csv')

# filtrar dados com Count acima de 10
tabela2 = tabela2[tabela2['Count'] > 15]

# criar um gráfico de barras com a contagem de cada projeto
plt.bar(tabela2['Project'], tabela2['Count'])
plt.xlabel('Project')
plt.xticks(rotation=75)
plt.tight_layout()
plt.ylabel('Large Files')
plt.title('TOP Projects with JavaScript Large Files')
plt.show()
