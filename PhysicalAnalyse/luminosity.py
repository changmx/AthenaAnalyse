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

# ## KEKB
# beta_ex = 0.59
# beta_ey = 0.0058
# beta_px = 0.58
# beta_py= 0.007

# emit_ex = 18e-9
# emit_ey = 0.18e-9
# emit_px = 24e-9
# emit_py = 0.24e-9

# sigma_ez = 0.0087
# sigma_pz = 0.0071

# phi = 1*11e-3    # 2*phi is real angles

# Ne = 7.364e+10
# Np = 5.2858e+10
# cf = 99462

# ## KEKB
# beta_ex = 0.33
# beta_ey = 0.01
# beta_px = 0.33
# beta_py= 0.01

# emit_ex = 18e-9
# emit_ey = 0.36e-9
# emit_px = 18e-9
# emit_py = 0.36e-9

# sigma_ez = 0.0087
# sigma_pz = 0.0071

# phi = 1*11e-3    # 2*phi is real angles

# Ne = 3.3e+10
# Np = 1.4e+10
# cf = 99462*5000

# ## PEP2
# beta_ex = 0.51
# beta_ey = 0.0121
# beta_px = 0.25
# beta_py= 0.0233

# emit_ex = 22e-9
# emit_ey = 1.49e-9
# emit_px = 49e-9
# emit_py = 2.33e-9

# sigma_ez = 0.0105
# sigma_pz = 0.0125

# phi = 0*11e-3    # 2*phi is real angles

# Ne = 7.34e+10
# Np = 5.58e+10
# cf = 136312

# EicC
beta_ex = 0.2
beta_ey = 0.06
beta_px = 0.04
beta_py= 0.02

emit_ex = 60e-9
emit_ey = 60e-9
emit_px = 300e-9
emit_py = 180e-9

sigma_ez = 0.04
sigma_pz = 0.02

phi = 0*25e-3    # 2*phi is real angles

Ne = 1.7e11
Np = 1.25e11
cf = 100e6
L = cal_luminosity(Ne,Np,cf,beta_ex,beta_ey,emit_ex,emit_ey,beta_px,beta_py,emit_px,emit_py)
print('With crossing angle: ',L*cal_crossing_angle_factor_beta(beta_ex,emit_ex,sigma_ez,beta_px,emit_px,sigma_pz,phi))

print('With hourglass:',L*0.78)