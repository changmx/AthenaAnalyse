import math

def cal_crossing_angle_factor_beta(beta1,emit1,sigmaZ1,beta2,emit2,sigmaZ2,halfAngle):
	sigma1 = math.sqrt(beta1*emit1)
	sigma2 = math.sqrt(beta2*emit2)
	# s = 1/(math.sqrt(1+(sigma/sigmaZ*math.tan(halfAngle))**2)*math.sqrt(1+(sigmaZ/sigma*math.tan(halfAngle))**2))
	s = 1/math.sqrt(1+(sigmaZ1**2+sigmaZ2**2)/(sigma1**2+sigma2**2)*(math.tan(halfAngle))**2)
	return s

def cal_crossing_angle_factor_sigma(sigma,sigmaZ,halfAngle):
	s = 1/(math.sqrt(1+(sigma/sigmaZ*math.tan(halfAngle))**2)*math.sqrt(1+(sigmaZ/sigma*math.tan(halfAngle))**2))

	return s

if __name__ == '__main__':

	# KEKB parameter

	# beta_ex = 0.33
	# beta_ey = 0.008
	# beta_px = 0.33
	# beta_py= 0.008

	# emit_ex = 1.8e-8
	# emit_ey = 3.6e-10
	# emit_px = 1.8e-8
	# emit_py = 3.6e-10

	# sigma_ez = 0.004	# calculate disruption parameter and crossing angle factor
	# sigma_pz = 0.004

	# phi = 2*11e-3		# 2*phi is real angle

	# sigma_ex = math.sqrt(beta_ex*emit_ex)
	# sigma_ey = math.sqrt(beta_ey*emit_ey)
	# sigma_px = math.sqrt(beta_px*emit_px)
	# sigma_py = math.sqrt(beta_py*emit_py)

	# # eRHIC parameter

	# beta_ex = 0.62
	# beta_ey = 0.073
	# beta_px = 0.94
	# beta_py= 0.042

	# emit_ex = 24.4e-9
	# emit_ey = 3.5e-9
	# emit_px = 16e-9
	# emit_py = 6.1e-9

	# sigma_ez = 0.01
	# sigma_pz = 0.07

	# phi = 2*11e-3    # 2*phi is real angles

	# LHC parameter

	# phi = 285e-6
	# sigma_ex = 16.7e-6
	# sigma_ey = 16.7e-6
	# sigma_px = 16.7e-6
	# sigma_py = 16.7e-6

	# sigma_ez = 7.7e-2
	# sigma_pz = 7.7e-2


	## EicC parameter
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

	phi = 2*25e-3    # 2*phi is real angles

	sigma_ex = math.sqrt(beta_ex*emit_ex)
	sigma_ey = math.sqrt(beta_ey*emit_ey)
	sigma_px = math.sqrt(beta_px*emit_px)
	sigma_py = math.sqrt(beta_py*emit_py)

	S = cal_crossing_angle_factor_beta(beta_ex,emit_ex,sigma_ez,beta_px,emit_px,sigma_pz,phi/2)
	print("crossing angle factor: %f" % (S))

	# step_size = 1e-3
	# for i in range(1,51):
	# 	S = cal_crossing_angle_factor_beta(beta_ex,emit_ex,sigma_ez,i*step_size)
	# 	print(i,S)
