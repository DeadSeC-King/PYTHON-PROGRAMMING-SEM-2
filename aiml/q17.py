
import pandas as pd
df = pd.read_csv("tips.csv")
#wap to print specific columns from tips .csv
print(df[['total_bill', 'tip']].describe())
#wap to calculate tip percentage and add as new column in tips .csv
df['tip_percentage'] = (df['tip'] / df['total_bill']) * 100
print(df[['total_bill', 'tip', 'tip_percentage']].head())
'''
#wap to print first 10 lines of tips .csv
import pandas as pd
df = pd.read_csv("tips.csv")

x = df.head(10)
print(x)

#wap to print shape and columns of tips .csv and data types of each column
import pandas as pd
df = pd.read_csv("tips.csv")
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)
#wap find number of missing values in tips .csv 
print(df.isna().sum())
'''