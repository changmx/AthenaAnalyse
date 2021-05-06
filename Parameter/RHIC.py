import Common as co

# RHIC
beta_ex_RHIC = 1
beta_ey_RHIC = 1
beta_px_RHIC = 1
beta_py_RHIC = 1

emit_ex_RHIC = 2.8e-6
emit_ey_RHIC = 2.8e-6
emit_px_RHIC = 2.8e-6
emit_py_RHIC = 2.8e-6

sigma_ez_RHIC = 0
sigma_pz_RHIC = 0

Ek_e_RHIC = 100e9
Ek_p_RHIC = 100e9

Ne_RHIC = 1.35e11
Np_RHIC = 1.35e11

p1_RHIC = co.Beam('RHIC-p1', beta_px_RHIC, beta_py_RHIC, emit_px_RHIC,
                  emit_py_RHIC, Ek_p_RHIC, co.Const.MASS_PROTON_EV,
                  co.Const.RADIUS_PROTON, sigma_pz_RHIC, Np_RHIC, 1)
p2_RHIC = co.Beam('RHIC-p2', beta_ex_RHIC, beta_ey_RHIC, emit_ex_RHIC,
                  emit_ey_RHIC, Ek_e_RHIC, co.Const.MASS_PROTON_EV,
                  co.Const.RADIUS_PROTON, sigma_ez_RHIC, Ne_RHIC, 1)

p1_RHIC.calTuneShift(p2_RHIC)
p2_RHIC.calTuneShift(p1_RHIC)

print('RHIC p1 beambeam parameter: ', p1_RHIC.xix, p1_RHIC.xiy)
print('RHIC p2 beambeam parameter: ', p2_RHIC.xix, p2_RHIC.xiy)
print('RHIC p1 tune shift: ', p1_RHIC.tuneshiftx, p1_RHIC.tuneshifty)
print('RHIC p2 tune shift: ', p2_RHIC.tuneshiftx, p2_RHIC.tuneshifty)
