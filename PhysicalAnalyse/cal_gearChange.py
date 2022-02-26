from typing import Text
import Common as co
import numpy as np

# v_250 = co.energy2velocity(250e9 - co.Const.MASS_NUCLEON_EV, co.Const.MASS_NUCLEON_EV)
# v_25 = co.energy2velocity(25e9 - co.Const.MASS_NUCLEON_EV, co.Const.MASS_NUCLEON_EV)
# print("v250/v25 = %f" % (v_250 / v_25))

# L = 3000
# T_250 = L / v_250
# L_25 = v_25 * T_250
# print("L 25Gev = %f" % L_25)

# H_250 = 2500
# f_250 = v_250 / L * H_250
# v_35_1 = co.energy2velocity(35.1e9 - co.Const.MASS_NUCLEON_EV, co.Const.MASS_NUCLEON_EV)
# H_35_1 = f_250 / (v_35_1 / L)
# print(H_35_1)

# H_20_4 = 2501
# v_20_4 = f_250 / H_20_4 * L
# beta_20_4 = v_20_4 / co.Const.LIGHT_SPEED
# gamma_20_4 = 1 / np.sqrt(1 - beta_20_4 ** 2)
# e_20_4 = gamma_20_4 * co.Const.MASS_NUCLEON_EV
# print(e_20_4 / 1e9)

v_p = co.energy2velocity(19.08e9, co.Const.MASS_PROTON_EV)
v_e = co.energy2velocity(3.5e9, co.Const.MASS_ELECTRON_EV)
print("vp = {0:f}, ve = {1:f}, vp/ve = {2:f}".format(v_p, v_e, v_p / v_e))

L_p = 1341.58
# L_e = 809.44
L_e = 1341.58
T_p = L_p / v_p
T_e = L_e / v_e
print("Tp = {0:f}, Te = {1:f}".format(T_p*1e9, T_e*1e9))

L_diff = (T_e-T_p)*3e8
print('L diff = {0:f}'.format(L_diff))
# H_250 = 2500
# f_250 = v_250 / L * H_250
# v_35_1 = co.energy2velocity(35.1e9 - co.Const.MASS_NUCLEON_EV, co.Const.MASS_NUCLEON_EV)
# H_35_1 = f_250 / (v_35_1 / L)
# print(H_35_1)

# H_20_4 = 2501
# v_20_4 = f_250 / H_20_4 * L
# beta_20_4 = v_20_4 / co.Const.LIGHT_SPEED
# gamma_20_4 = 1 / np.sqrt(1 - beta_20_4 ** 2)
# e_20_4 = gamma_20_4 * co.Const.MASS_NUCLEON_EV
# print(e_20_4 / 1e9)
