#wap 
import pandas as pd 
df=pd.read_csv("data.csv")
x=df.isnull().sum()
print(x)
