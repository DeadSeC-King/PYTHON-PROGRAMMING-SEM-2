import pandas as pd
df=pd.read_csv("tips.csv")
avg_tips_smoker=df.groupby('smoker')['tip'].mean()
print(avg_tips_smoker)
#wap to find avg tips by smoker and non smoker