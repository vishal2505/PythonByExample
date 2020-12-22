import pandas as pd
df=pd.read_csv("student.csv")
df1=df.groupby(["name","age"])["marks"].sum()
print(df1)