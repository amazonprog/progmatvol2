# Spyder (Python) - Code C144-1 
#  Grafo da estrutura em C144 
from matplotlib import pyplot as plt
from pgmpy.models import BayesianNetwork
import networkx as nx
model = BayesianNetwork([('N', 'D'), ('N', 'B'), ('F', 'D'), 
                       ('F', 'B'), ('F', 'N'), ('C', 'D'), 
                       ('C', 'B'), ('C', 'N'), ('C', 'F'), 
                       ('B', 'D'), ('A', 'D'), ('A', 'B'), 
                       ('A', 'N'), ('A', 'F'), ('A', 'C')])
nx.draw(model, with_labels=True)
plt.show()
#plt.savefig("Fig-4.11.png")

