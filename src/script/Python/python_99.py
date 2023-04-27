import pandas as pd

tabela1 = pd.read_csv('Large_Files\\final_output.csv', low_memory=False)

tabela2 = tabela1[(tabela1['code'] > 1732) & (tabela1['language'] == 'Python')]

tabela2.to_csv('Large-Files-Research\src\csvs\\python_99_pProject.csv', index=False)
