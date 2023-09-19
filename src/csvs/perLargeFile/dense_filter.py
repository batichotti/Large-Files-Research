import pandas as pd

# Nome do arquivo CSV original
input_file_name = 'admin_codemirror.js.csv'

# Carregar o CSV original em um DataFrame
original_df = pd.read_csv("src\\csvs\\perLargeFile\\" + input_file_name)

# Classificar o propósito do arquivo com base nas mensagens de commit
def classify_file_purpose(commit_message):
    commit_message = str(commit_message).lower()
    keywords = {
        'driver': 'Driver',
        'api': 'API',
        'business rule': 'Business Rule',
        'interface': 'Interface',
        'feature': 'Feature',
        'documentation': 'Documentation',
        'test': 'Test',
        'configuration': 'Configuration',
        # Adicione mais palavras-chave e classificações conforme necessário
    }

    # Classificação padrão se nenhuma palavra-chave for encontrada
    default_classification = 'Other'

    # Verifique as palavras-chave na mensagem de commit e retorne a classificação correspondente
    for keyword, classification in keywords.items():
        if keyword in commit_message:
            return classification

    return default_classification

# Aplicar a classificação de propósito de arquivo ao DataFrame original
original_df['File Purpose'] = original_df['Message'].apply(classify_file_purpose)

# Ordenar o DataFrame pelo nome do arquivo e a data do commit
original_df.sort_values(by=['File Name', 'Author Commit Date'], inplace=True)

# Calcular o sinal de crescimento ou diminuição de linhas
original_df['Lines Sinal'] = original_df.apply(lambda row: 'Grew' if row['Lines Added'] > row['Lines Deleted'] else 'Decreased', axis=1)

# Calcular a quantidade total de linhas alteradas no final
total_lines_changed = original_df.groupby('File Name')['Lines Modified per File'].sum().reset_index()

# Mesclar o total de linhas alteradas de volta ao DataFrame original
original_df = pd.merge(original_df, total_lines_changed, on='File Name', suffixes=('', '_total'))

# Renomear a coluna para 'Lines Trend'
original_df.rename(columns={'Lines Modified per File_total': 'Lines Trend'}, inplace=True)

# Salvar apenas as colunas criadas neste arquivo em um novo CSV
output_file_name = 'src\\csvs\\perLargeFile\\results.csv'
columns_to_save = ['File Name', 'File Purpose', 'Author Email', 'Lines Sinal', 'Lines Trend']
created_df = original_df[columns_to_save]
created_df.to_csv(output_file_name, index=False)

# Resultados
print("O arquivo 'results.csv' foi criado com as colunas relevantes.")
