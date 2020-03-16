import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.axes_grid1 import ImageGrid
import matplotlib as mpl

N = 257
M = N+2
Len=2e-5
file_path = r'D:\bb2019\potential\potential0.txt'
x = np.arange(0,N,1)
y = np.arange(0,N,1)

X,Y = np.meshgrid(x,y)
z = np.loadtxt(file_path, delimiter=',')
m = X+1
n = Y+1
p = m+n*M
Zx = -(z[p+1]-z[p-1])/(2*Len)
Zy = -(z[p+M]-z[p-M])/(2*Len)
Z = (Zx**2+Zy**2)**0.5

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['savefig.dpi'] = 300       #image pixel
plt.rcParams['figure.dpi'] = 300        #image resolution
fig = plt.figure()
ax = Axes3D(fig)
x1 = np.arange(0,N,1)*Len
y1 = np.arange(0,N,1)*Len
X1,Y1=np.meshgrid(x1,y1)
ax.plot_surface(X1, Y1, Z,rstride=1,cstride=1,cmap=mpl.cm.jet)     #print 3d surface plot
#ax.contourf(x,y,z,zdir='z',offset=-2,cmap='rainbow')            #print contour plot/project to the x-y plane
#ax.set_zlim(-1100,-2000)                                             #set the z value range
plt.title("KV分布三维电场,网格数为$256\\times 256$,网格长度为$0.02mm$ 宏粒子数为$1\\times 10^{5}$")
plt.xlabel("横向格点")
plt.ylabel("纵向格点")

plt.savefig(r'D:\bb2019\electricField\kv电场3d256网格长度2e-5宏粒子1e5变换坐标.png')
plt.show()
plt.close()
