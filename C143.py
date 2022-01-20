# Spyder (Python) - Code C143 
# HillClimbSearch
import pandas as pd
names = ['A', 'B', 'C', 'D', 'E',
         'F', 'G', 'H', 'I', 'J', 
         'K', 'L', 'M', 'N']
data = pd.read_csv('heart.csv', names = names)
data.head()
data.isnull().sum()
# deletar custos comp
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
# construir a rede
from pgmpy.estimators import HillClimbSearch, BicScore
est = HillClimbSearch(data, BicScore(data)) 
modelo = est.estimate()
print(modelo.nodes())
print("Trilhas: ", modelo.edges())
