# Spyder (Python) - Code C117
# X ~ Poi(x; λ) 
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
f, axes = plt.subplots(5, figsize=(6, 8), sharex=True)
for lambd in range(1, 6):
    k_axis = np.arange(0, 15)
    distribution = np.zeros(k_axis.shape[0])
    for i in range(k_axis.shape[0]):
        distribution[i] = poisson.pmf(i, lambd)
    axes[lambd-1].bar(k_axis, distribution, color='black')
    axes[lambd-1].set_xticks(np.arange(0, 15, 2))
    axes[lambd-1].set_title(f"$\lambda$ = {lambd}") 
    axes[lambd-1].set_ylabel("Probabilidade", fontsize="12")
plt.subplots_adjust(hspace=0.5)
plt.xlabel("X (Número de Eventos)", fontsize="12")   
#plt.savefig('Fig-1.8.png')