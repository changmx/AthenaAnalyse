from scipy import integrate
import numpy as np
from scipy.special import iv
import matplotlib.pyplot as plt 

# 本段代码对比sicpy中iv函数与直接积分结果，结果证明论文中就是第一类修饰
# 贝塞尔函数，且scipy中iv函数可以正确进行计算。
# I0 = lambda phi,x: 1/(np.pi)*np.exp(x*np.cos(phi))

# val,err = integrate.quad(I0,0,np.pi,args=(2,))
# print(val,err)

# val2 = iv(0,2)
# print(val2)

def detuning(x):
	func = lambda phi,x: 1/(np.pi)*np.exp(x*np.cos(phi))  # Modified Bessel Function of the First Kind

	J = (x/2)**2
	I,err = integrate.quad(func,0,np.pi,args=(J,))
	delta_q = 1/J*(np.exp(-J)*I-1)

	return delta_q

fig,ax = plt.subplots()
x = []
y = []
for i in np.linspace(-10,10,1000):
	x.append(i)
	y.append(detuning(i))

ax.plot(x,y)
plt.show()
