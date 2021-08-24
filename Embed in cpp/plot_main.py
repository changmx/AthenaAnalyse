from multiprocessing import Pool
import os
from plot_distribution import Distribution
import time
import matplotlib as mpl

from plot_statistic import *
from plot_luminosity import *
from load_parameter import *
from plot_tune import *
from plot_distribution import *


def plot_statistic_main(home, yearMonDay, hourMinSec, para, myfigsize):
    stat = []
    row = 3
    col = 3
    row2 = 2
    col2 = 2

    fig_stat0, ax_stat0 = plt.subplots(row, col, figsize=myfigsize)
    fig_stat1, ax_stat1 = plt.subplots(row, col, figsize=myfigsize)
    fig_stat2, ax_stat2 = plt.subplots(row, col, figsize=myfigsize)
    fig_stat3, ax_stat3 = plt.subplots(row2, col2, figsize=myfigsize)

    fig_stat0.subplots_adjust(left=0.05, right=0.96, bottom=0.05)
    fig_stat1.subplots_adjust(left=0.05, right=0.96, bottom=0.05)
    fig_stat2.subplots_adjust(left=0.05, right=0.96, bottom=0.05)
    fig_stat3.subplots_adjust(left=0.05, right=0.96, bottom=0.05)

    for i in range(para.nbunch):

        fig_stat_tmp0, ax_stat_tmp0 = plt.subplots(row, col, figsize=myfigsize)
        fig_stat_tmp1, ax_stat_tmp1 = plt.subplots(row, col, figsize=myfigsize)
        fig_stat_tmp2, ax_stat_tmp2 = plt.subplots(row, col, figsize=myfigsize)
        fig_stat_tmp3, ax_stat_tmp3 = plt.subplots(row2,
                                                   col2,
                                                   figsize=myfigsize)
        fig_stat_tmp0.subplots_adjust(left=0.05, right=0.96, bottom=0.05)
        fig_stat_tmp1.subplots_adjust(left=0.05, right=0.96, bottom=0.05)
        fig_stat_tmp2.subplots_adjust(left=0.05, right=0.96, bottom=0.05)
        fig_stat_tmp3.subplots_adjust(left=0.05, right=0.96, bottom=0.05)

        stat.append(
            Statistic(home, yearMonDay, hourMinSec, para.particle, i, para.nux,
                      para.nuy))

        stat[i].load_statistic()

        stat[i].plot_statistic_part0(ax_stat_tmp0, myalpha=1)
        stat[i].manage_axGrid(ax_stat_tmp0, row, col)
        fig_stat_tmp0.suptitle(para.statnote)
        stat[i].save_bunchStatistic(fig_stat_tmp0, part=0)

        if para.nbunch > 1:
            stat[i].plot_statistic_part0(ax_stat0, myalpha=0.5)

        if stat[i].version == 'new':
            stat[i].plot_statistic_part1(ax_stat_tmp1, myalpha=1)
            stat[i].plot_statistic_part2(ax_stat_tmp2, myalpha=1)
            stat[i].plot_statistic_part3(ax_stat_tmp3, myalpha=1)

            stat[i].manage_axGrid(ax_stat_tmp1, row, col)
            stat[i].manage_axGrid(ax_stat_tmp2, row, col)
            stat[i].manage_axGrid(ax_stat_tmp3, row2, col2)

            fig_stat_tmp1.suptitle(para.statnote_part1)
            fig_stat_tmp2.suptitle(para.statnote_part2)
            fig_stat_tmp3.suptitle(para.statnote)

            stat[i].save_bunchStatistic(fig_stat_tmp1, part=1)
            stat[i].save_bunchStatistic(fig_stat_tmp2, part=2)
            stat[i].save_bunchStatistic(fig_stat_tmp3, part=3)

            if para.nbunch > 1:
                stat[i].plot_statistic_part1(ax_stat1, myalpha=0.5)
                stat[i].plot_statistic_part2(ax_stat2, myalpha=0.5)
                stat[i].plot_statistic_part3(ax_stat3, myalpha=0.5)

        plt.close(fig_stat_tmp0)
        plt.close(fig_stat_tmp1)
        plt.close(fig_stat_tmp2)
        plt.close(fig_stat_tmp3)

        print('File has been drawn: {0}'.format(stat[i].stat_file))

    if para.nbunch > 1:
        stat[0].manage_axGrid(ax_stat0, row, col)
        fig_stat0.suptitle(para.statnote)
        stat[0].save_beamStatistic(fig_stat0, part=0)

        if stat[i].version == 'new':
            stat[0].manage_axGrid(ax_stat1, row, col)
            stat[0].manage_axGrid(ax_stat2, row, col)
            stat[0].manage_axGrid(ax_stat3, row2, col2)

            fig_stat1.suptitle(para.statnote)
            fig_stat2.suptitle(para.statnote)
            fig_stat3.suptitle(para.statnote)

            stat[0].save_beamStatistic(fig_stat1, part=1)
            stat[0].save_beamStatistic(fig_stat2, part=2)
            stat[0].save_beamStatistic(fig_stat3, part=3)

    plt.close(fig_stat0)
    plt.close(fig_stat1)
    plt.close(fig_stat2)
    plt.close(fig_stat3)


def plot_luminosity_main(home,
                         yearMonDay,
                         hourMinSec,
                         para1,
                         para2,
                         myfigsize,
                         particle3='suPeriod',
                         nbunch3=1):
    lumi = []
    particle = [para1.particle, para2.particle, particle3]
    skip = [para2.nbunch, para1.nbunch, nbunch3]
    
    fig_lumi, ax_lumi = plt.subplots(1, 3, figsize=myfigsize, sharey='all')

    for i in range(3):
        fig_tmp, ax_tmp = plt.subplots(1, figsize=myfigsize)
        mpl.rcParams['agg.path.chunksize']=10000
        lumi.append(Luminosity(home, yearMonDay, hourMinSec, particle[i]))
        lumi[i].load_luminosity(skip[i])
        lumi[i].plot_luminosity(ax_tmp, myalpha=1)
        lumi[i].plot_luminosity(ax_lumi[i], myalpha=1)

        ax_tmp.set_ylabel(r'Luminosity $(\mathrm{cm}^{-2}\mathrm{s}^{-1})$')
        ax_tmp.set_xlabel('Turn')
        ax_tmp.grid()
        ax_tmp.legend()
        ax_lumi[i].set_ylabel(
            r'Luminosity $(\mathrm{cm}^{-2}\mathrm{s}^{-1})$')
        ax_lumi[i].set_xlabel('Turn')
        ax_lumi[i].grid()

        fig_tmp.suptitle(para1.luminote)
        ax_lumi[i].legend()

        lumi[i].save_lumi(fig_tmp)
        plt.close(fig_tmp)
        print('File has been drawn: {0}'.format(lumi[i].lumi_file))

    fig_lumi.suptitle(para1.luminote)
    lumi[0].save_lumiPath = lumi[0].save_lumiTogetherPath
    lumi[0].save_lumi(fig_lumi)

    plt.close(fig_lumi)


def plot_tune_oneProcess(order, home, yearMonDay, hourMinSec, para, myfigsize,
                         i, xlim, ylim):
    '''
    使用多线程同时处理不同束团的tune信息

    之前在tune.load()函数之后使用多线程，即同时处理一个束团的不同phase_turn的数据，发现这样很慢。
    目前认为原因是在执行tune.load()之后，tune对象里数据量太大，传递这些数据给不同线程太耗时间，导致并行效果很差。
    因此改为并行处理不同束团，这样在不同线程内部加载数据文件，就可以省去传递数据所耗时间。
    '''
    tune = Tune(home, yearMonDay, hourMinSec, para.particle, i, para.nux,
                para.nuy, xlim, ylim)
    tune.load()
    for j in range(len(tune.file)):
        fig_tmp1, ax_tmp1 = plt.subplots(1, figsize=myfigsize)
        fig_tmp2, ax_tmp2 = plt.subplots(1, figsize=myfigsize)
        tune.plot_scatter(ax_tmp1,
                          j,
                          resonanceOrder=order,
                          myalpha=0.5,
                          mysize=1)
        ax_tmp1.scatter(para.nux,
                        para.nuy,
                        marker='x',
                        color='black',
                        zorder=order)

        ax_tmp1.set_xlabel(r'$\nu_x$')
        ax_tmp1.set_ylabel(r'$\nu_y$')

        ax_tmp1.set_title('{0:s} bunch{1:d} turn {2:s}'.format(
            para.particle, i, tune.tune_turn[j]))
        fig_tmp1.suptitle(para.statnote)

        tune.save_scatter(fig_tmp1, j)
        plt.close(fig_tmp1)

        # ax_tmp1.clear()
        # ax_tmp1.tick_params(top=False, right=False)

        tune.plot_hexbin(ax_tmp2,
                         j,
                         resonanceOrder=order,
                         myalpha=0.3,
                         mysize=200)
        ax_tmp2.scatter(para.nux,
                        para.nuy,
                        marker='x',
                        color='black',
                        zorder=order)

        ax_tmp2.set_xlabel(r'$\nu_x$')
        ax_tmp2.set_ylabel(r'$\nu_y$')

        ax_tmp2.set_title('{0:s} bunch{1:d} turn {2:s}'.format(
            para.particle, i, tune.tune_turn[j]))
        fig_tmp2.suptitle(para.statnote)
        # ax_tmp2.tick_params(top=False, right=False)

        tune.save_hexbin(fig_tmp2, j)

        plt.close(fig_tmp2)
        print('File has been drawn: {0}'.format(tune.file[j]))


def plot_tune_main(home, yearMonDay, hourMinSec, para, myfigsize):

    order = 10

    if para.particle == 'proton':
        factor = 8
    elif para.particle == 'electron':
        factor = 1

    if para.tuneshift_direction > 0:
        xmin = para.nux - 0.01
        ymin = para.nuy - 0.01
        xmax = para.nux + factor * para.xix
        ymax = para.nuy + factor * para.xiy
        xmax = float(format(xmax, '.2f'))
        ymax = float(format(ymax, '.2f'))
    else:
        xmax = para.nux - 0.01
        ymax = para.nuy - 0.01
        xmin = para.nux + factor * para.xix
        ymin = para.nuy + factor * para.xiy
        xmin = float(format(xmin, '.2f'))
        ymin = float(format(ymin, '.2f'))

    xmin = xmin if xmin >= 0 else 0
    xmax = xmax if xmax <= 1 else 1
    ymin = ymin if ymin >= 0 else 0
    ymax = ymax if ymax <= 1 else 1

    xlim = [xmin, xmax]
    ylim = [ymin, ymax]

    mypool = Pool(processes=(os.cpu_count() - 1))
    for i in range(para.nbunch):
        mypool.apply_async(plot_tune_oneProcess,
                           (order, home, yearMonDay, hourMinSec, para,
                            myfigsize, i, xlim, ylim))
    mypool.close()
    mypool.join()


def plot_distribution_main(home, yearMonDay, hourMinSec, para, myfigsize):

    for i in range(para.nbunch):
        dist = Distribution(home,
                            yearMonDay,
                            hourMinSec,
                            para.particle,
                            i,
                            dist='gaussian')
        dist.load_plot_save(para, myfigsize=myfigsize, mysize=200, mybins=300)


def main(home, yearMonDay, hourMinSec):
    beam1 = Parameter(home, yearMonDay, hourMinSec, 'beam1')
    beam2 = Parameter(home, yearMonDay, hourMinSec, 'beam2')

    my_figsize1 = (20, 10)
    my_figsize2 = (15, 10)

    # beam1.print()
    # beam2.print()

    beam1.gen_note_withPath(beam2)
    beam2.gen_note_withPath(beam1)

    # print(beam1.statnote)
    # print(beam2.statnote)

    plot_statistic_main(home, yearMonDay, hourMinSec, beam1, my_figsize1)

    plot_statistic_main(home, yearMonDay, hourMinSec, beam2, my_figsize1)

    plot_luminosity_main(home, yearMonDay, hourMinSec, beam1, beam2,
                         my_figsize1)

    plot_distribution_main(home, yearMonDay, hourMinSec, beam1, my_figsize1)

    plot_distribution_main(home, yearMonDay, hourMinSec, beam2, my_figsize1)

    plot_tune_main(home, yearMonDay, hourMinSec, beam1, my_figsize2)

    plot_tune_main(home, yearMonDay, hourMinSec, beam2, my_figsize2)

    return 0


if __name__ == '__main__':
    home = '/home/changmx/bb2021'
    yearMonDay = '2021_0820'
    hourMinSec = '1154_34'

    status = main(home, yearMonDay, hourMinSec)
    print(status)
