import pandas as pd


def count_values_list(list, path):
    data = { # KIM == Know In Mind
        'index': [],
        'count': []
    }
    for each in list:
        if each not in data['index']:
            data['index'].append(each)
            data['count'].append(1)
        else:
            to_add = int()
            for j in range(0, len(data['index'])):
                seeker = data['index'][j]
                if seeker == each:
                    to_add = j
                    break
            data['count'][to_add] += 1
    df = pd.DataFrame(data).sort_values(by=['count'], ascending=False)
    df.to_csv(path, index=False)

path = "src\\csvs\\final_output.csv"
files_ext_list = []
file_ext = str()
df = pd.read_csv(
    path,
    encoding='utf-8',
    sep=',',
    low_memory=False,
    )
len_df = len(df['language'])

file_ext = str(df['language']).split('.')[-1]
files_ext_list.append(file_ext)

for i in range(1, len_df):
    file_ext = str(df['language'][i]).split('.')[-1]
    files_ext_list.append(file_ext)

count_values_list(files_ext_list, "src\\csvs\\ext_output.csv")
