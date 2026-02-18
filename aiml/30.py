import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

fare_data = df["Fare"].dropna()

iteration = 1

while True:
    Q1 = fare_data.quantile(0.25)
    Q3 = fare_data.quantile(0.75)
    IQR = Q3 - Q1
    
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    
    outliers = fare_data[(fare_data < lower) | (fare_data > upper)]
    plt.figure()
    plt.boxplot(fare_data)
    plt.title(f"Fare Boxplot - Iteration {iteration}")
    plt.show()
    if outliers.empty:
        print("No outliers remain.")
        break
    fare_data = fare_data[(fare_data >= lower) & (fare_data <= upper)]
    iteration += 1
