import pandas as pd
df=pd.read_csv("tips.csv")
#wap find avg tips by day
avg_tips_by_day = df.groupby('day')['tip'].mean().sort_values(ascending=False)
print(avg_tips_by_day)