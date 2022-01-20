# Spyder (Python) - Code C141 
# Estrutura da Rede Bayesiana 
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
# Topologia do modelo.
model =BayesianModel([('A','B'),('B','D'),('C','D')])
# CPDs individuais
cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.5], [0.5]])
cpd_c = TabularCPD(variable='C', variable_card=2, values=[[0.2], [0.8]])
cpd_b = TabularCPD(variable='B', variable_card=2,
                    values=[[0.7, 0.3],
                            [0.3, 0.7]],
                    evidence=['A'],
                    evidence_card=[2])
cpd_d = TabularCPD(variable='D', variable_card=2, 
                   values=[[0.9, 0.9, 0.9, 0],
                           [0.1, 0.1, 0.1, 1]],
                   evidence=['B','C'],
                   evidence_card=[2, 2])
model.add_cpds(cpd_a, cpd_c, cpd_b, cpd_d)
# Integridade da estrutura e das CPDs 
model.check_model()
# Atribuindo ‘sim’-‘não’ estados_sn
cpd_a_sn = TabularCPD(variable='A', variable_card=2, values=[[0.5],[ 0.5]], state_names={'A': ['sim', 'não']})
cpd_c_sn = TabularCPD(variable='C', variable_card=2, values=[[0.2], [0.8]], state_names={'C': ['sim', 'não']})
cpd_b_sn = TabularCPD(variable='B', variable_card=2,
                      values=[[0.7, 0.3],
                            [0.3, 0.7]],
                      evidence=['A'],
                      evidence_card=[2],
                      state_names={'B': ['sim', 'não'],
                                   'A': ['sim', 'não']})
cpd_d_sn=TabularCPD(variable='D', variable_card=2,
                      values=[[0.9, 0.9, 0.9, 0],
                           [0.1, 0.1, 0.1, 1]],                               
                      evidence=['B', 'C'],
                      evidence_card=[2, 2],
                      state_names={'D':['sim', 'não'],
                                   'A': ['sim', 'não'],
                                   'B': ['sim', 'não'],
                                   'C': ['sim', 'não']})
print(model.check_model())
# Adição de CPDs especificando nomes de estados
model.add_cpds(cpd_a_sn,cpd_b_sn,cpd_c_sn,cpd_d_sn)
model.check_model()
model.get_cpds()
print(cpd_a_sn)
print(cpd_b_sn)
print(cpd_c_sn)
print(cpd_d_sn)
print('Independência local verificada na rede: ', model.local_independencies('D'))
a = model.active_trail_nodes('D')
print('Nós ativos na rede: ', a)
#from pgmpy.inference import VariableElimination
#infer = VariableElimination(model)
#conj=infer.query(['C','A','B','D'])
#print(conj)
#print(infer.query(['D']))
#print(infer.query(['A'], evidence={'D':"sim"}))


