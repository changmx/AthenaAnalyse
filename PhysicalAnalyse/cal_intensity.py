import math
import Common as co

# KEKB parameter
# E = 8e9
# circumference = 3016.26
# npPerBunch = 1.4e10
# nBunch = 5000

# eRHIC parameter
Ek_p_eRHIC = 275e9
Ek_e_eRHIC = 18e9
circumference_p_eRHIC = 3833.94
circumference_e_eRHIC = 3833.94
Np_p_eRHIC = 6.9e10
Np_e_eRHIC = 17.2e10
nBunch_p_eRHIC = 1160
nBunch_e_eRHIC = 1160

eRHIC = co.Ring(Ek_p_eRHIC, Ek_e_eRHIC, Np_p_eRHIC, Np_e_eRHIC, nBunch_p_eRHIC,
                nBunch_e_eRHIC, circumference_p_eRHIC, circumference_e_eRHIC,
                co.Const.MASS_PROTON_EV, co.Const.MASS_ELECTRON_EV)

# BEPC2 parameter
# Ek = 1.89e9
# circumference = 237.53
# npPerBunch = 4.85e10
# nBunch = 1

eRHIC.print()