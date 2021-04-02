import Common as co

# EicC
beta_ex = 0.2
beta_ey = 0.06
beta_px = 0.04
beta_py = 0.02

emit_ex = 60e-9
emit_ey = 60e-9
emit_px = 300e-9
emit_py = 180e-9

sigma_ez = 0.02
sigma_pz = 0.04

Ek_e = 3.5e9
Ek_p = 19.08e9

Ne = 1.7e11
Np = 1.25e11

sigma_ex = co.sigma(beta_ex, emit_ex)
sigma_ey = co.sigma(beta_ey, emit_ey)
sigma_px = co.sigma(beta_px, emit_px)
sigma_py = co.sigma(beta_py, emit_py)

xi_e_x, xi_e_y = co.cal_tuneShift(Np, beta_ex, beta_ey, Ek_e, sigma_px,
                                  sigma_py, co.Const.MASS_ELECTRON_EV, co.Const.RADIUS_ELECTRON)
xi_p_x, xi_p_y = co.cal_tuneShift(
    Ne, beta_px, beta_py, Ek_p, sigma_ex, sigma_ey, co.Const.MASS_PROTON_EV, co.Const.RADIUS_PROTON)

print("xi_e_x:%f, xi_e_y:%f\nxi_p_x:%f, xi_p_y:%f"%(xi_e_x,xi_e_y,xi_p_x,xi_p_y))
