import numpy as np
import matplotlib.pyplot as plt


score = [9.61999999999999, 103.519999999999,164.56,145.599999999999,
        159.129999999999,141.36,155.96,136.789999999999,166.289999999999,
        143.099999999999,164.4,179.33,152.84,164.389999999999,149.819999999999,
        154.8,156.539999999999,155.09999999999,149.02,161.62]

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
