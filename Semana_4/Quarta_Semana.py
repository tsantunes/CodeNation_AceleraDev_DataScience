import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sct
import seaborn as sns
from statsmodels.distributions.empirical_distribution import ECDF

np.random.seed(42)
    
dataframe = pd.DataFrame({"normal": sct.norm.rvs(20, 4, size=10000),
                     "binomial": sct.binom.rvs(100, 0.2, size=10000)})

#Questão 1

d = dataframe.quantile([0.25, 0.5, 0.75], axis = 0)
e = (d['normal']-d['binomial']).round(3)
tuple(e)

#Questão 2

inferior = dataframe.normal.mean() - dataframe.normal.std()
superior = dataframe.normal.mean() + dataframe.normal.std()

ecdf = ECDF(dataframe.normal)

np.float(round(ecdf(superior) - ecdf(inferior), 3))

#Questão 3

m_binom = dataframe.binomial.mean()
m_norm = dataframe.normal.mean()
v_binom = dataframe.binomial.var()
v_norm = dataframe.normal.var()

m = round(m_binom - m_norm, 3) 
v = round(v_binom - v_norm, 3)

x = [m, v]
tuple(x)

#Parte 2
#Questão 4

stars = pd.read_csv("pulsar_stars.csv")

stars.rename({old_name: new_name
              for (old_name, new_name)
              in zip(stars.columns,
                     ["mean_profile", "sd_profile", "kurt_profile", "skew_profile", "mean_curve", "sd_curve", "kurt_curve", "skew_curve", "target"])
             },
             axis=1, inplace=True)

stars.loc[:, "target"] = stars.target.astype(bool)

stars.head()


false_pulsar_mean_profile = stars.loc[stars['target'] == False, ['mean_profile']]

def standardization(x):
    return (x - x.mean()) / x.std()

false_pulsar_mean_profile_standardized = standardization(false_pulsar_mean_profile)

ecdf = ECDF(false_pulsar_mean_profile_standardized)
    
ppf = pd.Series(ecdf(sct.norm.ppf([0.80, 0.90, 0.95])), [0.80, 0.90, 0.95])


