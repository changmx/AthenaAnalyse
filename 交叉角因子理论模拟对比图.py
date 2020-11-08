import numpy as np
import matplotlib.pyplot as plt

half_angle,r_theory,r_sim= np.loadtxt(r'D:\AthenaOrigin\crossingAngle_compare.txt', delimiter=' ', skiprows=1, usecols=(0, 1, 4), unpack=True)
half_angle=half_angle*1000    # 把单位由rad转化为mrad

# fig,ax = plt.subplots()
fig,ax = plt.subplots(figsize=(12,8),dpi=600)


ax.scatter(half_angle,r_sim,label='Simulated result')
ax.plot(half_angle,r_theory,color='orange',label='Theoretical value')
part=1
# 计算相对误差
error = [0]*half_angle.shape[0]
sum_error = 0
sum_error_first_half = 0
sum_error_second_half = 0
for i in range(half_angle.shape[0]):
	error[i]=abs(r_sim[i]-r_theory[i])/r_theory[i]
	sum_error+=error[i]
	

ax.text(half_angle[0],0.5*r_sim[0],r'$Average\ relative\ error= $'+str(format(sum_error/(part*half_angle.shape[0])*100,".2f"))+'%',bbox=dict(boxstyle="round", fc="w"),fontsize='medium')
# ax.text(sigma_z[0],0.46*r_sim[0],'Average relative error of the second half of the data = '+str(format(sum_error_second_half/(sigma_z.shape[0]/2)*100,".2f"))+'%',bbox=dict(boxstyle="round", fc="w"),fontsize='medium')
ax.locator_params("x",tight=True,nbins=10)
ax.set_xlabel('Half angle (mrad)',loc='center')
ax.set_ylabel('Crossing angle factor')
ax.set_title('Comparison of simulated and theoretical crossing angle factor of gaussian beams (1 slice)')
ax.grid()
ax.legend()

# plt.savefig(r'./'+'crossingAngleFactorCompare'+'.png')
plt.show()

