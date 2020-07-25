# !git add "file.py"
# !git commit -m "My commit"
# !git push origin master

# Useful commands to work in daily life:

# git checkout -b "branchname" ->  creates new branch
# git branch                   ->  lists all branches
# git checkout "branchname"    ->  switches to your branch
# git push origin "branchname" ->  Pushes to your branch
# git add */filename           -> Stages *(All files) or by given file name
# git commit -m "commit message" -> Commits staged files
# git push                     -> Pushes to your current branch

import pandas as pd

pd.set_option('display.max_columns', 100000)
pd.set_option('display.max_rows', 100000) 
pd.set_option('display.max_colwidth', 100000) 
pd.set_option('display.width', None) 

pd.data
df = pd.read_csv("datasets_554905_1035602_houses_to_rent.csv")
df.describe()
df.shape
df.columns
df.info()

df.isnull().sum()

df.groupby('furniture')['area'].mean()

df
print(df)

