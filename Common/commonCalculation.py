import numpy as np
from Common.physicalConstant import Const
import numpy.fft as nf


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


def intensity(kinetic_energy_ev, invariant_mass_ev, circumference, npPerBunch,
              nBunch):
    "Calculate beam intensity"
    T = circumference / energy2velocity(kinetic_energy_ev, invariant_mass_ev)
    I = npPerBunch * nBunch * const.ELEMENTARY_CHARGE / T

    return I


def sigma(beta, emit):
    "Calculate beam size from twiss beta and emittence"

    return np.sqrt(beta * emit)


def cal_freq_fft(N, T, freq_start, freq_end):
    freq = np.arange(0, 1, 1 / N)
    for i in range(freq.shape[0]):
        freq[i] = freq[i] / T
    freq_part = freq[range(int(freq_start * T * N), int(freq_end * T * N))]

    return freq_part


def cal_spctrum_fft(N, T, freq_start, freq_end, sequence):
    spectrum = np.abs(nf.fft(sequence))
    spectrum_part = spectrum[range(int(freq_start * T * N),
                                   int(freq_end * T * N))]

    return spectrum_part


def cal_tuneShift(
    N_opp,
    betaX,
    betaY,
    Ek,
    sigmaX_opp,
    sigmaY_opp,
    invariant_mass_ev,
    classical_radius,
):
    _, gamma = energy2betagamma(Ek, invariant_mass_ev)

    xi_x = (N_opp * classical_radius * betaX /
            (2 * np.pi * gamma * sigmaX_opp * (sigmaX_opp + sigmaY_opp)))
    xi_y = (N_opp * classical_radius * betaY /
            (2 * np.pi * gamma * sigmaY_opp * (sigmaX_opp + sigmaY_opp)))

    return xi_x, xi_y


def cal_YokoyaFactor(sigmaX, sigmaY):
    r = sigmaY / (sigmaX + sigmaY)

    Yokoya_x = 1.33 - 0.37 * r + 0.279 * r * r
    Yokoya_y = 1.33 - 0.37 * (1 - r) + 0.279 * (1 - r) * (1 - r)

    return Yokoya_x, Yokoya_y


def cal_disruptionParameter(
    N_opp,
    Ek,
    sigmaX_opp,
    sigmaY_opp,
    sigmaZ_opp,
    invariant_mass_ev,
    classical_radius,
):
    _, gamma = energy2betagamma(Ek, invariant_mass_ev)

    focal_distance_x = 1 / (N_opp * classical_radius /
                            (0.5 * gamma * sigmaX_opp * (sigmaX_opp + sigmaY_opp)))
    focal_distance_y = 1 / (N_opp * classical_radius /
                            (0.5 * gamma * sigmaY_opp * (sigmaX_opp + sigmaY_opp)))

    disruption_parameter_x = sigmaZ_opp / focal_distance_x
    disruption_parameter_y = sigmaZ_opp / focal_distance_y

    return disruption_parameter_x, disruption_parameter_y


if __name__ == "__main__":

    print(np.pi)
