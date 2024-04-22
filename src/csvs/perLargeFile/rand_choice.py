import pandas as pd
from random import randint

choiced = []
commits = pd.read_csv(f'src/csvs/perLargeFile/JS/commit_total.csv', low_memory=False)
rand_choiced = []

while len(choiced) <= 384:
    rand = randint(0, len(commits))
    if rand not in rand_choiced:
        choiced.append(commits['Total'].loc[rand])
        rand_choiced.append(rand)

choiced_df = pd.DataFrame({'Commits Choiced' : choiced})
choiced_df.to_csv('src/csvs/perLargeFile/JS/commits_choiced.csv')
