import math
import os

def cal_tuneShift(N_opp,betaX,betaY,Ek,betaX_opp,betaY_opp,emitX_opp,emitY_opp,direction,particle):
	me = 0.510998950e6
	mp = 938.27208816e6
	re = 2.8179403262e-15
	rp = re*me/mp
	r0=0
	m0=0
	if particle=="electron" or particle=="positron":
		r0=re
		m0=me
	elif particle=="proton":
		r0=rp
		m0=mp
	else:
		print("Error: input wrong particle kind parameter at cal_tuneShift!")
		exit(1)

	gamma = Ek/m0 + 1
	sigmaX_opp = math.sqrt(betaX_opp*emitX_opp)
	sigmaY_opp = math.sqrt(betaY_opp*emitY_opp)
	xi = 0
	if direction=="x":
		xi = N_opp*r0*betaX/(2*math.pi*gamma*sigmaX_opp*(sigmaX_opp+sigmaY_opp))
	elif direction=="y":
		xi = N_opp*r0*betaY/(2*math.pi*gamma*sigmaY_opp*(sigmaX_opp+sigmaY_opp))
		# print('y')
	else:
		print("Error: input wrong direction parameter!")
		exit(1)
	return xi

def cal_YokoyaFactor(betaX,betaY,emitX,emitY,direction):
	sigmaX = math.sqrt(betaX*emitX)
	sigmaY = math.sqrt(betaY*emitY)
	r = sigmaY/(sigmaX+sigmaY)
	Yokoya = 0
	if direction=="x":
		Yokoya = 1.33-0.37*r+0.279*r*r
	elif direction=="y":
		Yokoya = 1.33-0.37*(1-r)+0.279*(1-r)*(1-r)
	else:
		print("Error: input wrong direction parameter in func cal_YokoyaFactor!")
		exit(1)
	return Yokoya

def cal_disruptionParameter(N_opp,Ek,betaX_opp,betaY_opp,emitX_opp,emitY_opp,sigmaZ_opp,direction,particle):
	me = 0.510998950e6
	mp = 938.27208816e6
	re = 2.8179403262e-15
	rp = re*me/mp
	r0=0
	m0=0
	if particle=="electron" or particle=="positron":
		r0=re
		m0=me
	elif particle=="proton":
		r0=rp
		m0=mp
	else:
		print("Error: input wrong particle kind parameter at cal_disruptionParameter!")
		exit(1)

	gamma = Ek/m0 + 1
	sigmaX_opp = math.sqrt(betaX_opp*emitX_opp)
	sigmaY_opp = math.sqrt(betaY_opp*emitY_opp)
	focal_distance = 0
	if direction=="x":
		focal_distance = 1/(N_opp*r0/(0.5*gamma*sigmaX_opp*(sigmaX_opp+sigmaY_opp)))
	elif direction=="y":
		focal_distance = 1/(N_opp*r0/(0.5*gamma*sigmaY_opp*(sigmaX_opp+sigmaY_opp)))
	else:
		print("Error: input wrong direction parameter in function cal_disruptionParameter!")
		exit(1)
	# print(focal_distance)
	disruption_parameter = sigmaZ_opp/focal_distance

	return disruption_parameter


if __name__ == '__main__':
	print(cal_tuneShift(1.15e11,1.25,0.05,7e12,1.25,0.05,3.75e-9,3.75e-9,'x','proton'))