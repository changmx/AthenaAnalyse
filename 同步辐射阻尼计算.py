import math

Eke = 8e9
Ekp = 8e9
rho = 104.5
C_e = 3016.26	# circumference

me = 0.510998950e6
mp = 938.27208816e6
c = 299792458
epsilon0 = 8.8541878128e-12
pi = 3.141592653589793238
e = 1.602176634e-19

gamma_e = Eke/me + 1
gamma_p = Ekp/mp + 1

beta_e = math.sqrt(1-(1/gamma_e)**2)
beta_p = math.sqrt(1-(1/gamma_p)**2)

T_e = C_e/(beta_e*c)
cf = 1/T_e*5000

P_e = 2/3*e*e*c/(4*pi*epsilon0)*beta_e**4*gamma_e**4/(rho**2) 	# total power is P times N
P_p = 2/3*e*e*c/(4*pi*epsilon0)*beta_p**4*gamma_p**4/(rho**2)
U_e = P_e*2*pi*rho/(beta_e*c)/e 	# in units of eV
U_p = P_p*2*pi*rho/(beta_p*c)/e

alpha_y = U_e/(2*Eke*T_e)
tau_y = 1/alpha_y

print("Radiaiton energy of electron   : %f MeV" %(U_e*1e-6))
print("Radiaiton energy of proton     : %e MeV" %(U_p*1e-6))
print("Damping time in the y direction: %f ms %f turns" %(tau_y*1000,tau_y/T_e))
print("Damping time in the z direction: %f ms %f turns" %(tau_y*1000/2,tau_y/2/T_e))