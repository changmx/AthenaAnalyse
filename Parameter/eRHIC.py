import Common as co

# eRHIC
# From 'Electron-Ion Collider at Brookhaven National
# Laboratory Conceptual Design Report 2021

beta_ex_eRHIC = 0.45
beta_ey_eRHIC = 0.056
beta_px_eRHIC = 0.8
beta_py_eRHIC = 0.072

emit_ex_eRHIC = 20e-9
emit_ey_eRHIC = 1.3e-9
emit_px_eRHIC = 11.3e-9
emit_py_eRHIC = 1.0e-9

sigma_ez_eRHIC = 0.007
sigma_pz_eRHIC = 0.06

Ek_e_eRHIC = 10e9
Ek_p_eRHIC = 275e9

Ne_eRHIC = 17.2e10
Np_eRHIC = 6.9e10

Nbunch_e_eRHIC = 1160
Nbunch_p_eRHIC = 1160

circumference_e_eRHIC = 0
circumference_p_eRHIC = 3834

electron_eRHIC = co.Beam('eRHIC-electron', beta_ex_eRHIC, beta_ey_eRHIC,
                         emit_ex_eRHIC, emit_ey_eRHIC, Ek_e_eRHIC,
                         co.Const.MASS_ELECTRON_EV, co.Const.RADIUS_ELECTRON,
                         sigma_ez_eRHIC, Ne_eRHIC, Nbunch_e_eRHIC,
                         circumference_e_eRHIC)
proton_eRHIC = co.Beam('eRHIC-proton', beta_px_eRHIC, beta_py_eRHIC,
                       emit_px_eRHIC, emit_py_eRHIC, Ek_p_eRHIC,
                       co.Const.MASS_PROTON_EV, co.Const.RADIUS_PROTON,
                       sigma_pz_eRHIC, Np_eRHIC, Nbunch_p_eRHIC,
                       circumference_p_eRHIC)

proton_eRHIC.calTuneShift(electron_eRHIC)
electron_eRHIC.calTuneShift(proton_eRHIC)

print('eRHIC proton beambeam parameter: ', proton_eRHIC.xix, proton_eRHIC.xiy)
print('eRHIC electron beambeam parameter: ', electron_eRHIC.xix,
      electron_eRHIC.xiy)
# print('eRHIC proton tune shift: ', proton_eRHIC.tuneshiftx,
#       proton_eRHIC.tuneshifty)
# print('eRHIC electron tune shift: ', electron_eRHIC.tuneshiftx,
#       electron_eRHIC.tuneshifty)

proton_eRHIC.print()
electron_eRHIC.print()