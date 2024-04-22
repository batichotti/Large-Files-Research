import pandas as pd
from os import makedirs, path, system
import FlagsKeywords
import re


system('clear')

tiny_files = pd.read_csv("src/csvs/perLargeFile/tiny/random_1001_tiny_rows.csv")
tiny_files = tiny_files.sort_values(by='Project Name', ascending=True)
tiny_files_list = []

commits_total = []

def classify_commit_purpose(commit_message):
    classification_list = []
    commit_message = str(commit_message).lower()

    for expression, classification in FlagsKeywords.regex.items():
        if len(re.compile(expression).findall(commit_message)) > 0:
            if classification == "Commit Operation":
                classification_list.append(classification)
                break
            if classification == "Build Configuration":
                classification_list.append(classification)
                break
            if classification not in classification_list:
                classification_list.append(classification)
    if len(classification_list) > 1:
        classification_list.append("Tangled Commits")
    elif len(classification_list) == 0:
        if len(re.compile(r"test").findall(commit_message)) > 0:
            classification_list.append("Test")
        else:
            classification_list.append("Other")

    return classification_list


csv_name = ''
for i in range(len(tiny_files)):
    if i==0 or tiny_files['Project Name'].loc[i] != tiny_files['Project Name'].loc[i-1]:
        csv_name = tiny_files['Project Name'].loc[i]
        try:
            input_csv_file = f'src/csvs/Commits/JS/csvs/{csv_name}.csv'
        except:
            continue
        df = pd.read_csv(input_csv_file, low_memory=False)

    commits_unclassified_total = []


    large_file = tiny_files['File Name'].loc[i]
    filtered_df = df[df['File Name'] == large_file]


    output_csv_file = f'src/csvs/perLargeFile/tiny/{csv_name}/{large_file}/{csv_name}{large_file.strip().replace(" ", "")}.csv'

    parent_directory = path.dirname(output_csv_file)
    makedirs(parent_directory, exist_ok=True)

    filtered_df.to_csv(output_csv_file, index=False)

    input_file = output_csv_file

    original_df = pd.read_csv(input_file)

    try:
        original_df['Commit Purpose'] = original_df['Message'].apply(classify_commit_purpose)

        for i in range(len(original_df)):
            if "Other" in original_df['Commit Purpose'].loc[i]:
                commits_unclassified.append(original_df['Hash'].loc[i])
                if original_df['Hash'].loc[i] not in commits_unclassified_total:
                    commits_unclassified_total.append(original_df['Hash'].loc[i])
            if original_df['Hash'].loc[i] not in commits_total:
                    commits_total.append(original_df['Hash'].loc[i])

        original_df.sort_values(by=['Hash','File Name', 'Author Email', 'Author Commit Date'], inplace=True)

        output_file_name = f'{input_file}_mgcommit_anal.csv'
        columns_to_save = ['Hash','File Name', 'Author Commit Date', 'Author Email', 'Commit Purpose', 'Message']
        created_df = original_df[columns_to_save].sort_values('Author Commit Date')
        created_df.to_csv(output_file_name, index=False)

        commits_unclassified.append(f"{len(commits_unclassified)*100/len(original_df):.3f}%")
        unclassified_df = pd.DataFrame({'Other':commits_unclassified})
        unclassified_df.to_csv(f'{input_file}_unclassified_commits.csv')
        unclassified_total_df = pd.DataFrame({'Other':commits_unclassified_total})
        unclassified_total_df.to_csv(f'src/csvs/perLargeFile/tiny/{csv_name}/{csv_name}_unclassified.csv')

        commits_unclassified = []

        print(f"\033[32mO arquivo '{csv_name}_{large_file}_mgcommit_anal.csv' foi criado com as colunas relevantes.\033[m")
    except:
        pass

total_df = pd.DataFrame({'Total':commits_total})
total_df.to_csv(f'src/csvs/perLargeFile/tiny/commit_total.csv')
