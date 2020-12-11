import numpy as np 
import matplotlib.pyplot as plt 

q0 = np.linspace(0,0.5,100)
# xi = [0.06]
xi = [0.003,0.01,0.03,0.06,0.1]

fig,ax = plt.subplots()

for i in xi:
	dq = np.arccos(np.cos(2*np.pi*q0)-2*np.pi*i*np.sin(2*np.pi*q0))/(2*np.pi)-q0
	# ax.scatter(q0,dq,s=5,label=str(i))
	ax.plot(q0,dq,label=str(i))

ax.grid()
plt.legend()
plt.show()