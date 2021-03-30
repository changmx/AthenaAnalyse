import Common as co
import numpy as np

v_250 = co.energy2velocity(250e9 - co.const.MASS_NUCLEON_EV, co.const.MASS_NUCLEON_EV)
v_25 = co.energy2velocity(35.1e9 - co.const.MASS_NUCLEON_EV, co.const.MASS_NUCLEON_EV)
print("v250/v25 = %f" % (v_250 / v_25))

L = 3000
T_250 = L / v_250
L_25 = v_25 * T_250
print("L 25Gev = %f" % L_25)

H_250 = 2500
f_250 = v_250 / L * H_250
v_35_1 = co.energy2velocity(35.1e9 - co.const.MASS_NUCLEON_EV, co.const.MASS_NUCLEON_EV)
H_35_1 = f_250 / (v_35_1 / L)
print(H_35_1)

H_20_4 = 2501
v_20_4 = f_250 / H_20_4 * L
beta_20_4 = v_20_4 / co.const.LIGHT_SPEED
gamma_20_4 = 1 / np.sqrt(1 - beta_20_4 ** 2)
e_20_4 = gamma_20_4 * co.const.MASS_NUCLEON_EV
print(e_20_4 / 1e9)
