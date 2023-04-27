import pandas as pd

tbl = pd.read_csv("src\\csvs\\javascript_count.csv", low_memory=False)

print((tbl['Count'].sum()))