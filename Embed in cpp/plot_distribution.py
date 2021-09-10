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
            if not os.path.exists(savePath):
                os.makedirs(savePath)
            savePath = os.sep.join([
                savePath, self.hourMinSec + '_dist_' + self.particle +
                "_bunch" + str(self.bunchid) + '_' + self.turnUnit + '_' +
                self.dist_turn[i]
            ])

            self.savePath.append(savePath)

    def load_plot_save(self, para, myfigsize, mysize, mybins):
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

                plot_hexbin(fig, ax[0, 0], x / para.sigmax, px / para.sigmapx,
                            mysize, 1, 1, r'$\rm x/\sigma_x$',
                            r'$\rm x^{\prime}/\sigma_{{x^{\prime}}}$')
                plot_hexbin(fig, ax[1, 0], y / para.sigmay, py / para.sigmapy,
                            mysize, 1, 1, r'$\rm y/\sigma_y$',
                            r'$\rm y^{\prime}/\sigma_{{y^{\prime}}}$')
                plot_hexbin(fig, ax[2, 0], z / para.sigmaz, pz / para.sigmapz,
                            mysize, 1, 1, r'$\rm z/\sigma_z$',
                            r'$\rm \delta_p/\sigma_{{\delta_p}}$')

                plot_hexbin(fig, ax[0, 1], x / para.sigmax, y / para.sigmay,
                            mysize, 1, 1, r'$\rm x/\sigma_x$',
                            r'$\rm y/\sigma_y$')
                plot_hexbin(fig, ax[1, 1], z / para.sigmaz, x / para.sigmax,
                            mysize, 1, 1, r'$\rm z/\sigma_z$',
                            r'$\rm x/\sigma_x$')
                plot_hexbin(fig, ax[2, 1], z / para.sigmaz, y / para.sigmay,
                            mysize, 1, 1, r'$\rm z/\sigma_z$',
                            r'$\rm y/\sigma_y$')

                plot_hist(ax[0, 2], x / para.sigmax, mybins, 1,
                          self.bunchLabel, r'$\rm x/\sigma_x$', 'counts')
                plot_hist(ax[0,
                             3], px / para.sigmapx, mybins, 1, self.bunchLabel,
                          r'$\rm x^{\prime}/\sigma_{{x^{\prime}}}$', 'counts')
                plot_hist(ax[1, 2], y / para.sigmay, mybins, 1,
                          self.bunchLabel, r'$\rm y/\sigma_y$', 'counts')
                plot_hist(ax[1,
                             3], py / para.sigmapy, mybins, 1, self.bunchLabel,
                          r'$\rm y^{\prime}/\sigma_{{y^{\prime}}}$', 'counts')
                plot_hist(ax[2, 2], z / para.sigmaz, mybins, 1,
                          self.bunchLabel, r'$\rm z/\sigma_z$', 'counts')
                plot_hist(ax[2,
                             3], pz / para.sigmapz, mybins, 1, self.bunchLabel,
                          r'$\rm \delta_p/\sigma_{{\delta_p}}$', 'counts')

                plt.subplots_adjust(left=0.05,
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

                plt.suptitle(self.note)
                plt.savefig(self.savePath[i], dpi=300)
                plt.close(fig)
                print('File has been drawn: {0}'.format(self.file[i]))


def plot_hexbin(fig, ax, x, y, mysize, xscale, yscale, myxlabel, myylabel):
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


def plot_hist(ax, x, mybins, xscale, mylabel, myxlabel, myylabel):
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


if __name__ == '__main__':
    home = 'D:\\bb2021'
    yearMonDay = '2021_0817'
    hourMinSec = '1607_31'
