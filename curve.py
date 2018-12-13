import numpy as np
import matplotlib.pyplot as plt


q05  = open('max_q_mean05.data', 'r')
q09  = open('max_q_mean09.data', 'r')
q095  = open('max_q_mean095.data', 'r')
q099  = open('max_q_mean099.data', 'r')
#q0999  = open('max_q_mean0999.data', 'r')

Q = [q05, q09, q095, q099]#, q0999]
Q_arr = [[],[],[],[]]#,[]]

i=0
for q in Q:
    for line in q:
        line.append(q[i])
    q.close()
    i+=1


node = np.arange(1,101,5)

fig = plt.figure()
plt.plot(node, score)
plt.xlabel('Number of neurones')
plt.ylabel(u'Average score')
ax = fig.gca()
ax.set_xticks(np.arange(0, 110, 10))
ax.set_yticks(np.arange(0, 200, 20))
plt.grid(True)
plt.savefig('number_neurones.eps')
plt.show()
