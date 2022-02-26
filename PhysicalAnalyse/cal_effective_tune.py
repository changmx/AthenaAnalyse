import numpy as np


def cal_effective_tune(nu_opp, Nbunch, Nbunch_opp):
    fund = nu_opp * Nbunch / Nbunch_opp
    nu_eff = []
    for i in range(Nbunch_opp):
        nu_tmp = fund + i / Nbunch_opp
        nu_eff.append(nu_tmp - int(nu_tmp))
    nu_minus_eff = [1 - nu for nu in nu_eff]
    return nu_eff, nu_minus_eff


if __name__ == '__main__':
    nueff, numinus = cal_effective_tune(0.318, 4, 7)
    print(nueff)
    print(numinus)