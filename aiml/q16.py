import pandas as pd
df=pd.read_csv("sales_dataset_500.csv")
groups = df.groupby('Region')
summary = groups['Sales'].sum()
print(groups)
print(summary)
