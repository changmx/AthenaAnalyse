import numpy as np
import matplotlib.pyplot as plt
import math

damp = 5000
val = 100
x = np.linspace(0,10000,10000)
y1 = val*np.exp(-x/1000)
y2 = val*np.exp(-x/2000)
y3 = val*np.exp(-x/3000)
y4 = val*np.exp(-x/4000)
y5 = val*np.exp(-x/5000)
y6 = val*np.exp(-x/6000)

fig,ax=plt.subplots(1,1)

ax.plot(x,y1,label='1000')
ax.plot(x,y2,label='2000')
ax.plot(x,y3,label='3000')
ax.plot(x,y4,label='4000')
ax.plot(x,y5,label='5000')
ax.plot(x,y6,label='6000')
ax.plot(x,val*np.exp(-1)+x*0)

plt.legend()
plt.show()