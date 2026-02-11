#wap to read the data from csv file and print the first 15 rows
import pandas as pd
df=pd.read_csv('data.csv')
x=df.head(15)
print(x)