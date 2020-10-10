import numpy  as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import matplotlib as mpl
import mpl_toolkits.axisartist.axislines as axislines

M = 257
N = int((M-1)/2)
file_path = r'E:\changmx\bb2019\potential\2020_1010_gaussian_proton\1044\proton_bunch0_slice0_10000_turn0.csv'
x = np.arange(-N,N+1,1)
y = np.arange(-N,N+1,1)
X,Y = np.meshgrid(x,y)
z = np.loadtxt(file_path, delimiter=',')
Z=z[((X.astype('int64')+N)+(Y.astype('int64')+N)*M)]
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['savefig.dpi'] = 300       #image pixel
# plt.rcParams['figure.dpi'] = 300        #image resolution
P=np.arange(0,5e3,100)#用来指明等高线对应的值为多少时才出现对应图线
fig=plt.figure()#设定图形大小
# fig.add_subplot(121)#画第一张图
# CS=plt.contour(Z,N,linewidth=2,cmap=mpl.cm.jet)#画出等高线图，cmap表示颜色的图层。
# plt.clabel(CS,inline=True,fmt='%1.1f',fontsize=10)#在等高线图里面加入每条线对应的值
# plt.colorbar(CS)#标注右侧的图例

#fig.add_subplot(122)#画第二张图
# CS=plt.contourf(Z,P,linewidth=2,cmap='rainbow')#画出等高线填充图，cmap表示颜色的图层。
CS=plt.contourf(Z,P,linewidth=2,cmap=mpl.cm.jet)#画出等高线填充图，cmap表示颜色的图层。
#plt.colorbar(CS)#标注右侧的图例
cbar = plt.colorbar(CS)
cbar.set_label('电势')
plt.title("KV分布电势在$xy$平面的投影,格点数为$256\\times 256$,格点长度为$0.02mm$")
plt.xlabel("横向格点")
plt.ylabel("纵向格点")

# fig, ax = plt.subplots()
#
# cs = ax.contourf(X, Y, Z, locator=ticker.LogLocator(), cmap=cm.PuBu_r)
#cmap=mpl.cm.jet
# cbar = fig.colorbar(cs)
plt.savefig(r'D:\bb2019\potential\kv电势投影256格点长度2e-5.png')
plt.show()
plt.close()