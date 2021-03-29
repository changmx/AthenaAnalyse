import matplotlib.pyplot as plt
import numpy as np

def cal_gamma(beta):
    gamma = 1/(1-(beta*beta)**2)
    return gamma

# beta1 = np.linspace(0.5,1,50)
# fig = plt.figure()
# plt.rcParams['font.sans-serif'] = ['SimHei']
# for beta2 in np.linspace(0.8,0.99,7):
#     k = (1+beta1*beta2)/(beta1+beta2)
#     gamma = cal_gamma(beta2)
#     Ek = (gamma-1)*0.931
#     Ek_label = round(Ek*100)/100
#     beta_lable = round(beta2*100)/100
#     plt.plot(beta1,k,label='$\\beta_{2}=$'+str(beta_lable)+', '+'$E_{k}=$'+str(Ek_label)+'GeV/u')
# plt.xlabel('$\\beta_{1}$')
# plt.ylabel('k factor')
# plt.title('不同速度的相对论k因子')
# plt.legend()
# plt.grid()
# plt.savefig(r'D:\bb2019\beamforce\k_factor.png')
# plt.show()
# plt.close()


def cal_k(Ek):
	gamma = Ek/0.931+1
	beta = (1-1/(gamma*gamma))**0.5
	k = (1+beta*beta)/(beta+beta)
	print('Ek = ',Ek,'GeV','beta = ',beta,'gamma = ',gamma,'k = ',k)
for E in np.linspace(0.5,5,10):
	cal_k(E)