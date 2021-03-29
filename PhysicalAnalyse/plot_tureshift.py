from tuneShift import cal_tuneShift

# EicC
beta_ex = 0.2
beta_ey = 0.06
beta_px = 0.04
beta_py= 0.02

emit_ex = 60e-9
emit_ey = 60e-9
emit_px = 300e-9
emit_py = 180e-9

sigma_ez = 0.02
sigma_pz = 0.04

phi = 0*25e-3    # 2*phi is real angles

Ek_e = 3.5e9
Ek_p = 19.08e9

Ne = 1.7e11
Np = 1.25e11
cf = 100e6

xi_e_x = cal_tuneShift(Np,beta_ex,beta_ey,Ek_e,beta_px,beta_py,emit_px,emit_py,"x","electron")
xi_e_y = cal_tuneShift(Np,beta_ex,beta_ey,Ek_e,beta_px,beta_py,emit_px,emit_py,"y","electron")
xi_p_x = cal_tuneShift(Ne,beta_px,beta_py,Ek_p,beta_ex,beta_ey,emit_ex,emit_ey,"x","proton")
xi_p_y = cal_tuneShift(Ne,beta_px,beta_py,Ek_p,beta_ex,beta_ey,emit_ex,emit_ey,"y","proton")

print("xi_e_x:%f, xi_e_y:%f, xi_p_x:%f, xi_p_y:%f"%(xi_e_x,xi_e_y,xi_p_x,xi_p_y))