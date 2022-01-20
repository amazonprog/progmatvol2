# Spyder (Python) - Code C147 
#  Estimador MLE
import pandas as pd
names = ['A', 'F', 'N']
data = pd.read_csv('AFN.csv', names = names)
data.head()
print(data.head(15))
from pgmpy.models import BayesianModel
model=BayesianModel([('A','N'),('F','N')])  
from pgmpy.estimators import ParameterEstimator
ParameterEstimator(model, data)
from pgmpy.estimators import MaximumLikelihoodEstimator
mle = MaximumLikelihoodEstimator(model, data)
# Calibragem das CDPs com uso de MLE
model.fit(data, estimator=MaximumLikelihoodEstimator)
print('MLE estimator', mle.estimate_cpd('N'))
