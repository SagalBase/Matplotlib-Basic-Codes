import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0.05,10,1000)
y=np.sin(x)

plt.plot(x,y,ls='-.',lw=2,label='plot figures')
plt.legend()
plt.xlabel='x-axis'
plt.ylabel='y-axis'
plt.grid(ls=':',c='r')
plt.text(3.10,0.09,"y=sin(x)",weight="bold",color='b')
plt.show()