# Spyder (Python) - Code C111 
#  X ~ Bernoulli(p)
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
def pmf(x,p):
    f = p**x*(1-p)**(1-x)
    return f
X = [0,1]
p = 0.5
plt.bar(X, bernoulli.pmf(X, p), width=0.1, color=['black', 'black'])
plt.xlabel('Valores de X → {0, 1}')
plt.ylabel('Probabilidade')
plt.show()
#plt.savefig('Fig-1.1.png')
mean= bernoulli.stats(p, moments = 'mvsk')
var = bernoulli.stats(p, moments = 'mvsk')
print("Valor Esperado =", mean)
print("Variância =", var)