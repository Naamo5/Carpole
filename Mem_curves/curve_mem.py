import numpy as np
import matplotlib.pyplot as plt


q05  = open('max_q_mean500.data', 'r')
q09  = open('max_q_mean1000.data', 'r')
q095  = open('max_q_mean5000.data', 'r')
q099  = open('max_q_mean10000.data', 'r')
q99  = open('max_q_mean25000.data', 'r')
q999  = open('max_q_mean50000.data', 'r')

Q = [q05, q09, q095, q099,q99, q999]


Q_arr = [[], [], [],[],[],[]]

i=0
for q in Q:
    for line in q:
        nbr = line.split('\n')
        Q_arr[i].append(float(nbr[0]))
    q.close()
    i+=1


episode = np.arange(1,1001,1)


fig = plt.figure()
for i in range(6):
        plt.plot(np.arange(1,len(Q_arr[i])+1), Q_arr[i])
plt.xlabel("Episodes")
plt.ylabel("Average Q Value")
plt.legend([r'${\cal M}_{size} = 500$',r'${\cal M}_{size} = 1000$',
r'${\cal M}_{size} = 5000$',r'${\cal M}_{size} = 10000$',r'${\cal M}_{size} = 25000$',r'${\cal M}_{size} = 50000$'])
ax = fig.gca()
ax.set_xticks(np.arange(-200, 1000, 100))
#ax.set_yticks(np.arange(0, 2, 20))
plt.grid(True)
plt.savefig('alpha_score.eps')
plt.show()
