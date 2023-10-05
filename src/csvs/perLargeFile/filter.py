import pandas as pd

input_csv_file = 'src\\csvs\\PerLargeFile\\gogs.csv'
df = pd.read_csv(input_csv_file)

valor_filtro = ['pdf.worker.js', 'pdf.js', 'viewer.js', 'gogs.js']

for valor in valor_filtro:
    filtered_df = df[df['File Name'] == valor]
    output_csv_file = f'src\\csvs\\PerLargeFile\\gogs_{valor.strip().replace(" ", "_")}.csv'
    filtered_df.to_csv(output_csv_file, index=False)

    print("Dados filtrados salvos com sucesso!")

print('Todos os dados foram coletados')
