import pandas as pd

data = {'Category':['A','A','B','B','B'],
        'Sales':[100,200,150,300,250]}
df = pd.DataFrame(data)

result = df.groupby('Category')['Sales'].sum()
print(result)