import pandas as pd
df1 = pd.DataFrame({'ID':[1,2,3],'Name':['A','B','C']})
df2 = pd.DataFrame({'ID':[2,3,4],'Marks':[85,90,75]})

result = pd.merge(df1, df2, on='ID', how='inner')
print(result)

df1 = pd.DataFrame({'A':[1,2,3]}, index=['x','y','z'])
df2 = pd.DataFrame({'B':[4,5,6]}, index=['x','y','z'])

df = df1.join(df2)
print(df)
