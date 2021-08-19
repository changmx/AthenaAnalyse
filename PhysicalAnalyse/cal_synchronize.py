from Common.commonCalculation import energy2betagamma, energy2velocity
import numpy as np

import Common as co
from cal_centerOfMass_energy import cal_2particle_centerOfMass_energy

Brho = 86
L = 1341
quantity = 2
N_proton = 2
N_neutron = 1

mass = 0
N_total = 0
speed_light = 3e8
if N_proton == 0 and N_neutron == 0:
    mass = 1 * co.Const.MASS_ELECTRON_EV
    N_total = 1  # 只有一个电子
elif N_proton != 0 and N_neutron == 0:
    mass = 1 * co.Const.MASS_PROTON_EV
    N_total = N_proton
else:
    mass = 1 * co.Const.MASS_NUCLEON_EV
    N_total = N_proton + N_neutron

momentum_total = Brho * quantity * speed_light
momentum = momentum_total / N_total
E = np.sqrt(momentum**2 + mass**2)
Ek = E - mass

v = energy2velocity(Ek, mass)

print('Kinetic energy(GeV/u): {0:f}'.format(Ek / 1e9))
print('Momentum(GeV/c/u):     {0:f}'.format(momentum / 1e9))
print('Total energy(GeV/u):   {0:f}'.format(E / 1e9))