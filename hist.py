import matplotlib as mpl

mpl.rcParams['font.sans-serif']=['Songti SC']
mpl.rcParams['axes.unicode_minus']=False

import matplotlib.pyplot as plt
import numpy as np

boxWeight=np.random.randint(0,10,100)

x=boxWeight

bins=range(0,11,1)

plt.hist(x,bins=bins,color='g',histtype='bar',rwidth=1,alpha=0.6)

plt.xlabel("箱子重量(kg)")
plt.ylabel("销售数量(个)")

plt.show()
