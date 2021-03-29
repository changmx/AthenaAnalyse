import numpy as np
from data_physicalConstant import const


def energy2betagamma(total_energy_ev, invariant_mass_ev):

    # total_energy_ev = kinetic_energy_ev + invariant_mass_ev
    gamma = total_energy_ev/invariant_mass_ev
    beta = np.sqrt(1-1/(gamma*gamma))
    return beta, gamma


if __name__ == "__main__":

    v_250 = energy2betagamma(250e9, const.MASS_PROTON_EV)[
        0] * const.LIGHT_SPEED
    v_25 = energy2betagamma(25e9, const.MASS_PROTON_EV)[0] * const.LIGHT_SPEED
    print(v_250/v_25)

    L = 3000
    T_250 = L / v_250
    L_25 = v_25 * T_250
    print(L_25)

    H_250 = 2500
    f_250 = v_250 / L * H_250
    v_35_1 = energy2betagamma(20.4e9, const.MASS_PROTON_EV)[
        0] * const.LIGHT_SPEED
    H_35_1 = f_250/(v_35_1/L)
    print(H_35_1)

    H_20_4 = 2503
    # v_20_4 = L / energy2betagamma(20.4e9, const.MASS_PROTON_EV)[0]* const.LIGHT_SPEED
    v_20_4 = f_250/H_20_4*L
    beta_20_4 = v_20_4/const.LIGHT_SPEED
    gamma_20_4 = 1/np.sqrt(1-beta_20_4**2)
    e_20_4 = gamma_20_4*const.MASS_PROTON_EV
    print(e_20_4/1e9)
