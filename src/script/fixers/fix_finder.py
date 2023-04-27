import pandas as pd


path = "src\\csvs\\final_output.csv"
some_words = []
df = pd.read_csv(
    path,
    encoding='utf-8',
    sep=',',
    low_memory=False,
    )

i = 1

for index, row in df.iterrows():
    i +=1
    try:
        if type(float(row['code'])) != float:
            some_words.append(i)
    except:
        some_words.append(i)

for word in some_words:
    print(word)