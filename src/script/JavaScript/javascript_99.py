import pandas as pd

tabela1 = pd.read_csv('src\\csvs\\final_output.csv', low_memory=False)

tabela2 = tabela1[(tabela1['code'] > 1147) & (tabela1['language'] == 'JavaScript')]

tabela2.to_csv('src\\csvs\\javascript_99_pProject.csv', index=False)
