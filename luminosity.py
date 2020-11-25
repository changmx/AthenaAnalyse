import matplotlib.pyplot as plt
import numpy as np
import math
from crossingAngle import cal_crossing_angle_factor_beta

def cal_luminosity(N1,N2,collisionFrenquency,betaX1,betaY1,emitX1,emitY1,betaX2,betaY2,emitX2,emitY2,):
	sigmaX1 = math.sqrt(betaX1*emitX1)
	sigmaY1 = math.sqrt(betaY1*emitY1)
	sigmaX2 = math.sqrt(betaX2*emitX2)
	sigmaY2 = math.sqrt(betaY2*emitY2)
	L = N1*N2*collisionFrenquency/(2*math.pi*math.sqrt(sigmaX1**2+sigmaX2**2)*math.sqrt(sigmaY1**2+sigmaY2**2))*1e-4
	print('Luminosity: %e'%(L))
	return L


beta_ex = 0.62
beta_ey = 0.073
beta_px = 0.94
beta_py= 0.042

emit_ex = 24.4e-9
emit_ey = 3.5e-9
emit_px = 16e-9
emit_py = 6.1e-9

sigma_ez = 0.01
sigma_pz = 0.07

phi = 0*11e-3    # 2*phi is real angles

Np = 1.11e11
Ne = 3.05e11
# cf = 496.96e6
# cf = 99462
# cf=330*78250
cf=25e6


L = cal_luminosity(Ne,Np,cf,beta_ex,beta_ey,emit_ex,emit_ey,beta_px,beta_py,emit_px,emit_py)
print(L*0.8642)