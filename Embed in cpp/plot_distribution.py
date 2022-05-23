import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import os
import glob
import re

from numpy.lib import delete
from load_parameter import Parameter

from plot_general import myhexbin


class Distribution:
    '''
    Load and plot particles distribution
    '''

    def __init__(self, home, yearMonDay, hourMinSec, particle, bunchidList,
                 dist, ncpu) -> None:
        self.home = home
        self.yearMonDay = yearMonDay
        self.hourMinSec = hourMinSec
        self.particle = particle
        self.bunchid = bunchidList
        self.dist = dist
        self.ncpu = ncpu

        self.bunchLabel = []

        self.filePath = []
        self.dist_turn = []
        self.savePath = []
        self.savePath_single = []

        for bunchid in self.bunchid:
            filePath = self.hourMinSec + '_' + self.dist + '_' + self.particle + '_bunch' + str(
                bunchid)
            filePath = os.sep.join([
                self.home, 'distribution', self.yearMonDay, self.hourMinSec,
                filePath
            ])

            filePath = glob.glob(filePath + '*')
            dist_turn = []

            for i in range(len(filePath)):
                if os.path.exists(filePath[i]):
                    matchObj = re.match(
                        r'(.*)bunch(.*)_(.*)_([a-zA-Z]*)([0-9]*).csv',
                        filePath[i])
                    self.Nmp = matchObj.group(3)
                    self.turnUnit = matchObj.group(4)
                    dist_turn.append(matchObj.group(5))

                    savePath = os.sep.join([
                        self.home, 'statLumiPara', self.yearMonDay,
                        self.hourMinSec, 'figure_distribution'
                    ])
                    savePath_single = os.sep.join([
                        self.home, 'statLumiPara', self.yearMonDay,
                        self.hourMinSec, 'figure_distribution', 'single'
                    ])

                    if not os.path.exists(savePath):
                        os.makedirs(savePath)
                    if not os.path.exists(savePath_single):
                        os.makedirs(savePath_single)

                    savePath = os.sep.join([
                        savePath,
                        self.hourMinSec + '_dist_' + self.particle + "_bunch" +
                        str(bunchid) + '_' + self.turnUnit + '_' + dist_turn[i]
                    ])
                    savePath_single = os.sep.join([
                        savePath_single,
                        self.hourMinSec + '_dist_' + self.particle + "_bunch" +
                        str(bunchid) + '_' + self.turnUnit + '_' + dist_turn[i]
                    ])

                    self.filePath.append(filePath[i])
                    self.dist_turn.append(dist_turn[i])
                    self.savePath.append(savePath)
                    self.savePath_single.append(savePath_single)
                    self.bunchLabel.append(self.particle + " bunch" +
                                           str(bunchid))
        # for i in range(len(self.filePath)):
        #     print(self.filePath[i])
        #     print(self.savePath[i])
        self.nfile = len(self.filePath)
        self.ntask = self.nfile if self.nfile < self.ncpu else self.ncpu
        print('{0:d} files will be drawn'.format(self.nfile))

    def allocate_dist_file(self):
        self.fileIndex = []
        for i in range(self.ntask):
            self.fileIndex.append([])
        for i in range(self.nfile):
            self.fileIndex[i % self.ntask].append(i)
        # print(self.fileIndex)


def load_dist(filePath):
    x, px, y, py, z, pz, tag = np.loadtxt(filePath,
                                          delimiter=',',
                                          skiprows=1,
                                          usecols=(0, 1, 2, 3, 4, 5, 6),
                                          unpack=True)
    delete_list = []  # 保存需要删除的元素下标，最后统一删除
    for j in range(len(tag)):
        if tag[j] <= 0:
            delete_list.append(j)

    x = np.delete(x, delete_list)
    px = np.delete(px, delete_list)
    y = np.delete(y, delete_list)
    py = np.delete(py, delete_list)
    z = np.delete(z, delete_list)
    pz = np.delete(pz, delete_list)

    return x, px, y, py, z, pz


def plot_dist_save(dist, para, x, px, y, py, z, pz, myfigsize, myfontsize,
                   mybunchlabel, title, savePath, savePath_single, mysize,
                   mybins, isPlotSingle):
    # plt.rcParams.update({'figure.max_open_warning': 0})
    row = 3
    col = 4
    fig, ax = plt.subplots(row, col, figsize=myfigsize)

    fig_single = []
    ax_single = []
    single_name = [
        'x-px', 'y-py', 'z-pz', 'x-y', 'z-x', 'z-y', 'count-x', 'count-px',
        'count-y', 'count-py', 'count-z', 'count-pz'
    ]

    for i_single in range(12):
        if isPlotSingle:
            fig_tmp, ax_tmp = plt.subplots(figsize=(8, 6))
            fig_tmp.subplots_adjust(left=0.15, right=0.925)
            plt.xticks(fontsize=myfontsize)
            plt.yticks(fontsize=myfontsize)
        else:
            fig_tmp = ''
            ax_tmp = ''
            
        fig_single.append(fig_tmp)
        ax_single.append(ax_tmp)

    plot_dist_hexbin(fig,
                     ax[0, 0],
                     x / para.sigmax,
                     px / para.sigmapx,
                     mysize,
                     1,
                     1,
                     r'$\rm x/\sigma_x$',
                     r'$\rm x^{\prime}/\sigma_{{x^{\prime}}}$',
                     isPlotSingle,
                     ax_single=ax_single[0],
                     fig_single=fig_single[0])
    plot_dist_hexbin(fig,
                     ax[1, 0],
                     y / para.sigmay,
                     py / para.sigmapy,
                     mysize,
                     1,
                     1,
                     r'$\rm y/\sigma_y$',
                     r'$\rm y^{\prime}/\sigma_{{y^{\prime}}}$',
                     isPlotSingle,
                     ax_single=ax_single[1],
                     fig_single=fig_single[1])
    plot_dist_hexbin(fig,
                     ax[2, 0],
                     z / para.sigmaz,
                     pz / para.sigmapz,
                     mysize,
                     1,
                     1,
                     r'$\rm z/\sigma_z$',
                     r'$\rm \delta_p/\sigma_{{\delta_p}}$',
                     isPlotSingle,
                     ax_single=ax_single[2],
                     fig_single=fig_single[2])

    plot_dist_hexbin(fig,
                     ax[0, 1],
                     x / para.sigmax,
                     y / para.sigmay,
                     mysize,
                     1,
                     1,
                     r'$\rm x/\sigma_x$',
                     r'$\rm y/\sigma_y$',
                     isPlotSingle,
                     ax_single=ax_single[3],
                     fig_single=fig_single[3])
    plot_dist_hexbin(fig,
                     ax[1, 1],
                     z / para.sigmaz,
                     x / para.sigmax,
                     mysize,
                     1,
                     1,
                     r'$\rm z/\sigma_z$',
                     r'$\rm x/\sigma_x$',
                     isPlotSingle,
                     ax_single=ax_single[4],
                     fig_single=fig_single[4])
    plot_dist_hexbin(fig,
                     ax[2, 1],
                     z / para.sigmaz,
                     y / para.sigmay,
                     mysize,
                     1,
                     1,
                     r'$\rm z/\sigma_z$',
                     r'$\rm y/\sigma_y$',
                     isPlotSingle,
                     ax_single=ax_single[5],
                     fig_single=fig_single[5])

    plot_dist_hist(ax[0, 2],
                   x / para.sigmax,
                   mybins,
                   1,
                   mybunchlabel,
                   r'$\rm x/\sigma_x$',
                   'Count',
                   isPlotSingle,
                   ax_single=ax_single[6])
    plot_dist_hist(ax[0, 3],
                   px / para.sigmapx,
                   mybins,
                   1,
                   mybunchlabel,
                   r'$\rm x^{\prime}/\sigma_{{x^{\prime}}}$',
                   'Count',
                   isPlotSingle,
                   ax_single=ax_single[7])
    plot_dist_hist(ax[1, 2],
                   y / para.sigmay,
                   mybins,
                   1,
                   mybunchlabel,
                   r'$\rm y/\sigma_y$',
                   'Count',
                   isPlotSingle,
                   ax_single=ax_single[8])
    plot_dist_hist(ax[1, 3],
                   py / para.sigmapy,
                   mybins,
                   1,
                   mybunchlabel,
                   r'$\rm y^{\prime}/\sigma_{{y^{\prime}}}$',
                   'Count',
                   isPlotSingle,
                   ax_single=ax_single[9])
    plot_dist_hist(ax[2, 2],
                   z / para.sigmaz,
                   mybins,
                   1,
                   mybunchlabel,
                   r'$\rm z/\sigma_z$',
                   'Count',
                   isPlotSingle,
                   ax_single=ax_single[10])
    plot_dist_hist(ax[2, 3],
                   pz / para.sigmapz,
                   mybins,
                   1,
                   mybunchlabel,
                   r'$\rm \delta_p/\sigma_{{\delta_p}}$',
                   'Count',
                   isPlotSingle,
                   ax_single=ax_single[11])

    fig.subplots_adjust(left=0.05,
                        right=0.98,
                        bottom=0.05,
                        wspace=0.22,
                        hspace=0.22)
    # plt.show()

    fig.suptitle(title)
    fig.savefig(savePath, dpi=300)
    plt.close(fig)

    if isPlotSingle:
        for i_single in range(12):
            fig_single[i_single].savefig(savePath_single + '_' +
                                         single_name[i_single],
                                         dpi=300)
            plt.close(fig_single[i_single])


def plot_dist_hexbin(fig, ax, x, y, mysize, xscale, yscale, myxlabel, myylabel,
                     isPlotSingle, **kwargs):
    scale = 6
    xmin = -scale * xscale
    xmax = scale * xscale
    ymin = -scale * yscale
    ymax = scale * yscale
    ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))

    hb = myhexbin(ax,
                  x,
                  y,
                  gridsize=mysize,
                  scattersize=1,
                  norm=matplotlib.colors.LogNorm(),
                  cmap='jet',
                  alpha=1)
    # hb = ax.hexbin(x, y, gridsize=mysize, cmap='Blues', bins='log')
    cb = fig.colorbar(hb, ax=ax)
    ax.set_xlabel(myxlabel)
    ax.set_ylabel(myylabel)
    ax.grid()
    # cb.set_label(r'$\mathrm{log_{10}(N)}$')
    # ax.ticklabel_format(axis='x', style='sci', scilimits=(0, 0))
    # ax.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
    if isPlotSingle:
        if 'ax_single' in kwargs:
            kwargs['ax_single'].set(xlim=(xmin, xmax), ylim=(ymin, ymax))
            hb_single = myhexbin(kwargs['ax_single'],
                                 x,
                                 y,
                                 gridsize=mysize,
                                 scattersize=1,
                                 norm=matplotlib.colors.LogNorm(),
                                 cmap='jet',
                                 alpha=1)
            cb_single = kwargs['fig_single'].colorbar(hb_single,
                                                      ax=kwargs['ax_single'])
            kwargs['ax_single'].set_xlabel(myxlabel, fontsize=15)
            kwargs['ax_single'].set_ylabel(myylabel, fontsize=15)
            kwargs['ax_single'].grid()


def plot_dist_hist(ax, x, mybins, xscale, mylabel, myxlabel, myylabel,
                   isPlotSingle, **kwargs):
    scale = 6
    xmin = -scale * xscale
    xmax = scale * xscale
    # n, bins, patches = ax.hist(x, density=True)
    N, bins, patches = ax.hist(x,
                               density=True,
                               bins=mybins,
                               range=(xmin, xmax))
    fracs = N / N.max()
    norm = matplotlib.colors.Normalize(fracs.min(), fracs.max())
    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)
    # ax.hist(x, bins=mybins, label=mylabel)
    ax.set_xlabel(myxlabel)
    # ax.set_ylabel(myylabel)
    # ax.ticklabel_format(axis='x', style='sci', scilimits=(0, 0))
    ax.grid()
    ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(xmax=1))
    # ax.legend()
    if isPlotSingle:
        if 'ax_single' in kwargs:
            N_single, bins_single, patches_single = kwargs['ax_single'].hist(
                x, density=True, bins=mybins, range=(xmin, xmax))
            fracs_single = N_single / N_single.max()
            norm_single = matplotlib.colors.Normalize(fracs.min(), fracs.max())
            for thisfrac, thispatch in zip(fracs_single, patches_single):
                color = plt.cm.viridis(norm(thisfrac))
                thispatch.set_facecolor(color)
            # ax.hist(x, bins=mybins, label=mylabel)
            kwargs['ax_single'].set_xlabel(myxlabel, fontsize=15)
            kwargs['ax_single'].set_ylabel(myylabel, fontsize=15)
            # ax.ticklabel_format(axis='x', style='sci', scilimits=(0, 0))
            kwargs['ax_single'].grid()
            kwargs['ax_single'].yaxis.set_major_formatter(
                matplotlib.ticker.PercentFormatter(xmax=1))


if __name__ == '__main__':
    home = 'D:\\bb2021'
    yearMonDay = '2021_0817'
    hourMinSec = '1607_31'
