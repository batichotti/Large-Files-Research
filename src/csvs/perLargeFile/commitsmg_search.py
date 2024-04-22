import os
import pandas as pd

os.system('clear')

def read_large_files_data(folder_path:str) -> pd.DataFrame:
    dataframes = []
    for folder in os.listdir(folder_path):
        folder_full_path = os.path.join(folder_path, folder)
        if os.path.isdir(folder_full_path):
            for file in os.listdir(folder_full_path):
                file_full_path = os.path.join(folder_full_path, file)
                if os.path.isdir(file_full_path):
                    for each in os.listdir(file_full_path):
                        each_full_path = os.path.join(file_full_path, each)
                        if each.endswith("csv_mgcommit_anal.csv"):
                            print("Processing CSV file:", each_full_path)
                            df = pd.read_csv(each_full_path)
                            df['Project'] = folder
                            dataframes.append(df)
    os.system('clear')
    return pd.concat(dataframes, ignore_index=True)

def main():
    folder_path_large_files = os.path.join("src", "csvs", "perLargeFile", "JS")
    commits = read_large_files_data(folder_path_large_files)
    choiced = pd.read_csv('src/csvs/perLargeFile/JS/commits_choiced.csv', low_memory=False)
    
    commits = commits.drop_duplicates(subset='Hash')
    novo_df = commits.merge(choiced, left_on='Hash', right_on='Commits Choiced', suffixes=('_commits', '_choiced'))
    novo_df = novo_df[['Hash', 'File Name', 'Project', 'Commit Purpose', 'Message']]
    novo_df.to_csv('src/csvs/perLargeFile/JS/choiced_message.csv')
    
if __name__ == "__main__":
    main()
