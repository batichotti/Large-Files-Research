import os
import pandas as pd


folder_path = 'src\\csvs\\TopLanguages'
dfs = []

for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)
        nome = df['language'][0]
        minimo = df['code'].min()
        maximo = df['code'].max()
        mediana = df['code'].median()
        media = df['code'].mean()
        quartis = df['code'].quantile([0.9, 0.95, 0.99])
        quant_acima_99 = len(df[df['code'] > quartis.loc[0.99]].dropna())
        quant_total = len(df['code'])
        summary = pd.DataFrame({
            'Linguagem': [nome],
            'min': [minimo],
            'max': [maximo],
            'mediana': [mediana],
            'avg': [media],
            'quartile_90': [quartis.loc[0.9]],
            'quartile_95': [quartis.loc[0.95]],
            'quartile_99': [quartis.loc[0.99]],
            'archives_quartile_99': [quant_acima_99],
            'total_archives': [quant_total]
        })
        dfs.append(summary)

summary_df = pd.concat(dfs, ignore_index=True)

summary_df.to_csv('src\\csvs\\summaryTOP.csv', index=False)
