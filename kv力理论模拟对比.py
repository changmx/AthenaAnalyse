import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

n = 1.04e11
e = 1.602176565e-19
epsilon0 = 8.854187817e-12
sigma = 0.000218
rmssigma = sigma/2
pi = math.pi

Ngrid = 256
gridLen = 2e-5          ##########################
stride = 1e-6

fScale = 1e-13
figYscale = -13

direction = "y"
type = "kv"

x = []
y = []

for r in np.arange(0, (Ngrid / 2) * gridLen, stride):
    if (r % gridLen) != 0:
        if r < sigma:
            E = n * e * r / (2 * pi * epsilon0 * sigma * sigma)
            F = 2 * e * E
            x.append(r / rmssigma)
            y.append(F / fScale)
        else:
            E = n * e / (2 * pi * epsilon0 * r)
            F = 2 * e * E
            x.append(r / rmssigma)
            y.append(F / fScale)

fig, ax = plt.subplots()
ax.plot(x, y, label="理论值")

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# plt.rcParams['savefig.dpi'] = 600       #image pixel
# plt.rcParams['figure.dpi'] = 600        #image resolution
# plt.figure(figsize=(18,6))
figXlable = '径向距离$(r/ {\\sigma_{RMS}})$'
figYlable = '束束力$(\\times 10^{a}N)$'.format(a=figYscale)
figTitle = '{Ftype}分布,{Fdirection}方向,网格(${Fgrid}\\times$'.format(Ftype=type, Fdirection=direction, Fgrid=Ngrid)
ax.set(xlabel=figXlable, ylabel=figYlable,
       title=figTitle + '$2\\times 10^{-5}m)$,束束力理论值与模拟值对比')        ############
ax.grid()

# file_path1 = r'D:\bb2019\beamforce\kv10000turn0.txt'
# X1, Y1 = np.loadtxt(file_path1, delimiter=',', usecols=(0, 1), unpack=True)
# ax.plot(X1 / rmssigma, Y1 / fScale, label="$1\\times 10^{4}$个宏粒子模拟值")

file_path2 = r'D:\bb2019\beamforce\kv100000turn0.txt'
X2, Y2 = np.loadtxt(file_path2, delimiter=',', usecols=(0, 1), unpack=True)
ax.plot(X2 / rmssigma, Y2 / fScale, label="$1\\times 10^{5}$个宏粒子模拟值")

# file_path3 = r'D:\bb2019\beamforce\kv1000000turn0.txt'
# X3, Y3 = np.loadtxt(file_path3, delimiter=',', usecols=(0, 1), unpack=True)
# ax.plot(X3 / rmssigma, Y3 / fScale, label="$1\\times 10^{6}$个宏粒子模拟值")
name = "D:\\bb2019\\beamforce\\plot1024\\" + type + direction + str(Ngrid) + '长度' + str(gridLen) + ".png"
# name = "D:\\bb2019\\beamforce\\test.eps"

ax.legend()
fig.savefig(name)
plt.show()
plt.close()