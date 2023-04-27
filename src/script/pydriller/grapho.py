from pydriller import Repository
import matplotlib.pyplot as plt

repo = Repository('https://github.com/nodejs/node')
authors = []
for commit in repo.traverse_commits():
    authors.append(commit.author.name)

authors_dict = {}

for nome in authors:
    if nome in authors_dict:
        authors_dict[nome] += 1
    else:
        authors_dict[nome] = 1

nomes = [nome for nome, valor in authors_dict.items() if valor > 500]
valores = [valor for nome, valor in authors_dict.items() if valor > 500]

plt.bar(nomes, valores)
plt.xlabel('Authors')
plt.xticks(rotation=75)
plt.ylabel('Commits')
plt.tight_layout()
# Exibir o gráfico
plt.show()
