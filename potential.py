import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import linecache
from mpl_toolkits.axes_grid1 import ImageGrid
import matplotlib as mpl
N = 259
#file_path = r'D:\bb2019\potential0.txt'
file_path = r'D:\bb2019\potential\potential0.txt'
x = np.arange(0,N,1)
y = np.arange(0,N,1)
x,y = np.meshgrid(x,y)

#define a function to get value in any row
def get_line(filepath,line_number):
    return float(linecache.getline(filepath,line_number).strip())

#create 2d array, because the plot_surface function requires that the z parameter must be a 2d array
z = np.zeros((N,N),dtype=np.float)
# assign values to array
for i in range(0,N,1):
    for j in range(0,N,1):
        z[j][i] = get_line(file_path, j+1+i*N)
        #print(j+1+i*N)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['savefig.dpi'] = 300       #image pixel
plt.rcParams['figure.dpi'] = 300        #image resolution
fig = plt.figure()
ax = Axes3D(fig)

# ax.plot_surface(x, y, z,rstride=1,cstride=1,cmap='rainbow')     #print 3d surface plot
ax.plot_surface(x, y, z,rstride=1,cstride=1,cmap=mpl.cm.jet)     #print 3d surface plot
#ax.contourf(x,y,z,zdir='z',offset=-2,cmap='rainbow')            #print contour plot/project to the x-y plane
ax.set_zlim(-1100,-2000)                                             #set the z value range
plt.title("KV分布三维电势,格点数为$256\\times 256$,格点长度为$0.02mm$")
plt.xlabel("横向格点")
plt.ylabel("纵向格点")

plt.savefig(r'D:\bb2019\potential\kv电势3d256格点长度2e-5.png')
plt.show()
