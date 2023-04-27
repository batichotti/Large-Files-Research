import pandas as pd
import matplotlib.pyplot as plt
import glob

lista_caminhos = glob.glob('src\\csvs\\Languages\\*.csv')

lista_dataframes = [pd.read_csv(caminho) for caminho in lista_caminhos]

dados = pd.concat(lista_dataframes)

grupos = dados.groupby('language')

grupos.boxplot(column='code')

plt.show()
