import matplotlib.pyplot as plt
import numpy as np
import os
import glob
import re

from numpy.lib import delete
from load_parameter import Parameter


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
            matchObj = re.match(r'(.*)bunch(.*)_(.*)_turn(.*).csv',
                                self.file[i])
            self.Nmp = matchObj.group(3)
            self.dist_turn.append(matchObj.group(4))

            savePath = os.sep.join([
                self.home, 'statLumiPara', self.yearMonDay, self.hourMinSec,
                'figure_distribution'
            ])
            if not os.path.exists(savePath):
                os.makedirs(savePath)
            savePath = os.sep.join([
                savePath, self.hourMinSec + '_dist_' + self.particle +
                "_bunch" + str(self.bunchid) + '_superPeriod_' + self.dist_turn[i]
            ])

            self.savePath.append(savePath)

    def load_plot_save(self, para, myfigsize, mysize, mybins):
        for i in range(len(self.file)):
            x, px, y, py, z, pz, tag = np.loadtxt(self.file[i],
                                                  delimiter=',',
                                                  skiprows=1,
                                                  usecols=(0, 1, 2, 3, 4, 5,
                                                           6),
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

            plot_hexbin(fig, ax[0, 0], x, px, mysize, para.sigmax,
                        para.sigmapx, 'x', 'px')
            plot_hexbin(fig, ax[1, 0], y, py, mysize, para.sigmay,
                        para.sigmapy, 'y', 'py')
            plot_hexbin(fig, ax[2, 0], z, pz, mysize, para.sigmaz,
                        para.sigmapz, 'z', 'pz')

            plot_hexbin(fig, ax[0, 1], x, y, mysize, para.sigmax, para.sigmay,
                        'x', 'y')
            plot_hexbin(fig, ax[1, 1], z, x, mysize, para.sigmaz, para.sigmax,
                        'z', 'x')
            plot_hexbin(fig, ax[2, 1], z, y, mysize, para.sigmaz, para.sigmay,
                        'z', 'y')

            plot_hist(ax[0, 2], x, mybins, para.sigmax, self.bunchLabel, 'x',
                      'counts')
            plot_hist(ax[0, 3], px, mybins, para.sigmapx, self.bunchLabel,
                      'px', 'counts')
            plot_hist(ax[1, 2], y, mybins, para.sigmay, self.bunchLabel, 'y',
                      'counts')
            plot_hist(ax[1, 3], py, mybins, para.sigmapy, self.bunchLabel,
                      'py', 'counts')
            plot_hist(ax[2, 2], z, mybins, para.sigmaz, self.bunchLabel, 'z',
                      'counts')
            plot_hist(ax[2, 3], pz, mybins, para.sigmapz, self.bunchLabel,
                      'dp', 'counts')

            plt.subplots_adjust(left=0.05,
                                right=0.98,
                                bottom=0.05,
                                wspace=0.22,
                                hspace=0.22)
            # plt.show()
            self.note = '{0}, super period {1}\n'.format(self.bunchLabel,
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
    hb = ax.hexbin(x, y, gridsize=mysize, cmap='Blues', bins='log')
    cb = fig.colorbar(hb, ax=ax)
    ax.set_xlabel(myxlabel)
    ax.set_ylabel(myylabel)
    # cb.set_label(r'$\mathrm{log_{10}(N)}$')
    ax.ticklabel_format(axis='x', style='sci', scilimits=(0, 0))
    # ax.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))


def plot_hist(ax, x, mybins, xscale, mylabel, myxlabel, myylabel):
    scale = 6
    xmin = -scale * xscale
    xmax = scale * xscale
    # n, bins, patches = ax.hist(x, density=True)
    n, bins, patches = ax.hist(x, density=True, bins=mybins, range=(xmin, xmax))
    # ax.hist(x, bins=mybins, label=mylabel)
    ax.set_xlabel(myxlabel)
    ax.set_ylabel(myylabel)
    ax.ticklabel_format(axis='x', style='sci', scilimits=(0, 0))
    ax.grid()
    # ax.legend()


if __name__ == '__main__':
    home = 'D:\\bb2021'
    yearMonDay = '2021_0817'
    hourMinSec = '1607_31'
