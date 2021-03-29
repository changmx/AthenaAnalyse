import Common as co
import numpy as np

v_250 = co.energy2betagamma(250e9, co.const.MASS_PROTON_EV)[
    0] * co.const.LIGHT_SPEED
v_25 = co.energy2betagamma(25e9, co.const.MASS_PROTON_EV)[0] * co.const.LIGHT_SPEED
print(v_250/v_25)

L = 3000
T_250 = L / v_250
L_25 = v_25 * T_250
print(L_25)

H_250 = 2500
f_250 = v_250 / L * H_250
v_35_1 = co.energy2betagamma(20.4e9, co.const.MASS_PROTON_EV)[
    0] * co.const.LIGHT_SPEED
H_35_1 = f_250/(v_35_1/L)
print(H_35_1)

H_20_4 = 2503
# v_20_4 = L / co.energy2betagamma(20.4e9, co.const.MASS_PROTON_EV)[0]* co.const.LIGHT_SPEED
v_20_4 = f_250/H_20_4*L
beta_20_4 = v_20_4/co.const.LIGHT_SPEED
gamma_20_4 = 1/np.sqrt(1-beta_20_4**2)
e_20_4 = gamma_20_4*co.const.MASS_PROTON_EV
print(e_20_4/1e9)
