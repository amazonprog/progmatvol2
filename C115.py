# Spyder (Python) - Code C115
# X ∼ Geo(p)
import matplotlib.pyplot as plt
from scipy.stats import geom
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p = 0.5
geom_pd = geom.pmf(X, p)
plt.bar(X, geom_pd, width=0.5, color=['black', 'black'])
plt.ylabel("Probabilidade", fontsize="12")
plt.xlabel("X (Número de lançamentos)", fontsize="12")
plt.show()
#plt.savefig('Fig-1.6.png')