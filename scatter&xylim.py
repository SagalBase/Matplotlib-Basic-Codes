import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0.05, 10, 1000)
y=np.random.rand(1000)
plt.scatter(x,y,label='scatter figures', c='red')
plt.legend()
plt.xlim(0.05, 10)
plt.ylim(0.01,1)
plt.show()