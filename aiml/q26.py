#wap to make line chart according tip by party size
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("tips.csv")
plt.plot(df.groupby('size')['tip'].mean().index, df.groupby('size')['tip'].mean().values , marker='o', color='purple')
plt.title("Average Tip by Party Size")
plt.xlabel("Party Size")    
plt.ylabel("Average Tip")
plt.grid()
plt.show()
