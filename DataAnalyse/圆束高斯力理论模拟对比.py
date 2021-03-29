import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

n = 1.25e11
e = 1.602176565e-19
epsilon0 = 8.854187817e-12
beta_x = 0.06
emit_x = 6e-8
sigma = math.sqrt(beta_x*emit_x)
pi = math.pi

Ngrid = 128
gridLenX = 2.5e-5
gridLenY = 2.5e-5
stride = 1e-6

fScale = 1e-13
figYscale = -13

direction = "x"
file_path2 = r'E:\changmx\bb2021\electricForce\2021_0224_gaussian_proton\1726_20_proton_50000_x.csv' # poisson
file_path3 = r'E:\changmx\bb2021\electricForce\2021_0224_gaussian_proton\1729_36_proton_50000_x.csv' # fft
type = "gaussian"

x = []
y = []

if direction=="x":
	for r_x in np.arange(-(Ngrid / 2) * gridLenX, (Ngrid / 2) * gridLenX, stride):
		r_y = 0
		r = np.sqrt(r_y**2+r_x**2)
		F = -n*e*e/(2*pi*epsilon0)*(r_x/(r*r))*(1-math.exp(-r*r/(2*sigma*sigma)))
		# print(r,F)
		x.append(r_x / sigma )
		y.append(F / fScale)
    	

    	
elif direction=="y":
	for r_y in np.arange(-(Ngrid / 2) * gridLenY, (Ngrid / 2) * gridLenY, stride):
		r_x = 0
		r = (r_x*r_x+r_y*r_y)**0.5*r_y/abs(r_y)
		F = -n*e*e/(2*pi*epsilon0*r)*(1-math.exp(-r*r/(2*sigma*sigma)))
		x.append(r / sigma)
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

X2, Y2 = np.loadtxt(file_path2, delimiter=',', usecols=(0, 1), unpack=True)
ax.plot(X2 / sigma, Y2 / fScale, label="$5\\times 10^{4}$个宏粒子模拟值")
X3, Y3 = np.loadtxt(file_path3, delimiter=',', usecols=(0, 1), unpack=True)
ax.plot(X3 / sigma, Y3 / fScale, label="$fft 5\\times 10^{4}$个宏粒子模拟值")

# name = "E:\\changmx\\bb2019\electricForce\\" + type + direction + str(Ngrid) + '长度' + str(gridLen) + "1.png"

ax.legend()
# fig.savefig(name)
plt.show()
plt.close()