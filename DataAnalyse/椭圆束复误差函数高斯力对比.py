import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import special
import scipy
import os

e = 1.602176565e-19
epsilon0 = 8.854187817e-12
n = 1.7e11
beta_x = 0.2
beta_y = 0.06
emit_x = 6e-8
emit_y = 6e-8
# n = 1.25e11
# beta_x = 0.04
# beta_y = 0.02
# emit_x = 30e-8
# emit_y = 18e-8
sigmax = math.sqrt(beta_x * emit_x)
sigmay = math.sqrt(beta_y * emit_y)
print('sigmax = %e, sigmay = %e' % (sigmax, sigmay))

NgridX = 256
NgridY = 256
gridLenX = 2e-5
gridLenY = 1e-5
stride = 1e-6

yearMonDay = '2021_1011'
hourMonSec = '0908_14'
particle = 'proton'
Np = '1000000'
direction = 'x'

myfontsize = 20

file_path = os.sep.join([
    'D:\\bb2021\\electricForce', yearMonDay, '1146_57',
    '1146_57' + '_' + particle + '_' + Np + '_' + direction + '.csv'
])
# file_path2 = os.sep.join([
#     'D:\\bb2021\\electricForce', yearMonDay, '1614_37',
#     '1614_37' + '_' + particle + '_' + '50000' + '_' + direction + '.csv'
# ])
file_path3 = os.sep.join([
    'D:\\bb2021\\electricForce', yearMonDay, '1147_51',
    '1147_51' + '_' + particle + '_' + '1000000' + '_' + direction + '.csv'
])
# file_path4 = os.sep.join([
#     'D:\\bb2021\\electricForce', yearMonDay, '1619_03',
#     '1619_03' + '_' + particle + '_' + '500000' + '_' + direction + '.csv'
# ])
file_path5 = os.sep.join([
    'D:\\bb2021\\electricForce', yearMonDay, '1148_50',
    '1148_50' + '_' + particle + '_' + '1000000' + '_' + direction + '.csv'
])
fScale = 1e-13
figYscale = -13

x = []
y = []


def w(x, y):
    z = x + 1j * y
    a = np.exp(-z * z) * (1 - special.erf(-1j * z))
    return a


def gaussianField(x, y, sigmax, sigmay, n, direction):
    e = 1.602176565e-19
    epsilon0 = 8.854187817e-12
    z = x + 1j * y
    a = z / (np.sqrt(2 * (sigmax * sigmax - sigmay * sigmay)))
    xs = -x * x / (2 * sigmax * sigmax)
    ys = -y * y / (2 * sigmay * sigmay)
    b = np.exp(xs + ys)
    # print(xs,ys,b)
    c = (x * sigmay / sigmax + 1j * y * sigmax / sigmay) / (np.sqrt(
        2 * (sigmax * sigmax - sigmay * sigmay)))

    # print(a.real,a.imag,b.real,b.imag, c.real,c.imag)
    Im = w(a.real, a.imag).imag - (b * w(c.real, c.imag)).imag
    Re = w(a.real, a.imag).real - (b * w(c.real, c.imag)).real
    # print(w(a.real,a.imag).imag,(b*w(c.real,c.imag)).imag)
    # print(w(a.real,a.imag).real,(b*w(c.real,c.imag)).real)
    # print(Im,Re)
    Ex = n * e / (2 * epsilon0 *
                  np.sqrt(2 * scipy.pi *
                          (sigmax * sigmax - sigmay * sigmay))) * Im
    Ey = n * e / (2 * epsilon0 *
                  np.sqrt(2 * scipy.pi *
                          (sigmax * sigmax - sigmay * sigmay))) * Re
    if direction == "x":
        return Ex
    elif direction == "y":
        return Ey


fig, ax = plt.subplots()

if direction == "x":
    # for tmp in np.linspace(-5e-5,5e-5,20):
    for start in np.arange(-(NgridX / 2) * gridLenX, (NgridX / 2) * gridLenX,
                           stride):
        r_y = 0e-4
        r_x = start
        r = np.sqrt(r_x * r_x + r_y * r_y)
        Ex = gaussianField(r_x, r_y, sigmax, sigmay, n, direction)
        Fx = -e * Ex
        x.append(r_x / sigmax)
        y.append(Fx / fScale)
    ax.plot(x, y, label='Theoretical value')
    x.clear()
    y.clear()

elif direction == "y":
    # for tmp in np.linspace(-5e-4,5e-4,20):
    for start in np.arange(-(NgridY / 2) * gridLenY, (NgridY / 2) * gridLenY,
                           stride):
        r_x = 0e-5
        r_y = start
        r = np.sqrt(r_x * r_x + r_y * r_y)
        Ey = gaussianField(r_x, r_y, sigmax, sigmay, n, direction)
        Fy = -e * Ey
        x.append(r_y / sigmay)
        y.append(Fy / fScale)
    ax.plot(x, y, label='Theoretical value')
    x.clear()
    y.clear()

elif direction == "45":
    # for tmp in np.linspace(-5e-4,5e-4,20):
    N45 = 10000
    startx = -(NgridX - 3) / 2 * gridLenX
    stridex = (NgridX - 3) * gridLenX / N45
    starty = -(NgridY - 3) / 2 * gridLenY
    stridey = (NgridY - 3) * gridLenY / N45

    for i in np.arange(N45):
        r_x = startx + i * stridex
        r_y = starty + i * stridey
        r = np.sqrt(r_x * r_x + r_y * r_y)
        Ex = gaussianField(r_x, r_y, sigmax, sigmay, n, 'x')
        Ey = gaussianField(r_x, r_y, sigmax, sigmay, n, 'y')
        Fx = -e * Ex
        Fy = -e * Ey
        F45 = np.sqrt(Fx**2 + Fy**2) * np.sign(Fx)
        r45 = np.sqrt(r_x**2 + r_y**2) * np.sign(r_x)
        x.append(r45 / np.sqrt(sigmax**2 + sigmay**2))
        y.append(F45 / fScale)

    ax.plot(x, y, label='Theoretical value')
    x.clear()
    y.clear()

figXlable = 'Distance $(r/ {\sigma})$'
figYlable = r'Electric field force $(\times 10^{{{0}}}N)$'.format(figYscale)

ax.set_xlabel(figXlable, fontsize=myfontsize)
ax.set_ylabel(figYlable, fontsize=myfontsize)
plt.tick_params(labelsize=myfontsize)
ax.grid()

X, Y = np.loadtxt(file_path, delimiter=',', usecols=(0, 1), unpack=True)
# X2, Y2 = np.loadtxt(file_path2, delimiter=',', usecols=(0, 1), unpack=True)
X3, Y3 = np.loadtxt(file_path3, delimiter=',', usecols=(0, 1), unpack=True)
# X4, Y4 = np.loadtxt(file_path4, delimiter=',', usecols=(0, 1), unpack=True)
X5, Y5 = np.loadtxt(file_path5, delimiter=',', usecols=(0, 1), unpack=True)

if direction == "x":
    ax.plot(X / sigmax, Y / fScale, label=r'2 grids per $\sigma$')
    # ax.plot(X2 / sigmax, Y2 / fScale, label=r'$5\times 10^{4}$ macro particles')
    ax.plot(X3 / sigmax, Y3 / fScale, label=r'6 grids per $\sigma$')
    # # ax.plot(X4 / sigmax, Y4 / fScale, label=r'$5\times 10^{5}$ macro particles')
    ax.plot(X5 / sigmax, Y5 / fScale, label=r'11 grids per $\sigma$')

elif direction == "y":
    ax.plot(X / sigmay, Y / fScale, label=r'2 grids per $\sigma$')
    ax.plot(X3 / sigmay, Y3 / fScale, label=r'6 grids per $\sigma$')
    ax.plot(X5 / sigmay, Y5 / fScale, label=r'11 grids per $\sigma$')

elif direction == "45":
    ax.plot(X / np.sqrt(sigmax**2 + sigmay**2),
            Y / fScale,
            label=r'$1\times 10^{4}$ macro particles')
    ax.plot(X3 / np.sqrt(sigmax**2 + sigmay**2),
            Y3 / fScale,
            label=r'$1\times 10^{5}$ macro particles')
    ax.plot(X5 / np.sqrt(sigmax**2 + sigmay**2),
            Y5 / fScale,
            label=r'$1\times 10^{6}$ macro particles')
# file_path3 = r'.\proton_100000.csv'
# X3, Y3 = np.loadtxt(file_path3, delimiter=',', usecols=(0, 1), unpack=True)
# ax.plot(X3 / sigmay, Y3 / fScale, label="$1\\times 10^{6}$个宏粒子模拟值")
# ax.set_xlim([0, 3])
# ax.set_ylim([-4, 1])
# ax.set_xlim([6, 6.2])
# ax.set_ylim([-1.23,-1.17])
# ax.set_xlim([-10, 10])
# ax.set_ylim([-5, 5])
ax.legend(fontsize=myfontsize)
# fig.savefig(name)
plt.show()
plt.close()

# 有时理论计算结果在某些点处会出错，可以通过set_xlim来避开错误值
# 这一组参数可以正常计算
# n = 1.0e11
# e = 1.602176565e-19
# epsilon0 = 8.854187817e-12
# beta_x = 0.04
# beta_y = 0.02
# emit_x = 30e-8
# emit_y = 18e-9
# sigmax = math.sqrt(beta_x*emit_x)
# sigmay = math.sqrt(beta_y*emit_y)
# print(sigmax,sigmay)

# NgridX = 64
# NgridY = 128
# gridLenX = 2e-5
# gridLenY = 5e-6
# stride = 1e-6