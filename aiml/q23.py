#plot a bar chart avg tip by day 
import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv("tips.csv")
plt.plot(df.groupby('day')['tip'].mean(), marker='o')
plt.title("Average Tip by Day")
plt.xlabel("Day")
plt.ylabel("Average Tip")
plt.grid()
plt.show()
