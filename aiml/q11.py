#wap to find the statistical summary of the given data
import pandas as pd
df=pd.read_csv('data.csv')
x=df["Pulse"].describe()
print(x)
