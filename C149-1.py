"""
HEART-DISEASE DATASET

https://www.youtube.com/watch?v=Jk4-POycbR8

https://www.youtube.com/watch?v=sCqpWCYaL5U&t=216s
PC estimator

"""
import pandas as pd
data = pd.read_csv('heart.csv')
finalData = data.rename(columns={'age':'A','sex':'B', 'cp':'C','trestbps':'D','chol':'E','fbs':'F','restecg':'G','thalach':'H','exang':'I','oldpeak':'J','slope':'K', 'ca':'L','thal':'M','target':'N'})                     
# 5 primeiras linhas

del finalData['J']
del finalData['K']
del finalData['I']
del finalData['L']
del finalData['M']


df = pd.DataFrame(finalData.head())
df.loc[df['A'] < 39,'A'] = 0
df.loc[(df['A']>40) & (df['A']< 60),'A'] = 1
df.loc[df['A']>60, 'A'] = 2
print(df.head(20))
from pgmpy.estimators import PC
est = PC(data=df)
# modelo estimado
modelo_est = est.estimate(significance_level=5)
# exibir tuplas causais
print("Trilhas: ", modelo_est.edges())
from pgmpy.models import BayesianModel
# criar a estrutura para o modelo Bayesiano
modelo = BayesianModel(modelo_est)
# criar tabelas de probab com dados ajustados
modelo.fit(df)
# iterar tabelas de probab
print(modelo.get_cpds())
# usar o modelo em inferências com VE
from pgmpy.inference import VariableElimination
infer = VariableElimination(modelo)
print(infer.query(variables=['N']))
dist=infer.query(variables=["N"], evidence={"A":1})
print(dist)
