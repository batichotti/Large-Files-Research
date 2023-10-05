import pandas as pd

# Nome do arquivo CSV original
input_file_name = 'gogs_gogs.js.csv'

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
    }

    default_classification = 'Other'

    for keyword, classification in keywords.items():
        if keyword in commit_message:
            return classification

    return default_classification

original_df['File Purpose'] = original_df['Message'].apply(classify_file_purpose)

original_df.sort_values(by=['File Name', 'Author Email', 'Author Commit Date'], inplace=True)

original_df['Lines Sinal'] = original_df.apply(lambda row: 'Grew' if row['Lines Added'] > row['Lines Deleted'] else 'Decreased', axis=1)

original_df['Change alone'] = original_df['Number of Files'] > 1

total_lines_changed = original_df.groupby(['File Name', 'Author Email'])['Lines Modified per File'].sum().reset_index()

original_df = pd.merge(original_df, total_lines_changed, on=['File Name', 'Author Email'], suffixes=('', '_total'))

original_df.rename(columns={'Lines Modified per File': 'Lines Trend'}, inplace=True)

output_file_name = 'src\\csvs\\perLargeFile\\results.csv'
columns_to_save = ['File Name', 'Author Commit Date', 'File Purpose', 'Change alone', 'Author Email', 'Lines Sinal', 'Lines Trend']
created_df = original_df[columns_to_save].sort_values('Author Commit Date')
created_df.to_csv(output_file_name, index=False)

print("O arquivo 'results.csv' foi criado com as colunas relevantes.")
