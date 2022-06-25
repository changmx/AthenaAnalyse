from ast import arg
from multiprocessing import Pool
from multiprocessing import Manager
from multiprocessing import process
from multiprocessing.context import Process
import os
import platform
import sys
import socket
import getopt

from matplotlib.pyplot import legend, title
from plot_distribution import Distribution
import time
import matplotlib as mpl
import matplotlib
from plot_general import TimeStat

from plot_statistic import *
from plot_luminosity import *
from load_parameter import *
from plot_tune import *
from plot_distribution import *
from plot_footprint import *


def plot_statistic_bunch_oneProcess(bunchid, row, col, row2, col2, home,
                                    yearMonDay, hourMinSec, para, nbunch_opp,
                                    myfigsize, myfontsize, myqueue,
                                    isPlotSingle):
    matplotlib.rcParams['agg.path.chunksize'] = 10000
    plt.rcParams.update({'figure.max_open_warning': 0})
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
    fig_stat_tmp4, ax_stat_tmp4 = plt.subplots(row2, col2, figsize=myfigsize)
    plt.xticks(fontsize=myfontsize)
    plt.yticks(fontsize=myfontsize)

    fig_stat_tmp0.subplots_adjust(left=0.05, right=0.96, bottom=0.05)
    fig_stat_tmp1.subplots_adjust(left=0.05, right=0.96, bottom=0.05)
    fig_stat_tmp2.subplots_adjust(left=0.05, right=0.96, bottom=0.05)
    fig_stat_tmp3.subplots_adjust(left=0.05, right=0.96, bottom=0.05)
    fig_stat_tmp0.subplots_adjust(top=0.87)
    fig_stat_tmp3.subplots_adjust(top=0.86, hspace=0.13)

    fig_single = []
    ax_single = []
    single_name = [
        'x-average', 'x-sigma', 'x-emit', 'y-average', 'y-sigma', 'y-emit',
        'x-fft', 'y-fft', 'loss', 'px-average', 'px-sigma', 'z-average',
        'py-average', 'py-sigma', 'z-sigma', 'pz-average', 'pz-sigma',
        'loss-percent', 'beta-x', 'beta-y', 'invariant-x', 'alpha-x',
        'alpha-y', 'invariant-y', 'gamma-x', 'gamma-y', 'xz-average',
        'xy-average', 'yz-average', 'xzDevideSigmaxSigmaZ', 'x-skewness',
        'x-kurtosis', 'y-skewness', 'y-kurtosis'
    ]
    if isPlotSingle:
        for i_single in range(34):
            fig_tmp, ax_tmp = plt.subplots(figsize=(8, 6))
            plt.xticks(fontsize=15)
            plt.yticks(fontsize=15)
            fig_single.append(fig_tmp)
            ax_single.append(ax_tmp)

    stat = Statistic(home, yearMonDay, hourMinSec, para.particle, bunchid,
                     para.nux, para.nuy, para.sigmax, para.sigmay,
                     para.sigmapx, para.sigmapy, nbunch_opp, isPlotSingle)

    stat.load_statistic()

    stat.plot_statistic_part0(ax_stat_tmp0,
                              ax_single,
                              myalpha=1,
                              myfontsize=myfontsize)
    stat.plot_statistic_part1(ax_stat_tmp1,
                              ax_single,
                              myalpha=1,
                              myfontsize=myfontsize)
    stat.plot_statistic_part2(ax_stat_tmp2,
                              ax_single,
                              myalpha=1,
                              myfontsize=myfontsize)
    stat.plot_statistic_part3(ax_stat_tmp3,
                              ax_single,
                              myalpha=1,
                              myfontsize=myfontsize)
    stat.plot_statistic_part4(ax_stat_tmp4,
                              ax_single,
                              myalpha=1,
                              myfontsize=myfontsize)

    stat.manage_axGrid(ax_stat_tmp0, row, col)
    stat.manage_axGrid(ax_stat_tmp1, row, col)
    stat.manage_axGrid(ax_stat_tmp2, row, col)
    stat.manage_axGrid(ax_stat_tmp3, row2, col2)
    stat.manage_axGrid(ax_stat_tmp4, row2, col2)

    fig_stat_tmp0.suptitle(para.statnote)
    fig_stat_tmp1.suptitle(para.statnote_part1)
    fig_stat_tmp2.suptitle(para.statnote_part2)
    fig_stat_tmp3.suptitle(para.statnote)
    fig_stat_tmp4.suptitle(para.statnote)

    stat.save_bunchStatistic(fig_stat_tmp0, part=0)
    stat.save_bunchStatistic(fig_stat_tmp1, part=1)
    stat.save_bunchStatistic(fig_stat_tmp2, part=2)
    stat.save_bunchStatistic(fig_stat_tmp3, part=3)
    stat.save_bunchStatistic(fig_stat_tmp4, part=4)

    plt.close(fig_stat_tmp0)
    plt.close(fig_stat_tmp1)
    plt.close(fig_stat_tmp2)
    plt.close(fig_stat_tmp3)
    plt.close(fig_stat_tmp4)

    if isPlotSingle:
        for i_single in range(34):
            fig_single[i_single].savefig(stat.save_bunchStatisticPath_single +
                                         '_' + single_name[i_single],
                                         dpi=300)
            plt.close(fig_single[i_single])

    print('File has been drawn: {0}'.format(stat.stat_file))


def plot_statistic_beam(row, col, row2, col2, home, yearMonDay, hourMinSec,
                        para, nbunch_opp, myfigsize, myfontsize, isPlotSingle):
    matplotlib.rcParams['agg.path.chunksize'] = 10000
    plt.rcParams.update({'figure.max_open_warning': 0})

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
        fig_stat4, ax_stat4 = plt.subplots(row2, col2, figsize=myfigsize)
        plt.xticks(fontsize=myfontsize)
        plt.yticks(fontsize=myfontsize)

        fig_stat0.subplots_adjust(left=0.05, right=0.96, bottom=0.05)
        fig_stat1.subplots_adjust(left=0.05, right=0.96, bottom=0.05)
        fig_stat2.subplots_adjust(left=0.05, right=0.96, bottom=0.05)
        fig_stat3.subplots_adjust(left=0.05, right=0.96, bottom=0.05)

        fig_stat0.subplots_adjust(top=0.87)
        fig_stat3.subplots_adjust(top=0.86, hspace=0.13)

        fig_single = []
        ax_single = []
        single_name = [
            'x-average', 'x-sigma', 'x-emit', 'y-average', 'y-sigma', 'y-emit',
            'x-fft', 'y-fft', 'loss', 'px-average', 'px-sigma', 'z-average',
            'py-average', 'py-sigma', 'z-sigma', 'pz-average', 'pz-sigma',
            'loss-percent', 'beta-x', 'beta-y', 'invariant-x', 'alpha-x',
            'alpha-y', 'invariant-y', 'gamma-x', 'gamma-y', 'xz-average',
            'xy-average', 'yz-average', 'xzDevideSigmaxSigmaZ', 'x-skewness',
            'x-kurtosis', 'y-skewness', 'y-kurtosis'
        ]
        if isPlotSingle:
            for i_single in range(34):
                fig_tmp, ax_tmp = plt.subplots(figsize=(8, 6))
                plt.xticks(fontsize=15)
                plt.yticks(fontsize=15)
                fig_single.append(fig_tmp)
                ax_tmp.grid()
                ax_single.append(ax_tmp)

        for i in range(para.nbunch):
            stat = Statistic(home, yearMonDay, hourMinSec, para.particle, i,
                             para.nux, para.nuy, para.sigmax, para.sigmay,
                             para.sigmapx, para.sigmapy, nbunch_opp,
                             isPlotSingle)

            stat.load_statistic()

            stat.plot_statistic_part0(ax_stat0,
                                      ax_single,
                                      myalpha=0.5,
                                      myfontsize=myfontsize)

            stat.plot_statistic_part1(ax_stat1,
                                      ax_single,
                                      myalpha=0.5,
                                      myfontsize=myfontsize)
            stat.plot_statistic_part2(ax_stat2,
                                      ax_single,
                                      myalpha=0.5,
                                      myfontsize=myfontsize)
            stat.plot_statistic_part3(ax_stat3,
                                      ax_single,
                                      myalpha=0.5,
                                      myfontsize=myfontsize)
            stat.plot_statistic_part4(ax_stat4,
                                      ax_single,
                                      myalpha=0.5,
                                      myfontsize=myfontsize)

        stat.manage_axGrid(ax_stat0, row, col)
        stat.manage_axGrid(ax_stat1, row, col)
        stat.manage_axGrid(ax_stat2, row, col)
        stat.manage_axGrid(ax_stat3, row2, col2)
        stat.manage_axGrid(ax_stat4, row2, col2)

        fig_stat0.suptitle(para.statnote)
        fig_stat1.suptitle(para.statnote_part1)
        fig_stat2.suptitle(para.statnote_part2)
        fig_stat3.suptitle(para.statnote)
        fig_stat4.suptitle(para.statnote)

        stat.save_beamStatistic(fig_stat0, part=0)
        stat.save_beamStatistic(fig_stat1, part=1)
        stat.save_beamStatistic(fig_stat2, part=2)
        stat.save_beamStatistic(fig_stat3, part=3)
        stat.save_beamStatistic(fig_stat4, part=4)

        plt.close(fig_stat0)
        plt.close(fig_stat1)
        plt.close(fig_stat2)
        plt.close(fig_stat3)
        plt.close(fig_stat4)

        if isPlotSingle:
            for i_single in range(34):
                fig_single[i_single].savefig(
                    stat.save_beamStatisticPath_single + '_' +
                    single_name[i_single],
                    dpi=300)
                plt.close(fig_single[i_single])

        print('File has been drawn: beam {0}'.format(stat.particle))


def plot_statistic_main(home, yearMonDay, hourMinSec, para, nbunch_opp,
                        myfigsize, myfontsize, ncpu, timestat, isPlotSingle):
    timestat.start('stat')
    print('\nStart drawing {0:s} statistic data'.format(para.particle))
    row = 3
    col = 3
    row2 = 2
    col2 = 2

    if ncpu == 1:
        for i in range(para.nbunch):
            plot_statistic_bunch_oneProcess(i, row, col, row2, col2, home,
                                            yearMonDay, hourMinSec, para,
                                            nbunch_opp, myfigsize, myfontsize,
                                            'no queue', isPlotSingle)
    else:
        ps = []
        for i in range(para.nbunch):
            p = Process(target=plot_statistic_bunch_oneProcess,
                        args=(i, row, col, row2, col2, home, yearMonDay,
                              hourMinSec, para, nbunch_opp, myfigsize,
                              myfontsize, 'queue', isPlotSingle))
            ps.append(p)
        for i in range(para.nbunch):
            ps[i].start()
            print('Total cpu cores: {0:d}, task {1:d}/{2:d} has been added'.
                  format(os.cpu_count(), i, para.nbunch))
            time.sleep(1)
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
                        para, nbunch_opp, myfigsize, myfontsize, isPlotSingle)
    timestat.end('stat')


def plot_luminosity_main(home,
                         yearMonDay,
                         hourMinSec,
                         para1,
                         para2,
                         myfigsize,
                         myfontsize,
                         timestat,
                         particle3='suPeriod',
                         nbunch3=1):
    timestat.start('lumi')
    print('\nStart drawing luminosity data')
    lumi = 'tmp'
    particle = [para1.particle, para2.particle, particle3]
    skip = [para2.nbunch, para1.nbunch, nbunch3]

    fig_lumi, ax_lumi = plt.subplots(1, 3, figsize=myfigsize, sharey='all')
    fig_lumi.subplots_adjust(left=0.04, right=0.98, bottom=0.06, wspace=0.12)
    plt.xticks(fontsize=myfontsize)
    plt.yticks(fontsize=myfontsize)

    myxlabel = [particle[0] + ' turn', particle[1] + ' turn', 'Super period']
    for i in range(3):
        fig_tmp, ax_tmp = plt.subplots(1, figsize=(8, 6))
        plt.xticks(fontsize=myfontsize)
        plt.yticks(fontsize=myfontsize)
        # fig_tmp.subplots_adjust(left=0.09, right=0.97, top=0.83, bottom=0.08)
        mpl.rcParams['agg.path.chunksize'] = 10000

        lumi = Luminosity(home, yearMonDay, hourMinSec, particle[i],
                          myfontsize)
        lumi.load_luminosity(skip[i] + 1)
        lumi.plot_luminosity(ax_tmp, isLabel=False, myalpha=1)
        lumi.plot_luminosity(ax_lumi[i], isLabel=True, myalpha=1)

        ax_tmp.set_ylabel(r'Luminosity $(\mathrm{cm}^{-2}\mathrm{s}^{-1})$',
                          fontsize=myfontsize)
        ax_tmp.set_xlabel(myxlabel[i], fontsize=myfontsize)
        ax_tmp.grid()
        # ax_tmp.legend(fontsize=myfontsize)

        ax_lumi[i].set_ylabel(
            r'Luminosity $(\mathrm{cm}^{-2}\mathrm{s}^{-1})$',
            fontsize=myfontsize)

        ax_lumi[i].set_xlabel(myxlabel[i], fontsize=myfontsize)
        ax_lumi[i].grid()
        ax_lumi[i].legend(fontsize=myfontsize)

        # fig_tmp.suptitle(para1.luminote)

        lumi.save_lumi(fig_tmp)
        plt.close(fig_tmp)
        print('File has been drawn: {0}'.format(lumi.lumi_file))

    fig_lumi.suptitle(para1.luminote)
    lumi.save_lumiPath = lumi.save_lumiTogetherPath
    lumi.save_lumi(fig_lumi)
    plt.close(fig_lumi)
    timestat.end('lumi')


def plot_tune_oneProcess(tune, para, order, myfigsize, myfontsize, cpuid):
    '''
    使用多线程同时处理不同束团的tune信息
    '''

    for index in tune.fileIndex[cpuid]:
        nuX, nuY = load_phase(tune.filePath[index])

        fig, ax = plt.subplots(1, figsize=myfigsize)
        fig.subplots_adjust(right=1)
        plt.xticks(fontsize=myfontsize)
        plt.yticks(fontsize=myfontsize)

        plot_phase_hexbin(tune,
                          fig,
                          ax,
                          nuX,
                          nuY,
                          order,
                          myalpha=0.8,
                          myfontsize=myfontsize)

        ax.scatter(para.nux,
                   para.nuy,
                   marker='x',
                   color='black',
                   s=50,
                   zorder=order)

        ax.set_xlabel(r'$\nu_x$', fontsize=myfontsize)
        ax.set_ylabel(r'$\nu_y$', fontsize=myfontsize)

        save_phase_hexbin(fig, tune.savePath_hexbin[index])
        plt.close(fig)
        print('File has been drawn: {0}'.format(tune.filePath[index]))


def plot_tune_main(home,
                   yearMonDay,
                   hourMinSec,
                   para,
                   myfigsize,
                   myfontsize,
                   mygridsize,
                   ncpu,
                   timestat,
                   bunchid=[0]):
    timestat.start('tune')
    print('\nStart drawing {0:s} tune spread data'.format(para.particle))
    order = 10
    tune = Tune(home,
                yearMonDay,
                hourMinSec,
                para.particle,
                bunchid,
                para.nux,
                para.nuy,
                para.tuneshift_direction,
                ncpu,
                mygridsize,
                xlim=[0, 1],
                ylim=[0, 1])
    # print(tune.particle, tune.xlim, tune.ylim)
    tune.get_phase_limit()
    tune.allocate_phase_file()

    ps = []
    for cpuid in range(tune.ntask):
        p = Process(target=plot_tune_oneProcess,
                    args=(tune, para, order, myfigsize, myfontsize, cpuid))
        ps.append(p)
    for cpuid in range(tune.ntask):
        ps[cpuid].start()
        print('Total cpu cores: {0:d}, task {1:d}/{2:d} has been added'.format(
            os.cpu_count(), cpuid, tune.ntask))
        time.sleep(0.01)
    for cpuid in range(tune.ntask):
        ps[cpuid].join()

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
    timestat.end('tune')


def plot_distribution_oneProcess(dist, para, myfigsize, myfontsize, cpuid,
                                 isPlotSingle):
    '''
    使用多线程同时处理不同束团的dist信息
    '''

    for index in dist.fileIndex[cpuid]:
        title = '{0}, {1} {2}\n'.format(dist.bunchLabel[index], dist.turnUnit,
                                        dist.dist_turn[index])

        title += r'$\sigma_x={0:e}, \sigma_{{x^\prime}}={1:e}, \sigma_y={2:e}, \sigma_{{y^\prime}}={3:e}, \sigma_z={4:e}, \delta_p={5:e}$'.format(
            para.sigmax, para.sigmapx, para.sigmay, para.sigmapy, para.sigmaz,
            para.sigmapz)
        x, px, y, py, z, pz = load_dist(dist.filePath[index])

        plot_dist_save(dist,
                       para,
                       x,
                       px,
                       y,
                       py,
                       z,
                       pz,
                       myfigsize,
                       myfontsize,
                       dist.bunchLabel[index],
                       title,
                       dist.savePath[index],
                       dist.savePath_single[index],
                       mysize=200,
                       mybins=300,
                       isPlotSingle=isPlotSingle)

        print('File has been drawn: {0}'.format(dist.filePath[index]))


def plot_distribution_main(home,
                           yearMonDay,
                           hourMinSec,
                           para,
                           myfigsize,
                           myfontsize,
                           ncpu,
                           timestat,
                           bunchid=[0],
                           isPlotSingle=False):
    timestat.start('dist')
    print('\nStart drawing {0:s} distribution data'.format(para.particle))
    dist = Distribution(home, yearMonDay, hourMinSec, para.particle, bunchid,
                        para.dist, ncpu)
    dist.allocate_dist_file()

    ps = []
    for cpuid in range(dist.ntask):
        p = Process(target=plot_distribution_oneProcess,
                    args=(dist, para, myfigsize, myfontsize, cpuid,
                          isPlotSingle))
        ps.append(p)
    for cpuid in range(dist.ntask):
        ps[cpuid].start()
        print('Total cpu cores: {0:d}, task {1:d}/{2:d} has been added'.format(
            os.cpu_count(), cpuid, dist.ntask))
        time.sleep(0.01)
    for cpuid in range(dist.ntask):
        ps[cpuid].join()

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
    timestat.end('dist')


def plot_fma_oneProcess(myfootprint, para, myfigsize, myfontsize,
                        myscattersize, mydistTurnStep, isDistZip, plotkind,
                        cpuid):

    for index in myfootprint.fileIndex[cpuid]:

        myfootprint.load_plot_save(index, para, myfigsize, myfontsize,
                                   myscattersize, mydistTurnStep, isDistZip,
                                   plotkind)


def plot_fma_main(home,
                  yearMonDay,
                  hourMinSec,
                  para,
                  myfigsize,
                  myfontsize,
                  myscattersize,
                  mydistTurnStep,
                  isDistZip,
                  plotkind,
                  ncpu,
                  timestat,
                  xlim=[0, 1],
                  ylim=[0, 1],
                  vmin=None,
                  vmax=None,
                  bunchid=[0]):
    timestat.start('fma')
    print('\nStart drawing {0:s} Frequency Map'.format(para.particle))

    myfootprint = FootPrint(home,
                            yearMonDay,
                            hourMinSec,
                            para.particle,
                            bunchid,
                            para.nux,
                            para.nuy,
                            para.tuneshift_direction,
                            ncpu,
                            xlim=xlim,
                            ylim=ylim,
                            vmin=vmin,
                            vmax=vmax,
                            dist='gaussian')
    myfootprint.get_phase_limit(para)
    myfootprint.allocate_phase_file()

    ps = []
    for cpuid in range(myfootprint.ntask):
        p = Process(target=plot_fma_oneProcess,
                    args=(myfootprint, para, myfigsize, myfontsize,
                          myscattersize, mydistTurnStep, isDistZip, plotkind,
                          cpuid))
        ps.append(p)
    for cpuid in range(myfootprint.ntask):
        ps[cpuid].start()
        print('Total cpu cores: {0:d}, task {1:d}/{2:d} has been added'.format(
            os.cpu_count(), cpuid, myfootprint.ntask))
        time.sleep(0.01)
    for cpuid in range(myfootprint.ntask):
        ps[cpuid].join()
    # if ncpu == 1:
    #     for i in range(para.nbunch):
    #         plot_fma_oneProcess(i, home, yearMonDay, hourMinSec, para,
    #                             myfigsize, myfontsize, myscattersize,
    #                             mydistTurnStep, isDistZip, plotkind)
    # else:
    #     ps = []
    #     for i in range(para.nbunch):
    #         p = Process(target=plot_fma_oneProcess,
    #                     args=(i, home, yearMonDay, hourMinSec, para, myfigsize,
    #                           myfontsize, myscattersize, mydistTurnStep,
    #                           isDistZip, plotkind))
    #         ps.append(p)
    #     for i in range(para.nbunch):
    #         ps[i].start()
    #         print('Total cpu cores: {0:d}, task {1:d}/{2:d} has been added'.
    #               format(os.cpu_count(), i, para.nbunch))
    #         time.sleep(1)
    #     for i in range(para.nbunch):
    #         ps[i].join()
    timestat.end('fma')


def main(home,
         yearMonDay,
         hourMinSec,
         command_beam1=['all'],
         command_beam2=['all'],
         ncpu=1):
    # Default contexts and start methods on Windows is spawn.
    # Default contexts and start methods on Unix is fork.
    if platform.system() == 'Linux':
        ncpu = os.cpu_count() - 1

    runningTime = TimeStat()
    runningTime.start('total')
    beam1 = Parameter(home, yearMonDay, hourMinSec, 'beam1')
    beam2 = Parameter(home, yearMonDay, hourMinSec, 'beam2')
    beam2.superiod = beam1.superiod

    my_figsize1 = (20, 10)
    my_figsize_tune = (8, 6)
    my_figsize_fma = (8, 6)
    my_fontsize_stat = 12
    my_fontsize_lumi = 12
    my_fontsize_tune = 12
    my_fontsize_fma = 12
    my_fontsize_dist = 15

    mygridsize_tune = 200

    my_fma_scattersize = 1
    my_fma_distTurnStep = 25
    my_fma_dist_isZip = True
    if platform.system() == 'Linux':
        my_fma_dist_isZip = True
    elif platform.system() == 'Windows':
        my_fma_dist_isZip = False

    tune_beam1_bunchid = [0]
    tune_beam2_bunchid = [0]

    dist_beam1_bunchid = [0]
    dist_beam2_bunchid = [0]

    fma_beam1_bunchid = [0]
    fma_beam2_bunchid = [0]

    # beam1.print()
    # beam2.print()

    beam1.gen_note_withPath(beam2)
    beam2.gen_note_withPath(beam1)

    beam1_isPlotSingle_stat = False
    beam2_isPlotSingle_stat = False

    beam1_isPlotSingle_dist = False
    beam2_isPlotSingle_dist = False

    # print(beam1.statnote)
    # print(beam2.statnote)

    if 'all' in command_beam1 or 'lumi' in command_beam1 or 'all' in command_beam2 or 'lumi' in command_beam2:
        plot_luminosity_main(home, yearMonDay, hourMinSec, beam1, beam2,
                             my_figsize1, my_fontsize_lumi, runningTime)

    for cmd in command_beam1:
        if cmd == 'all' or cmd == 'stat':
            plot_statistic_main(home, yearMonDay, hourMinSec, beam1,
                                beam2.nbunch, my_figsize1, my_fontsize_stat,
                                ncpu, runningTime, beam1_isPlotSingle_stat)

        if cmd == 'all' or cmd == 'dist':
            plot_distribution_main(home, yearMonDay, hourMinSec, beam1,
                                   my_figsize1, my_fontsize_dist, ncpu,
                                   runningTime, dist_beam1_bunchid,
                                   beam1_isPlotSingle_dist)

        if cmd == 'all' or cmd == 'tune':
            plot_tune_main(home, yearMonDay, hourMinSec, beam1,
                           my_figsize_tune, my_fontsize_tune, mygridsize_tune,
                           ncpu, runningTime, tune_beam1_bunchid)

        if cmd == 'all' or cmd == 'fma' or cmd == 'fmafma' or cmd == 'fmadist':
            plot_fma_main(home,
                          yearMonDay,
                          hourMinSec,
                          beam1,
                          my_figsize_fma,
                          my_fontsize_fma,
                          my_fma_scattersize,
                          my_fma_distTurnStep,
                          my_fma_dist_isZip,
                          cmd,
                          ncpu,
                          runningTime,
                          xlim=[0, 1],
                          ylim=[0, 1],
                          vmin=None,
                          vmax=None,
                          bunchid=fma_beam1_bunchid)

    for cmd in command_beam2:
        if cmd == 'all' or cmd == 'stat':
            plot_statistic_main(home, yearMonDay, hourMinSec, beam2,
                                beam1.nbunch, my_figsize1, my_fontsize_stat,
                                ncpu, runningTime, beam2_isPlotSingle_stat)

        if cmd == 'all' or cmd == 'dist':
            plot_distribution_main(home, yearMonDay, hourMinSec, beam2,
                                   my_figsize1, my_fontsize_dist, ncpu,
                                   runningTime, dist_beam2_bunchid,
                                   beam2_isPlotSingle_dist)

        if cmd == 'all' or cmd == 'tune':
            plot_tune_main(home, yearMonDay, hourMinSec, beam2,
                           my_figsize_tune, my_fontsize_tune, mygridsize_tune,
                           ncpu, runningTime, tune_beam2_bunchid)

        if cmd == 'all' or cmd == 'fma' or cmd == 'fmafma' or cmd == 'fmadist':
            plot_fma_main(home,
                          yearMonDay,
                          hourMinSec,
                          beam2,
                          my_figsize_fma,
                          my_fontsize_fma,
                          my_fma_scattersize,
                          my_fma_distTurnStep,
                          my_fma_dist_isZip,
                          cmd,
                          ncpu,
                          runningTime,
                          xlim=[0, 1],
                          ylim=[0, 1],
                          vmin=None,
                          vmax=None,
                          bunchid=fma_beam2_bunchid)

    runningTime.end('total')
    runningTime.printTimeStat()

    return 0


if __name__ == '__main__':
    home = os.sep.join(['/home', 'changmx', 'bb2022'])
    if socket.gethostname() == 'DESKTOP-T722QRP':
        home = os.sep.join(['D:', 'bb2022'])
    elif socket.gethostname() == 'zts-gpu':
        home = os.sep.join(['/home', 'changmx', 'bb2022'])
    elif socket.gethostname() == 'sdgx-server01':
        home = os.sep.join(['/raid', 'home', 'changmx', 'bb2022'])
    else:
        print(
            'We do not support current machine now, please add hostname: {0} to home path list.'
            .format(socket.gethostname()))
        # os.exit(1)
        print('Try default path: {0}'.format(home))

    command = ('all', 'stat', 'lumi', 'tune', 'dist', 'fma', 'fmafma',
               'fmadist')

    command_beam1 = []
    command_beam2 = []

    if len(sys.argv) == 1:
        command_beam1 = ['all']
        command_beam2 = ['all']
    else:
        opts, args = getopt.getopt(sys.argv[1:], 'a:b:', ['beam1=', 'beam2='])
        for opt, arg in opts:
            if opt in ('-a', '--beam1'):
                command_beam1 = arg.split('-')
            if opt in ('-b', '--beam2'):
                command_beam2 = arg.split('-')

    print('--beam1: ', command_beam1)
    print('--beam2: ', command_beam2)

    for iargv in command_beam1:
        if iargv not in command:
            print('Warning: invalid option of beam1: {0}'.format(iargv))
    for iargv in command_beam2:
        if iargv not in command:
            print('Warning: invalid option of beam2: {0}'.format(iargv))

    yearMonDay = '2022_0622'
    hourMinSec = '1652_21'

    ncpu = os.cpu_count() - 1
    status = main(
        home,
        yearMonDay,
        hourMinSec,
        command_beam1,
        command_beam2,
        ncpu=ncpu,
    )
    print(status)
