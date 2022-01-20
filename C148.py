# Spyder (Python) - Code C148 
#  Estimador Bayesiano BDeu
import pandas as pd
names = ['A', 'F', 'N']
data = pd.read_csv('AFN.csv', names = names)
data.head()
print(data.head(15))
from pgmpy.models import BayesianModel
model=BayesianModel([('A','N'),('F','N')])  
from pgmpy.estimators import ParameterEstimator
ParameterEstimator(model, data)
from pgmpy.estimators import BayesianEstimator
est = BayesianEstimator(model, data)
print('BDeu:', est.estimate_cpd('N', prior_type='BDeu', equivalent_sample_size=15))
