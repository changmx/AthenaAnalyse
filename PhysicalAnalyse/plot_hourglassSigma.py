import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

sigmaxS = []
sigmayS = []
s = []

name = 'EicC electron'
betax = 0.2
betay = 0.06
sigmaZ = 0.02

name = 'EicC proton'
betax = 0.04
betay = 0.02
sigmaZ = 0.04

name = 'KEKB'
betax = 0.33
betay = 0.01
sigmaZ = 0.004

for position in np.linspace(-6 * sigmaZ, 6 * sigmaZ, 100):
    sigmaxS.append(np.sqrt(1 + position**2 / (betax**2)))
    sigmayS.append(np.sqrt(1 + position**2 / (betay**2)))
    s.append(position / sigmaZ)

ax.plot(s, sigmaxS, label=r'$\sigma_x$')
ax.plot(s, sigmayS, label=r'$\sigma_y$')
ax.set_xlabel(r'$z/\sigma_z$')
ax.set_ylabel(r'$\sigma/\sigma_0$')
ax.set_title(name)
ax.grid()
ax.legend()

plt.show()