import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()
#sigma_s = np.linspace(0.01,0.5,0.01)

bunch1 = 50
bunch2 = 50
freq = 10**6

Nparticle = np.linspace(10**9,10**10,10**9)

emittence_x = 0.001
beta_x = 0.1
sigma_x = (emittence_x*beta_x)**0.05

emittence_y = 0.001
beta_y = 0.1
sigma_y = (emittence_y*beta_y)**0.05
Lum = bunch1 * bunch2 * freq * Nparticle/(4*np.pi*sigma_x *sigma_y)
plt.plot(Nparticle,Lum)
plt.show()