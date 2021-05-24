import numpy as np
import matplotlib.pyplot as plt

nu = np.arange(0, np.pi, 0.01)
xi = (2 * np.cos(nu) - 1) / (4 * np.pi * np.sin(nu))
xi_2 = 1 / (np.pi * 2 * np.tan(nu / 2))

fig, ax = plt.subplots()
ax.plot(nu / (2 * np.pi), xi, label='1')
ax.plot(nu / (2 * np.pi), xi_2, label='2')
ax.set_ylim(-0.5, 0.5)
ax.grid()
ax.legend()
plt.show()