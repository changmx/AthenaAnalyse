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

    def __init__(self,
                 home,
                 yearMonDay,
                 hourMinSec,
                 particle,
                 bunchid,
                 dist='gaussian') -> None:
        self.home = home
        self.yearMonDay = yearMonDay
        self.hourMinSec = hourMinSec
        self.particle = particle
        self.bunchid = bunchid
        self.dist = dist
        self.bunchLabel = self.particle + " bunch" + str(bunchid)

        self.file = self.hourMinSec + '_' + self.dist + '_' + self.particle + '_bunch' + str(
            bunchid)
        self.file = os.sep.join([
            self.home, 'distribution', self.yearMonDay, self.hourMinSec,
            self.file
        ])

        self.file = glob.glob(self.file + '*')
        self.dist_turn = []
        self.Nmp = 0
        self.isExist = []
        self.savePath = []
        self.savePath_single = []

        for i in range(len(self.file)):
            self.isExist.append(os.path.exists(self.file[i]))

            matchObj = re.match(r'(.*)bunch(.*)_(.*)_([a-zA-Z]*)([0-9]*).csv',
                                self.file[i])
            self.Nmp = matchObj.group(3)
            self.turnUnit = matchObj.group(4)
            self.dist_turn.append(matchObj.group(5))

            savePath = os.sep.join([
                self.home, 'statLumiPara', self.yearMonDay, self.hourMinSec,
                'figure_distribution'
            ])
            savePath_single = os.sep.join([
                self.home, 'statLumiPara', self.yearMonDay, self.hourMinSec,
                'figure_distribution', 'single'
            ])

            if not os.path.exists(savePath):
                os.makedirs(savePath)
            if not os.path.exists(savePath_single):
                os.makedirs(savePath_single)

            savePath = os.sep.join([
                savePath, self.hourMinSec + '_dist_' + self.particle +
                "_bunch" + str(self.bunchid) + '_' + self.turnUnit + '_' +
                self.dist_turn[i]
            ])
            savePath_single = os.sep.join([
                savePath_single, self.hourMinSec + '_dist_' + self.particle +
                "_bunch" + str(self.bunchid) + '_' + self.turnUnit + '_' +
                self.dist_turn[i]
            ])

            self.savePath.append(savePath)
            self.savePath_single.append(savePath_single)

    def load_plot_save(self, para, myfigsize, mysize, mybins):
        plt.rcParams.update({'figure.max_open_warning': 0})
        for i in range(len(self.file)):
            if self.isExist[i]:
                x, px, y, py, z, pz, tag = np.loadtxt(self.file[i],
                                                      delimiter=',',
                                                      skiprows=1,
                                                      usecols=(0, 1, 2, 3, 4,
                                                               5, 6),
                                                      unpack=True)
                delete_number = 0
                for j in range(len(tag)):
                    if tag[j] <= 0:
                        x = np.delete(x, j - delete_number)
                        px = np.delete(px, j - delete_number)
                        y = np.delete(y, j - delete_number)
                        py = np.delete(py, j - delete_number)
                        z = np.delete(z, j - delete_number)
                        pz = np.delete(pz, j - delete_number)
                        delete_number += 1

                row = 3
                col = 4
                fig, ax = plt.subplots(row, col, figsize=myfigsize)

                fig_single = []
                ax_single = []
                single_name = ['x-px', 'y-py', 'z-pz', 'x-y', 'z-x', 'z-y',
                               'count-x', 'count-px', 'count-y', 'count-py', 'count-z', 'count-pz']
                for i_single in range(12):
                    fig_tmp, ax_tmp = plt.subplots(figsize=(8, 6))
                    fig_tmp.subplots_adjust(left=0.15,
                                            right=0.925)
                    plt.xticks(fontsize=15)
                    plt.yticks(fontsize=15)
                    fig_single.append(fig_tmp)
                    ax_single.append(ax_tmp)

                plot_hexbin(fig, ax[0, 0], x / para.sigmax, px / para.sigmapx,
                            mysize, 1, 1, r'$\rm x/\sigma_x$',
                            r'$\rm x^{\prime}/\sigma_{{x^{\prime}}}$', ax_single=ax_single[0], fig_single=fig_single[0])
                plot_hexbin(fig, ax[1, 0], y / para.sigmay, py / para.sigmapy,
                            mysize, 1, 1, r'$\rm y/\sigma_y$',
                            r'$\rm y^{\prime}/\sigma_{{y^{\prime}}}$', ax_single=ax_single[1], fig_single=fig_single[1])
                plot_hexbin(fig, ax[2, 0], z / para.sigmaz, pz / para.sigmapz,
                            mysize, 1, 1, r'$\rm z/\sigma_z$',
                            r'$\rm \delta_p/\sigma_{{\delta_p}}$', ax_single=ax_single[2], fig_single=fig_single[2])

                plot_hexbin(fig, ax[0, 1], x / para.sigmax, y / para.sigmay,
                            mysize, 1, 1, r'$\rm x/\sigma_x$',
                            r'$\rm y/\sigma_y$', ax_single=ax_single[3], fig_single=fig_single[3])
                plot_hexbin(fig, ax[1, 1], z / para.sigmaz, x / para.sigmax,
                            mysize, 1, 1, r'$\rm z/\sigma_z$',
                            r'$\rm x/\sigma_x$', ax_single=ax_single[4], fig_single=fig_single[4])
                plot_hexbin(fig, ax[2, 1], z / para.sigmaz, y / para.sigmay,
                            mysize, 1, 1, r'$\rm z/\sigma_z$',
                            r'$\rm y/\sigma_y$', ax_single=ax_single[5], fig_single=fig_single[5])

                plot_hist(ax[0, 2], x / para.sigmax, mybins, 1,
                          self.bunchLabel, r'$\rm x/\sigma_x$', 'Count', ax_single=ax_single[6])
                plot_hist(ax[0,
                             3], px / para.sigmapx, mybins, 1, self.bunchLabel,
                          r'$\rm x^{\prime}/\sigma_{{x^{\prime}}}$', 'Count', ax_single=ax_single[7])
                plot_hist(ax[1, 2], y / para.sigmay, mybins, 1,
                          self.bunchLabel, r'$\rm y/\sigma_y$', 'Count', ax_single=ax_single[8])
                plot_hist(ax[1,
                             3], py / para.sigmapy, mybins, 1, self.bunchLabel,
                          r'$\rm y^{\prime}/\sigma_{{y^{\prime}}}$', 'Count', ax_single=ax_single[9])
                plot_hist(ax[2, 2], z / para.sigmaz, mybins, 1,
                          self.bunchLabel, r'$\rm z/\sigma_z$', 'Count', ax_single=ax_single[10])
                plot_hist(ax[2,
                             3], pz / para.sigmapz, mybins, 1, self.bunchLabel,
                          r'$\rm \delta_p/\sigma_{{\delta_p}}$', 'Count', ax_single=ax_single[11])

                fig.subplots_adjust(left=0.05,
                                    right=0.98,
                                    bottom=0.05,
                                    wspace=0.22,
                                    hspace=0.22)
                # plt.show()
                self.note = '{0}, {1} {2}\n'.format(self.bunchLabel,
                                                    self.turnUnit,
                                                    self.dist_turn[i])

                self.note += r'$\sigma_x={0:e}, \sigma_{{x^\prime}}={1:e}, \sigma_y={2:e}, \sigma_{{y^\prime}}={3:e}, \sigma_z={4:e}, \delta_p={5:e}$'.format(
                    para.sigmax, para.sigmapx, para.sigmay, para.sigmapy,
                    para.sigmaz, para.sigmapz)

                fig.suptitle(self.note)
                fig.savefig(self.savePath[i], dpi=300)
                plt.close(fig)

                for i_single in range(12):
                    fig_single[i_single].savefig(
                        self.savePath_single[i]+'_'+single_name[i_single], dpi=300)
                    plt.close(fig_single[i_single])

                print('File has been drawn: {0}'.format(self.file[i]))


def plot_hexbin(fig, ax, x, y, mysize, xscale, yscale, myxlabel, myylabel, **kwargs):
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
        cb_single = kwargs['fig_single'].colorbar(
            hb_single, ax=kwargs['ax_single'])
        kwargs['ax_single'].set_xlabel(myxlabel, fontsize=15)
        kwargs['ax_single'].set_ylabel(myylabel, fontsize=15)
        kwargs['ax_single'].grid()


def plot_hist(ax, x, mybins, xscale, mylabel, myxlabel, myylabel, **kwargs):
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
    if 'ax_single' in kwargs:
        N_single, bins_single, patches_single = kwargs['ax_single'].hist(x,
                                                                         density=True,
                                                                         bins=mybins,
                                                                         range=(xmin, xmax))
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
