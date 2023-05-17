import pydriller as drl

repositories = ['https://github.com/Wolfterro/Projetos-em-C', 'https://github.com/django/django', 'https://github.com/nodejs/node']

for repository in repositories:
    print(repository)
    for commit in drl.Repository(repository).traverse_commits():
#    for commit in drl.Repository(repository, only_no_merge=True).traverse_commits():
        hash = commit.hash
        print(f'Hash: {hash}')
        print(f'{commit.merge}')
        for file in commit.modified_files :
            file_name = file.filename
            lines_balance = file.added_lines - file.deleted_lines
            print(file_name)
            print(lines_balance)
            
