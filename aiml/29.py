import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("titanic.csv")
for col in df.select_dtypes(include=['float64', 'int64']).columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df_no_outliers = df[(df[col] >= lower) & (df[col] <= upper)]
    if len(df_no_outliers) != len(df):
        print(f"Outliers found in column '{col}'")
        plt.figure(figsize=(10,5))
        plt.subplot(1,2,1)
        plt.boxplot(df[col].dropna())
        plt.title(f"{col} (With Outliers)")
        plt.subplot(1,2,2)
        plt.boxplot(df_no_outliers[col].dropna())
        plt.title(f"{col} (Without Outliers)")
        plt.tight_layout()
        plt.show()
        
    else:
        print(f"No outliers found in column '{col}'")
