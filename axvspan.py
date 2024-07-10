import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0.05,10,1000)
y=np.sin(x)

plt.plot(x,y,c='c',lw=2,ls='-.',label='plot figures')
plt.legend()

plt.axvspan(xmin=4,xmax=6,facecolor='y',alpha=0.2)
plt.axhspan(ymin=0.2,ymax=0.6,facecolor='y',alpha=0.2)

plt.show()