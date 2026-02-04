import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("tips.csv")
df["tip_percentage"] = (df["tip"] / df["total_bill"]) * 100
a=df["tip_percentage"]
plt.hist(a, bins=10, color='blue', edgecolor='black')
plt.title("Tip Percentage Distribution")
plt.xlabel("Tip Percentage")
plt.ylabel("Frequency")
plt.show()