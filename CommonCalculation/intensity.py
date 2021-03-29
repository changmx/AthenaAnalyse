import math

def cal_intensity(Ek,circumference,npPerBunch,nBunch,particle):
	m=0
	c = 299792458
	e = 1.602176634e-19

	if particle=='electron' or particle=='positron':
		m=0.510998950e6
	elif particle=='proton':
		m=938.27208816e6
	else:
		print("Error: input wrong particle parameter at cal_intensity!")
		exit(1)

	gamma = Ek/m + 1
	beta = math.sqrt(1-(1/gamma)**2)
	T = circumference/(beta*c)

	I = npPerBunch*nBunch*e/T

	return I

if __name__ == '__main__':
	
	# KEKB parameter
	Ek = 8e9
	circumference = 3016.26
	npPerBunch = 1.4e10
	nBunch = 5000

	## eRHIC parameter
	# Ek = 10e9
	# circumference = 3833.845
	# npPerBunch = 3.05e11
	# nBunch = 330

	# I = cal_intensity(Ek,circumference,npPerBunch,nBunch,'electron')
	# print("Beam current: %f A" % (I))Ek = 10e9

	## BEPC2 parameter
	# Ek = 1.89e9
	# circumference = 237.53
	# npPerBunch = 4.85e10
	# nBunch = 1

	I = cal_intensity(Ek,circumference,npPerBunch,nBunch,'electron')
	print("Beam current: %f A" % (I))


