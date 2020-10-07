import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

n = 1.0e11
e = 1.602176565e-19
epsilon0 = 8.854187817e-12
sigma = 2.19e-4
rmssigma = sigma/2
pi = math.pi

Ngrid = 256
gridLen = 1e-5          ##########################
stride = 1e-6

fScale = 1e-13
figYscale = -13

direction = "45°"
type = "gaussian"

x = []
y = []

for r_x in np.arange(-(Ngrid / 2) * gridLen, (Ngrid / 2) * gridLen, stride):
    r_y = r_x
    r = (r_x*r_x+r_y*r_y)**0.5*r_x/abs(r_x)
    F = n*e*e/(2*pi*epsilon0*r)*(1-math.exp(-r*r/(2*rmssigma*rmssigma)))
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
       title=figTitle + '$1\\times 10^{-5}m)$,束束力理论值与模拟值对比')        ############
ax.grid()

file_path2 = r'E:\changmx\bb2019\electricForce\2020_0818_gaussian_proton\2057\proton_10000.csv'
X2, Y2 = np.loadtxt(file_path2, delimiter=',', usecols=(0, 1), unpack=True)
ax.plot(X2 / rmssigma, Y2 / fScale, label="$1\\times 10^{5}$个宏粒子模拟值")

name = "E:\\changmx\\bb2019\electricForce\\" + type + direction + str(Ngrid) + '长度' + str(gridLen) + "1.png"

ax.legend()
fig.savefig(name)
plt.show()
plt.close()