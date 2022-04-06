'''
Author: 常铭轩
Date: 2022-02-24 17:44:03
LastEditTime: 2022-02-28 13:35:19
LastEditors: Please set LastEditors
Description: 从文件中读取数据做fft，同时绘制理论effective tune
'''

from cProfile import label
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'


def plot_x_fft(path, ax):
    x = np.loadtxt(path, delimiter=',', unpack=True, skiprows=1, usecols=(1, ))

    N = x.shape[0]
    freq = np.arange(0, 1, 1 / N)
    spectrum = np.abs(np.fft.fft(x))

    ax.plot(freq, spectrum, linewidth=0.5, color='tab:blue')
    # ax.plot(freq, spectrum, linewidth=0.5, color='royalblue')
    ax.set_yscale('log')


def cal_effective_tune(nu_opp, Nbunch, Nbunch_opp):
    fund = nu_opp * Nbunch / Nbunch_opp
    nu_eff = []
    for i in range(Nbunch_opp):
        nu_tmp = fund + i / Nbunch_opp
        nu_eff.append(nu_tmp - int(nu_tmp))
    nu_minus_eff = [1 - nu for nu in nu_eff]
    return nu_eff, nu_minus_eff


if __name__ == '__main__':

    nu_e_eff, nu_e_minus = cal_effective_tune(0.624, 7, 4)
    nu_p_eff, nu_p_minus = cal_effective_tune(0.317, 4, 7)

    path_4e7p_electron = r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-1.0Np-稳定-1538_11\1538_11_electron_bunch0_statistic.csv'
    path_4e7p_proton = r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-1.0Np-稳定-1538_11\1538_11_proton_bunch0_statistic.csv'

    myfontsize = 12

    fig_e, ax_e = plt.subplots()
    plt.xticks(fontsize=myfontsize)
    plt.yticks(fontsize=myfontsize)
    fig_p, ax_p = plt.subplots()
    plt.xticks(fontsize=myfontsize)
    plt.yticks(fontsize=myfontsize)

    plot_x_fft(path_4e7p_electron, ax_e)
    plot_x_fft(path_4e7p_proton, ax_p)

    ax_e.tick_params(axis='both', which='both', direction='in')
    ax_p.tick_params(axis='both', which='both', direction='in')

    ax_e.set_xlim((0.5, 1))
    ax_e.set_ylim((1e-9, 1e-2))
    ax_e.set_xlabel(r'$\nu_e$', fontsize=myfontsize)
    ax_e.set_ylabel('Amplitude', fontsize=myfontsize)
    ax_e.grid()

    ax_p.set_xlim((0, 0.5))
    ax_p.set_ylim((1e-9, 1e-2))
    ax_p.set_xlabel(r'$\nu_p$', fontsize=myfontsize)
    ax_p.set_ylabel('Amplitude', fontsize=myfontsize)
    ax_p.grid()

    bbox_props = dict(boxstyle='round', fc='w', alpha=0.8)
    text_pos = -0.017
    text_y = 1e-8
    for i in range(len(nu_p_eff)):
        mylable = r'$\nu_p^{eff}$' if i == 0 else None
        ax_e.axvline(x=nu_p_eff[i],
                     ymin=0.2,
                     ymax=0.78,
                     color='red',
                     linestyle="--",
                     linewidth=1.5,
                     label=mylable)
        if nu_p_eff[i] > 0.5:
            ax_e.text(nu_p_eff[i] + text_pos,
                      text_y,
                      '{0:.3f}'.format(nu_p_eff[i]),
                      bbox=bbox_props)
    for i in range(len(nu_p_minus)):
        mylable = r'$1-\nu_p^{eff}$' if i == 0 else None
        ax_e.axvline(x=nu_p_minus[i],
                     ymin=0.2,
                     ymax=0.78,
                     color='orange',
                     linestyle="--",
                     linewidth=1.5,
                     label=mylable)
        if nu_p_minus[i] > 0.5:
            ax_e.text(nu_p_minus[i] + text_pos,
                      text_y,
                      '{0:.3f}'.format(nu_p_minus[i]),
                      bbox=bbox_props)
    ax_e.legend(fontsize=12, loc='upper right', framealpha=0)
    fig_e.savefig(
        r'D:\OneDrive\文档\Simulation of beam\article\figure\fft_e_4e7p.png',
        dpi=300)

    for i in range(len(nu_e_eff)):
        mylable = r'$\nu_e^{eff}$' if i == 0 else None
        ax_p.axvline(x=nu_e_eff[i],
                     ymin=0.2,
                     ymax=0.78,
                     color='red',
                     linestyle="--",
                     linewidth=1.5,
                     label=mylable)
        if nu_e_eff[i] < 0.5:
            ax_p.text(nu_e_eff[i] + text_pos,
                      text_y,
                      '{0:.3f}'.format(nu_e_eff[i]),
                      bbox=bbox_props)
    for i in range(len(nu_e_minus)):
        mylable = r'$1-\nu_e^{eff}$' if i == 0 else None
        ax_p.axvline(x=nu_e_minus[i],
                     ymin=0.2,
                     ymax=0.78,
                     color='orange',
                     linestyle="--",
                     linewidth=1.5,
                     label=mylable)
        if nu_e_minus[i] < 0.5:
            ax_p.text(nu_e_minus[i] + text_pos,
                      text_y,
                      '{0:.3f}'.format(nu_e_minus[i]),
                      bbox=bbox_props)
    ax_p.legend(fontsize=12, loc='upper right', framealpha=0)
    fig_p.savefig(
        r'D:\OneDrive\文档\Simulation of beam\article\figure\fft_p_4e7p.png',
        dpi=300)
    plt.show()
