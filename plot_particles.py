import sys
import numpy as np
import matplotlib.pyplot as plt
import math

def plot_distribution(axes,row,col,x,y,xlable,ylable):
	alpha=0.2  #透明度
	size=2  #散点尺寸
	# axes[row][col].hexbin(x,y,cmap='twilight',gridsize=200)
	axes[row][col].scatter(x,y,alpha=alpha,s=size)
	axes[row][col].set_xlabel(xlable,fontsize=15)
	axes[row][col].set_ylabel(ylable,fontsize=15)
	axes[row][col].tick_params(labelsize=15)
	axes[row][col].tick_params(labelsize=15)


if __name__ == '__main__':
	### filePath = str(sys.argv[1])
	# filePath = r'E:\changmx\bb2019\distribution\2020_1105\1637_positron_turn0_bunch0_slice3_3_50000.csv'
	filePath = r'E:\changmx\bb2019\distribution\2020_1105\2022_positron_turn300_bunch0_50000.csv'

	# fig,axes=plt.subplots(3,3,figsize=(25,15),dpi=300)
	fig,axes=plt.subplots(3,3)

	x,px,y,py,z,pz= np.loadtxt(filePath, delimiter=',', skiprows=1, usecols=(0, 1, 2, 3, 4, 5), unpack=True)

	plot_distribution(axes,0,0,x,px,'x','px')
	plot_distribution(axes,0,1,y,py,'y','py')
	plot_distribution(axes,0,2,x,y,'x','y')
	plot_distribution(axes,1,0,z,x,'z','x')
	plot_distribution(axes,1,1,z,px,'z','px')
	plot_distribution(axes,1,2,px,py,'px','py')
	plot_distribution(axes,2,0,z,y,'z','y')
	plot_distribution(axes,2,1,z,py,'z','py')

	annatation=' After collision, 10 slices, with beam-beam'
	plt.suptitle(filePath+'\n'+annatation,fontsize=20)
	# plt.savefig(r'./'+annatation+'.png')
	plt.show()
