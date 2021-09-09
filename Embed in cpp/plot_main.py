from multiprocessing import Pool
from multiprocessing import Manager
from multiprocessing import process
from multiprocessing.context import Process
import os
import platform
import sys

from matplotlib.pyplot import legend
from plot_distribution import Distribution
import time
import matplotlib as mpl

from plot_statistic import *
from plot_luminosity import *
from load_parameter import *
from plot_tune import *
from plot_distribution import *
from plot_footprint import *


def plot_statistic_bunch_oneProcess(bunchid, row, col, row2, col2, home,
                                    yearMonDay, hourMinSec, para, myfigsize,
                                    myfontsize, myqueue):
    fig_stat_tmp0, ax_stat_tmp0 = plt.subplots(row, col, figsize=myfigsize)
    plt.xticks(fontsize=myfontsize)
    plt.yticks(fontsize=myfontsize)
    fig_stat_tmp1, ax_stat_tmp1 = plt.subplots(row, col, figsize=myfigsize)
    plt.xticks(fontsize=myfontsize)
    plt.yticks(fontsize=myfontsize)
    fig_stat_tmp2, ax_stat_tmp2 = plt.subplots(row, col, figsize=myfigsize)
    plt.xticks(fontsize=myfontsize)
    plt.yticks(fontsize=myfontsize)
    fig_stat_tmp3, ax_stat_tmp3 = plt.subplots(row2, col2, figsize=myfigsize)
    plt.xticks(fontsize=myfontsize)
    plt.yticks(fontsize=myfontsize)

    fig_stat_tmp0.subplots_adjust(left=0.05, right=0.96, bottom=0.05)
    fig_stat_tmp1.subplots_adjust(left=0.05, right=0.96, bottom=0.05)
    fig_stat_tmp2.subplots_adjust(left=0.05, right=0.96, bottom=0.05)
    fig_stat_tmp3.subplots_adjust(left=0.05, right=0.96, bottom=0.05)
    fig_stat_tmp0.subplots_adjust(top=0.87)
    fig_stat_tmp3.subplots_adjust(top=0.86, hspace=0.13)

    stat = Statistic(home, yearMonDay, hourMinSec, para.particle, bunchid,
                     para.nux, para.nuy)

    stat.load_statistic()

    stat.plot_statistic_part0(ax_stat_tmp0, myalpha=1, myfontsize=myfontsize)
    stat.manage_axGrid(ax_stat_tmp0, row, col)
    fig_stat_tmp0.suptitle(para.statnote)
    stat.save_bunchStatistic(fig_stat_tmp0, part=0)

    if stat.version == 'new':
        stat.plot_statistic_part1(ax_stat_tmp1,
                                  myalpha=1,
                                  myfontsize=myfontsize)
        stat.plot_statistic_part2(ax_stat_tmp2,
                                  myalpha=1,
                                  myfontsize=myfontsize)
        stat.plot_statistic_part3(ax_stat_tmp3,
                                  myalpha=1,
                                  myfontsize=myfontsize)

        stat.manage_axGrid(ax_stat_tmp1, row, col)
        stat.manage_axGrid(ax_stat_tmp2, row, col)
        stat.manage_axGrid(ax_stat_tmp3, row2, col2)

        fig_stat_tmp1.suptitle(para.statnote_part1)
        fig_stat_tmp2.suptitle(para.statnote_part2)
        fig_stat_tmp3.suptitle(para.statnote)

        stat.save_bunchStatistic(fig_stat_tmp1, part=1)
        stat.save_bunchStatistic(fig_stat_tmp2, part=2)
        stat.save_bunchStatistic(fig_stat_tmp3, part=3)

    plt.close(fig_stat_tmp0)
    plt.close(fig_stat_tmp1)
    plt.close(fig_stat_tmp2)
    plt.close(fig_stat_tmp3)

    print('File has been drawn: {0}'.format(stat.stat_file))


def plot_statistic_beam(row, col, row2, col2, home, yearMonDay, hourMinSec,
                        para, myfigsize, myfontsize):
    if para.nbunch > 1:
        fig_stat0, ax_stat0 = plt.subplots(row, col, figsize=myfigsize)
        plt.xticks(fontsize=myfontsize)
        plt.yticks(fontsize=myfontsize)
        fig_stat1, ax_stat1 = plt.subplots(row, col, figsize=myfigsize)
        plt.xticks(fontsize=myfontsize)
        plt.yticks(fontsize=myfontsize)
        fig_stat2, ax_stat2 = plt.subplots(row, col, figsize=myfigsize)
        plt.xticks(fontsize=myfontsize)
        plt.yticks(fontsize=myfontsize)
        fig_stat3, ax_stat3 = plt.subplots(row2, col2, figsize=myfigsize)
        plt.xticks(fontsize=myfontsize)
        plt.yticks(fontsize=myfontsize)

        fig_stat0.subplots_adjust(left=0.05, right=0.96, bottom=0.05)
        fig_stat1.subplots_adjust(left=0.05, right=0.96, bottom=0.05)
        fig_stat2.subplots_adjust(left=0.05, right=0.96, bottom=0.05)
        fig_stat3.subplots_adjust(left=0.05, right=0.96, bottom=0.05)

        fig_stat0.subplots_adjust(top=0.87)
        fig_stat3.subplots_adjust(top=0.86, hspace=0.13)

        for i in range(para.nbunch):
            stat = Statistic(home, yearMonDay, hourMinSec, para.particle, i,
                             para.nux, para.nuy)

            stat.load_statistic()

            stat.plot_statistic_part0(ax_stat0,
                                      myalpha=0.5,
                                      myfontsize=myfontsize)
            if stat.version == 'new':
                stat.plot_statistic_part1(ax_stat1,
                                          myalpha=0.5,
                                          myfontsize=myfontsize)
                stat.plot_statistic_part2(ax_stat2,
                                          myalpha=0.5,
                                          myfontsize=myfontsize)
                stat.plot_statistic_part3(ax_stat3,
                                          myalpha=0.5,
                                          myfontsize=myfontsize)

        stat.manage_axGrid(ax_stat0, row, col)
        fig_stat0.suptitle(para.statnote)
        stat.save_beamStatistic(fig_stat0, part=0)
        if stat.version == 'new':
            stat.manage_axGrid(ax_stat1, row, col)
            stat.manage_axGrid(ax_stat2, row, col)
            stat.manage_axGrid(ax_stat3, row2, col2)

            fig_stat1.suptitle(para.statnote_part1)
            fig_stat2.suptitle(para.statnote_part2)
            fig_stat3.suptitle(para.statnote)

            stat.save_beamStatistic(fig_stat1, part=1)
            stat.save_beamStatistic(fig_stat2, part=2)
            stat.save_beamStatistic(fig_stat3, part=3)

        plt.close(fig_stat0)
        plt.close(fig_stat1)
        plt.close(fig_stat2)
        plt.close(fig_stat3)
        print('File has been drawn: beam {0}'.format(stat.particle))


def plot_statistic_main(home, yearMonDay, hourMinSec, para, myfigsize,
                        myfontsize, ncpu):
    print('\nStart drawing {0:s} statistic data'.format(para.particle))
    row = 3
    col = 3
    row2 = 2
    col2 = 2

    if ncpu == 1:
        for i in range(para.nbunch):
            plot_statistic_bunch_oneProcess(i, row, col, row2, col2, home,
                                            yearMonDay, hourMinSec, para,
                                            myfigsize, myfontsize, 'no queue')
    else:
        ps = []
        for i in range(para.nbunch):
            p = Process(target=plot_statistic_bunch_oneProcess,
                        args=(i, row, col, row2, col2, home, yearMonDay,
                              hourMinSec, para, myfigsize, myfontsize,
                              'queue'))
            ps.append(p)
        for i in range(para.nbunch):
            ps[i].start()
            print('Total cpu cores: {0:d}, task {1:d}/{2:d} has been added'.
                  format(os.cpu_count(), i, para.nbunch))
        for i in range(para.nbunch):
            ps[i].join()

        # mymanager = Manager()
        # myqueue = mymanager.Queue(ncpu)
        # mypool = Pool(processes=ncpu)
        # for i in range(para.nbunch):
        #     mypool.apply_async(
        #         plot_statistic_bunch_oneProcess,
        #         (i, row, col, row2, col2, home, yearMonDay, hourMinSec, para,
        #          myfigsize, myfontsize, myqueue))
        #     print(
        #         'Process pool size: {0:d}, task {1:d}/{2:d} has been added asynchronously'
        #         .format(ncpu, i, para.nbunch))
        # mypool.close()
        # mypool.join()

    plot_statistic_beam(row, col, row2, col2, home, yearMonDay, hourMinSec,
                        para, myfigsize, myfontsize)


def plot_luminosity_main(home,
                         yearMonDay,
                         hourMinSec,
                         para1,
                         para2,
                         myfigsize,
                         myfontsize,
                         particle3='suPeriod',
                         nbunch3=1):
    print('\nStart drawing luminosity data')
    lumi = 'tmp'
    particle = [para1.particle, para2.particle, particle3]
    skip = [para2.nbunch, para1.nbunch, nbunch3]

    fig_lumi, ax_lumi = plt.subplots(1, 3, figsize=myfigsize, sharey='all')
    fig_lumi.subplots_adjust(left=0.04, right=0.98, bottom=0.06, wspace=0.12)
    plt.xticks(fontsize=myfontsize)
    plt.yticks(fontsize=myfontsize)

    for i in range(3):
        fig_tmp, ax_tmp = plt.subplots(1, figsize=(8, 6))
        plt.xticks(fontsize=myfontsize)
        plt.yticks(fontsize=myfontsize)

        fig_tmp.subplots_adjust(left=0.09, right=0.97, top=0.83, bottom=0.08)
        mpl.rcParams['agg.path.chunksize'] = 10000
        lumi = Luminosity(home, yearMonDay, hourMinSec, particle[i],
                          myfontsize)
        lumi.load_luminosity(skip[i])
        lumi.plot_luminosity(ax_tmp, myalpha=1)
        lumi.plot_luminosity(ax_lumi[i], myalpha=1)

        ax_tmp.set_ylabel(r'Luminosity $(\mathrm{cm}^{-2}\mathrm{s}^{-1})$',
                          fontsize=myfontsize)
        ax_tmp.set_xlabel('Turn', fontsize=myfontsize)
        ax_tmp.grid()
        ax_tmp.legend(fontsize=myfontsize)
        ax_lumi[i].set_ylabel(
            r'Luminosity $(\mathrm{cm}^{-2}\mathrm{s}^{-1})$',
            fontsize=myfontsize)
        ax_lumi[i].set_xlabel('Turn', fontsize=myfontsize)
        ax_lumi[i].grid()

        fig_tmp.suptitle(para1.luminote)
        ax_lumi[i].legend(fontsize=myfontsize)

        lumi.save_lumi(fig_tmp)
        plt.close(fig_tmp)
        print('File has been drawn: {0}'.format(lumi.lumi_file))

    fig_lumi.suptitle(para1.luminote)
    lumi.save_lumiPath = lumi.save_lumiTogetherPath
    lumi.save_lumi(fig_lumi)
    plt.close(fig_lumi)


def plot_tune_oneProcess(order, home, yearMonDay, hourMinSec, para, myfigsize,
                         myfontsize, i, xlim, ylim, myqueue):
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
        if tune.isExist[j]:
            fig_tmp1, ax_tmp1 = plt.subplots(1, figsize=myfigsize)
            fig_tmp1.subplots_adjust(left=0.1, right=0.96, bottom=0.08)
            plt.xticks(fontsize=myfontsize)
            plt.yticks(fontsize=myfontsize)

            fig_tmp2, ax_tmp2 = plt.subplots(1, figsize=myfigsize)
            fig_tmp2.subplots_adjust(left=0.1, right=0.96, bottom=0.08)
            plt.xticks(fontsize=myfontsize)
            plt.yticks(fontsize=myfontsize)

            tune.plot_scatter(ax_tmp1,
                              j,
                              resonanceOrder=order,
                              myalpha=0.5,
                              mysize=1,
                              myfontsize=myfontsize)
            ax_tmp1.scatter(para.nux,
                            para.nuy,
                            marker='x',
                            color='black',
                            s=100,
                            zorder=order)

            ax_tmp1.set_xlabel(r'$\nu_x$', fontsize=myfontsize)
            ax_tmp1.set_ylabel(r'$\nu_y$', fontsize=myfontsize)

            fig_tmp1.suptitle('{0:s}\n{1:s} bunch{2:d} turn {3:s}'.format(
                para.statnote, para.particle, i, tune.tune_turn[j]),
                              fontsize=10)

            tune.save_scatter(fig_tmp1, j)
            plt.close(fig_tmp1)

            # ax_tmp1.clear()
            # ax_tmp1.tick_params(top=False, right=False)

            tune.plot_hexbin(ax_tmp2,
                             j,
                             resonanceOrder=order,
                             myalpha=0.3,
                             mysize=200,
                             myfontsize=myfontsize)
            ax_tmp2.scatter(para.nux,
                            para.nuy,
                            marker='x',
                            color='black',
                            s=100,
                            zorder=order)

            ax_tmp2.set_xlabel(r'$\nu_x$', fontsize=myfontsize)
            ax_tmp2.set_ylabel(r'$\nu_y$', fontsize=myfontsize)

            fig_tmp2.suptitle('{0:s}\n{1:s} bunch{2:d} turn {3:s}'.format(
                para.statnote, para.particle, i, tune.tune_turn[j]),
                              fontsize=10)
            # ax_tmp2.tick_params(top=False, right=False)

            tune.save_hexbin(fig_tmp2, j)
            plt.close(fig_tmp2)
            print('File has been drawn: {0}'.format(tune.file[j]))


def plot_tune_main(home, yearMonDay, hourMinSec, para, myfigsize, myfontsize,
                   ncpu):
    print('\nStart drawing {0:s} tune spread data'.format(para.particle))
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

    if ncpu == 1:
        for i in range(para.nbunch):
            plot_tune_oneProcess(order, home, yearMonDay, hourMinSec, para,
                                 myfigsize, myfontsize, i, xlim, ylim,
                                 'no queue')
    else:
        ps = []
        for i in range(para.nbunch):
            p = Process(target=plot_tune_oneProcess,
                        args=(order, home, yearMonDay, hourMinSec, para,
                              myfigsize, myfontsize, i, xlim, ylim, 'queue'))
            ps.append(p)
        for i in range(para.nbunch):
            ps[i].start()
            print('Total cpu cores: {0:d}, task {1:d}/{2:d} has been added'.
                  format(os.cpu_count(), i, para.nbunch))
        for i in range(para.nbunch):
            ps[i].join()
        # mymanager = Manager()
        # myqueue = mymanager.Queue(ncpu)
        # mypool = Pool(processes=ncpu)
        # for i in range(para.nbunch):
        #     mypool.apply_async(plot_tune_oneProcess,
        #                        (order, home, yearMonDay, hourMinSec, para,
        #                         myfigsize, myfontsize, i, xlim, ylim, myqueue))
        #     print(
        #         'Process pool size: {0:d}, task {1:d}/{2:d} has been added asynchronously'
        #         .format(ncpu, i, para.nbunch))
        # mypool.close()
        # mypool.join()


def plot_distribution_oneProcess(bunchid, home, yearMonDay, hourMinSec, para,
                                 myfigsize, myqueue):
    dist = Distribution(home,
                        yearMonDay,
                        hourMinSec,
                        para.particle,
                        bunchid,
                        dist='gaussian')

    dist.load_plot_save(para, myfigsize=myfigsize, mysize=200, mybins=300)


def plot_distribution_main(home, yearMonDay, hourMinSec, para, myfigsize,
                           ncpu):
    print('\nStart drawing {0:s} distribution data'.format(para.particle))
    if ncpu == 1:
        for i in range(para.nbunch):
            plot_distribution_oneProcess(i, home, yearMonDay, hourMinSec, para,
                                         myfigsize, 'no queue')
    else:
        ps = []
        for i in range(para.nbunch):
            p = Process(target=plot_distribution_oneProcess,
                        args=(i, home, yearMonDay, hourMinSec, para, myfigsize,
                              'queue'))
            ps.append(p)
        for i in range(para.nbunch):
            ps[i].start()
            print('Total cpu cores: {0:d}, task {1:d}/{2:d} has been added'.
                  format(os.cpu_count(), i, para.nbunch))
        for i in range(para.nbunch):
            ps[i].join()
        # mymanager = Manager()
        # myqueue = mymanager.Queue(ncpu)
        # mypool = Pool(processes=ncpu)
        # for i in range(para.nbunch):
        #     mypool.apply_async(
        #         plot_distribution_oneProcess,
        #         (i, home, yearMonDay, hourMinSec, para, myfigsize, myqueue))
        #     print(
        #         'Process pool size: {0:d}, task {1:d}/{2:d} has been added asynchronously'
        #         .format(ncpu, i, para.nbunch))
        # mypool.close()
        # mypool.join()


def plot_fma_oneProcess(bunchid, home, yearMonDay, hourMinSec, para, myfigsize,
                        myfontsize):
    myfootprint = FootPrint(home, yearMonDay, hourMinSec, para.particle,
                            bunchid)
    myfootprint.load_plot_save(para, myfigsize, myfontsize)


def plot_fma_main(home, yearMonDay, hourMinSec, para, myfigsize, myfontsize,
                  ncpu):
    print('\nStart drawing {0:s} Frequency Map'.format(para.particle))
    if ncpu == 1:
        for i in range(para.nbunch):
            plot_fma_oneProcess(i, home, yearMonDay, hourMinSec, para,
                                myfigsize, myfontsize)
    else:
        ps = []
        for i in range(para.nbunch):
            p = Process(target=plot_fma_oneProcess,
                        args=(i, home, yearMonDay, hourMinSec, para, myfigsize,
                              myfontsize))
            ps.append(p)
        for i in range(para.nbunch):
            ps[i].start()
            print('Total cpu cores: {0:d}, task {1:d}/{2:d} has been added'.
                  format(os.cpu_count(), i, para.nbunch))
        for i in range(para.nbunch):
            ps[i].join()


def main(home, yearMonDay, hourMinSec, ncpu=1, type=['all']):
    # Default contexts and start methods on Windows is spawn.
    # Default contexts and start methods on Unix is fork.
    if platform.system() == 'Linux':
        ncpu = os.cpu_count() - 1

    startTime = time.time()
    beam1 = Parameter(home, yearMonDay, hourMinSec, 'beam1')
    beam2 = Parameter(home, yearMonDay, hourMinSec, 'beam2')

    my_figsize1 = (20, 10)
    my_figsize2 = (15, 10)
    my_figsize_fma = (8, 6)
    my_fontsize_stat = 12
    my_fontsize_lumi = 12
    my_fontsize_tune = 20
    my_fontsize_fma = 15

    # beam1.print()
    # beam2.print()

    beam1.gen_note_withPath(beam2)
    beam2.gen_note_withPath(beam1)

    # print(beam1.statnote)
    # print(beam2.statnote)

    for kind in type:
        if kind == 'all' or kind == 'stat':
            plot_statistic_main(home, yearMonDay, hourMinSec, beam1,
                                my_figsize1, my_fontsize_stat, ncpu)

            plot_statistic_main(home, yearMonDay, hourMinSec, beam2,
                                my_figsize1, my_fontsize_stat, ncpu)

        if kind == 'all' or kind == 'lumi':
            plot_luminosity_main(home, yearMonDay, hourMinSec, beam1, beam2,
                                 my_figsize1, my_fontsize_lumi)

        if kind == 'all' or kind == 'dist':
            plot_distribution_main(home, yearMonDay, hourMinSec, beam1,
                                   my_figsize1, ncpu)

            plot_distribution_main(home, yearMonDay, hourMinSec, beam2,
                                   my_figsize1, ncpu)

        if kind == 'all' or kind == 'tune':
            plot_tune_main(home, yearMonDay, hourMinSec, beam1, my_figsize2,
                           my_fontsize_tune, ncpu)

            plot_tune_main(home, yearMonDay, hourMinSec, beam2, my_figsize2,
                           my_fontsize_tune, ncpu)

        if kind == 'all' or kind == 'fma':
            plot_fma_main(home, yearMonDay, hourMinSec, beam1, my_figsize_fma,
                          my_fontsize_fma, ncpu)

            plot_fma_main(home, yearMonDay, hourMinSec, beam2, my_figsize_fma,
                          my_fontsize_fma, ncpu)

    endtime = time.time()
    print('start   : ', time.asctime(time.localtime(startTime)))
    print('end     : ', time.asctime(time.localtime(endtime)))
    print('running :  {0:d} min'.format(int((endtime - startTime) / 60)))

    return 0


if __name__ == '__main__':
    home = ''
    if platform.system() == 'Windows':
        home = os.sep.join(['D:', 'bb2021'])
    elif platform.system() == 'Linux':
        home = os.sep.join(['/home', 'changmx', 'bb2021'])
    else:
        print('We do not support {0} system now.}'.format(platform.system()))
        os.exit(1)

    command = ('all', 'stat', 'lumi', 'tune', 'dist', 'fma')

    type = []
    if len(sys.argv) == 1:
        type = ['all']
    else:
        for iargv in range(1, len(sys.argv)):
            if sys.argv[iargv] in command:
                type.append(sys.argv[iargv])
            else:
                print('Warning: invalid option "{0}"'.format(
                    sys.argv[iargv]))

    yearMonDay = '2021_0908'
    hourMinSec = '1713_19'
    # yearMonDay = '2021_0907'
    # hourMinSec = '0938_30'

    ncpu = os.cpu_count() - 1
    status = main(home, yearMonDay, hourMinSec, ncpu=ncpu, type=type)
    print(status)
