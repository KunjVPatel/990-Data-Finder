import pandas as pd
import os

num = 100
merged_df = pd.DataFrame()

for i in range(num):
    filename = f'/home/dark/GitHub/Opportunity-Hack-KSJ/OpportunityHack/Batch/out_batch_{i}.csv'
    df = pd.read_csv(filename)
    merged_df = pd.concat([merged_df, df], ignore_index=True)

merged_filename = '/home/dark/GitHub/Opportunity-Hack-KSJ/OpportunityHack/Data/merged_out.csv'
merged_df.to_csv(merged_filename, index=False)

for i in range(num):
    filename = f'/home/dark/GitHub/Opportunity-Hack-KSJ/OpportunityHack/Batch/out_batch_{i}.csv'
    os.remove(filename)

print(f'Merged data successfully written to {merged_filename}. Batch files have been deleted.')
