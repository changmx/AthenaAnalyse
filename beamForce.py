import numpy as np
from matplotlib import pyplot as plt
import math

filePath = r'E:\changmx\bb2019\distribution\2020_1117\1647_electron_turn400_bunch0_50000.csv'
x1,px1,y1,py1= np.loadtxt(filePath, delimiter=',', skiprows=1, usecols=(0, 1, 2, 3), unpack=True)

Len = 2.5e-5/2*128
x=np.linspace(-Len,Len,128)
Ek =3.5e9

me = 0.510998950e6
mp = 938.27208816e6
re = 2.8179403262e-15
rp = re*me/mp
n = 1.04e11
e = 1.602176565e-19

gamma_v = Ek/me + 1
beta = math.sqrt(1-(1/gamma_v)**2)
epsilon = 8.854187817e-12
sigma = math.sqrt(3.0e-7*0.04)
pi = 3.1415926535
d = sigma*5
y = n*e*e*(1+beta*beta)/(2*pi*epsilon)*(x/(x**2))*(1-np.exp(-(x**2)/(2*sigma*sigma)))
dy = n*e*e*(1+beta*beta)/(2*pi*epsilon)*(-1/(x*x)*(1-np.exp(-(x*x)/(2*sigma*sigma)))+np.exp(-(x*x)/(2*sigma*sigma))/(sigma*sigma))
dp = -2*n*re/gamma_v*((x+d)/((x+d)**2))*(1-np.exp(-((x+d)**2)/(2*sigma*sigma)))

plt.figure(1)
plt.xlabel("x")
plt.ylabel("y")
# plt.title(r"$F(x) = (1+x)e^{1-x}$")
# plt.plot(x,y)
# plt.scatter(y1,py1,s=2,color='r')
# plt.plot(x,dp)
plt.plot(x,dy)
# plt.plot(x,dy*0)
# plt.savefig('beamForce.png',dpi = 300)
plt.grid()
plt.show()