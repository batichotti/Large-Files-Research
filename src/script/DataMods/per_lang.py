import pandas as pd


path = "src\\csvs\\final_output.csv"
df = pd.read_csv(
    path,
    encoding='utf-8',
    sep=',',
    low_memory=False,
    )

titles = df['language'].unique()
for title in titles:
    df_to_print = df[df['language'] == title]
    if '/' in title:
        title = str(title).replace('/', '_')
        title = str(title).replace(' ', '_')
    df_to_print.to_csv(f"src\\csvs\\Language\\{title}.csv", index=False)
