import pandas as pd

data = {'Product':['Pen','Pen','Pencil','Pencil'],
        'City':['Chennai','Delhi','Chennai','Delhi'],
        'Sales':[120,150,90,110]}
df = pd.DataFrame(data)

pivot = pd.pivot_table(df, values='Sales', index='Product', columns='City', aggfunc='sum')
print(pivot)

