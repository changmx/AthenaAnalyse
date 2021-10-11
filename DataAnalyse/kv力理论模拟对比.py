import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

n = 1.7e11
e = 1.602176565e-19
epsilon0 = 8.854187817e-12
beta_x = 0.06
beta_y = 0.06
emit_x = 6e-8
emit_y = 6e-8
sigmax = math.sqrt(beta_x * emit_x)
sigmay = math.sqrt(beta_y * emit_y)
rmssigma = np.sqrt(sigmax**2)
sigma = rmssigma*2
pi = math.pi

Ngrid = 256
gridLen = 2e-5
stride = 1e-6

fScale = 1e-13
figYscale = -13

direction = "x"

type = "kv"
myfontsize = 20
x = []
y = []

for r_x in np.arange(-(Ngrid / 2) * gridLen, (Ngrid / 2) * gridLen, stride):
    r_y = 0
    if (r_x % gridLen) != 0:
        r = (r_x*r_x+r_y*r_y)**0.5*r_x/abs(r_x)
        if r < sigma and r > -sigma:
            E = n * e * r / (2 * pi * epsilon0 * sigma * sigma)
            F = -e * E
            x.append(r / rmssigma)
            y.append(F / fScale)
        else:
            E = n * e / (2 * pi * epsilon0 * r)
            F = -e * E
            x.append(r / rmssigma)
            y.append(F / fScale)

fig, ax = plt.subplots()
ax.plot(x, y, label="Theoretical value")

figXlable = 'Distance $(r/ {\sigma})$'
figYlable = r'Electric field force $(\times 10^{{{0}}}N)$'.format(figYscale)
ax.set_xlabel(figXlable, fontsize=myfontsize)
ax.set_ylabel(figYlable, fontsize=myfontsize)
plt.tick_params(labelsize=myfontsize)
ax.grid()

# file_path = r'D:\bb2021\electricForce\2021_1008\1124_18\1124_18_proton_10000_x.csv'
# file_path2 = r'D:\bb2021\electricForce\2021_1008\1124_38\1124_38_proton_100000_x.csv'
# file_path3 = r'D:\bb2021\electricForce\2021_1008\1125_42\1125_42_proton_1000000_x.csv'
file_path = r'D:\bb2021\electricForce\2021_1008\1131_14\1131_14_proton_10000_x.csv'
file_path2 = r'D:\bb2021\electricForce\2021_1008\1130_43\1130_43_proton_100000_x.csv'
file_path3 = r'D:\bb2021\electricForce\2021_1008\1129_31\1129_31_proton_1000000_x.csv'

X, Y = np.loadtxt(file_path, delimiter=',', usecols=(0, 1), unpack=True)
X2, Y2 = np.loadtxt(file_path2, delimiter=',', usecols=(0, 1), unpack=True)
X3, Y3 = np.loadtxt(file_path3, delimiter=',', usecols=(0, 1), unpack=True)

ax.plot(X / rmssigma, Y / fScale, label=r'$1\times 10^{4}$ macro particles')
ax.plot(X2 / rmssigma, Y2 / fScale, label=r'$1\times 10^{5}$ macro particles')
ax.plot(X3 / rmssigma, Y3 / fScale, label=r'$1\times 10^{6}$ macro particles')

name = "E:\\changmx\\bb2019\\electricForce\\" + type + \
    direction + str(Ngrid) + '长度' + str(gridLen) + "1.png"

# ax.set_xlim([0, 3])
# ax.set_ylim([-7, 1])
ax.set_xlim([6, 6.2])
ax.set_ylim([-2.2, -2.1])

ax.legend(fontsize=myfontsize)
# fig.savefig(name)
plt.show()
plt.close()
