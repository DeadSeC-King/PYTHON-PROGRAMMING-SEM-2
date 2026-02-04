#wap to box ploat comparing tip for lunch and dinner
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("tips.csv")
lunch_tips = df[df['time'] == 'Lunch']['tip']
dinner_tips = df[df['time'] == 'Dinner']['tip']
data = [lunch_tips, dinner_tips]
plt.boxplot(data, labels=['Lunch', 'Dinner'])
plt.title("Tip Comparison: Lunch vs Dinner")
plt.ylabel("Tip Amount")
plt.xlabel("Time of Day")
plt.show()