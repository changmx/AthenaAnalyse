import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import special
import scipy

n = 1.0e11
e = 1.602176565e-19
epsilon0 = 8.854187817e-12
beta_x = 0.04
beta_y = 0.02
emit_x = 30e-8
emit_y = 18e-9
sigmax = math.sqrt(beta_x*emit_x)
sigmay = math.sqrt(beta_y*emit_y)
print(sigmax,sigmay)

NgridX = 64
NgridY = 128
gridLenX = 2e-5
gridLenY = 5e-6
stride = 1e-6

direction = "x"
file_path = r'E:\changmx\bb2019\electricForce\2020_1010_gaussian_proton\1625\proton_10000_x.csv'

fScale = 1e-13
figYscale = -13

type = "gaussian"
kind = 'electron'
N = '2e5'

x = []
y = []

def w(x,y):
    z = x+1j*y
    a = scipy.exp(-z*z)*(1-special.erf(-1j*z))
    return a

def gaussianField(x,y,sigmax,sigmay,n,direction):
    e = 1.602176565e-19
    epsilon0 = 8.854187817e-12
    z = x+1j*y
    a = z/(scipy.sqrt(2*(sigmax*sigmax-sigmay*sigmay)))
    xs = -x*x/(2*sigmax*sigmax)
    ys = -y*y/(2*sigmay*sigmay)
    b = scipy.exp(xs+ys)
    # print(xs,ys,b)
    c = (x*sigmay/sigmax+1j*y*sigmax/sigmay)/(scipy.sqrt(2*(sigmax*sigmax-sigmay*sigmay)))

    # print(a.real,a.imag,b.real,b.imag, c.real,c.imag)
    Im = w(a.real,a.imag).imag-(b*w(c.real,c.imag)).imag
    Re = w(a.real,a.imag).real-(b*w(c.real,c.imag)).real
    # print(w(a.real,a.imag).imag,(b*w(c.real,c.imag)).imag)
    # print(w(a.real,a.imag).real,(b*w(c.real,c.imag)).real)
    print(Im,Re)
    Ex = n*e/(2*epsilon0*scipy.sqrt(2*scipy.pi*(sigmax*sigmax-sigmay*sigmay)))*Im
    Ey = n*e/(2*epsilon0*scipy.sqrt(2*scipy.pi*(sigmax*sigmax-sigmay*sigmay)))*Re
    if direction=="x":
        Ey=0
    elif direction=="y":
        Ex=0
    # print(Ex,Ey)
    E = scipy.sqrt(Ex*Ex+Ey*Ey)

    return E

if direction=="x":
    for start in np.arange(-(NgridX / 2) * gridLenX, (NgridX / 2) * gridLenX, stride):
        r_y = 0
        r_x = start
        r = (r_x*r_x+r_y*r_y)**0.5*start/abs(start)
        E = gaussianField(r_x,r_y,sigmax,sigmay,n,direction)*start/abs(start)
        F = -e*E
        x.append(r / sigmax)
        y.append(F / fScale)
elif direction=="y":
    for start in np.arange(-(NgridY / 2) * gridLenY, (NgridY / 2) * gridLenY, stride):
        r_x = 0
        r_y = start
        r = (r_x*r_x+r_y*r_y)**0.5*start/abs(start)
        E = gaussianField(r_x,r_y,sigmax,sigmay,n,direction)*start/abs(start)
        F = -e*E
        x.append(r / sigmay)
        y.append(F / fScale)

fig, ax = plt.subplots()
ax.plot(x, y, label="理论值")

name = "tmp"
figTitle = "tmp"
X2, Y2 = np.loadtxt(file_path, delimiter=',', usecols=(0, 1), unpack=True)
if direction=="x":
    name = ".\\" + kind + '椭圆束' + N + type + direction + str(NgridX) + '长度' + str(gridLenX) + ".png"
    figTitle = '{Ftype}分布,{Fdirection}方向,网格(${Fgrid}\\times$'.format(Ftype=type, Fdirection=direction, Fgrid=NgridX)
elif direction=="y":
    name = ".\\" + kind + '椭圆束' + N + type + direction + str(NgridY) + '长度' + str(gridLenY) + ".png"
    figTitle = '{Ftype}分布,{Fdirection}方向,网格(${Fgrid}\\times$'.format(Ftype=type, Fdirection=direction, Fgrid=NgridY)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['savefig.dpi'] = 600       #image pixel
plt.rcParams['figure.dpi'] = 600        #image resolution
plt.figure(figsize=(18,6))
figXlable = '径向距离$(r/ {\\sigma_{RMS}})$'
figYlable = '束束力$(\\times 10^{a}N)$'.format(a=figYscale)

ax.set(xlabel=figXlable, ylabel=figYlable,
       title=figTitle + '$5\\times 10^{-6}m)$,束束力理论值与模拟值对比')        ############
ax.grid()

name = "tmp"
figTitle = "tmp"
X2, Y2 = np.loadtxt(file_path, delimiter=',', usecols=(0, 1), unpack=True)
if direction=="x":
    ax.plot(X2 / sigmax, Y2 / fScale, label="$2\\times 10^{5}$个宏粒子模拟值")

elif direction=="y":
    ax.plot(X2 / sigmay, Y2 / fScale, label="$2\\times 10^{5}$个宏粒子模拟值")



# file_path3 = r'.\proton_100000.csv'
# X3, Y3 = np.loadtxt(file_path3, delimiter=',', usecols=(0, 1), unpack=True)
# ax.plot(X3 / sigmay, Y3 / fScale, label="$1\\times 10^{6}$个宏粒子模拟值")



ax.legend()
# fig.savefig(name)
plt.show()
plt.close()

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