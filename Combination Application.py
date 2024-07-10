import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm as cm

x=np.linspace(0.5,3.5,100)
y=np.sin(x)
y1=np.random.randn(100)
plt.scatter(x,y1,c='0.25',label='scatter figure')
plt.plot(x,y,ls='--',lw=2,label='plot figure')
for spine in plt.gca
