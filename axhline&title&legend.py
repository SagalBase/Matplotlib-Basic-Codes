import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0.05,10,1000)
y=np.sin(x)

plt.plot(x,y,ls='-.',lw=2,label='plot figures',c='c')
plt.legend(loc='lower left')
plt.axhline(y=0.0,c='r',ls='--',lw=2)
plt.axvline(x=4.0,c='r',ls='--',lw=2)
plt.title("y=sin(x)")
plt.show()