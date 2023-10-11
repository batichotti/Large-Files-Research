import pandas as pd
import datetime

df = pd.read_csv('Large-Files-Research\\src\\csvs\\perLargeFile\\gogs_gogs.js.csv')

#convert str to datetime
for i in range(len(df)):
    df.loc[i, 'Author Commit Date'] = datetime.datetime.strptime(df['Author Commit Date'].loc[i][:-6], '%Y-%m-%d %H:%M:%S')

#calc commit time difference
ndt = []
for i in range(len(df)-1):
    diff = df['Author Commit Date'].loc[i+1] - df['Author Commit Date'].loc[i]
    ndt.append(diff)
ndf = pd.DataFrame({'Difference': ndt})

ndf['File Name'] = df['File Name']

#generate csvs
ndf.to_csv(f'Large-Files-Research\\src\\csvs\\perLargeFile\\date_difference.csv', index=False)

mean = ndf.groupby('File Name').mean()
median = ndf.groupby('File Name').median()


measures = pd.DataFrame()

measures['Mean'] = mean['Difference']
measures['Median'] = median['Difference']
measures.insert(0, 'File Name', [ndf['File Name'].loc[1]], True)

measures.to_csv(f'Large-Files-Research\\src\\csvs\\perLargeFile\\date_measure.csv', index=False)
