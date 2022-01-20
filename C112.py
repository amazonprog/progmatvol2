# Spyder (Python) - Code C112
#  X ~ Bin(n, p)
from scipy.stats import binom 
n = 10
p = 0.5
x_valores = list(range(n + 1)) 
dist = [binom.pmf(x, n, p) for x in x_valores] 
print("x\tP(X=x)") 
for i in range(n + 1): 
    print(str(x_valores[i]) + "\t" + str(dist[i])) 
print("Valor Esperado =", binom.mean(n=10,p=.5))
print("Variância =", binom.var(n=10,p=.5))