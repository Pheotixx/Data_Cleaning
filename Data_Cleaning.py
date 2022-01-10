import pandas as pd 
import csv

df = pd.read_csv('Final.csv')
print(df.shape)

del df["hyperlink"]
df = df.rename({
    'pl_hostname':"Solar_System_Name"
},axis= 'columns')

df.to_csv('Main.csv')
print(df.shape)
