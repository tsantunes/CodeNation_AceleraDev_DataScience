    import pandas as pd

pd.set_option('display.max_columns', 100000)
pd.set_option('display.max_rows', 100000) 
pd.set_option('display.max_colwidth', 100000) 
pd.set_option('display.width', None) 


    df = pd.read_csv("datasets_554905_1035602_houses_to_rent.csv")
    df.describe()
    df.shape
    df.columns
    df.info()
    
    df.isnull().sum()
    
    df.groupby('furniture')['area'].mean()

df
print(df)
