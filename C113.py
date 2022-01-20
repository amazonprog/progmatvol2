# Spyder (Python) - Code C113
import numpy as np
import matplotlib.pyplot as plt 
n = int(input("Número de jogadas = "))
p = 0.6
# Entre com o valor de n
Repetições = int(input("Número de repetições = "))
x=np.random.binomial(n=n, p=p, size=Repetições)
# Espaço amostral de x_sucessos
print('Array',x)
# Resultado da soma para cada valor de x_sucesso 
y=[np.equal(x,i).sum() for i in range(n)]
print(y)
# Cálculo da probalidade de x_sucessos/Repetições
probs = [np.equal(x,i).mean() for i in range(n)]
print(probs)
plt.xticks(range(n))
plt.bar(list(range(n)), probs, color='black')
plt.xlabel('x (Números de caras)',fontsize=12)
plt.ylabel('Probabilidade',fontsize=12)
# Figs. 1.2 a 1.4
#plt.savefig('Fig-1.x.png')
