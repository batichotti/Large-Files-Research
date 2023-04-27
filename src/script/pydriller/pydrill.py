from pydriller import Repository


url = ["https://github.com/nodejs/node", 'https://github.com/Wolfterro/Projetos-em-C', 'https://github.com/JabRef/jabref']
#file_path = "/deps/v8/test/mjsunit/wasm/embenchen/lua_binarytrees.js"
#file_name = "lua_binarytrees.js"

for commit in Repository(url[2]).traverse_commits():
        print(f'{commit.author.name}: {commit.author.email}')
        print(commit.author_date)

        for file in commit.modified_files:
                print(file.filename)
