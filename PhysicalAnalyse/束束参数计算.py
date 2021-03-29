import math
from tuneShift import cal_tuneShift
from tuneShift import cal_YokoyaFactor
from tuneShift import cal_disruptionParameter

Eke = 1.89e9
Ekp = 1.89e9
Np = 4.85e10
Ne = 4.85e10
# cf = 496.96e6
cf = 99462

me = 0.510998950e6
# mp = 938.27208816e6
mp = 0.510998950e6
re = 2.8179403262e-15
rp = 2.8179403262e-15
# rp = re*me/mp
pi = 3.141592653589793238
e = 1.602176634e-19

beta_ex = 1
beta_ey = 0.015
beta_px = 1
beta_py= 0.015

emit_ex = 144e-9
emit_ey = 2.2e-9
emit_px = 144e-9
emit_py = 2.2e-9

sigma_ez = 0.004	# calculate disruption parameter and crossing angle factor
sigma_pz = 0.004

phi = 2*11e-3		# 2*phi is real angle
gamma_e = Eke/me + 1
gamma_p = Ekp/mp + 1

sigma_ex = math.sqrt(beta_ex*emit_ex)
sigma_ey = math.sqrt(beta_ey*emit_ey)
sigma_px = math.sqrt(beta_px*emit_px)
sigma_py = math.sqrt(beta_py*emit_py)

# beam-beam parameter
xi_ex = cal_tuneShift(Np,beta_ex,beta_ey,Eke,beta_px,beta_py,emit_px,emit_py,"x","electron")
xi_ey = cal_tuneShift(Np,beta_ex,beta_ey,Eke,beta_px,beta_py,emit_px,emit_py,"y","electron")
xi_px = cal_tuneShift(Ne,beta_px,beta_py,Ekp,beta_ex,beta_ey,emit_ex,emit_ey,"x","electron")
xi_py = cal_tuneShift(Ne,beta_px,beta_py,Ekp,beta_ex,beta_ey,emit_ex,emit_ey,"y","electron")

# Yokoya factor
Yokoya_e_x = cal_YokoyaFactor(beta_ex,beta_ey,emit_ex,emit_ey,"x")
Yokoya_e_y = cal_YokoyaFactor(beta_ex,beta_ey,emit_ex,emit_ey,"y")
Yokoya_p_x = cal_YokoyaFactor(beta_px,beta_py,emit_px,emit_py,"x")
Yokoya_p_y = cal_YokoyaFactor(beta_px,beta_py,emit_px,emit_py,"y")

# disruption parameter
D_ex = cal_disruptionParameter(Np,Eke,beta_px,beta_py,emit_px,emit_py,sigma_pz,"x","electron")
D_ey = cal_disruptionParameter(Np,Eke,beta_px,beta_py,emit_px,emit_py,sigma_pz,"y","electron")
D_px = cal_disruptionParameter(Ne,Ekp,beta_ex,beta_ey,emit_ex,emit_ey,sigma_ez,"x","electron")
D_py = cal_disruptionParameter(Ne,Ekp,beta_ex,beta_ey,emit_ex,emit_ey,sigma_ez,"y","electron")

print("sigma of proton   x: %f, y: %f" % (sigma_px,sigma_py))
print("sigma of electron x: %f, y: %f" % (sigma_ex,sigma_ey))
print("Beam-beam parameter for proton   x: %f, y: %f" % (xi_px,xi_py))
print("Beam-beam parameter for electron x: %f, y: %f" % (xi_ex,xi_ey))
print("Yokoya factor for proton         x: %f, y: %f" % (Yokoya_p_x,Yokoya_p_y))
print("Yokoya factor for electron       x: %f, y: %f" % (Yokoya_e_x,Yokoya_e_y))
print("Tune shift for proton            x: %f, y: %f" % (Yokoya_p_x*xi_px,Yokoya_p_y*xi_py))
print("Tune shift for electron          x: %f, y: %f" % (Yokoya_e_x*xi_ex,Yokoya_e_y*xi_ey))
print("Disruption factor for proton     x: %f, y: %f" % (D_px,D_py))
print("Disruption factor for electron   x: %f, y: %f" % (D_ex,D_ey))

L2 = gamma_e*1.1/(e*2*re*beta_ey)*xi_ey*1e-4
print(L2)