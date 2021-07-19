from json import load
import gc

from plot_statistic import *
from plot_luminosity import *
from load_parameter import *
from plot_tune import *


def plot_statistic_main(home, yearMonDay, hourMinSec, para, myfigsize):
    stat = []
    row = 3
    col = 3
    fig_stat, ax_stat = plt.subplots(row, col, figsize=myfigsize)

    for i in range(para.nbunch):
        fig_stat_tmp, ax_stat_tmp = plt.subplots(row, col, figsize=myfigsize)
        stat.append(
            Statistic(home, yearMonDay, hourMinSec, para.particle, i, para.nux,
                      para.nuy))

        stat[i].load_statistic()
        stat[i].plot_statistic(ax_stat_tmp, myalpha=1)
        stat[i].manage_axGrid(ax_stat_tmp)

        fig_stat_tmp.suptitle(para.statnote)
        stat[i].plot_statistic(ax_stat, myalpha=0.5)
        stat[i].save_bunchStatistic(fig_stat_tmp)

        plt.close(fig_stat_tmp)
        print('File has been drawn: {0}'.format(stat[i].stat_file))

    stat[0].manage_axGrid(ax_stat)
    fig_stat.suptitle(para.statnote)
    stat[0].save_beamStatistic(fig_stat)

    plt.close(fig_stat)


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


def plot_tune_main(home, yearMonDay, hourMinSec, para, myfigsize, xlim, ylim):
    tune = []
    order = 10
    for i in range(para.nbunch):
        tune.append(
            Tune(home, yearMonDay, hourMinSec, para.particle, i, para.nux,
                 para.nuy, xlim, ylim))

    for i in range(para.nbunch):
        tune[i].load()
        for j in range(len(tune[i].file)):
            fig_tmp, ax_tmp = plt.subplots(1, figsize=myfigsize)
            tune[i].plot_scatter(ax_tmp,
                                 j,
                                 resonanceOrder=order,
                                 myalpha=0.5,
                                 mysize=1)
            ax_tmp.scatter(para.nux,
                           para.nuy,
                           marker='x',
                           color='black',
                           zorder=order)

            ax_tmp.set_xlabel(r'$\nu_x$')
            ax_tmp.set_ylabel(r'$\nu_y$')

            ax_tmp.set_title('{0:s} bunch{1:d} turn {2:s}'.format(
                para.particle, i, tune[i].tune_turn[j]))
            fig_tmp.suptitle(para.statnote)

            tune[i].save_scatter(fig_tmp, j)

            ax_tmp.clear()
            ax_tmp.tick_params(top=False, right=False)

            tune[i].plot_hexbin(ax_tmp,
                                j,
                                resonanceOrder=order,
                                myalpha=0.3,
                                mysize=200)
            ax_tmp.scatter(para.nux,
                           para.nuy,
                           marker='x',
                           color='black',
                           zorder=order)

            ax_tmp.set_xlabel(r'$\nu_x$')
            ax_tmp.set_ylabel(r'$\nu_y$')

            ax_tmp.set_title('{0:s} bunch{1:d} turn {2:s}'.format(
                para.particle, i, tune[i].tune_turn[j]))
            fig_tmp.suptitle(para.statnote)
            ax_tmp.tick_params(top=False, right=False)

            tune[i].save_hexbin(fig_tmp, j)

            plt.close(fig_tmp)
            print('File has been drawn: {0}'.format(tune[i].file[j]))


def main(home, yearMonDay, hourMinSec):
    beam1 = Parameter(home, yearMonDay, hourMinSec, 'beam1')
    beam2 = Parameter(home, yearMonDay, hourMinSec, 'beam2')

    my_figsize1 = (20, 10)
    my_figsize2 = (15, 10)

    xlim_0 = [0, 1]
    xlim_1 = [0.3, 0.33]
    xlim_2 = [0.575, 0.615]
    ylim_0 = [0, 1]
    ylim_1 = [0.27, 0.34]
    ylim_2 = [0.545, 0.575]
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

    plot_tune_main(home, yearMonDay, hourMinSec, beam1, my_figsize2, xlim_1,
                   ylim_1)
    plot_tune_main(home, yearMonDay, hourMinSec, beam2, my_figsize2, xlim_2,
                   ylim_2)

    return 0


if __name__ == '__main__':
    home = 'D:\\bb2021'
    yearMonDay = '2021_0712-3e5p'
    hourMinSec = '1836_39'

    status = main(home, yearMonDay, hourMinSec)
    print(status)