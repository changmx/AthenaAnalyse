import numpy as np
import matplotlib.pyplot as plt

sigma_z,r_sim,r_theory = np.loadtxt(r'D:\AthenaOrigin\hourglass_compare.txt', delimiter=' ', skiprows=1, usecols=(0, 3, 4), unpack=True)
sigma_z=sigma_z*100    # 把单位由m转化为cm

fig,ax = plt.subplots(figsize=(12,8),dpi=600)

ax.scatter(sigma_z,r_sim,label='Simulated result')
ax.plot(sigma_z,r_theory,color='orange',label='Theoretical value')
part=0.6
# 计算相对误差
error = [0]*sigma_z.shape[0]
sum_error = 0
sum_error_first_half = 0
sum_error_second_half = 0
for i in range(sigma_z.shape[0]):
	error[i]=abs(r_sim[i]-r_theory[i])/r_theory[i]
	sum_error+=error[i]
	if i<sigma_z.shape[0]*part:
		sum_error_first_half+=error[i]
	else:
		sum_error_second_half+=error[i]

ax.text(sigma_z[0],0.5*r_sim[0],r'$Average\ relative\ error(\sigma_z <3cm)= $'+str(format(sum_error_first_half/(part*sigma_z.shape[0])*100,".2f"))+'%'+'\n'+\
	r'$Average\ relative\ error(\sigma_z  \geq 3cm)= $'+str(format(sum_error_second_half/((1-part)*sigma_z.shape[0])*100,".2f"))+'%',bbox=dict(boxstyle="round", fc="w"),fontsize='medium')
# ax.text(sigma_z[0],0.46*r_sim[0],'Average relative error of the second half of the data = '+str(format(sum_error_second_half/(sigma_z.shape[0]/2)*100,".2f"))+'%',bbox=dict(boxstyle="round", fc="w"),fontsize='medium')
ax.locator_params("x",tight=True,nbins=10)
ax.set_xlabel(r'$\sigma_z\ (cm)$',loc='center')
ax.set_ylabel('hourglass factor')
ax.set_title('Comparison of simulated and theoretical hourglass factor of gaussian beams (20 slices)')
ax.grid()
ax.legend()

# plt.savefig(r'./'+'hourglassFactorCompare'+'.png')
plt.show()
