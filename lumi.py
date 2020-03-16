import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

Nbunch = 50
Np = np.linspace(10**7,2*10**8,20)
#Np = 5*10**9
Nd = Np
freq = 10**6

betax = 0.1
betay = 0.1
emitx = 10**(-6)
emity = 10**(-6)
sigmax = (betax*emitx)**0.5
sigmay = (betay*emity)**0.5
sigmas = np.linspace(0.001,0.1,50)

#S = 1/((1+((sigmax/sigmas)*np.tan(0.025))**2)**0.5)*1/((1+((sigmas/sigmax)*np.tan(0.025))**2)**0.5)
L = Np*Nd*freq*Nbunch/(4*np.pi*sigmax*sigmay)
plt.plot(Np,L)
plt.xlabel('particles per bunch')
plt.ylabel('luminosity')
plt.legend()
#fig.savefig('1.jpg')
plt.show()