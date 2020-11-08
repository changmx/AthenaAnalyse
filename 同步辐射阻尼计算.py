import math

Eke = 8e9
Ekp = 3.5e9
rho_e = 104.5
rho_p = 16.3
C_e = 3016.26	# circumference
C_p = 3016.26

me = 0.510998950e6
mp = 0.510998950e6
# me = 938.27208816e6
# mp = 938.27208816e6

c = 299792458
epsilon0 = 8.8541878128e-12
pi = 3.141592653589793238
e = 1.602176634e-19

gamma_e = Eke/me + 1
gamma_p = Ekp/mp + 1

beta_e = math.sqrt(1-(1/gamma_e)**2)
beta_p = math.sqrt(1-(1/gamma_p)**2)

T_e = C_e/(beta_e*c)
T_p = C_p/(beta_p*c)

P_e = 2/3*e*e*c/(4*pi*epsilon0)*beta_e**4*gamma_e**4/(rho_e**2) 	# total power is P times N
P_p = 2/3*e*e*c/(4*pi*epsilon0)*beta_p**4*gamma_p**4/(rho_p**2)
U_e = P_e*2*pi*rho_e/(beta_e*c)/e 	# in units of eV
U_p = P_p*2*pi*rho_p/(beta_p*c)/e

alpha_y_e = U_e/(2*Eke*T_e)
tau_y_e = 1/alpha_y_e
alpha_y_p = U_p/(2*Ekp*T_p)
tau_y_p = 1/alpha_y_p

print("Radiaiton energy of electron   : %e eV" %(U_e))
print("Radiaiton energy of proton     : %e eV" %(U_p))
print("Damping time in the y direction of proton  : %f ms %f turns" %(tau_y_p*1000,tau_y_p/T_p))
print("Damping time in the z direction of proton  : %f ms %f turns" %(tau_y_p*1000/2,tau_y_p/2/T_p))
print("Damping time in the y direction of electron: %f ms %f turns" %(tau_y_e*1000,tau_y_e/T_e))
print("Damping time in the z direction of electron: %f ms %f turns" %(tau_y_e*1000/2,tau_y_e/2/T_e))