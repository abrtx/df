import pandas as pd

# df = pd.DataFrame([['Bananas', 0.2, 2.2],
#                    ['Cafe', 0.5, 4.5],
#                    ['Milk', 0.7, 3.8]],
#                   columns=['Item','Tax','Price'])

df = pd.DataFrame([['Product','Bananas','Cafe', 'Milk'],
                   ['Tax',1.3, 0.5, 4.5],
                   ['Price',1.2, 0.7, 3.8]],
                  columns=['Item','Item0','Item1','Item2'])


def mapping(row):
    
    if row.name == 'Item0':
        row.Price = row.Price + row.Tax
    return row

print(f'\ndf previous:\n {df}\n')

df=df.set_index('Item').T

print(f'df set_index(tipo):\n {df}\n')

df.apply(mapping, axis='columns')
print(f'df :\n {df}\n')
df = df.T
df = df.reset_index()
item = df.pop('Item')
df.insert(0, 'Item', item)

print(f'df Transpose (df):\n {df}\n')
