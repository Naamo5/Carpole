import numpy as np
import matplotlib.pyplot as plt


q05  = open('max_q_mean1.data', 'r')
q2  = open('max_q_mean2.data', 'r')
q5  = open('max_q_mean5.data', 'r')
q09  = open('max_q_mean10.data', 'r')
q095  = open('max_q_mean50.data', 'r')
q099  = open('max_q_mean100.data', 'r')
#q99  = open('max_q_mean25000.data', 'r')
#q999  = open('max_q_mean50000.data', 'r')

Q = [q05,q2, q5, q09, q095, q099]


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
plt.legend([r'$f = 1$',r'$f = 2$',r'$f = 5$',r'$f = 10$', r'$f = 50$',r'$f = 100$'])
ax = fig.gca()
#ax.set_xticks(np.arange(-200, 1000, 100))
#ax.set_yticks(np.arange(0, 2, 20))
plt.grid(True)
plt.savefig('freq5000.eps')
plt.show()
