import pandas as pd

df = pd.read_csv("Large Files.csv")

df_filtered = df[(df['Purpose'] == 'Library')]

projects_with_more_than_5 = df_filtered['Project'].value_counts()[df_filtered['Project'].value_counts() > 5].index
df_sampled = pd.DataFrame()
for project in projects_with_more_than_5:
    project_subset = df_filtered[df_filtered['Project'] == project].sample(n=5, random_state=42)
    df_sampled = pd.concat([df_sampled, project_subset])


remaining_needed = len(df) - len(df_sampled)

projects_with_less_than_5 = df_filtered['Project'].value_counts()[df_filtered['Project'].value_counts() <= 5].index

for project in projects_with_less_than_5:
    project_subset = df_filtered[df_filtered['Project'] == project]
    num_to_sample = min(5, remaining_needed, len(project_subset))
    df_sampled = pd.concat([df_sampled, project_subset.sample(n=num_to_sample, random_state=13)])
    remaining_needed -= num_to_sample

print(len(df_sampled))
df_sampled.to_csv("Library_Sortee.csv", index=False)
