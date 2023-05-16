from pydriller import Repository
import pandas as pd


dataframe = []
def dataFramer():
    #global dataframe
    summary = pd.DataFrame({
                'Hash': [hash],
                'Project Name': [project_name],
                'Local Commit PATH': [project_path],
                'Message': [msg],
                'Branch': [branch_name],
                'Main Branch': [is_main_branch],
                #'DMM size': [DMM_size],
                #'DMM complexity': [DMM_complex],
                #'DMM Interfacing': [DMM_interfacing],
                'Number of Files': [num_files],
                'Modified Lines': [mod_lines],
                'File Name': [file_name],
                'Change Type': [file_change_type],
                'Local File PATH Old': [file_old_path],
                'Local File PATH New': [file_new_path],
                'Author Name': [author_name],
                'Author Email': [author_email],
                'Author Commit Date': [author_date],
                'Author Commit Timezone' : [author_timezone],
                'Committer Name': [committer_name],
                'Committer Email': [committer_email],
                'Committer Commit Date': [committer_date],
                'Committer Timezone': [committer_timezone],
                'Merge Commit': [is_merge_commit],
                'Complexity': [file_complex],
                'Methods': [file_methods],
                #if len(file.methods) != 0:
                #    print('Methods Before:')
                #    for method in file.methods_before:
                #        print(method)
                #    print('Changed Method: ')
                #    for method in file.changed_methods:
                #        print(method)
                'Tokens': [file_tokens],
                'Lines Of Code(nloc)': [file_nloc],
                'Lines Added': [file_lines_added],
                'Lines Deleted': [file_lines_deleted],
                'Lines Modified per File': [file_modified_lines],
                'Lines Balance': [file_lines_balance]
            })
    dataframe.append(summary)


for commit in Repository('https://github.com/matomo-org/matomo').traverse_commits():

    for branch in commit.branches:
        hash = commit.hash
        project_name = commit.project_name
        project_path = commit.project_path
        msg = commit.msg
        branch_name = branch
        is_main_branch = commit.in_main_branch
        #DMM_size = commit.dmm_unit_size
        #DMM_complex = commit.dmm_unit_complexity
        #DMM_interfacing = commit.dmm_unit_interfacing
        num_files = commit.files
        mod_lines = commit.lines
        author_name = commit.author.name
        author_email = commit.author.email
        author_date = commit.author_date
        author_timezone = commit.author_timezone
        committer_name = commit.committer.name
        committer_email = commit.committer.email
        committer_date = commit.committer_date
        committer_timezone = commit.committer_timezone
        is_merge_commit = commit.merge
        for file in commit.modified_files:
            file_name = file.filename
            file_change_type = str(file.change_type).split('.')[-1]
            file_old_path = file.old_path
            file_new_path = file.new_path
            file_complex = (file.complexity if (str(type(file.complexity)).split("\'")[1] != "NoneType") else 'null')
            file_methods = len(file.methods)
            file_tokens = (file.token_count if (str(type(file.token_count)).split("\'")[1] != "NoneType") else 'null')
            file_nloc = (file.nloc if (str(type(file.nloc)).split("\'")[1] != "NoneType") else 'null')
            file_lines_added = file.added_lines
            file_lines_deleted = file.deleted_lines
            file_modified_lines = (file.added_lines + file.deleted_lines)
            file_lines_balance = (file.added_lines - file.deleted_lines)

        dataFramer()

summary_df = pd.concat(dataframe, ignore_index=True)

summary_df.to_csv(f'src\\csvs\\Commits\\summary{commit.project_name}.csv', index=False)