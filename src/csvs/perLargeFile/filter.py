import pandas as pd

input_csv_file = 'src\\csvs\\PerLargeFile\\admin.csv'
df = pd.read_csv(input_csv_file)

valor_filtro = ['codemirror.js', 'reql_docs.js']

for valor in valor_filtro:
    filtered_df = df[df['File Name'] == valor]
    output_csv_file = f'src\\csvs\\PerLargeFile\\admin_{valor.strip().replace(" ", "_")}.csv'
    filtered_df.to_csv(output_csv_file, index=False)

    print("Dados filtrados salvos com sucesso!")

print('Todos os dados foram coletados')
