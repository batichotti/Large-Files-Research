import pandas as pd


path = "src\\csvs\\final_output.csv"
df = pd.read_csv(
    path,
    encoding='utf-8',
    sep=',',
    low_memory=False,
    )

titles = df['project'].unique()
for title in titles:
    df_to_print = df[df['project'] == title]
    if '/' in title:
        title = str(title).replace('/', '_')
        title = str(title).replace(' ', '_')
    df_to_print.to_csv(f"src\\csvs\\Projects\\{title}.csv", index=False)
