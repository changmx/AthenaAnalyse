import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

n = 1.04e11
e = 1.602176565e-19
epsilon0 = 8.854187817e-12
sigma = 0.000218
rmssigma= sigma/2
pi = math.pi

Ngrid = 256
gridLen = 1e-5
stride = 1e-6
macroNo = 1e5

fScale = 1e-13
figYscale = -13
xScale = 1e-3

direction = "x"
type = "kv"

x = []
yequal = []
yopposite = []

for r in np.arange(-(Ngrid / 2) * gridLen, (Ngrid / 2) * gridLen, stride):
    if (r < sigma and r > -sigma):
        E = n * e * r / (2 * pi * epsilon0 * sigma * sigma)
        F = 2 * e * E
        x.append(r / rmssigma)
        yequal.append(F / fScale)
        yopposite.append(-F / fScale)
    else:
        E = n * e / (2 * pi * epsilon0 * r)
        F = 2 * e * E
        x.append(r / rmssigma)
        yequal.append(F / fScale)
        yopposite.append(-F / fScale)


fig, ax = plt.subplots()
ax.plot(x, yequal, label="电性相同")
ax.plot(x, yopposite, label="电性相反")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# plt.rcParams['savefig.dpi'] = 600       #image pixel
# plt.rcParams['figure.dpi'] = 600        #image resolution
# plt.figure(figsize=(18,6))
figXlable = '径向距离$(x/ {\\sigma_{RMS}})$'
figYlable = '束束力$(\\times 10^{a}N)$'.format(a=figYscale)
figTitle = 'kv分布束束相互作用力'
ax.set(xlabel=figXlable, ylabel=figYlable,
       title=figTitle)
ax.grid()
plt.xticks(np.arange(-10,11,2))
ax.legend()
name = "D:\\bb2019\\beamforce\\kvtheory.png"

fig.savefig(name)
plt.show()
plt.close()
