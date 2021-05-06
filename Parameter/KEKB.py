import Common as co

# KEKB
beta_ex_KEKB = 0.33
beta_ey_KEKB = 0.01
beta_px_KEKB = 0.33
beta_py_KEKB = 0.01

emit_ex_KEKB = 1.8e-8
emit_ey_KEKB = 3.6e-10
emit_px_KEKB = 1.8e-8
emit_py_KEKB = 3.6e-10

sigma_ez_KEKB = 0.004
sigma_pz_KEKB = 0.004

Ek_e_KEKB = 8e9
Ek_p_KEKB = 3.5e9

Ne_KEKB = 1.4e9
Np_KEKB = 3.3e9

positron_KEKB = co.Beam('KEKB-positron', beta_px_KEKB, beta_py_KEKB,
                        emit_px_KEKB, emit_py_KEKB, Ek_p_KEKB,
                        co.Const.MASS_ELECTRON_EV, co.Const.RADIUS_ELECTRON,
                        sigma_pz_KEKB, Np_KEKB, 1)
electron_KEKB = co.Beam('KEKB-electron', beta_ex_KEKB, beta_ey_KEKB,
                        emit_ex_KEKB, emit_ey_KEKB, Ek_e_KEKB,
                        co.Const.MASS_ELECTRON_EV, co.Const.RADIUS_ELECTRON,
                        sigma_ez_KEKB, Ne_KEKB, 1)

positron_KEKB.calTuneShift(electron_KEKB)
electron_KEKB.calTuneShift(positron_KEKB)

positron_KEKB.print()
electron_KEKB.print()
