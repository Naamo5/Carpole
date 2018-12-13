import numpy as np
import matplotlib.pyplot as plt


q05  = open('scores001.data', 'r')
q09  = open('scores0005.data', 'r')
q095  = open('scores0001.data', 'r')
q099  = open('scores00005.data', 'r')

Q = [q05, q09, q095, q099]


Q_arr = [[], [], [],[]]

i=0
for q in Q:
    for line in q:
        nbr = line.split('\n')
        Q_arr[i].append(float(nbr[0]))
    q.close()
    i+=1


episode = np.arange(1,1001,1)


fig = plt.figure()
for i in range(4):
        plt.plot(np.arange(1,len(Q_arr[i])+1), Q_arr[i], lw=0.4)
plt.xlabel("Episodes")
plt.ylabel("Average Q Value")
plt.legend([r'$\alpha = 0.01$',r'$\alpha = 0.005$',r'$\alpha = 0.001$',r'$\alpha = 0.0005$'])
ax = fig.gca()
#ax.set_xticks(np.arange(0, 110, 10))
#ax.set_yticks(np.arange(0, 2, 20))
plt.grid(True)
plt.savefig('alpha_score.eps')
plt.show()
