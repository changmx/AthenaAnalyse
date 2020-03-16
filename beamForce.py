import numpy as np
from matplotlib import pyplot as plt

file = open("D:\\bb2019\\beamforce\\gaussTheory.txt", "w")

Len = 6.4e-4
x = np.linspace(-Len,Len,128)

n = 1.04e11
e = 1.602176565e-19
beta = 1
epsilon = 8.854187817e-12
sigma = 1.095445115e-4*3
pi = 3.1415926535

y = n*e*e*(1+beta*beta)/(2*pi*epsilon)*(1/x)*(1-np.exp(-x*x/(2*sigma*sigma)))

# for index in range(len(x)):
#     file.write(x[index])
#     file.write(",")
#     file.write(y[index])
#     file.write('\n')

file.close()

plt.figure(1)
plt.xlabel("x")
plt.ylabel("y")
plt.title(r"$F(x) = (1+x)e^{1-x}$")
plt.plot(x,y)
plt.savefig('beamForce.png',dpi = 300)
plt.show()