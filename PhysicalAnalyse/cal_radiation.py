import math
import numpy as np 
import matplotlib.pyplot as plt

def radiation(Ek=0,rho=1,circumference=1,particle='electron'):
	
	c = 299792458
	epsilon0 = 8.8541878128e-12
	pi = 3.141592653589793238
	e = 1.602176634e-19
	m0 = 0
	me = 0.510998950e6
	mp = 938.27208816e6

	if particle=='electron':
		m0 = me
	elif particle=='proton':
		m0 = mp
	else:
		print('Error: Input wrong particle parameter @ func radiation')

	gamma = Ek/m0 + 1
	beta = math.sqrt(1-(1/gamma)**2)
	T = circumference/(beta*c)
	# T = (2*pi*rho)/(beta*c)
	P = 2/3*e*e*c/(4*pi*epsilon0)*beta**4*gamma**4/(rho**2) 	# total power is U(energy, eV) times I(intensity, A)
	U = P*2*pi*rho/(beta*c)/e 	# in units of eV
	alpha_y = U/(2*Ek*T)
	tau_y = 1/alpha_y
	tau_z = tau_y/2
	print('Ratiation energy of %s    : %f MeV' %(particle,U/1e6))
	print('Revolution period               : %e s' %(T))
	print("Damping time in the z direction : %f ms, %f turns" %(tau_z*1000,tau_z/T))
	print("Damping time in the y direction : %f ms, %f turns" %(tau_y*1000,tau_y/T))


if __name__ == '__main__':
	pass
	# radiation(Ek=2.2e9,rho=10.53,circumference=240.4,particle='electron')  # BEPC S.Y.Lee
	# radiation(Ek=6e9,rho=60,circumference=768.4,particle='electron')  # CESR S.Y.Lee
	# radiation(Ek=3.2e9,rho=30.6,circumference=2199.3,particle='electron')  # LER S.Y.Lee
	# radiation(Ek=9e9,rho=165,circumference=2199.3,particle='electron')  # HER S.Y.Lee
	# radiation(Ek=3.5e9,rho=16.3,circumference=3016.26,particle='electron')  # LER KEKB design repport
	radiation(Ek=8e9,rho=104.5,circumference=3016.26,particle='electron')  # HER2 KEKB design report
	# radiation(Ek=7e9,rho=38.96,circumference=1104,particle='electron')  # APS S.Y.Lee
	# radiation(Ek=1.5e9,rho=4.01,circumference=196.8,particle='electron')  # ALS S.Y.Lee
	# radiation(Ek=55e9,rho=3096.2,circumference=26658.9,particle='electron')  # LEP S.Y.Lee
	# radiation(Ek=7000e9,rho=3096.2,circumference=26658.9,particle='proton')  # LHC S.Y.Lee
	radiation(Ek=3.5e9,rho=28,circumference=819,particle='electron')  # EicC