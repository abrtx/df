
# Table of Contents

1.  [Python&rsquo;s Pandas Dataframes](#org229a88f)
2.  [Why?](#org8b04431)
3.  [How](#org4c56ec4)
4.  [Example](#orgba714f5)
    1.  [Extract](#orgfed3ae7)
    2.  [Transform](#orgfad68d0)
        1.  [TO DF](#org0543875)
        2.  [Tax apply](#orgcd0a904)
    3.  [Load](#org825b23e)
        1.  [Reset transformations](#orgaff9917)
        2.  [Insert to a database](#orgee9df8d)
5.  [Code](#orgf240572)
6.  [Product](#org5463cb2)



<a id="org229a88f"></a>

# Python&rsquo;s Pandas Dataframes

Data structure that are Two-dimentional, size-mutable, 
tabular data representation.
For more information:
<https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html>


<a id="org8b04431"></a>

# Why?

Sometime We&rsquo;ll need to deal with data from some API where 
that data representation isn&rsquo;t fit for some kind of process.
Well, this is a formula that is possible fit well


<a id="org4c56ec4"></a>

# How

Its time for famous ETL process. 


<a id="orgba714f5"></a>

# Example


<a id="orgfed3ae7"></a>

## Extract

Suppose we receive a list of dicts from the API for apply
some taxes to a particular product. 

    
    data = [{'Product':'Bananas','Tax':1.3,'Price':1.2},
    	{'Product':'Cafe','Tax': 0.5,'Price':0.7},
    	{'Product':'Milk','Price':3.8,'Tax': 4.5}]


<a id="orgfad68d0"></a>

## Transform


<a id="org0543875"></a>

### TO DF

    df = pd.DataFrame(data)


<a id="orgcd0a904"></a>

### Tax apply

    
    def tax_apply(row):
    
        if row.name == 'Bananas':
    	row.Price = row.Price * row.Tax
        return row
    
    df=df.set_index('Product')
    
    df.apply(tax_apply, axis='columns')


<a id="org825b23e"></a>

## Load


<a id="orgaff9917"></a>

### Reset transformations

    
    df = df.reset_index()
    item = df.pop('Product')
    df.insert(0, 'Product', item)


<a id="orgee9df8d"></a>

### Insert to a database

Sorry, but don&rsquo;t care this time


<a id="orgf240572"></a>

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


<a id="org5463cb2"></a>

# Product

    
    (dataframes) abrtx@abrtx-laptop:~/work/python/pd$ python test.py 
    
    df previous:
        Product  Tax  Price
    0  Bananas  1.3    1.2
    1     Cafe  0.5    0.7
    2     Milk  4.5    3.8
    
    df set_index(tipo):
    	  Tax  Price
    Product            
    Bananas  1.3    1.2
    Cafe     0.5    0.7
    Milk     4.5    3.8
    
    df :
    	  Tax  Price
    Product            
    Bananas  1.3   1.56
    Cafe     0.5   0.70
    Milk     4.5   3.80
    
    df Transpose (df):
        Product  Tax  Price
    0  Bananas  1.3   1.56
    1     Cafe  0.5   0.70
    2     Milk  4.5   3.80
    
    (dataframes) abrtx@abrtx-laptop:~/work/python/pd$ 

