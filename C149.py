# Spyder (Python) - Code C147 
#  Rede Completa
import pandas as pd
names = ['A', 'B', 'C', 'D', 'E',
         'F', 'G', 'H', 'I', 'J', 
         'K', 'L', 'M', 'N']
data = pd.read_csv('heart.csv', names = names)
data.head()
#print(data.head())
#print("Colunas nulas :", data.isnull().sum())
#data = data.replace('?', np.nan)
data.dtypes
#verificar colunas
#print(data.columns)
# informar dataframes
#print(data.info())
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
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import BayesianEstimator
modelo = BayesianNetwork ([('N', 'D'), ('N', 'B'),
                           ('F', 'D'), ('F', 'B'),
                           ('F', 'N'), ('C', 'D'), 
                           ('C', 'B'), ('C', 'N'), 
                           ('C', 'F'), ('B', 'D'), 
                           ('A', 'D'), ('A', 'B'), 
                           ('A', 'N'), ('A', 'F'), 
                           ('A', 'C')])
# aprendizagem de CPDs com BDeu
modelo.fit(data, estimator=BayesianEstimator, prior_type="BDeu")
# iterar tabelas de probab
#for cpd in modelo.get_cpds():
    #print(cpd)
#print("Independencias :",modelo.get_independencies())
# Inferência exata (Variable Elimination)
from pgmpy.inference import VariableElimination
infer = VariableElimination(modelo)
print('Sem evidência:', infer.query(variables=['N']))
print('Com evidência:', infer.query(variables=['N'], evidence={'D': 1, 'A': 0}))
