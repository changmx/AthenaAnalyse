from scipy import integrate
import numpy as np
from scipy.special import iv
import matplotlib.pyplot as plt 

# 本段代码对比sicpy中iv函数与直接积分结果，证明论文中就是第一类修饰
# 贝塞尔函数，且scipy中iv函数可以正确进行计算。
# I0 = lambda phi,x: 1/(np.pi)*np.exp(x*np.cos(phi))

# val,err = integrate.quad(I0,0,np.pi,args=(2,))
# print(val,err)

# val2 = iv(0,2)
# print(val2)

def detuning_1d(x):
	# func = lambda phi,x: 1/(np.pi)*np.exp(x*np.cos(phi))  # Modified Bessel Function of the First Kind
	# I,err = integrate.quad(func,0,np.pi,args=(J,))
	J = (x/2)**2
	I = iv(0,J)
	delta_q = 1/J*(1-np.exp(-J)*I)

	return delta_q

def detuning_1d2(xmax,ymax):
	sigma_x = 1
	R = np.sqrt(xmax*xmax+1)
	# t = x/np.sqrt(x*x+y*y)
	# func = lambda x: -1/(x*x)+1/(x*x)*np.exp(-x*x/(2*sigma_x*sigma_x))+1/(sigma_x*sigma_x)*np.exp(-x*x/(2*sigma_x*sigma_x))
	func = lambda phi,x,y: (1-np.exp(((-(x*x+y*y)*x/np.sqrt(x*x+y*y))*np.cos(phi)*np.cos(phi))/(2*sigma_x*sigma_x)))/((x*x+y*y)*x/np.sqrt(x*x+y*y))
	val,err = integrate.quad(func,0,2*np.pi,args=(xmax,ymax,))
	val = val/(2*np.pi)*4
	val2,err = integrate.quad(func,0,2*np.pi,args=(ymax,xmax,))
	val2 = val2/(2*np.pi)*4
	return val,val2
# def detunint_2d(Ax,Ay,sigma_x,sigma_y,xi_x=1,xi_y=1):

# 	r =  np.sqrt(Ax*Ax*sigma_x*sigma_x+Ay*Ay*sigma_y*sigma_y)
# 	J = r**2/(2*(sigma_x*sigma_x+sigma_y*sigma_y))
# 	I = iv(0,J)
# 	if Ax == 0 and Ay == 0:
# 		delta_qx=-xi_x
# 		delta_qy=-xi_y
# 	elif Ax == 0 and Ay != 0:
# 		delta_qx=-xi_x
# 		delta_qy = xi_y/J*(np.exp(-J)*I-1)*np.sqrt(Ay*Ay*sigma_y*sigma_y)/r
# 	elif Ax != 0 and Ay == 0:
# 		delta_qx = xi_x/J*(np.exp(-J)*I-1)*np.sqrt(Ax*Ax*sigma_x*sigma_x)/r 
# 		delta_qy=-xi_y
# 	else:
# 		delta_qx = xi_x/J*(np.exp(-J)*I-1)*np.sqrt(Ax*Ax*sigma_x*sigma_x)/r
# 		delta_qy = xi_y/J*(np.exp(-J)*I-1)*np.sqrt(Ay*Ay*sigma_y*sigma_y)/r
	
def detuning_2d(Ax,Ay,sigma_x,sigma_y,xi_x=1,xi_y=1):

	x = Ax*sigma_x
	y = Ay*sigma_y
	r =  np.sqrt(x**2+y**2)
	Jx = x**2/(2*sigma_x*(sigma_x+sigma_y))
	Jy = y**2/(2*sigma_y*(sigma_x+sigma_y))
	# Jx = r**2*x/r/(2*sigma_x*(sigma_x+sigma_x))
	# Jy = r**2*y/r/(2*sigma_y*(sigma_x+sigma_y))
	J = r**2/(2*(sigma_x*sigma_x+sigma_y*sigma_y))
	Ix = iv(0,Jx)
	Iy = iv(0,Jy)

	part1 = np.exp(-Jx)*Ix
	part2 = np.exp(-Jy)*Iy
	delta_q = 1/J*(1-part1*part2)
	# delta_qx = xi_x*(1-part1*part2)/Jx
	# delta_qy = xi_y*(1-part1*part2)/Jy

	if Ax == 0 and Ay == 0:
		delta_qx=xi_x
		delta_qy=xi_y
	# # elif Ax == 0 and Ay != 0:
	# # 	delta_qx=-xi_x
	# # 	delta_qy = xi_y/Jy*(np.exp(-Jy)*Iy-1)
	# # elif Ax != 0 and Ay == 0:
	# # 	delta_qx = xi_x/Jx*(np.exp(-Jx)*Ix-1)
	# # 	delta_qy=-xi_y
	else:
		# delta_qx = xi_x/Jx*(1-np.exp(-Jx)*Ix)
		# delta_qy = xi_y/Jy*(1-np.exp(-Jy)*Iy)
		delta_qx = xi_x/J*(1-np.exp(-Jx)*Ix*np.exp(-Jy))
		delta_qy = xi_y/J*(1-np.exp(-Jy)*Iy*np.exp(-Jx))
	

	
	return delta_qx,delta_qy

if __name__ == '__main__':
	
	# print(detuning_1d2(4,0))
	print('1',detuning_1d(10))
	print('2',detuning_2d(10,0,1,1))
	sigma_x = 1
	sigma_y = 1
	xi_x = 1
	xi_y = 1
	print('iv',iv(0,0))
	fig,ax = plt.subplots()
	x = []
	y1 = []
	y2 = []
	# for i in np.linspace(0,6):
	# 	x.append(i)
	# 	y1.append(detuning_1d(i))
	# 	y2.append(detuning_1d2(i,0))

	# 		# print(-detuning_1d2(i,j)/detuning_1d(i))
	# ax.plot(x,y1,label='1d')
	# ax.plot(x,y2,label='1d2')
	# # y1 = detuning_1d(x)
	# # y2 = detuning_1d2(x)
	# ax.plot(x,y1,label='1d')
	# ax.plot(x,y2,label='1d2')
	Am = 6  # 振幅范围，Am=10即计算到10倍振幅范围
	Amx = 5
	Amy = 5
	Ax = [[] for i in range(Amy)]
	Ay = [[] for i in range(Amy)]
	# print(A)
	
	for x in range(0,Amx):
		# print(x)
		# print(Ax)
		# dq_x=[]
		# dq_y=[]
		# Ayl=[]
		for y in range(0,Amy):
			# print('y',y)
			# dq_x.append(detuning_2d(x,y,sigma_x,sigma_y,xi_x,xi_y)[0])
			# dq_y.append(detuning_2d(x,y,sigma_x,sigma_y,xi_x,xi_y)[1])
			# dq_x.append(detuning_1d2(Ax,Ay)[0]*1)
			# dq_y.append(detuning_1d2(Ax,Ay)[1]*1)
			# Ayl.append(Ay)
			# ax.scatter(dq_x,dq_y)
			Ax[x].append(detuning_2d(x,y,sigma_x,sigma_y,xi_x,xi_y)[0])
			Ay[x].append(detuning_2d(x,y,sigma_x,sigma_y,xi_x,xi_y)[1])
		# ax.plot(dq_x,dq_y)
		for i in range(0,Amy):
			ax.text(Ax[x][i],Ay[x][i],(round(x,2),round(i,2)))
		# for i in range(0,len(Ay[0])):
		# 	ax.text(dq_x[i],dq_y[i],(round(Ax,2),round(Ayl[i],2)))
	for i in range(0,Amx):
		ax.plot(Ax[i],Ay[i])
	for i in range(0,Amy):
		dqx2=[]
		dqy2=[]
		for j in range(0,Amx):
			dqx2.append(Ax[j][i])
			dqy2.append(Ay[j][i])
		ax.plot(dqx2,dqy2)
	# print(Ax)
	# print(Ay)
	ax.set_xlabel(r'$\Delta \nu_x/\xi_x$')
	ax.set_ylabel(r'$\Delta \nu_y/\xi_y$')
	ax.grid()
	# Ax=0.01
	# dq_x=[]
	# dq_y=[]
	# Ayl=[]
	# for Ay in np.linspace(1,20,6):
			
	# 	dq_x.append(-detunint_2d(Ax,Ay,sigma_x,sigma_y,xi_x,xi_y)[0])
	# 	dq_y.append(-detunint_2d(Ax,Ay,sigma_x,sigma_y,xi_x,xi_y)[1])
	# 	Ayl.append(Ay)
	# 	ax.scatter(dq_x,dq_y)
	# for i in range(0,len(Ayl)):
	# 	ax.text(dq_x[i],dq_y[i],(int(Ax),int(Ayl[i])))
		
		# ax.plot(dq_x,dq_y)
	# ax.scatter(0.28,0.31)
	# ax.scatter(1,1)
		# print(dq_x)
		# print(dq_y,'\n')
	# ax.plot([0.25,0.3],[0.25,0.3])

	# dq_x=[]
	# dq_x.append(0.3+detunint_2d(Am,Am,sigma_x,sigma_y,xi_x,xi_y)[0])

	# Ax = 0
	# dq_x=[]
	# dq_y=[]
	# Ax = 0
	# for Ay in np.linspace(0.1,10,10):
			
	# 	dq_x.append(-detunint_2d(Ax,Ay,sigma_x,sigma_y,xi_x,xi_y)[0])
	# 	dq_y.append(-detunint_2d(Ax,Ay,sigma_x,sigma_y,xi_x,xi_y)[1])

	# ax.plot(dq_x,dq_y)
	# print(dq_x,dq_y)
	# I0 = lambda phi,x: 1/(np.pi)*np.exp(x*np.cos(phi))

	# val,err = integrate.quad(I0,0,np.pi,args=(2,))
	# print(val,err)

	# val2 = iv(0,2)
	# print(val2)
	# plt.legend()
	plt.show()


