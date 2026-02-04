#plot a bar chart avg tip by day 
import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv("tips.csv")
plt.bar(df.groupby('day')['tip'].mean().index, df.groupby('day')['tip'].mean().values , color='green', edgecolor='black')
plt.title("Average Tip by Day")     
plt.xlabel("Day")
plt.ylabel("Average Tip")
plt.show()
