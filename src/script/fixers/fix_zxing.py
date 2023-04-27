import pandas as pd

    
#READ JUST ONE PROJECT PER TIME
path = "src\\csvs\\fix.csv"
files_proj_list = []
df = pd.read_csv(
    path,
    encoding='utf-8',
    sep=',',
    low_memory=False,
    )

len_df = len(df['project'])
escopo = str(df['project'])
files_proj_list.append(escopo)

for i in range(1, len_df):
    escopo = str(df['project'][i])
    if escopo not in files_proj_list:
        """empty = pd.DataFrame()
        empty.to_csv(f".\\pProject\\{escopo}.csv", index=False)"""
        files_proj_list.append(escopo)

language = []
code = []
aux = 1
print('\033[31m * DATAFRAME CRIADO * \033[m')

loading = 100.00
current_load = 0.00
step_to_load = loading/len(df['project'])

for index, row in df.iterrows():
    print(f'{round(current_load, 2)}%')
    current_load += step_to_load
    if aux == 1:
        to_turn_project = 'sopa de macaco'
        aux += 1
    tuner = False
    for project in files_proj_list:
        if project == row['project']:
            if (index+1) == len(df['project']):
                to_turn_project = project
            if project == to_turn_project:

                df_csv = pd.DataFrame({
                    'language': language,
                    'lines': code
                })
                df_csv.to_csv(f"src\\csvs\\Projects\\{to_turn_project}.csv", index=False)

                language = []
                code =[]
                to_turn_project = project
            tuner = True
            if row['language'] not in language:
                language.append(row['language'])
                code.append(int(row['code']))
            else:
                to_add = int(row['code'])
                position = language.index(row['language'])
                code[position] = int(row['code']) + int(code[position])
        if tuner:
            break
print('AE, PORRA!')
