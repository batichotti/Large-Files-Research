from pydriller import Repository
import pandas as pd


dataframe = []
repositories = ['https://github.com/nodejs/node', 'https://github.com/matomo-org/matomo', 'https://github.com/gabrielfroes/webscraping_python_selenium', 'https://github.com/official-stockfish/Stockfish', 'https://github.com/LorittaBot/Loritta']
def dataFramer(commit, file):
    summary = pd.DataFrame({
        'Hash': [commit.hash],
        'Project Name': [commit.project_name],
        'Local Commit PATH': [commit.project_path],
        'Message': [commit.msg],
        'Main Branch': [commit.in_main_branch],
        'Number of Files': [commit.files],
        'Modified Lines': [commit.lines],
        'File Name': [file.filename],
        'Change Type': [str(file.change_type).split('.')[-1]],
        'Local File PATH Old': [file.old_path],
        'Local File PATH New': [file.new_path],
        'Author Name': [commit.author.name],
        'Author Email': [commit.author.email],
        'Author Commit Date': [commit.author_date],
        'Author Commit Timezone': [commit.author_timezone],
        'Committer Name': [commit.committer.name],
        'Committer Email': [commit.committer.email],
        'Committer Commit Date': [commit.committer_date],
        'Committer Timezone': [commit.committer_timezone],
        'Merge Commit': [commit.merge],
        'Complexity': [file.complexity if file.complexity else 'null'],
        'Methods': [len(file.methods)],
        'Tokens': [file.token_count if file.token_count else 'null'],
        'Lines Of Code(nloc)': [file.nloc if file.nloc else 'null'],
        'Lines Added': [file.added_lines],
        'Lines Deleted': [file.deleted_lines],
        'Lines Modified per File': [file.added_lines + file.deleted_lines],
        'Lines Balance': [file.added_lines - file.deleted_lines]
    })
    dataframe.append(summary)

repo = Repository(repositories[-1])
i = -1
for commit in repo.traverse_commits():
    if i == -1:
        csv_name = commit.project_name
        i += 1
    try:
        for file in commit.modified_files:
            dataFramer(commit, file)
            print(commit.committer_date)
    except Exception:
        i += 1
        print("Error")

print(f"ERRORS {i}")
summary_df = pd.concat(dataframe, ignore_index=True)
summary_df.to_csv(f'src\\csvs\\Commits\\summary_{csv_name}.csv', index=False)
