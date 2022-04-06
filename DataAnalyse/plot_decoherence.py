from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'


def plot_x(ax,
           path,
           sigmaxInit=1,
           skiprows=1,
           turnScale=None,
           mymarker='o',
           mymarkersize=1,
           myalpha=1,
           mylinewidth=1,
           mycolor='tab:blue',
           myfontsize=12,
           label='',
           zorder=100):
    turn, x = np.loadtxt(path,
                         delimiter=',',
                         usecols=(0, 1),
                         unpack=True,
                         skiprows=skiprows)

    if turnScale == None:
        ax.scatter(turn,
                   x / sigmaxInit,
                   alpha=myalpha,
                   s=mymarkersize,
                   marker=mymarker,
                   linewidth=mylinewidth,
                   c=mycolor,
                   label=label,
                   zorder=zorder)
    else:
        ax.scatter(turn[turnScale[0]:turnScale[1]],
                   x[turnScale[0]:turnScale[1]] / sigmaxInit,
                   alpha=myalpha,
                   s=mymarkersize,
                   marker=mymarker,
                   linewidth=mylinewidth,
                   c=mycolor,
                   label=label,
                   zorder=zorder)


def plot_emitx(ax, path, skiprows=1, turnScale=None, myfontsize=12, label=''):
    turn, xemit = np.loadtxt(path,
                             skiprows=skiprows,
                             usecols=(0, 13),
                             delimiter=',',
                             unpack=True)
    if turnScale == None:
        ax.plot(turn, xemit, label=label)
    else:
        ax.plot(turn[turnScale[0]:turnScale[1]],
                xemit[turnScale[0]:turnScale[1]],
                label=label)


def plot_x_mian():
    path_p_4e7p_offset_1sigmax = r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\质子-水平1.0-bunch0-水平轻微不稳定后恢复稳定-亮度比0.8σ时略低-1553_19\1553_19_proton_bunch0_statistic.csv'
    path_p_1e1p_offset_1sigmax = r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-水平1.0-bunch0-不稳定-1516_27\1516_27_proton_bunch0_statistic.csv'

    myfontsize = 12
    turnScale = (0, 5000)

    fig, ax = plt.subplots()
    plt.xticks(fontsize=myfontsize)
    plt.yticks(fontsize=myfontsize)

    sigmax = np.sqrt(300e-9 * 0.04)

    plot_x(ax,
           path_p_4e7p_offset_1sigmax,
           turnScale=turnScale,
           mycolor='tab:blue',
           myalpha=0.8,
           mymarkersize=1,
           mylinewidth=0.1,
           sigmaxInit=sigmax,
           myfontsize=myfontsize,
           label='4e vs. 7p',
           zorder=100)
    plot_x(ax,
           path_p_1e1p_offset_1sigmax,
           turnScale=turnScale,
           mycolor='tab:orange',
           myalpha=0.8,
           mymarkersize=1,
           mylinewidth=0.5,
           sigmaxInit=sigmax,
           myfontsize=myfontsize,
           label='1e vs. 1p',
           zorder=90)

    ax.grid(axis='both', zorder=10)
    ax.legend(fontsize=myfontsize, markerscale=5)

    ax.set_xlabel('Proton turns', fontsize=myfontsize)
    ax.set_ylabel(r'$\overline{x}/\sigma_x$', fontsize=myfontsize)

    ax.tick_params(axis='both', direction='in')
    plt.savefig(r'D:\OneDrive\模拟数据2\offset_decoherence_x.png', dpi=300)
    plt.show()


def plot_emitx_main():
    path_p_4e7p_offset_1sigmax_bunch0 = r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\质子-水平1.0-bunch0-水平轻微不稳定后恢复稳定-亮度比0.8σ时略低-1553_19\1553_19_proton_bunch0_statistic.csv'
    path_p_4e7p_offset_1sigmax_bunch1 = r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\质子-水平1.0-bunch0-水平轻微不稳定后恢复稳定-亮度比0.8σ时略低-1553_19\1553_19_proton_bunch1_statistic.csv'
    path_p_4e7p_offset_1sigmax_bunch2 = r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\质子-水平1.0-bunch0-水平轻微不稳定后恢复稳定-亮度比0.8σ时略低-1553_19\1553_19_proton_bunch2_statistic.csv'
    path_p_4e7p_offset_1sigmax_bunch3 = r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\质子-水平1.0-bunch0-水平轻微不稳定后恢复稳定-亮度比0.8σ时略低-1553_19\1553_19_proton_bunch3_statistic.csv'
    path_p_4e7p_offset_1sigmax_bunch4 = r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\质子-水平1.0-bunch0-水平轻微不稳定后恢复稳定-亮度比0.8σ时略低-1553_19\1553_19_proton_bunch4_statistic.csv'
    path_p_4e7p_offset_1sigmax_bunch5 = r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\质子-水平1.0-bunch0-水平轻微不稳定后恢复稳定-亮度比0.8σ时略低-1553_19\1553_19_proton_bunch5_statistic.csv'
    path_p_4e7p_offset_1sigmax_bunch6 = r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\质子-水平1.0-bunch0-水平轻微不稳定后恢复稳定-亮度比0.8σ时略低-1553_19\1553_19_proton_bunch6_statistic.csv'

    myfontsize = 12
    turnScale = (0, 5000)

    fig, ax = plt.subplots()
    plt.xticks(fontsize=myfontsize)
    plt.yticks(fontsize=myfontsize)

    plot_emitx(ax,
               path_p_4e7p_offset_1sigmax_bunch0,
               turnScale=turnScale,
               myfontsize=myfontsize,
               label='proton bunch 0')
    plot_emitx(ax,
               path_p_4e7p_offset_1sigmax_bunch1,
               turnScale=turnScale,
               myfontsize=myfontsize,
               label='proton bunch 1')
    plot_emitx(ax,
               path_p_4e7p_offset_1sigmax_bunch2,
               turnScale=turnScale,
               myfontsize=myfontsize,
               label='proton bunch 2')
    plot_emitx(ax,
               path_p_4e7p_offset_1sigmax_bunch3,
               turnScale=turnScale,
               myfontsize=myfontsize,
               label='proton bunch 3')
    plot_emitx(ax,
               path_p_4e7p_offset_1sigmax_bunch4,
               turnScale=turnScale,
               myfontsize=myfontsize,
               label='proton bunch 4')
    plot_emitx(ax,
               path_p_4e7p_offset_1sigmax_bunch5,
               turnScale=turnScale,
               myfontsize=myfontsize,
               label='proton bunch 5')
    plot_emitx(ax,
               path_p_4e7p_offset_1sigmax_bunch6,
               turnScale=turnScale,
               myfontsize=myfontsize,
               label='proton bunch 6')

    ax.hlines(300e-9,
              turnScale[0],
              turnScale[1],
              linestyles='dashed',
              colors='tab:grey',
              label=r'without offset')

    ax.grid(axis='both')
    ax.legend(fontsize=myfontsize)

    ax.set_ylim((295e-9, 400e-9))
    ax.set_xlabel('Proton turns', fontsize=myfontsize)
    ax.set_ylabel(r'$\epsilon_x\ (\mathrm{m\cdot rad})$', fontsize=myfontsize)
    ax.tick_params(axis='both', direction='in')
    plt.savefig(r'D:\OneDrive\模拟数据2\offset_decoherence_emitx.png', dpi=300)
    plt.show()


if __name__ == '__main__':
    plot_x_mian()
    plot_emitx_main()
