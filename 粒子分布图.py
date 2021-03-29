import numpy as np
import matplotlib.pyplot as plt
import os

inputPath = r'E:\changmx\bb2019\distribution\2020_1222'
time = r'\1705_41'
remark = '_with hourglass'
kind = '_positron_turn'
bunch = '_bunch0_50000.csv'
angle = '0'
Nturn = 100

direction = 'ypy'

xlimit = 1e-3
pxlimit = 6e-2
ylimit = 1.0e-4
pylimit = 4e-3

outputPath = inputPath+time+remark
if not os.path.exists(outputPath):
	os.makedirs(outputPath)

for i in range(0,Nturn):
	turn = str(400+i)
	# fig,ax = plt.subplots(figsize=(6,4),dpi=300)
	fig,ax = plt.subplots()
	filePath = inputPath+time+kind+turn+bunch
	x,px,y,py= np.loadtxt(filePath, delimiter=',', skiprows=1, usecols=(0, 1, 2, 3), unpack=True)
	
	if direction=='xpx':
		# hb=ax.hexbin(x,px,cmap='twilight',gridsize=200)
		ax.scatter(x,px,alpha=0.2,s=0.2)
		ax.set_xlim((-1*xlimit,1*xlimit))
		ax.set_ylim((-1*pxlimit,1*pxlimit))
		ax.set_xlabel(r'$x\ (1\time {1s0}^{-4}m)$')
		ax.set_ylabel(r'$p_x\ (1\times {10}^{-3})$')
		ax.set_title(r'$x-p_x\ distribution, \phi /2 =$'+str(angle)+'mrad, '+str(i)+'turn')
		
	elif direction=='ypy':
		ax.scatter(y,py,alpha=0.2,s=0.2)
		ax.set_xlim((-1*ylimit,1*ylimit))
		ax.set_ylim((-1*pylimit,1*pylimit))
		ax.set_xlabel(r'$y\ (1\times {10}^{-4}m)$')
		ax.set_ylabel(r'$p_y\ (1\times {10}^{-3})$')
		ax.set_title(r'$y-py\ distribution, \phi /2 =$'+str(angle)+'mrad, '+str(i)+'turn')
	
	elif direction=='xy':
			ax.scatter(x,y,alpha=0.2,s=0.2)
			ax.set_xlim((-1*xlimit,1*xlimit))
			ax.set_ylim((-1*ylimit,1*ylimit))
			ax.set_xlabel(r'$x\ (1\times {10}^{-4}m)$')
			ax.set_ylabel(r'$y\ (1\times {10}^{-3})$')
			ax.set_title(r'$x-y\ distribution, \phi /2 =$'+str(angle)+'mrad, '+str(i)+'turn')

	# cb = fig.colorbar(hb)
	
	plt.savefig(outputPath+'\\'+kind+'_'+direction+'_'+turn+'.png')
	# plt.show()
	plt.close()
	print(i)
	

