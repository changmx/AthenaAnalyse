from plot_particles import plot_distribution
import numpy as np
import matplotlib.pyplot as plt

filePath1 = r'E:\changmx\bb2019\distribution\2020_1111\1143_positron_turn300_bunch0_50000.csv'
filePath2 = r'E:\changmx\bb2019\distribution\2020_1111\1141_positron_turn300_bunch0_50000.csv'

# fig,axes=plt.subplots(2,3,figsize=(25,15),dpi=300)
fig,axes=plt.subplots(2,3)

x1,px1,y1,py1,z1,pz1= np.loadtxt(filePath1, delimiter=',', skiprows=1, usecols=(0, 1, 2, 3, 4, 5), unpack=True)
x2,px2,y2,py2,z2,pz2= np.loadtxt(filePath2, delimiter=',', skiprows=1, usecols=(0, 1, 2, 3, 4, 5), unpack=True)
particle = range(0,50000,1)

plot_distribution(axes,0,0,z1,x1,'z (m)','x (m)')
plot_distribution(axes,0,1,z1,y1,'z (m)','y (m)')
plot_distribution(axes,0,2,particle,z1,'particle','z (m)')
axes[0,2].grid()
axes[1,2].grid()

plot_distribution(axes,1,0,z2,x2,'z (m)','x (m)')
plot_distribution(axes,1,1,z2,y2,'z (m)','y (m)')
plot_distribution(axes,1,2,particle,z2,'particle','z (m)')

plt.suptitle('Beam distribution when x-z half crossing angle is 0(upper) and 45 degrees(lower).',y=0.96)
plt.savefig(r'./'+'before and after cross angle'+'.pdf')
plt.show()