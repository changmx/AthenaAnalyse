import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

me = 0.51099895e6
mp = 938.27208816e6
re = 2.8179403262e-15
rp = re*me/mp
epsilon0 = 8.854187817e-12
e = 1.602176565e-19
c = 299792458

Ek_e = 3.5e9
Ek_p = 19.08e9

gamma_e = Ek_e/me+1
gamma_p = Ek_p/mp+1

beta_e = math.sqrt(1-1/(gamma_e*gamma_e))
beta_p = math.sqrt(1-1/(gamma_p*gamma_p))

p0_e = gamma_e*me*e*beta_e/c
p0_p = gamma_p*mp*e*beta_p/c

Ne = 6.8e11
Np = 1.04e11

emit_e_x = 6.0e-8
emit_e_y = 6.0e-8
beta_e_x = 0.2
beta_e_y = 0.2

emit_p_x = 3.0e-7
emit_p_y = 3.0e-7
beta_p_x = 0.04
beta_p_y = 0.04

Ngrid = 256
gridLen = 5e-6
stride = 1e-6

sigma_e_x = math.sqrt(beta_e_x*emit_e_x)
sigma_e_y = math.sqrt(beta_e_y*emit_e_y)
sigma_p_x = math.sqrt(beta_p_x*emit_p_x)
sigma_p_y = math.sqrt(beta_p_y*emit_p_y)

dpx_e = []
dpy_e = []
dpx_e_2 = []
dpy_e_2 = []
x = []
y = []

def delta_p(r0, N, gamma, sigma, r):
	dp = -2*N*r0/(gamma*r)*(1-math.exp(-r*r/(2*sigma*sigma)))
	return dp

def cal_F(N, sigma, r):
	epsilon0 = 8.854187817e-12
	e = 1.602176565e-19
	F = - N*e*e/(2*math.pi*epsilon0*r)*(1-math.exp(-r*r/(2*sigma*sigma)))
	print(F)
	return F

def delta_p_2(N, sigma, r, p0):
	dp = cal_F(N,sigma,r)/p0/c;
	return dp

for start in np.arange(-(Ngrid / 2) * gridLen, (Ngrid / 2) * gridLen, stride):
    r_x = start
    r_y = start
    dpx_tmp = delta_p(re,Np,gamma_e,sigma_p_x,r_x)
    dpy_tmp = delta_p(re,Np,gamma_e,sigma_p_y,r_y)
    
    dpx_e.append(dpx_tmp)
    dpy_e.append(dpy_tmp)
    x.append(r_x)
    y.append(r_y)

    dpx_tmp_2 = delta_p_2(Np,sigma_p_x,r_x,p0_e)
    dpy_tmp_2 = delta_p_2(Np,sigma_p_y,r_y,p0_e)
    dpx_e_2.append(dpx_tmp_2)
    dpy_e_2.append(dpy_tmp_2)

ax1 = plt.subplot(1,2,1)
ax1.plot(x,dpx_e)
ax1.plot(x,dpx_e_2)
ax1.set_title('electron dpx')
ax1.set_xlabel('x')
ax1.set_ylabel('dpx')

ax2 = plt.subplot(1,2,2)
ax2.plot(y,dpy_e)
ax2.plot(y,dpy_e_2)
ax2.set_title('electron dpy')
ax2.set_xlabel('y')
ax2.set_ylabel('dpy')

plt.show()