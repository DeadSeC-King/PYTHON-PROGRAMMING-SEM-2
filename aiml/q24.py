#wap to plot a scatter plot of total bill vs tip
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("tips.csv")
plt.scatter(df['total_bill'], df['tip'], color='yellow', edgecolor='black')
plt.title("Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()