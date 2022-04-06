'''
Author: your name
Date: 2022-03-08 09:47:16
LastEditTime: 2022-03-08 16:30:31
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \AthenaAnalyse\DataAnalyse\plot_offset_lumiCompare.py
'''

from cProfile import label
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
                   plottype='scatter',
                   turnUnit=1e4,
                   lumiUnit=1e33,
                   mylable=None):
    turn, lumi = np.loadtxt(path,
                            delimiter=',',
                            skiprows=skiprows,
                            usecols=(0, 1),
                            unpack=True)

    if plottype == 'scatter':
        ax.scatter(turn[turnScale[0]:turnScale[1]] / turnUnit,
                   lumi[turnScale[0]:turnScale[1]] / lumiUnit,
                   marker=mymarker,
                   s=mymarkersize,
                   alpha=myalpha,
                   linewidth=mylinewidth,
                   c=mycolor,
                   zorder=myzorder,
                   label=mylable)
    elif plottype == 'plot':
        ax.plot(turn[turnScale[0]:turnScale[1]] / turnUnit,
                lumi[turnScale[0]:turnScale[1]] / lumiUnit,
                linewidth=mylinewidth,
                alpha=myalpha,
                c=mycolor,
                label=mylable)

    y_major_locator = plt.MultipleLocator(0.5)
    y_minor_locator = plt.MultipleLocator(0.1)
    x_major_locator = plt.MultipleLocator(10)
    x_minor_locator = plt.MultipleLocator(1)
    ax.yaxis.set_major_locator(y_major_locator)
    # ax.yaxis.set_minor_locator(y_minor_locator)
    # ax.xaxis.set_major_locator(x_major_locator)
    # ax.xaxis.set_minor_locator(x_minor_locator)

    plt.sca(ax)
    plt.xticks(fontsize=myfontsize)
    plt.yticks(fontsize=myfontsize)

    ax.tick_params(axis='x', direction='in', length=0)

    ax.grid(zorder=10)

    print('File has been drawn: {0:s}'.format(path))


def plot_proton_compare(fig, ax, myfontsize, myfontsize_sub):
    path_1e1p_offset_lumi = []
    path_4e7p_offset_oneBunch_lumi = []
    path_4e7p_offset_twoBunch_lumi = []
    path_4e7p_offset_allBunch_lumi = []

    ######## 1e vs. 1p, start ########
    # path_1e1p_offset_lumi.append(
    #     r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-水平0.2-bunch0-稳定-1514_07\1514_07_luminosity_electron_200000turns.csv'
    # )
    # path_1e1p_offset_lumi.append(
    #     r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-水平0.4-bunch0-不稳定-1515_51\1515_51_luminosity_proton_200000turns.csv'
    # )
    # path_1e1p_offset_lumi.append(
    #     r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-水平0.6-bunch0-不稳定-1516_09\1516_09_luminosity_proton_200000turns.csv'
    # )
    # path_1e1p_offset_lumi.append(
    #     r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-水平0.8-bunch0-不稳定-1516_17\1516_17_luminosity_proton_200000turns.csv'
    # )
    # path_1e1p_offset_lumi.append(
    #     r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-水平1.0-bunch0-不稳定-1516_27\1516_27_luminosity_proton_200000turns.csv'
    # )
    # path_1e1p_offset_lumi.append(
    #     r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-水平1.5-bunch0-不稳定-1521_54\1521_54_luminosity_proton_200000turns.csv'
    # )
    # path_1e1p_offset_lumi.append(
    #     r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-水平2.0-bunch0-不稳定-1523_45\1523_45_luminosity_proton_200000turns.csv'
    # )
    # path_1e1p_offset_lumi.append(
    #     r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-水平2.5-bunch0-不稳定-1523_54\1523_54_luminosity_proton_200000turns.csv'
    # )
    # path_1e1p_offset_lumi.append(
    #     r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-水平3.0-bunch0-不稳定-1524_09\1524_09_luminosity_proton_200000turns.csv'
    # )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-sp50w-水平0.2-bunch0-不稳定-1505_29\1505_29_luminosity_electron_500000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-sp50w-水平0.4-bunch0-不稳定-1506_47\1506_47_luminosity_electron_500000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-sp50w-水平0.6-bunch0-不稳定-1507_02\1507_02_luminosity_electron_500000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-sp50w-水平0.8-bunch0-不稳定-1507_10\1507_10_luminosity_electron_500000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-sp50w-水平1.0-bunch0-不稳定-1755_25\1755_25_luminosity_electron_500000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-sp50w-水平1.5-bunch0-不稳定-亮度跳变-1551_30\1551_30_luminosity_electron_500000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-sp50w-水平2.0-bunch0-不稳定-1814_52\1814_52_luminosity_electron_500000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-sp50w-水平2.5-bunch0-不稳定-1815_00\1815_00_luminosity_electron_500000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给质子加offset\质子-sp50w-水平3.0-bunch0-不稳定-1815_08\1815_08_luminosity_electron_500000turns.csv'
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

    ######## 4e vs. 7p, two bunch with offset, start ########
    path_4e7p_offset_twoBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_2质子offset\质子-水平0.2-bunch0,1-稳定-1121_13\1121_13_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_twoBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_2质子offset\质子-水平0.4-bunch0,1-稳定-1119_35\1119_35_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_twoBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_2质子offset\质子-水平0.6-bunch0,1-稳定-2110_27\2110_27_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_twoBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_2质子offset\质子-水平0.8-bunch0,1-不稳定-0835_57\0835_57_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_twoBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_2质子offset\质子-水平1.0-bunch0,1-不稳定-0944_24\0944_24_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_twoBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_2质子offset\质子-水平1.5-bunch0,1-不稳定-0946_45\0946_45_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_twoBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_2质子offset\质子-水平2.0-bunch0,1-不稳定-0949_33\0949_33_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_twoBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_2质子offset\质子-水平2.5-bunch0,1-不稳定-0950_53\0950_53_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_twoBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_2质子offset\质子-水平3.0-bunch0,1-不稳定-2111_11\2111_11_luminosity_electron_350000turns.csv'
    )

    ######## 4e vs. 7p, two bunch with offset, end ##########

    ######## 4e vs. 7p, all bunch with offset, start ########
    path_4e7p_offset_allBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_所有束团offset\质子-水平0.2所有-稳定-1028_14\1028_14_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_allBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_所有束团offset\质子-水平0.4所有-不稳定-亮度降至2.1e33-0850_31\0850_31_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_allBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_所有束团offset\质子-水平0.6所有-不稳定-亮度降至1.1e33-0239_39\0239_39_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_allBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_所有束团offset\质子-水平0.8所有-不稳定-亮度降至1.2e33-0853_14\0853_14_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_allBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_所有束团offset\质子-水平1.0所有-不稳定-亮度降至1.2e33-1902_11\1902_11_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_allBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_所有束团offset\质子-水平1.5所有-不稳定-亮度降至0.9e33-0124_36\0124_36_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_allBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_所有束团offset\质子-水平2.0所有-不稳定-亮度降至0.98e33-0833_18\0833_18_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_allBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_所有束团offset\质子-水平2.5所有-不稳定-亮度降至0.98e33-0834_28\0834_28_luminosity_electron_350000turns.csv'
    )
    path_4e7p_offset_allBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_所有束团offset\质子-水平3.0所有-不稳定-亮度降至1.0e33-0903_49\0903_49_luminosity_electron_350000turns.csv'
    )
    ######## 4e vs. 7p, all bunch with offset, end ##########

    for i in range(3):
        for j in range(3):
            index = i * 3 + j
            if index < len(path_1e1p_offset_lumi):
                read_plot_lumi(ax[i, j],
                               path_1e1p_offset_lumi[index], [0, 350000],
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
                               [0, 350000],
                               skiprows=8,
                               mymarkersize=0.01,
                               mylinewidth=0.1,
                               mycolor='tab:blue',
                               myalpha=0.2,
                               myfontsize=myfontsize_sub,
                               plottype='scatter')
            if index < len(path_4e7p_offset_twoBunch_lumi):
                read_plot_lumi(ax[i, j],
                               path_4e7p_offset_twoBunch_lumi[index],
                               [0, 350000],
                               skiprows=8,
                               mymarkersize=0.01,
                               mylinewidth=0.1,
                               mycolor='tab:green',
                               myalpha=0.2,
                               myfontsize=myfontsize_sub,
                               plottype='scatter')
            if index < len(path_4e7p_offset_allBunch_lumi):
                read_plot_lumi(ax[i, j],
                               path_4e7p_offset_allBunch_lumi[index],
                               [0, 350000],
                               skiprows=8,
                               mymarkersize=0.1,
                               mylinewidth=0.1,
                               mycolor='tab:red',
                               myalpha=0.02,
                               myfontsize=myfontsize_sub,
                               plottype='scatter')

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

    ax[0, 0].set_title(r'$\Delta x = 0.2\sigma_x$',
                       pad=4,
                       fontsize=myfontsize_sub)
    ax[0, 1].set_title(r'$\Delta x = 0.4\sigma_x$',
                       pad=4,
                       fontsize=myfontsize_sub)
    ax[0, 2].set_title(r'$\Delta x = 0.6\sigma_x$',
                       pad=4,
                       fontsize=myfontsize_sub)
    ax[1, 0].set_title(r'$\Delta x = 0.8\sigma_x$',
                       pad=4,
                       fontsize=myfontsize_sub)
    ax[1, 1].set_title(r'$\Delta x = 1.0\sigma_x$',
                       pad=4,
                       fontsize=myfontsize_sub)
    ax[1, 2].set_title(r'$\Delta x = 1.5\sigma_x$',
                       pad=4,
                       fontsize=myfontsize_sub)
    ax[2, 0].set_title(r'$\Delta x = 2.0\sigma_x$',
                       pad=4,
                       fontsize=myfontsize_sub)
    ax[2, 1].set_title(r'$\Delta x = 2.5\sigma_x$',
                       pad=4,
                       fontsize=myfontsize_sub)
    ax[2, 2].set_title(r'$\Delta x = 3.0\sigma_x$',
                       pad=4,
                       fontsize=myfontsize_sub)

    x_major_locator = plt.MultipleLocator(10)
    y_major_locator = plt.MultipleLocator(0.5)
    ax[0, 0].xaxis.set_major_locator(x_major_locator)
    ax[0, 0].yaxis.set_major_locator(y_major_locator)

    ax[0, 0].tick_params(axis='both', which='both', direction='in', left=False)
    ax[0, 1].tick_params(axis='both', which='both', direction='in', left=False)
    ax[0, 2].tick_params(axis='both', which='both', direction='in', left=False)
    ax[1, 0].tick_params(axis='both', which='both', direction='in', left=False)
    ax[1, 1].tick_params(axis='both', which='both', direction='in', left=False)
    ax[1, 2].tick_params(axis='both', which='both', direction='in', left=False)
    ax[2, 0].tick_params(axis='both', which='both', direction='in', left=False)
    ax[2, 1].tick_params(axis='both', which='both', direction='in', left=False)
    ax[2, 2].tick_params(axis='both', which='both', direction='in', left=False)
    # ax[2, 0].set_xlabel(r'Turn ($\times 10^4$)', fontsize=myfontsize)
    # ax[2, 1].set_xlabel(r'Turn ($\times 10^4$)', fontsize=myfontsize)
    # ax[2, 2].set_xlabel(r'Turn ($\times 10^4$)', fontsize=myfontsize)
    fig.supxlabel(r'Electron turns ($\times 10^4$)', fontsize=myfontsize)
    fig.supylabel(r'Luminosity $(\times 10^{33} \mathrm{cm^{-2}s^{-1}})$',
                  fontsize=myfontsize)
    fig.savefig(r'D:\OneDrive\模拟数据2\offset_compare_p.png', dpi=300)


def plot_electron_compare(fig, ax, myfontsize, myfontsize_sub):
    path_1e1p_offset_lumi = []
    path_4e7p_offset_oneBunch_lumi = []
    path_4e7p_offset_allBunch_lumi = []

    ######## 1e vs. 1p, start ########
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给电子加offset\电子-水平0.2-bunch0-稳定-1507_57\1507_57_luminosity_proton_100000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给电子加offset\电子-水平0.4-bunch0-稳定-1509_28\1509_28_luminosity_proton_100000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给电子加offset\电子-水平0.6-bunch0-稳定-1510_15\1510_15_luminosity_proton_100000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给电子加offset\电子-水平0.8-bunch0-稳定-1510_57\1510_57_luminosity_proton_100000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给电子加offset\电子-水平1.0-bunch0-稳定-0012_32\0012_32_luminosity_proton_100000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给电子加offset\电子-水平1.5-bunch0-稳定-0013_41\0013_41_luminosity_proton_100000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给电子加offset\电子-水平2.0-bunch0-稳定-0014_06\0014_06_luminosity_proton_100000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给电子加offset\电子-水平2.5-bunch0-稳定-0014_17\0014_17_luminosity_proton_100000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给电子加offset\电子-水平3.0-bunch0-稳定-0641_07\0641_07_luminosity_proton_100000turns.csv'
    )
    ######## 1e vs. 1p, end ########

    ######## 4e vs. 7p, one bunch with offset, start ########
    path_4e7p_offset_oneBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\电子-水平0.2-bunch0-稳定-0937_02\0937_02_luminosity_proton_200000turns.csv'
    )
    path_4e7p_offset_oneBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\电子-水平0.4-bunch0-稳定-0945_30\0945_30_luminosity_proton_200000turns.csv'
    )
    path_4e7p_offset_oneBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\电子-水平0.6-bunch0-稳定-1145_51\1145_51_luminosity_proton_200000turns.csv'
    )
    path_4e7p_offset_oneBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\电子-水平0.8-bunch0-稳定-0842_42\0842_42_luminosity_proton_200000turns.csv'
    )
    path_4e7p_offset_oneBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\电子-水平1.0-bunch0-稳定-2357_21\2357_21_luminosity_proton_200000turns.csv'
    )
    path_4e7p_offset_oneBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\电子-水平1.5-bunch0-稳定-1611_41\1611_41_luminosity_proton_200000turns.csv'
    )
    path_4e7p_offset_oneBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\电子-水平2.0-bunch0-稳定-0451_21\0451_21_luminosity_proton_200000turns.csv'
    )
    path_4e7p_offset_oneBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\电子-水平2.5-bunch0-稳定-1418_51\1418_51_luminosity_proton_200000turns.csv'
    )
    path_4e7p_offset_oneBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_单束团offset\电子-水平3.0-bunch0-稳定-1424_57\1424_57_luminosity_proton_200000turns.csv'
    )

    ######## 4e vs. 7p, one bunch with offset, end ##########

    for i in range(3):
        for j in range(3):
            index = i * 3 + j
            if index < len(path_1e1p_offset_lumi):
                read_plot_lumi(ax[i, j],
                               path_1e1p_offset_lumi[index], [0, 100000],
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
                               [0, 100000],
                               skiprows=8,
                               mymarkersize=0.01,
                               mylinewidth=0.1,
                               mycolor='tab:blue',
                               myalpha=0.2,
                               myfontsize=myfontsize_sub,
                               plottype='scatter')
            if index < len(path_4e7p_offset_allBunch_lumi):
                read_plot_lumi(ax[i, j],
                               path_4e7p_offset_allBunch_lumi[index],
                               [0, 350000],
                               skiprows=8,
                               mymarkersize=0.1,
                               mylinewidth=0.1,
                               mycolor='tab:green',
                               myalpha=0.02,
                               myfontsize=myfontsize_sub,
                               plottype='scatter')

    ax[0, 0].set_ylim((2, 2.5))

    ax[0, 0].set_title(r'$\Delta x = 0.2\sigma_x$',
                       pad=4,
                       fontsize=myfontsize_sub)
    ax[0, 1].set_title(r'$\Delta x = 0.4\sigma_x$',
                       pad=4,
                       fontsize=myfontsize_sub)
    ax[0, 2].set_title(r'$\Delta x = 0.6\sigma_x$',
                       pad=4,
                       fontsize=myfontsize_sub)
    ax[1, 0].set_title(r'$\Delta x = 0.8\sigma_x$',
                       pad=4,
                       fontsize=myfontsize_sub)
    ax[1, 1].set_title(r'$\Delta x = 1.0\sigma_x$',
                       pad=4,
                       fontsize=myfontsize_sub)
    ax[1, 2].set_title(r'$\Delta x = 1.5\sigma_x$',
                       pad=4,
                       fontsize=myfontsize_sub)
    ax[2, 0].set_title(r'$\Delta x = 2.0\sigma_x$',
                       pad=4,
                       fontsize=myfontsize_sub)
    ax[2, 1].set_title(r'$\Delta x = 2.5\sigma_x$',
                       pad=4,
                       fontsize=myfontsize_sub)
    ax[2, 2].set_title(r'$\Delta x = 3.0\sigma_x$',
                       pad=4,
                       fontsize=myfontsize_sub)

    # ax[2, 0].set_xlabel(r'Turn ($\times 10^4$)', fontsize=myfontsize)
    # ax[2, 1].set_xlabel(r'Turn ($\times 10^4$)', fontsize=myfontsize)
    # ax[2, 2].set_xlabel(r'Turn ($\times 10^4$)', fontsize=myfontsize)
    fig.supxlabel(r'Proton turns ($\times 10^4$)', fontsize=myfontsize)
    fig.supylabel(r'Luminosity $(\times 10^{33} \mathrm{cm^{-2}s^{-1}})$',
                  fontsize=myfontsize)

    x_major_locator = plt.MultipleLocator(2)
    y_major_locator = plt.MultipleLocator(0.1)
    ax[0, 0].xaxis.set_major_locator(x_major_locator)
    ax[0, 0].yaxis.set_major_locator(y_major_locator)

    fig.savefig(r'D:\OneDrive\模拟数据2\offset_compare_e.png', dpi=300)


def plot_electron_compare_largeSigam(fig, ax, myfontsize, myfontsize_sub):
    path_1e1p_offset_lumi = []
    path_4e7p_offset_allBunch_lumi = []

    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给电子加offset\电子-水平3.0-bunch0-稳定-0641_07\0641_07_luminosity_proton_100000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给电子加offset\2228_03_luminosity_proton_500000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给电子加offset\2229_57_luminosity_proton_500000turns.csv'
    )
    path_1e1p_offset_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_1e1p_给电子加offset\1618_03_luminosity_proton_500000turns.csv'
    )

    path_4e7p_offset_allBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_所有束团offset\电子-水平3.0所有-稳定-1625_42\1625_42_luminosity_proton_200000turns.csv'
    )
    path_4e7p_offset_allBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_所有束团offset\2216_48_luminosity_proton_200000turns.csv'
    )
    path_4e7p_offset_allBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_所有束团offset\2222_25_luminosity_proton_200000turns.csv'
    )
    path_4e7p_offset_allBunch_lumi.append(
        r'D:\OneDrive\模拟数据2\offset_4e7p_所有束团offset\1812_40_luminosity_proton_200000turns.csv'
    )

    for i in range(2):
        for j in range(2):
            index = i * 2 + j
            if index < len(path_1e1p_offset_lumi):
                read_plot_lumi(ax[i, j],
                               path_1e1p_offset_lumi[index], [0, 20000],
                               skiprows=2,
                               mymarkersize=0.01,
                               mylinewidth=1,
                               mycolor='tab:orange',
                               myalpha=0.8,
                               myfontsize=myfontsize_sub,
                               plottype='plot',
                               turnUnit=1,
                               mylable='1e vs. 1p')
            if index < len(path_4e7p_offset_allBunch_lumi):
                read_plot_lumi(ax[i, j],
                               path_4e7p_offset_allBunch_lumi[index],
                               [0, 20000],
                               skiprows=5,
                               mymarkersize=0.01,
                               mylinewidth=1,
                               mycolor='tab:blue',
                               myalpha=0.8,
                               myfontsize=myfontsize_sub,
                               plottype='plot',
                               turnUnit=1,
                               mylable='4e vs. 7p')
            ax[i, j].legend()
    ax[0, 0].set_ylim((-0.1, 2.5))

    ax[0, 0].set_title(r'$\Delta x = 3\sigma_x$',
                       pad=4,
                       fontsize=myfontsize_sub)
    ax[0, 1].set_title(r'$\Delta x = 5\sigma_x$',
                       pad=4,
                       fontsize=myfontsize_sub)
    ax[1, 0].set_title(r'$\Delta x = 10\sigma_x$',
                       pad=4,
                       fontsize=myfontsize_sub)
    ax[1, 1].set_title(r'$\Delta x = 15\sigma_x$',
                       pad=4,
                       fontsize=myfontsize_sub)
    ax[0, 0].tick_params(axis='both', which='both', direction='in', left=False)
    ax[0, 1].tick_params(axis='both', which='both', direction='in', left=False)
    ax[1, 0].tick_params(axis='both', which='both', direction='in', left=False)
    ax[1, 1].tick_params(axis='both', which='both', direction='in', left=False)
    fig.supxlabel(r'Proton turns', fontsize=myfontsize)
    fig.supylabel(r'Luminosity $(\times 10^{33} \mathrm{cm^{-2}s^{-1}})$',
                  fontsize=myfontsize)
    fig.savefig(r'D:\OneDrive\模拟数据2\offset_compare_e_largeSigma.png', dpi=300)


if __name__ == '__main__':

    myfontsize = 12
    myfontsize_sub = 10

    fig_p, ax_p = plt.subplots(3, 3, sharex=True, sharey=True)
    plot_proton_compare(fig_p, ax_p, myfontsize, myfontsize_sub)

    # fig_e, ax_e = plt.subplots(3, 3, sharex=True, sharey=True)
    # plot_electron_compare(fig_e, ax_e, myfontsize, myfontsize_sub)

    fig_e_1, ax_e_1 = plt.subplots(2, 2, sharex=True, sharey=True)
    plot_electron_compare_largeSigam(fig_e_1, ax_e_1, myfontsize,
                                     myfontsize_sub)

    plt.show()
