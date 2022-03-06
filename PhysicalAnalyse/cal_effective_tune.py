'''
Author: your name
Date: 2022-02-26 14:50:40
LastEditTime: 2022-03-01 16:10:57
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \AthenaAnalyse\PhysicalAnalyse\cal_effective_tune.py
'''
import numpy as np


def cal_effective_tune(nu_opp, Nbunch, Nbunch_opp):
    fund = nu_opp * Nbunch / Nbunch_opp
    nu_eff = []
    for i in range(Nbunch_opp):
        nu_tmp = fund + i / Nbunch_opp
        nu_eff.append(nu_tmp - int(nu_tmp))
    nu_minus_eff = [1 - nu for nu in nu_eff]
    return nu_eff, nu_minus_eff


if __name__ == '__main__':
    nueff, numinus = cal_effective_tune(0.624, 5, 3)
    print(nueff)
    print(numinus)