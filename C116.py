# Spyder (Python) - Code C116
# X ~ Poi(x; λ) 
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
Probabilidade=poisson.pmf(3, 2)
print('Probabilidade do Evento=', Probabilidade)
lambd=2
k_axis = np.arange(0, 10)
distribution = np.zeros(k_axis.shape[0])
for i in range(k_axis.shape[0]):
    distribution[i] = poisson.pmf(i, lambd)
plt.bar(k_axis, distribution, color='black')
plt.ylabel("Probabilidade", fontsize="12")
plt.xlabel("X (Número de Eventos)", fontsize="12")
#plt.savefig('Fig-1.7.png')