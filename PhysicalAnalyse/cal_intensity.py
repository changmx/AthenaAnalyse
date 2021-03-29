import math
import sys
sys.path.append('D:\\AthenaAnalyse\\CommonCalculation')
import common
from physicalConstant import const

# KEKB parameter
E = 8e9
circumference = 3016.26
npPerBunch = 1.4e10
nBunch = 5000

# eRHIC parameter
# Ek = 10e9
# circumference = 3833.845
# npPerBunch = 3.05e11
# nBunch = 330

# I = cal_intensity(Ek,circumference,npPerBunch,nBunch,'electron')
# print("Beam current: %f A" % (I))Ek = 10e9

# BEPC2 parameter
# Ek = 1.89e9
# circumference = 237.53
# npPerBunch = 4.85e10
# nBunch = 1

I = common.intensity(E,const.MASS_ELECTRON_EV,circumference,npPerBunch,nBunch)
print("Beam current: %f A" % (I))