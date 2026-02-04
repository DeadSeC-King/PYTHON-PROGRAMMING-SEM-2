#wap to stacker bar chart for smoker vs non smoker by day
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("tips.csv")
smoker_day = df.groupby(['day', 'smoker'])['tip'].sum().unstack(fill_value=0)
smoker_day.plot(kind='bar', stacked=True, color=['orange', 'cyan'], edgecolor='black')
plt.title("Stacked Bar Chart of Tips by Smoker Status and Day")
plt.xlabel("Day")
plt.ylabel("Total Tips")
plt.legend(title='Smoker')
plt.show()
