import pandas as pd

tabela1 = pd.read_csv('Large_Files\\python_99_pProject.csv')

contagem = tabela1['project'].value_counts()

tabela2 = pd.DataFrame({
    'Project': contagem.index,
    'Count': contagem.values
})

tabela2.to_csv('Large-Files-Research\src\csvs\\python_count.csv')
