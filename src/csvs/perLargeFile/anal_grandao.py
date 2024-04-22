import pandas as pd


df = pd.read_csv('src/csvs/perLargeFile/grandao.csv')

# Convert 'Author Commit Date' to datetime
df['Author Commit Date'] = pd.to_datetime(df['Author Commit Date'])

# Define a custom sorting function
def sort_by_date(group):
    return group.sort_values(by='Author Commit Date')

# Group by 'File Name' and 'Project Name', then apply the sorting function
sorted_grouped_df = df.groupby(['File Name', 'Project Name']).apply(sort_by_date)

# Drop the extra index level introduced by groupby
sorted_grouped_df.reset_index(drop=True, inplace=True)

# Sort the DataFrame by 'Author Commit Date' within each group
sorted_grouped_df = df.sort_values(by='Author Commit Date').groupby(['File Name', 'Project Name']).last()

print(sorted_grouped_df)

sorted_grouped_df.to_csv('src/csvs/perLargeFile/grandao_milado.csv')