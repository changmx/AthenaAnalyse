import numpy as np


def cal_2particle_centerOfMass_energy(m1_statistic, E1_total_energy,
                                      m2_statistic, E2_total_energy):
    '''
    在两个粒子对撞时，质心系中他们动量方向相反，cos项为-1

    如果超过两个粒子，质心系中粒子间夹角不确定，需要使用别的方法计算

    此函数只用来计算两个粒子对撞的质心系能量
    '''
    gamma1 = E1_total_energy / m1_statistic
    gamma2 = E2_total_energy / m2_statistic
    E_cm_square = m1_statistic**2+m2_statistic**2+2*m1_statistic * \
        m2_statistic*(gamma1*gamma2+np.sqrt((gamma1**2-1)*(gamma2**2-1)))
    E_cm = np.sqrt(E_cm_square)

    return E_cm


if __name__ == '__main__':
    m1_statistic = 938.27208816e6
    m2_statistic = 0.510998950e6
    E1_total_energy = 20.02e9
    E2_total_energy = 3.5e9

    E_cm = cal_2particle_centerOfMass_energy(m1_statistic, E1_total_energy,
                                             m2_statistic, E2_total_energy)
    print('center-of-mass energy: {0:f}GeV'.format(E_cm / 1e9))
