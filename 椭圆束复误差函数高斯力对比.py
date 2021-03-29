import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import special
import scipy

n = 1.25e11
e = 1.602176565e-19
epsilon0 = 8.854187817e-12
beta_x = 0.04
beta_y = 0.02
emit_x = 30e-8
emit_y = 18e-8
sigmax = math.sqrt(beta_x*emit_x)
sigmay = math.sqrt(beta_y*emit_y)
print('sigmax = %e, sigmay = %e' %(sigmax,sigmay))

NgridX = 128
NgridY = 128
gridLenX = 2e-5
gridLenY = 1e-5
stride = 1e-6

direction = "x"
## 普通格林函数下对比fft和poisson
# file_path = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\0846_57_proton_50000_x.csv' # poisson,5e4
# file_path3 = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\0931_43_proton_500000_x.csv' # poisson,5e5
# file_path4 = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\0912_03_proton_50000_x.csv' # fft,5e4
# file_path5 = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\0928_45_proton_500000_x.csv' # fft,5e5

# file_path = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\0846_57_proton_50000_y.csv' # poisson,5e4
# file_path3 = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\0931_43_proton_500000_y.csv' # poisson,5e5
# file_path4 = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\0912_03_proton_50000_y.csv' # fft,5e4
# file_path5 = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\0928_45_proton_500000_y.csv' # fft,5e5

## 对比原点格林函数的偏移
# file_path = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\0912_03_proton_50000_x.csv' # fft,5e4,green x = 0.1, y = 0
# file_path3 = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\1010_29_proton_50000_x.csv' # fft,5e4,green x = 0.5, y = 0
# file_path4 = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\1012_59_proton_50000_x.csv' # fft,5e4,green x = 0.01, y = 0
# file_path5 = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\1014_34_proton_50000_x.csv' # fft,5e4,green x = 0.05, y = 0

# file_path = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\0912_03_proton_50000_y.csv' # fft,5e4,green x = 0.1, y = 0
# file_path3 = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\1010_29_proton_50000_y.csv' # fft,5e4,green x = 0.5, y = 0
# file_path4 = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\1012_59_proton_50000_y.csv' # fft,5e4,green x = 0.01, y = 0
# file_path5 = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\1014_34_proton_50000_y.csv' # fft,5e4,green x = 0.05, y = 0

## green即普通格林函数，green1即偏移格林函数
# file_path = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\1027_21_proton_50000_x.csv' # fft,5e4,green x = 0.05, y = 0
# file_path3 = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\1030_26_proton_50000_x.csv' # fft,5e4,green1 x = 0.05, y = 0
# file_path4 = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\1035_30_proton_50000_x.csv' # fft,5e4,green x = 0.1, y = 0
# file_path5 = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\1055_36_proton_50000_x.csv' # fft,5e4,green x = 0.05, y = 0

# file_path = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\1027_21_proton_50000_y.csv' # fft,5e4,green x = 0.05, y = 0
# file_path3 = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\1030_26_proton_50000_y.csv' # fft,5e4,green1 x = 0.05, y = 0
# file_path4 = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\1035_30_proton_50000_y.csv' # fft,5e4,green x = 0.1, y = 0
# file_path5 = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\1055_36_proton_50000_y.csv' # fft,5e4,green x = 0.05, y = 0

## 积分格林函数下对比fft和poisson
file_path = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\1110_00_proton_50000_x.csv' # poisson,5e4,green1 x = 0.05, y = 0
file_path3 = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\1114_36_proton_50000_x.csv' # fft,5e4,green1 x = 0.05, y = 0
file_path4 = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\1116_03_proton_50000_x.csv' # fft,5e4,green x = 0.1, y = 0

# file_path = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\1110_00_proton_50000_y.csv' # poisson,5e4,green1 x = 0.05, y = 0
# file_path3 = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\1114_36_proton_50000_y.csv' # fft,5e4,green1 x = 0.05, y = 0
# file_path4 = r'E:\changmx\bb2021\electricForce\2021_0225_gaussian_proton\1116_03_proton_50000_y.csv' # fft,5e4,green x = 0.1, y = 0



fScale = 1e-13
figYscale = -13

type = "gaussian"
kind = 'electron'
N = '5e4'

x = []
y = []

def w(x,y):
    z = x+1j*y
    a = np.exp(-z*z)*(1-special.erf(-1j*z))
    return a

def gaussianField(x,y,sigmax,sigmay,n,direction):
    e = 1.602176565e-19
    epsilon0 = 8.854187817e-12
    z = x+1j*y
    a = z/(np.sqrt(2*(sigmax*sigmax-sigmay*sigmay)))
    xs = -x*x/(2*sigmax*sigmax)
    ys = -y*y/(2*sigmay*sigmay)
    b = np.exp(xs+ys)
    # print(xs,ys,b)
    c = (x*sigmay/sigmax+1j*y*sigmax/sigmay)/(np.sqrt(2*(sigmax*sigmax-sigmay*sigmay)))

    # print(a.real,a.imag,b.real,b.imag, c.real,c.imag)
    Im = w(a.real,a.imag).imag-(b*w(c.real,c.imag)).imag
    Re = w(a.real,a.imag).real-(b*w(c.real,c.imag)).real
    # print(w(a.real,a.imag).imag,(b*w(c.real,c.imag)).imag)
    # print(w(a.real,a.imag).real,(b*w(c.real,c.imag)).real)
    # print(Im,Re)
    Ex = n*e/(2*epsilon0*np.sqrt(2*scipy.pi*(sigmax*sigmax-sigmay*sigmay)))*Im
    Ey = n*e/(2*epsilon0*np.sqrt(2*scipy.pi*(sigmax*sigmax-sigmay*sigmay)))*Re
    if direction=="x":
        return Ex
    elif direction=="y":
        return Ey

fig, ax = plt.subplots()

if direction=="x":
    # for tmp in np.linspace(-5e-5,5e-5,20):
    for start in np.arange(-(NgridX / 2) * gridLenX, (NgridX / 2) * gridLenX, stride):
        r_y = 0e-4
        r_x = start
        r = np.sqrt(r_x*r_x+r_y*r_y)
        Ex = gaussianField(r_x,r_y,sigmax,sigmay,n,direction)
        Fx = -e*Ex
        x.append(r_x / sigmax)
        y.append(Fx / fScale)
    ax.plot(x, y, label="理论值")
    x.clear()
    y.clear()
    
elif direction=="y":
    # for tmp in np.linspace(-5e-4,5e-4,20):
    for start in np.arange(-(NgridY / 2) * gridLenY, (NgridY / 2) * gridLenY, stride):
        r_x = 0e-5
        r_y = start
        r = np.sqrt(r_x*r_x+r_y*r_y)
        Ey = gaussianField(r_x,r_y,sigmax,sigmay,n,direction)
        Fy = -e*Ey
        x.append(r_y / sigmay)
        y.append(Fy / fScale)
    ax.plot(x, y, label="理论值")
    x.clear()
    y.clear()



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
# plt.figure(figsize=(18,6))
figXlable = '径向距离$(r/ {\\sigma_{RMS}})$'
figYlable = '束束力$(\\times 10^{a}N)$'.format(a=figYscale)

ax.set(xlabel=figXlable, ylabel=figYlable,
       title=figTitle + '$2\\times 10^{-5}m)$,束束力理论值与模拟值对比')        ############
ax.grid()

name = "tmp"
figTitle = "tmp"
X2, Y2 = np.loadtxt(file_path, delimiter=',', usecols=(0, 1), unpack=True)
X3, Y3 = np.loadtxt(file_path3, delimiter=',', usecols=(0, 1), unpack=True)
X4, Y4 = np.loadtxt(file_path4, delimiter=',', usecols=(0, 1), unpack=True)
# X5, Y5 = np.loadtxt(file_path5, delimiter=',', usecols=(0, 1), unpack=True)
if direction=="x":
    pass
    ax.plot(X2 / sigmax, Y2 / fScale, label="$5\\times 10^{4}$个宏粒子,Poisson solver,green 0.05模拟值")
    ax.plot(X3 / sigmax, Y3 / fScale, label="$5\\times 10^{5}$个宏粒子,FFT solver,green1 0.05模拟值")
    ax.plot(X4 / sigmax, Y4 / fScale, label="$5\\times 10^{4}$个宏粒子,FFT solver,green1 0.1模拟值")
    # ax.plot(X5 / sigmax, Y5 / fScale, label="$5\\times 10^{5}$个宏粒子,FFT solver,green 0.05模拟值")

elif direction=="y":
    ax.plot(X2 / sigmay, Y2 / fScale, label="$5\\times 10^{4}$个宏粒子,Poisson solver,green 0.05模拟值")
    ax.plot(X3 / sigmay, Y3 / fScale, label="$5\\times 10^{5}$个宏粒子,FFT solver,green1 0.05模拟值")
    ax.plot(X4 / sigmay, Y4 / fScale, label="$5\\times 10^{4}$个宏粒子,FFT solver,green1 0.1模拟值")
    # ax.plot(X5 / sigmay, Y5 / fScale, label="$5\\times 10^{5}$个宏粒子,FFT solver,green 0.05模拟值")



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