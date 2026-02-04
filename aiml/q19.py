import pandas as pd
df=pd.read_csv("tips.csv")
#wap to find top 10 tip percentages
df['tip_percentage'] = (df['tip'] / df['total_bill']) * 100
top10=df.sort_values(by='tip_percentage', ascending=False).head(10)
#wap to print in decending order of tip percentage
top11=df.sort_values(by='tip_percentage', ascending=True).head(10)
print(top10)
print(top11)