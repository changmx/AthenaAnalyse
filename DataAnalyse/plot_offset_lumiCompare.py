'''
Author: your name
Date: 2022-03-08 09:47:16
LastEditTime: 2022-03-08 16:30:31
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \AthenaAnalyse\DataAnalyse\plot_offset_lumiCompare.py
'''

from sqlite3 import Row
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'


def read_plot_lumi(ax,
                   path,
                   turnScale,
                   skiprows=1,
                   mymarker='o',
                   mymarkersize=1,
                   myalpha=1,
                   mylinewidth=1,
                   mycolor='tab:blue',
                   myfontsize=12,
                   myzorder=20,
                   plottype='scatter'):
    turn, lumi = np.loadtxt(path,
                            delimiter=',',
                            skiprows=skiprows,
                            usecols=(0, 1),
                            unpack=True)

    if plottype == 'scatter':
        ax.scatter(turn[turnScale[0]:turnScale[1]] / 1e4,
                   lumi[turnScale[0]:turnScale[1]] / 1e33,
                   marker=mymarker,
                   s=mymarkersize,
                   alpha=myalpha,
                   linewidth=mylinewidth,
                   c=mycolor,
                   zorder=myzorder)
    elif plottype == 'plot':
        ax.plot(turn[turnScale[0]:turnScale[1]] / 1e4,
                lumi[turnScale[0]:turnScale[1]] / 1e33,
                linewidth=mylinewidth,
                alpha=myalpha,
                c=mycolor)

    y_major_locator = plt.MultipleLocator(0.5)
    y_minor_locator = plt.MultipleLocator(0.1)
    x_major_locator = plt.MultipleLocator(5)
    x_minor_locator = plt.MultipleLocator(1)
    ax.yaxis.set_major_locator(y_major_locator)
    # ax.yaxis.set_minor_locator(y_minor_locator)
    ax.xaxis.set_major_locator(x_major_locator)
    # ax.xaxis.set_minor_locator(x_minor_locator)

    plt.sca(ax)
    plt.xticks(fontsize=myfontsize)
    plt.yticks(fontsize=myfontsize)

    ax.tick_params(axis='x', direction='in', length=0)

    ax.grid(zorder=10)


if __name__ == '__main__':

    myfontsize = 12
    myfontsize_sub = 10

    path_1e1p_offset_lumi = []
    path_4e7p_offset_oneBunch_lumi = []
    path_4e7p_offset_allBunch_lumi = []

    fig, ax = plt.subplots(3, 3, sharex=True, sharey=True)
    # plt.rcParams['xtick.direction'] = 'in' # in; out; inout

    ######## 1e vs. 1p, start ########
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-水平0.2-bunch0-稳定-1514_07\1514_07_luminosity_electron_200000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-水平0.4-bunch0-不稳定-1515_51\1515_51_luminosity_proton_200000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-水平0.6-bunch0-不稳定-1516_09\1516_09_luminosity_proton_200000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-水平0.8-bunch0-不稳定-1516_17\1516_17_luminosity_proton_200000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-水平1.0-bunch0-不稳定-1516_27\1516_27_luminosity_proton_200000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-水平1.5-bunch0-不稳定-1521_54\1521_54_luminosity_proton_200000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-水平2.0-bunch0-不稳定-1523_45\1523_45_luminosity_proton_200000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-水平2.5-bunch0-不稳定-1523_54\1523_54_luminosity_proton_200000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-水平3.0-bunch0-不稳定-1524_09\1524_09_luminosity_proton_200000turns.csv'
    )
    ######## 1e vs. 1p, end ########

    ######## 4e vs. 7p, one bunch with offset, start ########
    path_4e7p_offset_oneBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\质子-水平0.2-bunch0-稳定-0935_13\0935_13_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_oneBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\质子-水平0.4-bunch0-稳定-0944_19\0944_19_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_oneBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\质子-水平0.6-bunch0-稳定-1145_23\1145_23_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_oneBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\质子-水平0.8-bunch0-水平轻微不稳定后恢复稳定-1528_12\1528_12_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_oneBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\质子-水平1.0-bunch0-水平轻微不稳定后恢复稳定-亮度比0.8σ时略低-1553_19\1553_19_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_oneBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\质子-水平1.5-bunch0-水平出现不稳定-质子水平空心-亮度降至2.05-1609_58\1609_58_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_oneBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\质子-水平2.0-bunch0-水平出现不稳定-亮度降至1.95-1614_47\1614_47_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_oneBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\质子-水平2.5-bunch0-水平出现不稳定-亮度降至1.7-0005_31\0005_31_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_oneBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\质子-水平3.0-bunch0-水平出现不稳定-亮度降至1.5-1424_19\1424_19_luminosity_electron_350000turns.csv'
    )

    ######## 4e vs. 7p, one bunch with offset, end ##########

    ######## 4e vs. 7p, all bunch with offset, start ########
    path_4e7p_offset_allBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_多束团offset\质子-水平0.2所有-稳定-1028_14\1028_14_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_allBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_多束团offset\质子-水平0.4所有-不稳定-亮度降至2.1e33-0850_31\0850_31_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_allBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_多束团offset\质子-水平0.6所有-不稳定-亮度降至1.1e33-0239_39\0239_39_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_allBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_多束团offset\质子-水平0.8所有-不稳定-亮度降至1.2e33-0853_14\0853_14_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_allBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_多束团offset\质子-水平1.0所有-不稳定-亮度降至1.2e33-1902_11\1902_11_luminosity_electron_350000turns.csv'
    )
    ######## 4e vs. 7p, all bunch with offset, end ##########

    for i in range(3):
        for j in range(3):
            index = i * 3 + j
            if index < len(path_1e1p_offset_lumi):
                read_plot_lumi(ax[i, j],
                               path_1e1p_offset_lumi[index], [0, 200000],
                               skiprows=2,
                               mymarkersize=0.01,
                               mylinewidth=0.1,
                               mycolor='tab:orange',
                               myalpha=0.2,
                               myfontsize=myfontsize_sub,
                               plottype='scatter')
            if index < len(path_4e7p_offset_oneBunch_lumi):
                read_plot_lumi(ax[i, j],
                               path_4e7p_offset_oneBunch_lumi[index],
                               [0, 200000],
                               skiprows=8,
                               mymarkersize=0.01,
                               mylinewidth=0.1,
                               mycolor='tab:blue',
                               myalpha=0.2,
                               myfontsize=myfontsize_sub,
                               plottype='scatter')
    #         if index < len(path_4e7p_offset_allBunch_lumi):
    #             read_plot_lumi(ax[i, j],
    #                            path_4e7p_offset_allBunch_lumi[index],
    #                            [0, 200000],
    #                            skiprows=8,
    #                            mymarkersize=0.1,
    #                            mylinewidth=0.1,
    #                            mycolor='tab:green',
    #                            myalpha=0.02,
    #                            myfontsize=myfontsize)

    # read_plot_lumi(
    #     ax[2, 2],
    #     r'D:\OneDrive\模拟数据2\offset_4e7p_多束团offset\质子-水平3.0所有-不稳定-亮度降至1.0e33-0903_49\0903_49_luminosity_electron_350000turns.csv',
    #     [0, 200000],
    #     skiprows=8,
    #     mymarkersize=0.01,
    #     mylinewidth=0.1,
    #     mycolor='tab:green',
    #     myalpha=0.1,
    #     myfontsize=myfontsize)

    ax[0, 0].set_ylim((0.3, 2.5))

    ax[0, 0].set_title(r'$\Delta x = 0.2\sigma_x$', pad=4, fontsize=myfontsize_sub)
    ax[0, 1].set_title(r'$\Delta x = 0.4\sigma_x$', pad=4, fontsize=myfontsize_sub)
    ax[0, 2].set_title(r'$\Delta x = 0.6\sigma_x$', pad=4, fontsize=myfontsize_sub)
    ax[1, 0].set_title(r'$\Delta x = 0.8\sigma_x$', pad=4, fontsize=myfontsize_sub)
    ax[1, 1].set_title(r'$\Delta x = 1.0\sigma_x$', pad=4, fontsize=myfontsize_sub)
    ax[1, 2].set_title(r'$\Delta x = 1.5\sigma_x$', pad=4, fontsize=myfontsize_sub)
    ax[2, 0].set_title(r'$\Delta x = 2.0\sigma_x$', pad=4, fontsize=myfontsize_sub)
    ax[2, 1].set_title(r'$\Delta x = 2.5\sigma_x$', pad=4, fontsize=myfontsize_sub)
    ax[2, 2].set_title(r'$\Delta x = 3.0\sigma_x$', pad=4, fontsize=myfontsize_sub)

    # ax[2, 0].set_xlabel(r'Turn ($\times 10^4$)', fontsize=myfontsize)
    # ax[2, 1].set_xlabel(r'Turn ($\times 10^4$)', fontsize=myfontsize)
    # ax[2, 2].set_xlabel(r'Turn ($\times 10^4$)', fontsize=myfontsize)
    fig.supxlabel(r'Electron turns ($\times 10^4$)', fontsize=myfontsize)
    fig.supylabel(r'Luminosity $(\times 10^{33} \mathrm{cm^{-2}s^{-1}})$',
                  fontsize=myfontsize)
    plt.savefig(r'D:\OneDrive\模拟数据2\offset_compare.png', dpi=300)
    # plt.show()
