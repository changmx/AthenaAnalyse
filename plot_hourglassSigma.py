import numpy as np 
import matplotlib.pyplot as plt 

fig,ax = plt.subplots()

sigmaxS = []
sigmayS = []
s = []
# emitx = 3e-7
# emity = 18e-9
betax = 0.2
betay = 0.06
# sigmax = np.sqrt(betax*emitx)
# sigmay = np.sqrt(betay*emity)
sigmaZ = 0.02

for position in np.linspace(-6*sigmaZ,6*sigmaZ,100):
	sigmaxS.append(np.sqrt(1+position**2/(betax**2)))
	sigmayS.append(np.sqrt(1+position**2/(betay**2)))
	s.append(position/sigmaZ)

ax.plot(s,sigmaxS,label=r'$\sigma_x$')
ax.plot(s,sigmayS,label=r'$\sigma_y$')
ax.set_xlabel(r'$z/\sigma_z$')
ax.grid()
ax.legend()

plt.show()