import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

def plot_statistic(filePath1,filePath2,row,col,kind,ymin,ymax,title,label1,label2):
	turn1, xAve1, sigmax1, yAve1, sigmay1, xEmit1, yEmit1, sigmaZ1, sigmaPz1, loss1, lossPer1 = \
	np.loadtxt(filePath1,delimiter=',',skiprows=1,usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), unpack=True)

	turn2, xAve2, sigmax2, yAve2, sigmay2, xEmit2, yEmit2, sigmaZ2, sigmaPz2, loss2, lossPer2 = \
	np.loadtxt(filePath2,delimiter=',',skiprows=1,usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), unpack=True)

	if kind=='sigmay':
		axes[row,col].plot(turn1,sigmay1,label=label1)
		axes[row,col].plot(turn2,sigmay2,label=label2)
		axes[row,col].set_ylim(ymin,ymax)
		axes[row,col].set_ylabel(r'$\sigma_y$')
		axes[row,col].set_title(title)
		axes[row,col].grid()
		axes[row,col].legend()
		axes[row,col].yaxis.set_major_locator(MultipleLocator(3e-6))  #设置y轴坐标间隔为3e-6的倍数
	elif kind=='sigmax':
		axes[row,col].plot(turn1,sigmax1,label=label1)
		axes[row,col].plot(turn2,sigmax2,label=label2)
		axes[row,col].set_ylim(ymin,ymax)
		axes[row,col].set_ylabel(r'$\sigma_x$')
		axes[row,col].set_title(title)
		axes[row,col].grid()
		axes[row,col].legend()
		# axes[row,col].yaxis.set_major_locator(MultipleLocator(3e-5))  #设置y轴坐标间隔为3e-6的倍数

fig,axes = plt.subplots(2,3)

# protonFile1 = r'E:\changmx\bb2019\statLumiPara\2020_1118\1728_proton_bunch0.csv'
# electronFile1 = r'E:\changmx\bb2019\statLumiPara\2020_1118\1728_electron_bunch0.csv'
# title1 = r'$128\times 10\times 10^{-6}m$'

# protonFile2 = r'E:\changmx\bb2019\statLumiPara\2020_1118\1727_proton_bunch0.csv'
# electronFile2 = r'E:\changmx\bb2019\statLumiPara\2020_1118\1727_electron_bunch0.csv'
# title2 = r'$512\times 2.5\times 10^{-6}m$'

# protonFile3 = r'E:\changmx\bb2019\statLumiPara\2020_1118\1829_proton_bunch0.csv'
# electronFile3 = r'E:\changmx\bb2019\statLumiPara\2020_1118\1829_electron_bunch0.csv'
# title3 = r'$128\times 15\times 10^{-6}m$'

# protonFile4 = r'E:\changmx\bb2019\statLumiPara\2020_1118\1827_proton_bunch0.csv'
# electronFile4 = r'E:\changmx\bb2019\statLumiPara\2020_1118\1827_electron_bunch0.csv'
# title4 = r'$128\times 20\times 10^{-6}m$'

# protonFile5 = r'E:\changmx\bb2019\statLumiPara\2020_1118\1828_proton_bunch0.csv'
# electronFile5 = r'E:\changmx\bb2019\statLumiPara\2020_1118\1828_electron_bunch0.csv'
# title5 = r'$128\times 30\times 10^{-6}m$'

# protonFile6 = r'E:\changmx\bb2019\statLumiPara\2020_1118\1830_proton_bunch0.csv'
# electronFile6 = r'E:\changmx\bb2019\statLumiPara\2020_1118\1830_electron_bunch0.csv'
# title6 = r'$128\times 40\times 10^{-6}$m'

# protonFile1 = r'E:\changmx\bb2019\statLumiPara\2020_1119\0927_proton_bunch0.csv'
# electronFile1 = r'E:\changmx\bb2019\statLumiPara\2020_1119\0927_electron_bunch0.csv'
# title1 = r'$\nu_{ex}=31.02,\nu_{ey}=34.12$'

# protonFile2 = r'E:\changmx\bb2019\statLumiPara\2020_1119\0928_proton_bunch0.csv'
# electronFile2 = r'E:\changmx\bb2019\statLumiPara\2020_1119\0928_electron_bunch0.csv'
# title2 = r'$\nu_{ex}=31.02,\nu_{ey}=34.02$'

# protonFile3 = r'E:\changmx\bb2019\statLumiPara\2020_1119\0929_proton_bunch0.csv'
# electronFile3 = r'E:\changmx\bb2019\statLumiPara\2020_1119\0929_electron_bunch0.csv'
# title3 = r'$\nu_{ex}=31.06,\nu_{ey}=34.08$'

# protonFile4 = r'E:\changmx\bb2019\statLumiPara\2020_1119\0930_proton_bunch0.csv'
# electronFile4 = r'E:\changmx\bb2019\statLumiPara\2020_1119\0930_electron_bunch0.csv'
# title4 = r'$\nu_{ex}=31.06,\nu_{ey}=34.06$'

# protonFile5 = r'E:\changmx\bb2019\statLumiPara\2020_1119\0931_proton_bunch0.csv'
# electronFile5 = r'E:\changmx\bb2019\statLumiPara\2020_1119\0931_electron_bunch0.csv'
# title5 = r'$\nu_{ex}=31.1,\nu_{ey}=34.1$'

# protonFile6 = r'E:\changmx\bb2019\statLumiPara\2020_1119\0932_proton_bunch0.csv'
# electronFile6 = r'E:\changmx\bb2019\statLumiPara\2020_1119\0932_electron_bunch0.csv'
# title6 = r'$\nu_{ex}=31.12,\nu_{ey}=34.12$m'

##
# protonFile1 = r'E:\changmx\bb2019\statLumiPara\new\2032_proton_bunch0.csv'
# electronFile1 = r'E:\changmx\bb2019\statLumiPara\new\2032_electron_bunch0.csv'
# title1 = r'$\nu_{ex}=31.02,\nu_{ey}=34.12$'

# protonFile2 = r'E:\changmx\bb2019\statLumiPara\new\2034_proton_bunch0.csv'
# electronFile2 = r'E:\changmx\bb2019\statLumiPara\new\2034_electron_bunch0.csv'
# title2 = r'$\nu_{ex}=31.02,\nu_{ey}=34.02$'

# protonFile3 = r'E:\changmx\bb2019\statLumiPara\new\2035_proton_bunch0.csv'
# electronFile3 = r'E:\changmx\bb2019\statLumiPara\new\2035_electron_bunch0.csv'
# title3 = r'$\nu_{ex}=31.06,\nu_{ey}=34.08$'

# protonFile4 = r'E:\changmx\bb2019\statLumiPara\new\2036_proton_bunch0.csv'
# electronFile4 = r'E:\changmx\bb2019\statLumiPara\new\2036_electron_bunch0.csv'
# title4 = r'$\nu_{ex}=31.06,\nu_{ey}=34.06$'

# protonFile5 = r'E:\changmx\bb2019\statLumiPara\new\2037_proton_bunch0.csv'
# electronFile5 = r'E:\changmx\bb2019\statLumiPara\new\2037_electron_bunch0.csv'
# title5 = r'$\nu_{ex}=31.1,\nu_{ey}=34.1$'

# protonFile6 = r'E:\changmx\bb2019\statLumiPara\new\2038_proton_bunch0.csv'
# electronFile6 = r'E:\changmx\bb2019\statLumiPara\new\2038_electron_bunch0.csv'
# title6 = r'$\nu_{ex}=31.12,\nu_{ey}=34.12$m'

## damp 2000, 128*20e-6
# protonFile1 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1132_proton_bunch0.csv'
# electronFile1 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1132_electron_bunch0.csv'
# title1 = r'$\nu_{ex}=31.02,\nu_{ey}=34.12$'

# protonFile2 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1131_proton_bunch0.csv'
# electronFile2 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1131_electron_bunch0.csv'
# title2 = r'$\nu_{ex}=31.02,\nu_{ey}=34.02$'

# protonFile3 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1130_proton_bunch0.csv'
# electronFile3 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1130_electron_bunch0.csv'
# title3 = r'$\nu_{ex}=31.06,\nu_{ey}=34.08$'

# protonFile4 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1129_proton_bunch0.csv'
# electronFile4 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1129_electron_bunch0.csv'
# title4 = r'$\nu_{ex}=31.06,\nu_{ey}=34.06$'

# protonFile5 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1128_proton_bunch0.csv'
# electronFile5 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1128_electron_bunch0.csv'
# title5 = r'$\nu_{ex}=31.1,\nu_{ey}=34.1$'

# protonFile6 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1127_proton_bunch0.csv'
# electronFile6 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1127_electron_bunch0.csv'
# title6 = r'$\nu_{ex}=31.12,\nu_{ey}=34.12$m'
# sigma_ymin = 12e-6
# sigma_ymax = 30e-6

## damp 1000, 128*20e-6
# protonFile1 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1519_proton_bunch0.csv'
# electronFile1 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1519_electron_bunch0.csv'
# title1 = r'$\nu_{ex}=31.02,\nu_{ey}=34.12$'

# protonFile2 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1520_proton_bunch0.csv'
# electronFile2 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1520_electron_bunch0.csv'
# title2 = r'$\nu_{ex}=31.02,\nu_{ey}=34.02$'

# protonFile3 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1521_proton_bunch0.csv'
# electronFile3 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1521_electron_bunch0.csv'
# title3 = r'$\nu_{ex}=31.06,\nu_{ey}=34.08$'

# protonFile4 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1522_proton_bunch0.csv'
# electronFile4 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1522_electron_bunch0.csv'
# title4 = r'$\nu_{ex}=31.06,\nu_{ey}=34.06$'

# protonFile5 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1523_proton_bunch0.csv'
# electronFile5 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1523_electron_bunch0.csv'
# title5 = r'$\nu_{ex}=31.1,\nu_{ey}=34.1$'

# protonFile6 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1524_proton_bunch0.csv'
# electronFile6 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1524_electron_bunch0.csv'
# title6 = r'$\nu_{ex}=31.12,\nu_{ey}=34.12$m'
# sigma_ymin = 12e-6
# sigma_ymax = 30e-6

## damp 1000, 128*10e-6
protonFile1 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1824_proton_bunch0.csv'
electronFile1 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1824_electron_bunch0.csv'
title1 = r'$\nu_{ex}=31.02,\nu_{ey}=34.12$'

protonFile2 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1823_proton_bunch0.csv'
electronFile2 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1823_electron_bunch0.csv'
title2 = r'$\nu_{ex}=31.02,\nu_{ey}=34.02$'

protonFile3 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1822_proton_bunch0.csv'
electronFile3 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1822_electron_bunch0.csv'
title3 = r'$\nu_{ex}=31.06,\nu_{ey}=34.08$'

protonFile4 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1821_proton_bunch0.csv'
electronFile4 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1821_electron_bunch0.csv'
title4 = r'$\nu_{ex}=31.06,\nu_{ey}=34.06$'

protonFile5 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1820_proton_bunch0.csv'
electronFile5 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1820_electron_bunch0.csv'
title5 = r'$\nu_{ex}=31.1,\nu_{ey}=34.1$'

protonFile6 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1819_proton_bunch0.csv'
electronFile6 = r'E:\changmx\bb2019\statLumiPara\2020_1119\1819_electron_bunch0.csv'
title6 = r'$\nu_{ex}=31.12,\nu_{ey}=34.12$m'

sigma_ymin = 12e-6
sigma_ymax = 30e-6
sigma_xmin = 8e-5
sigma_xmax = 20e-5

# plot_statistic(protonFile1,electronFile1,0,0,'sigmay',sigma_ymin,sigma_ymax,title1,'proton','electron')
# plot_statistic(protonFile2,electronFile2,0,1,'sigmay',sigma_ymin,sigma_ymax,title2,'proton','electron')
# plot_statistic(protonFile3,electronFile3,0,2,'sigmay',sigma_ymin,sigma_ymax,title3,'proton','electron')
# plot_statistic(protonFile4,electronFile4,1,0,'sigmay',sigma_ymin,sigma_ymax,title4,'proton','electron')
# plot_statistic(protonFile5,electronFile5,1,1,'sigmay',sigma_ymin,sigma_ymax,title5,'proton','electron')
# plot_statistic(protonFile6,electronFile6,1,2,'sigmay',sigma_ymin,sigma_ymax,title6,'proton','electron')

plot_statistic(protonFile1,electronFile1,0,0,'sigmax',sigma_xmin,sigma_xmax,title1,'proton','electron')
plot_statistic(protonFile2,electronFile2,0,1,'sigmax',sigma_xmin,sigma_xmax,title2,'proton','electron')
plot_statistic(protonFile3,electronFile3,0,2,'sigmax',sigma_xmin,sigma_xmax,title3,'proton','electron')
plot_statistic(protonFile4,electronFile4,1,0,'sigmax',sigma_xmin,sigma_xmax,title4,'proton','electron')
plot_statistic(protonFile5,electronFile5,1,1,'sigmax',sigma_xmin,sigma_xmax,title5,'proton','electron')
plot_statistic(protonFile6,electronFile6,1,2,'sigmax',sigma_xmin,sigma_xmax,title6,'proton','electron')


# fig.suptitle(r'$\nu_{ex}=31,12,\nu_{ey}=34.12,\sigma_{ey}=1.6\times 10^{-5}m$')
# fig.suptitle(r'$\sigma_{ey}=1.6\times 10^{-5}m$')

plt.show()

