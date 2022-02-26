import numpy as np
import matplotlib.pyplot as plt
'''
日期：2022年2月23日创建

功能：对比1e vs 2p， 2e vs 3p, 3e vs 5p, 4e vs 7p这几种模式下束团质心与尺寸的变化并绘图
'''


def plot_x_sigmax(path_e, path_p, ax, ax_col, norm_factor_e, norm_factor_p,
                  super_period_scale):
    turn_e, x_e, sigmax_e = np.loadtxt(path_e,
                                       delimiter=',',
                                       usecols=(0, 1, 3),
                                       unpack=True,
                                       skiprows=1)
    turn_p, x_p, sigmax_p = np.loadtxt(path_p,
                                       delimiter=',',
                                       usecols=(0, 1, 3),
                                       unpack=True,
                                       skiprows=1)
    turn_e /= norm_factor_e
    turn_p /= norm_factor_p

    turn_e /= 1e4
    turn_p /= 1e4

    x_e *= 1e6
    x_p *= 1e6

    sigmax_e *= 1e6
    sigmax_p *= 1e6

    myalpha = 0.2
    mymarkersize = 0.1
    mymarkertype = 'o'
    myfontsize = 10
    mylinewidth = 0.1

    color1 = 'skyblue'
    color2 = 'lightcoral'
    color3 = 'skyblue'
    color4 = 'lightcoral'
    ax[0, ax_col].scatter(turn_e,
                          x_e,
                          alpha=myalpha,
                          s=mymarkersize,
                          marker=mymarkertype,
                          linewidth=mylinewidth,
                          label='electron',
                          c=color1)
    ax[0, ax_col].scatter(turn_p,
                          x_p,
                          alpha=myalpha,
                          s=mymarkersize,
                          marker=mymarkertype,
                          linewidth=mylinewidth,
                          label='proton',
                          c=color2)

    ax[1, ax_col].scatter(turn_e,
                          sigmax_e,
                          alpha=myalpha,
                          s=mymarkersize,
                          marker=mymarkertype,
                          linewidth=mylinewidth,
                          label='electron',
                          c=color3)
    ax[1, ax_col].scatter(turn_p,
                          sigmax_p,
                          alpha=myalpha,
                          s=mymarkersize,
                          marker=mymarkertype,
                          linewidth=mylinewidth,
                          label='proton',
                          c=color4)

    plt.sca(ax[0, ax_col])
    plt.xticks(fontsize=myfontsize)
    plt.yticks(fontsize=myfontsize)
    plt.sca(ax[1, ax_col])
    plt.xticks(fontsize=myfontsize)
    plt.yticks(fontsize=myfontsize)

    ax[0, ax_col].set_xlim(super_period_scale[0], super_period_scale[1])
    ax[1, ax_col].set_xlim(super_period_scale[0], super_period_scale[1])

    # ax[0, ax_col].ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
    # ax[1, ax_col].ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
    # ax[0, ax_col].ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
    # ax[1, ax_col].ticklabel_format(axis="x", style="sci", scilimits=(0, 0))

    ax[0, ax_col].grid()
    ax[1, ax_col].grid()
    leg1 = ax[0, ax_col].legend(loc='upper left',
                                fontsize=myfontsize,
                                markerscale=10,
                                framealpha=0)
    for l in leg1.legendHandles:
        l.set_alpha(1)
    leg2 = ax[1, ax_col].legend(loc='upper left',
                                fontsize=myfontsize,
                                markerscale=10,
                                framealpha=0)
    for l in leg2.legendHandles:
        l.set_alpha(1)


if __name__ == '__main__':
    path_1e2p_e = r'D:\OneDrive\模拟数据2\1e-2p\Qe=0.58,0.56-水平方向不稳定-1730_06\1730_06_electron_bunch0_statistic.csv'
    path_1e2p_p = r'D:\OneDrive\模拟数据2\1e-2p\Qe=0.58,0.56-水平方向不稳定-1730_06\1730_06_proton_bunch0_statistic.csv'

    path_2e3p_e = r'D:\OneDrive\模拟数据2\2e-3p\Qe=0.58,0.56-水平方向不稳定-2004_31\2004_31_electron_bunch0_statistic.csv'
    path_2e3p_p = r'D:\OneDrive\模拟数据2\2e-3p\Qe=0.58,0.56-水平方向不稳定-2004_31\2004_31_proton_bunch0_statistic.csv'

    path_3e5p_e = r'D:\OneDrive\模拟数据2\3e-5p\Qe=0.58,0.56-Qp=0.315,0.3-水平方向不稳定-sp=10w-0953_19\0953_19_electron_bunch0_statistic.csv'
    path_3e5p_p = r'D:\OneDrive\模拟数据2\3e-5p\Qe=0.58,0.56-Qp=0.315,0.3-水平方向不稳定-sp=10w-0953_19\0953_19_proton_bunch0_statistic.csv'

    path_4e7p_e = r'D:\OneDrive\模拟数据2\4e-7p\Qe=0.58,0.56-稳定-sp=10w-1516_46\1516_46_electron_bunch0_statistic.csv'
    path_4e7p_p = r'D:\OneDrive\模拟数据2\4e-7p\Qe=0.58,0.56-稳定-sp=10w-1516_46\1516_46_proton_bunch0_statistic.csv'

    myfontsize = 10
    fig, ax = plt.subplots(2, 4, figsize=(15, 9), sharex=True)
    fig.subplots_adjust(left=0.1, right=0.925, top=0.89)

    plot_x_sigmax(path_1e2p_e, path_1e2p_p, ax, 0, 2, 1, [0, 10])
    plot_x_sigmax(path_2e3p_e, path_2e3p_p, ax, 1, 3, 2, [0, 10])
    plot_x_sigmax(path_3e5p_e, path_3e5p_p, ax, 2, 5, 3, [0, 5])
    plot_x_sigmax(path_4e7p_e, path_4e7p_p, ax, 3, 7, 4, [0, 10])

    ax[0, 0].set_ylim(-8, 8)
    ax[0, 1].set_ylim(-30, 30)
    ax[0, 2].set_ylim(-250, 250)
    # ax[0, 3].set_ylim(-1, 1)

    ax[1, 0].set_ylim(70, 140)
    ax[1, 1].set_ylim(70, 140)
    ax[1, 2].set_ylim(70, 250)
    ax[1, 3].set_ylim(70, 140)

    ax[0, 0].set_title('1e vs. 2p', fontsize=myfontsize)
    ax[0, 1].set_title('2e vs. 3p', fontsize=myfontsize)
    ax[0, 2].set_title('3e vs. 5p', fontsize=myfontsize)
    ax[0, 3].set_title('4e vs. 7p', fontsize=myfontsize)

    ax[0, 0].set_ylabel(r'$\overline{\mathrm{x}}$ ($\mathrm{\mu m}$)',
                        fontsize=myfontsize)
    ax[1, 0].set_ylabel(r'$\sigma_x$ ($\mathrm{\mu m}$)', fontsize=myfontsize)

    ax[1, 0].set_xlabel(r'Super period ($\times 10^4$)')
    ax[1, 1].set_xlabel(r'Super period ($\times 10^4$)')
    ax[1, 2].set_xlabel(r'Super period ($\times 10^4$)')
    ax[1, 3].set_xlabel(r'Super period ($\times 10^4$)')

    plt.savefig(r'D:\OneDrive\模拟数据2\compare.png', dpi=300)
    # plt.show()
