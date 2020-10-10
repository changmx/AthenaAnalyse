import numpy  as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import matplotlib as mpl
import mpl_toolkits.axisartist.axislines as axislines

N = 255
M = N+2
Lenx=1e-5
Leny=1e-5
file_path = r'E:\changmx\bb2019\potential\2020_1010_gaussian_proton\1044\proton_bunch0_slice0_10000_turn0.csv'
x = np.arange(0,N,1)
y = np.arange(0,N,1)
X,Y = np.meshgrid(x,y)
z = np.loadtxt(file_path, delimiter=',')
m = X+1
n = Y+1
p = m+n*M
Zx = -(z[p+1]-z[p-1])/(2*Lenx)
Zy = -(z[p+M]-z[p-M])/(2*Leny)
Z = (Zx**2+Zy**2)**0.5
# Z = Zy

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['savefig.dpi'] = 300       #image pixel
plt.rcParams['figure.dpi'] = 300        #image resolution
P=np.arange(-2e7,2e7,1e4)#用来指明等高线对应的值为多少时才出现对应图线
fig=plt.figure()#设定图形大小
CS=plt.contourf(Z,P,linewidth=2,cmap=mpl.cm.jet)#画出等高线填充图，cmap表示颜色的图层。
cbar = plt.colorbar(CS)
cbar.set_label('电场 V/m')
plt.title("KV分布电场在$xy$平面的投影,网格数为$256\\times 256$,网格长度为$0.01mm$")
plt.xlabel("横向格点")
plt.ylabel("纵向格点")

# fig, ax = plt.subplots()
#
# cs = ax.contourf(X, Y, Z, locator=ticker.LogLocator(), cmap=cm.PuBu_r)
#cmap=mpl.cm.jet
# cbar = fig.colorbar(cs)
# plt.savefig(r'D:\bb2019\electricField\kv电场投影256网格长度1e-5.png')
plt.show()