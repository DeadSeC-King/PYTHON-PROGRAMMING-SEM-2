import pandas as pd
df = pd.read_csv("titanic.csv")
for col in df.select_dtypes(include=['float64', 'int64']).columns:
     Q1 = df[col].quantile(0.25)
     Q3 = df[col].quantile(0.75) 
     IQR = Q3-Q1 
     lower = Q1 - 1.5 * IQR 
     upper = Q3 + 1.5 * IQR
     outliers = df[(df[col] < lower) | (df[col] > upper)]
     if not outliers.empty:
        print(f"Outliers found in column '{col}':")
        print(outliers)
     else:
        print(f"No outliers found in column '{col}'.")
print(lower)
print(upper)
print(IQR)
#wap to code find outliers are present in any column or not
#command to print first lines#print(df.head(10))
#command to print info about the data#print(df.info())
#to print number of null values#print(df.isnull().sum())
#print missing percentage#missing_percent = (df.isnull().sum() / len(df)) * 100#print(missing_percent)
#print the describe to see outlier#print(df.describe())