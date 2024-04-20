import pandas as pd

# df = pd.DataFrame([['Bananas', 0.2, 2.2],
#                    ['Cafe', 0.5, 4.5],
#                    ['Milk', 0.7, 3.8]],
#                   columns=['Item','Tax','Price'])

# [['Product','Bananas','Cafe', 'Milk'],
#                    ['Tax',1.3, 0.5, 4.5],
#                    ['Price',1.2, 0.7, 3.8]]
# data = [{'Product':'Bananas','Product':'Cafe','Product':'Milk'},
#         {'Tax':1.3,'Tax': 0.5,'Tax': 4.5},
#         {'Price':1.2,'Price':0.7,'Price':3.8}]


data = [{'Product':'Bananas','Tax':1.3,'Price':1.2},
        {'Product':'Cafe','Tax': 0.5,'Price':0.7},
        {'Product':'Milk','Price':3.8,'Tax': 4.5}]

df = pd.DataFrame(data)


def tax_apply(row):
    
    if row.name == 'Bananas':
        row.Price = row.Price * row.Tax
    return row

print(f'\ndf previous:\n {df}\n')

df=df.set_index('Product')

print(f'df set_index(tipo):\n {df}\n')

df.apply(tax_apply, axis='columns')
print(f'df :\n {df}\n')
# df = df.T
df = df.reset_index()
item = df.pop('Product')
df.insert(0, 'Product', item)

print(f'df Transpose (df):\n {df}\n')
