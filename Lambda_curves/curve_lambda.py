import numpy as np
import matplotlib.pyplot as plt


q05  = open('max_q_mean05.data', 'r')
q09  = open('max_q_mean09.data', 'r')
q095  = open('max_q_mean095.data', 'r')
q099  = open('max_q_mean099.data', 'r')
q0999  = open('max_q_mean0999.data', 'r')

Q = [q05, q09, q095, q099, q0999]

def rat(lambd):
    return (1-np.power(lambd,200))/(1-lambd)
ratio = [rat(0.5), rat(0.9), rat(0.95), rat(0.99), rat(0.999)]
Q_arr = [[], [], [],[],[]]

i=0
for q in Q:
    for line in q:
        nbr = line.split('\n')
        Q_arr[i].append(float(nbr[0])/ratio[i])
    q.close()
    i+=1


episode = np.arange(1,1001,1)


fig = plt.figure()
for i in range(5):
    plt.plot(episode, Q_arr[i])
plt.xlabel("Episodes")
plt.ylabel("Average Q Value")
plt.legend([r'$\lambda = 0.5$',r'$\lambda = 0.9$',r'$\lambda = 0.95$',r'$\lambda = 0.99$',r'$\lambda = 0.999$'])
ax = fig.gca()
#ax.set_xticks(np.arange(0, 110, 10))
#ax.set_yticks(np.arange(0, 2, 20))
plt.grid(True)
plt.savefig('lambda.eps')
plt.show()
