import matplotlib.pyplot as plt
import numpy as np
import math
from crossingAngle import cal_crossing_angle_factor_beta

beta_ex = 0.33
beta_ey = 0.008
beta_px = 0.33
beta_py= 0.008

emit_ex = 18e-9
emit_ey = 0.36e-9
emit_px = 18e-9
emit_py = 0.36e-9

sigma_ez = 0.004
sigma_pz = 0.004

phi = 2*11e-3    # 2*phi is real angles

Np = 0.045e10
Ne = 0.02e10
# cf = 496.96e6
cf = 99462

def cal_luminosity(N1,N2,collisionFrenquency,betaX1,betaY1,emitX1,emitY1,betaX2,betaY2,emitX2,emitY2,):
	sigmaX1 = math.sqrt(betaX1*emitX1)
	sigmaY1 = math.sqrt(betaY1*emitY1)
	sigmaX2 = math.sqrt(betaX2*emitX2)
	sigmaY2 = math.sqrt(betaY2*emitY2)
	L = N1*N2*collisionFrenquency/(2*math.pi*math.sqrt(sigmaX1**2+sigmaX2**2)*math.sqrt(sigmaY1**2+sigmaY2**2))*1e-4
	
	return L

L = cal_luminosity(Ne,Np,cf,beta_ex,beta_ey,emit_ex,emit_ey,beta_px,beta_py,emit_px,emit_py)