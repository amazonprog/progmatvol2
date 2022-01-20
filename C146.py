# Spyder (Python) - Code C146 
# Atributos A, F e N com 15 linhas
import pandas as pd
names = ['A', 'F', 'N']
data = pd.read_csv('AFN.csv', names = names)
data.head()
print(data.head(15))
