import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import special
import scipy

n = 1.0e11
e = 1.602176565e-19
epsilon0 = 8.854187817e-12
sigmax = 1.549e-4
sigmay = 1.095e-4

Ngrid = 256
gridLen = 5e-6
stride = 1e-6

fScale = 1e-13
figYscale = -13

direction = "x"
type = "gaussian"

x = []
y = []

def w(x,y):
    z = x+1j*y
    a = scipy.exp(-z*z)*(1-special.erf(-1j*z))
    return a

def gaussianField(x,y,sigmax,sigmay,n):
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
    Ex = 0
    # print(Ex,Ey)
    E = scipy.sqrt(Ex*Ex+Ey*Ey)

    return E

for start in np.arange(-(Ngrid / 2) * gridLen, (Ngrid / 2) * gridLen, stride):
    r_x = 0
    r_y = start
    r = (r_x*r_x+r_y*r_y)**0.5*start/abs(start)
    E = gaussianField(r_x,r_y,sigmax,sigmay,n)*start/abs(start)
    F = e*E
    x.append(r / sigmay)
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

# file_path2 = r'E:\changmx\bb2019\electricForce\2020_0819_gaussian_proton\1639\proton_100000.csv'
# X2, Y2 = np.loadtxt(file_path2, delimiter=',', usecols=(0, 1), unpack=True)
# ax.plot(X2 / sigmay, Y2 / fScale, label="$1\\times 10^{5}$个宏粒子模拟值")

name = "E:\\changmx\\bb2019\electricForce\\" + '椭圆束' + type + direction + str(Ngrid) + '长度' + str(gridLen) + ".png"

ax.legend()
fig.savefig(name)
plt.show()
plt.close()