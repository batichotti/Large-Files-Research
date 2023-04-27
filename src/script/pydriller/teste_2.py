from pydriller import Repository
import pandas as pd

dataframe = []

for commit in Repository('https://github.com/Wolfterro/Projetos-em-C').traverse_commits():

    for branch in commit.branches:
        for file in commit.modified_files:
            summary = pd.DataFrame({
                'Hash': [commit.hash],
                'Project Name': [file.project_name],
                'Local Commit PATH': [commit.project_path],
                'Message': [commit.msg],
                'Branch': [branch],
                'Main Branch': [commit.in_main_branch],
                #'DMM size': [commit.dmm_unit_size],
                #'DMM complexity': [commit.dmm_unit_complexity],
                #'DMM Interfacing': [commit.dmm_unit_interfacing],
                'Number of Files': [commit.files],
                'Modified Lines': [commit.lines],
                'File Name': [file.filename],
                'Change Type': [file.change_type],
                'Local File PATH Old': [file.old_path],
                'Local File PATH New': [file.new_path],
                'Author Name': [commit.author.name],
                'Author Email': [commit.author.email],
                'Author Commit Date': [commit.author_date],
                'Committer Name': [commit.committer.name],
                'Committer Email': [commit.committer.email],
                'Committer Commit Date': [commit.committer_date],
                'Merge Commit': [commit.merge],
                'Complexity': [file.complexity],
                'Methods': [len(file.methods)],
                #if len(file.methods) != 0:
                #    print('Methods Before:')
                #    for method in file.methods_before:
                #        print(method)
                #    print('Changed Method: ')
                #    for method in file.changed_methods:
                #        print(method)
                'Tokens': [file.tokens],
                'Lines Of Code(nloc)': [file.nloc],
                'Lines Added': [file.added_lines],
                'Lines Deleted': [file.deleted_lines],
                'Lines Modified per File': [file.added_lines + file.deleted_lines],
                'Lines Balance': [file.added_lines - file.deleted_lines]
            })
            dataframe.append(summary)
            summary = pd.DataFrame()

summary_df = pd.concat(dataframe, ignore_index=True)

summary_df.to_csv('summary.csv')
