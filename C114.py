# Spyder (Python) - Code C114
# X ∼ Geo(p)
import matplotlib.pyplot as plt
def probabilidade(lance, prob):
    return (1-p)**(lance - 1) * prob
p = 0.5
lance = 3
escala_de_tentavivas = range(16)[1:]
print('Exatamente em', lance, '=', probabilidade(lance, p))
plt.xlabel('X-tentativas')
plt.ylabel('probabilidade')
barlist = plt.bar(escala_de_tentavivas, color=['black'], height=[probabilidade(x, p)
for x in escala_de_tentavivas], tick_label=escala_de_tentavivas)
barlist[lance].set_color('yellow')
#plt.savefig('Fig-1.5.png')
plt.show()
def probabilidade_antes_de(lance, prob):
    return 1 - (1 - prob)**(lance - 1)
print("Antes de", lance,'=', probabilidade_antes_de(lance, p))