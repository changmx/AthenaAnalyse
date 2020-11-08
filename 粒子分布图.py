import numpy as np
import matplotlib.pyplot as plt

path = r'E:\changmx\bb2019\distribution\2020_1103'
time = r'\1734'
kind = '_positron_turn'
bunch = '_bunch0_50000.csv'
angle = '11'
Nturn = 100

direction = 'x'

xlimit = 3
pxlimit = 0.8
ylimit = 1.5e-3

for i in range(1,Nturn+1):
	turn = str(i)
	fig,ax = plt.subplots(figsize=(6,4),dpi=300)
	filePath = path+time+kind+turn+bunch
	x,px,y,py= np.loadtxt(filePath, delimiter=',', skiprows=1, usecols=(0, 1, 2, 3), unpack=True)
	x=x*1e4
	px=px*1e3
	if direction=='x':
		hb=ax.hexbin(x,px,cmap='twilight',gridsize=200)
		ax.set_xlim((-1*xlimit,1*xlimit))
		ax.set_ylim((-1*pxlimit,1*pxlimit))
		ax.set_xlabel(r'$x\ (1\times {10}^{-4}m)$')
		ax.set_ylabel(r'$p_x\ (1\times {10}^{-3})$')
		ax.set_title(r'$x-p_x\ distribution, \phi /2 =$'+str(angle)+'mrad, '+str(i)+'turn')
		
	elif direction=='y':
		ax.scstter(y,py)

	cb = fig.colorbar(hb)
	
	# plt.savefig(path+r'\figure\fig'+kind+turn+'.png')
	# plt.show()
	plt.close()
	print(i)
	

