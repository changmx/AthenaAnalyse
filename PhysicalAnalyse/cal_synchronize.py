from Common.commonCalculation import energy2betagamma, energy2velocity
import numpy as np

import Common as co
from cal_centerOfMass_energy import cal_2particle_centerOfMass_energy

Brho = 86
L = 809.44
# L = 1341.58
quantity = 1
N_proton = 1
N_neutron = 1
f_colli_input = 100e6
Nbunch = 270

mass = 0
N_total = 0
if N_proton == 0 and N_neutron == 0:
    mass = 1 * co.Const.MASS_ELECTRON_EV
    N_total = 1  # 只有一个电子
elif N_proton != 0 and N_neutron == 0:
    mass = 1 * co.Const.MASS_PROTON_EV
    N_total = N_proton
else:
    mass = 1 * co.Const.MASS_NUCLEON_EV
    N_total = N_proton + N_neutron

momentum_total = Brho * quantity * co.Const.LIGHT_SPEED
momentum = momentum_total / N_total
print(20e9/co.Const.LIGHT_SPEED)
print(3.5e9 / co.Const.LIGHT_SPEED)
E = np.sqrt(momentum**2 + mass**2)
Ek = E - mass

v = energy2velocity(Ek, mass)
f = v / L
f_colli_cal = f * Nbunch
L_need = v / (f_colli_input / Nbunch)

print('Kinetic energy(GeV/u): {0:f}'.format(Ek / 1e9))
print('Momentum(GeV/c/u):     {0:f}'.format(momentum / 1e9))
print('Total energy(GeV/u):   {0:f}'.format(E / 1e9))
print('Revolution freq(MHz):  {0:f}'.format(f / 1e6))
print('Nbunch need:           {0:f}'.format(f_colli_input / f))
print('L_need:                {0:f}'.format(L_need))
print('L_need-L:              {0:f}'.format(L_need - L))
print('f_collision_cal(MHz):  {0:f}'.format(f_colli_cal / 1e6))
