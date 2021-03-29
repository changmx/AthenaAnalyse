import numpy as np 

x, px, y, py, z = np.loadtxt(r"E:\changmx\bb2019\distribution\2020_0928\1005_proton_turn1_bunch0_10000.csv", delimiter=',',skiprows=1, usecols=(0, 1, 2, 3, 4), unpack=True)

np = 10000
slice = 100
npPerSlice = 100
sigma_x = []

for i in range(0,slice,1):
	xt = 0.0
	pxt = 0.0
	xpxt = 0.0
	zt = 0.0
	for j in range(0,npPerSlice,1):
		k = i*npPerSlice+j
		xt += x[k]*x[k]
		pxt += px[k]*px[k]
		xpxt += x[k]*px[k]
		zt += z[k]
	xt /= npPerSlice
	pxt /= npPerSlice
	xpxt /= npPerSlice
	zt /= npPerSlice
	# print(i,xt,pxt,xpxt)
	sigmax = (xt*pxt-xpxt*xpxt)**0.5
	print(i,zt,sigmax)
	# sigma_x.append(sigmax)

# print(sigma_x)