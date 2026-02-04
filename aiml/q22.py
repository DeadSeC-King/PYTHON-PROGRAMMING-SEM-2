#wap to print the histgram for the total bill
import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv("tips.csv")
plt.hist(df['total_bill'], bins=10, color='blue', edgecolor='black')
plt.title("Histogram of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()