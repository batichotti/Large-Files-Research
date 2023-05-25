import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.read_csv('Large-Files-Research\src\script\GraphMaker\\summary_webscraping_python_selenium.csv')

files = dataframe['Number of Files'] #commits

dates = []
for i in dataframe['Author Commit Date']:
    dates.append(str(i[:10]))

# Plotar o gráfico de linha
plt.bar(dates, files)

# Adicionar rótulos e título
plt.xlabel('Date')
plt.ylabel('Commits')
plt.title('Commits x Date')

# Configurar os rótulos do eixo x em diagonal
plt.xticks()

# Mostrar o gráfico
plt.show()