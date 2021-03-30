import numpy as np
from physicalConstant import const


def energy2betagamma(kinetic_energy_ev, invariant_mass_ev):
    "Calculate the Lorentz factor from the kinetic energy"
    total_energy_ev = kinetic_energy_ev + invariant_mass_ev
    gamma = total_energy_ev / invariant_mass_ev
    beta = np.sqrt(1 - 1 / (gamma * gamma))

    return beta, gamma


def energy2velocity(kinetic_energy_ev, invariant_mass_ev):
    "Calculate the velocity from the kinetic energy"
    beta, _ = energy2betagamma(kinetic_energy_ev, invariant_mass_ev)

    return beta * const.LIGHT_SPEED


def intensity(kinetic_energy_ev, invariant_mass_ev, circumference, npPerBunch, nBunch):
    "Calculate beam intensity"
    T = circumference / energy2velocity(kinetic_energy_ev, invariant_mass_ev)
    I = npPerBunch * nBunch * const.ELEMENTARY_CHARGE / T

    return I


def sigma(beta, emit):
    "Calculate beam size from twiss beta and emittence"

    return np.sqrt(beta * emit)


if __name__ == "__main__":

    pass
