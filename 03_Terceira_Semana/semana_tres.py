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

df = pd.read_csv("datasets_554905_1035602_houses_to_rent_v2.csv")
df.describe().round(2)

df.isnull().sum()

#Qual a cidade com média de alumeguel mais elevada

df.groupby('city')['rent amount (R$)'].mean().reset_index().sort_values('rent amount (R$)', ascending = False)

#Quantos banheiros existem em média nas residências com alugueis mais elevados?

df['rent amount (R$)'].describe()

#Definicao: alugueis mais altos sao valores acima de 5000

df['aluguel_alto'] = ['Alto' if x > 5000 else 'Baixo' for x in df['rent amount (R$)']]

df['aluguel_alto'].value_counts()

df.groupby('aluguel_alto')['bathroom'].median()

#Calculo de correlacao entre aluguel e banheiros

df[['rent amount (R$)','bathroom']].corr(method = 'spearman')

aux = pd.DataFrame({'colunas': df.columns, 'tipos': df.dtypes})

lista = list(aux[aux['tipos'] == 'int64']['colunas'])
lista

df2 = df[lista]
df2.head()
d = df2.corr(method='spearman').round(2)

#Visualizacao de dados

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize = (12,6))
sns.barplot(x = 'city', y = 'rent amount (R$)', data = df.groupby('city')['rent amount (R$)'].mean().reset_index().sort_values('rent amount (R$)', ascending = False))
plt.title('Média do valor de alugél por cidade')
plt.xticks(rotation=45)
plt.show()

#histograma
sns.distplot(df['rent amount (R$)'])

#scatterplot
plt.figure(figsize = (12,6))
sns.scatterplot(x = 'rent amount (R$)', y = 'bathroom', hue = 'city', size = 'aluguel_alto', data = df)

#correlacao
sns.heatmap(df.corr().round(2), annot=True)

#FacetGrid - grid de comparação
g = sns.FacetGrid(df, col='city', row='aluguel_alto')
g = g.map(plt.hist, 'rent amount (R$)')