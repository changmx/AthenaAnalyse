import Common as co

# EicC
beta_ex_EicC = 0.2
beta_ey_EicC = 0.06
beta_px_EicC = 0.04
beta_py_EicC = 0.02

emit_ex_EicC = 60e-9
emit_ey_EicC = 60e-9
emit_px_EicC = 300e-9
emit_py_EicC = 180e-9

sigma_ez_EicC = 0.02
sigma_pz_EicC = 0.04

nu_ex_EicC = 0.58
nu_ey_EicC = 0.55
nu_px_EicC = 0.315
nu_py_EicC = 0.3

Ek_e_EicC = 3.5e9
Ek_p_EicC = 19.08e9

Ne_EicC = 1.7e11
Np_EicC = 1.25e11

circumference_e = 809.44
circumference_p = 1341.58

Nbunch_e = 270
Nbunch_p = 448

proton_EicC = co.Beam('EicC-proton', beta_px_EicC, beta_py_EicC, emit_px_EicC,
                      emit_py_EicC, Ek_p_EicC, co.Const.MASS_PROTON_EV,
                      co.Const.RADIUS_PROTON, sigma_pz_EicC, Np_EicC, Nbunch_p,
                      circumference_p)
electron_EicC = co.Beam('EicC-electron', beta_ex_EicC, beta_ey_EicC,
                        emit_ex_EicC, emit_ey_EicC, Ek_e_EicC,
                        co.Const.MASS_ELECTRON_EV, co.Const.RADIUS_ELECTRON,
                        sigma_ez_EicC, Ne_EicC, Nbunch_e, circumference_e)

proton_EicC.calTuneShift(electron_EicC)
electron_EicC.calTuneShift(proton_EicC)

proton_EicC.print()
electron_EicC.print()