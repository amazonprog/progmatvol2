# Spyder (Python) - Code C144 
#  Estimador PC
import pandas as pd
names = ['A', 'B', 'C', 'D', 'E',
         'F', 'G', 'H', 'I', 'J', 
         'K', 'L', 'M', 'N']
data = pd.read_csv('heart.csv', names = names)
data.head()
data.isnull().sum()
# deletar custos comp não binários
del data['E']
del data['G']
del data['H']
del data['I']
del data['J']
del data['K']
del data['L']
del data['M']
# mudar faixa de valores de idade
data.loc[data['A']<= 40,'A'] = 0
data.loc[data['A']> 40, 'A'] = 1
# mudar faixa de D (1 = alta, 0 = baixa
data.loc[data['D']<= 120,'D'] = 0
data.loc[data['D']> 120, 'D'] = 1
# mudar faixa de doença cardiaca (1 = sim, 0 = não)
data.loc[(data['N']<=4) & (data['N']>1),'N'] = 1
print(data.head(20))
# construir a rede
from pgmpy.estimators import PC
est = PC(data)
modelo = est.estimate(significance_level=1)
print("Trilhas: ", modelo.edges())