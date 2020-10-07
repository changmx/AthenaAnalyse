import math

Eke = 8e9
Ekp = 3.5e9
Np = 3.3e10
Ne = 1.4e10
cf = 496.96e6

me = 0.510998950e6
# mp = 938.27208816e6
mp = 0.510998950e6
re = 2.8179403262e-15
rp = 2.8179403262e-15
# rp = re*me/mp
pi = 3.141592653589793238
e = 1.602176634e-19

beta_ex = 0.33
beta_ey = 0.008
beta_px = 0.33
beta_py= 0.008

emit_ex = 1.8e-8
emit_ey = 3.6e-10
emit_px = 1.8e-8
emit_py = 3.6e-10

sigma_ez = 0.019	# calculate disruption parameter
sigma_pz = 0.05

gamma_e = Eke/me + 1
gamma_p = Ekp/mp + 1
print(gamma_e)
sigma_ex = math.sqrt(beta_ex*emit_ex)
sigma_ey = math.sqrt(beta_ey*emit_ey)
sigma_px = math.sqrt(beta_px*emit_px)
sigma_py = math.sqrt(beta_py*emit_py)

# beam-beam parameter
xi_ex = Np*re*beta_ex/(2*pi*gamma_e*sigma_px*(sigma_px+sigma_py))
xi_ey = Np*re*beta_ey/(2*pi*gamma_e*sigma_py*(sigma_px+sigma_py))
xi_px = Ne*rp*beta_px/(2*pi*gamma_p*sigma_ex*(sigma_ex+sigma_ey))
xi_py = Ne*rp*beta_py/(2*pi*gamma_p*sigma_ey*(sigma_ex+sigma_ey))

# focal distance
f_ex = 1/(Np*re/(0.5*sigma_px*(sigma_px+sigma_py)*gamma_e))
f_ey = 1/(Np*re/(0.5*sigma_py*(sigma_px+sigma_py)*gamma_e))
f_px = 1/(Ne*rp/(0.5*sigma_ex*(sigma_ex+sigma_ey)*gamma_p))
f_py = 1/(Ne*rp/(0.5*sigma_ey*(sigma_ex+sigma_ey)*gamma_p))

# disruption parameter
D_ex = sigma_pz/f_ex
D_ey = sigma_pz/f_ey
D_px = sigma_ez/f_px
D_py = sigma_ez/f_py

L = Ne*Np*cf/(2*pi*math.sqrt(sigma_ex**2+sigma_px**2)*math.sqrt(sigma_ey**2+sigma_py**2))*1e-4

print("Beam-beam parameter for proton   x: %f, y: %f" % (xi_px,xi_py))
print("Beam-beam parameter for electron x: %f, y: %f" % (xi_ex,xi_ey))
print("Disruption factor for proton     x: %f, y: %f" % (D_ex,D_ey))
print("Disruption factor for electron   x: %f, y: %f" % (D_px,D_py))
print("Luminosity: %e" % (L))

L2 = gamma_e*1.1/(e*2*re*beta_ey)*xi_ey*1e-4
print(L2)