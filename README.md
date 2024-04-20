
# Table of Contents

1.  [Python&rsquo;s Pandas Dataframes](#orgbe4da47)
2.  [Why?](#orgdd65e09)
3.  [How](#orgdd900d5)
4.  [Example](#org4c70879)
    1.  [Extract](#org4b191e5)
    2.  [Transform](#orgecaa326)
        1.  [TO DF](#org6fcf5b5)
        2.  [Tax apply](#org8a41061)
    3.  [Load](#orge085c37)
        1.  [Reset transformations](#org50510bf)
        2.  [Insert to a database](#orgcfd0fb0)
5.  [Code](#org321f6a0)



<a id="orgbe4da47"></a>

# Python&rsquo;s Pandas Dataframes

Data structure that are Two-dimentional, size-mutable, 
tabular data representation.
For more information:
<https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html>


<a id="orgdd65e09"></a>

# Why?

Sometime We&rsquo;ll need to deal with data from some API where 
that data representation isn&rsquo;t fit for some kind of process.
Well, this is a formula that is possible fit well


<a id="orgdd900d5"></a>

# How

Its time for famous ETL process. 


<a id="org4c70879"></a>

# Example


<a id="org4b191e5"></a>

## Extract

Suppose we receive a list of dicts from the API for apply
some taxes to a particular product. 

    
    data = [{'Product':'Bananas','Tax':1.3,'Price':1.2},
    	{'Product':'Cafe','Tax': 0.5,'Price':0.7},
    	{'Product':'Milk','Price':3.8,'Tax': 4.5}]


<a id="orgecaa326"></a>

## Transform


<a id="org6fcf5b5"></a>

### TO DF

    df = pd.DataFrame(data)


<a id="org8a41061"></a>

### Tax apply

    
    def tax_apply(row):
    
        if row.name == 'Bananas':
    	row.Price = row.Price * row.Tax
        return row
    
    df=df.set_index('Product')
    
    df.apply(tax_apply, axis='columns')


<a id="orge085c37"></a>

## Load


<a id="org50510bf"></a>

### Reset transformations

    
    df = df.reset_index()
    item = df.pop('Product')
    df.insert(0, 'Product', item)


<a id="orgcfd0fb0"></a>

### Insert to a database

Sorry, but don&rsquo;t care this time


<a id="org321f6a0"></a>

# Code

    
    import pandas as pd
    
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
    
    df = df.reset_index()
    item = df.pop('Product')
    df.insert(0, 'Product', item)
    
    print(f'df Transpose (df):\n {df}\n')

