import numpy as np
from physicalConstant import const


def energy2betagamma(total_energy_ev, invariant_mass_ev):

    # total_energy_ev = kinetic_energy_ev + invariant_mass_ev
    gamma = total_energy_ev/invariant_mass_ev
    beta = np.sqrt(1-1/(gamma*gamma))
    
    return beta, gamma

def intensity(total_energy_ev,invariant_mass_ev,circumference,npPerBunch,nBunch):
	
    beta,_ = energy2betagamma(total_energy_ev,invariant_mass_ev)
    T = circumference/(beta*const.LIGHT_SPEED)
    I = npPerBunch*nBunch*const.ELEMENTARY_CHARGE/T

    return I

if __name__ == "__main__":

    pass
    