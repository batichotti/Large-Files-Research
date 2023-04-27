import pandas as pd

tabela1 = pd.read_csv('src\\csvs\\javascript_99_pProject.csv')

contagem = tabela1['project'].value_counts()

tabela2 = pd.DataFrame({
    'Project': contagem.index,
    'Count': contagem.values
})

tabela2.to_csv('src\\csvs\\javascript_count.csv', index=False)
