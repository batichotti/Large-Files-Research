import pandas as pd
import datetime
from os import makedirs, path, system
import ProjectsFiles

system('clear')
for i in range(len(ProjectsFiles.project_list)):
    csv_name = ProjectsFiles.project_list[i]
    try:
        input_csv_file = f'src/csvs/Commits/JS/csvs/{csv_name}.csv'
    except:
        continue
    df = pd.read_csv(input_csv_file, low_memory=False)

    large_flie_not_founded_list = []
    for large_file in ProjectsFiles.large_file_list[i]:
        filtered_df = df[df['File Name'] == large_file]
        output_csv_file = f'src/csvs/perLargeFile/JS/{csv_name}/{large_file}/{csv_name}{large_file.strip().replace(" ", "")}.csv'
        parent_directory = path.dirname(output_csv_file)
        makedirs(parent_directory, exist_ok=True)
        filtered_df.to_csv(output_csv_file, index=False)

        input_file = output_csv_file

        original_df = pd.read_csv(input_file)

        try:
            original_df.sort_values(by=['File Name', 'Author Email', 'Author Commit Date'], inplace=True)

            original_df['Lines Sinal'] = original_df.apply(lambda row: 'Grew' if row['Lines Added'] > row['Lines Deleted'] else 'Decreased', axis=1)

            original_df['Change alone'] = original_df['Number of Files'] > 1

            total_lines_changed = original_df.groupby(['File Name', 'Author Email'])['Lines Modified per File'].sum().reset_index()

            original_df = pd.merge(original_df, total_lines_changed, on=['File Name', 'Author Email'], suffixes=('', '_total'))

            original_df.rename(columns={'Lines Modified per File': 'Lines Trend'}, inplace=True)

            output_file_name = f'{input_file}_result.csv'
            columns_to_save = ['File Name', 'Author Commit Date', 'Change alone', 'Author Email', 'Lines Sinal', 'Lines Trend']
            created_df = original_df[columns_to_save].sort_values('Author Commit Date')
            created_df.to_csv(output_file_name, index=False)

            print(f"O arquivo '{csv_name}_{large_file}_results.csv' foi criado com as colunas relevantes.")
        except:
            pass

        input_file = output_csv_file
        tdf = pd.read_csv(input_file)

        try:
            for i in range(len(tdf)):
                tdf.loc[i, 'Commit Date'] = datetime.datetime.strptime(tdf['Committer Commit Date'].loc[i][:-6], '%Y-%m-%d %H:%M:%S')

            ndt = []
            ntdf = pd.DataFrame()
            if len(tdf) > 1:
                for i in range(len(tdf)-1):
                    diff = tdf['Commit Date'].loc[i+1] - tdf['Commit Date'].loc[i]
                    ndt.append(diff)

                ntdf = pd.DataFrame({'Difference': ndt})
                ntdf['File Name'] = tdf['File Name']
            else:
                dic = {'Difference':'Only Created',
                    'File Name':[tdf['File Name'].loc[0]]}
                ntdf = pd.DataFrame(dic)

            ntdf.to_csv(f'{input_file}_date_difference.csv', index=False)

            measures = pd.DataFrame()
            if len(ntdf) > 1:
                mean = ntdf.groupby('File Name').mean()
                median = ntdf.groupby('File Name').median()

                measures['Mean'] = mean['Difference']
                measures['Median'] = median['Difference']
                measures.insert(0, 'File Name', [ntdf['File Name'].loc[1]], True)
            else:
                dic = {'File Name':[ntdf['File Name'].loc[0]],
                    'Mean': [ntdf['Difference'].loc[0]],
                    'Median': [ntdf['Difference'].loc[0]]}
                measures = pd.DataFrame(dic)

            measures.to_csv(f'{input_file}_date_measure.csv', index=False)

            print("Datas filtradas e salvas com sucesso!")
        except:
            large_flie_not_founded_list.append(large_file)

    if len(large_flie_not_founded_list) > 0:
        lfnf = pd.DataFrame(large_flie_not_founded_list, columns=['Not Founded'])
        lfnf.to_csv(f'src/csvs/perLargeFile/JS/{csv_name}/{csv_name}_not_founded.csv')
