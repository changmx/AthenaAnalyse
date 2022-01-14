from json import load

from matplotlib.colors import Normalize
import matplotlib
from plot_resonance import plot_resonanceDiagram_color
import matplotlib.pyplot as plt
import numpy as np
import os
import glob
import re

from plot_general import myhexbin


class Tune:
    """
    Load and plot tune data
    """

    def __init__(self,
                 home,
                 yearMonDay,
                 hourMinSec,
                 particle,
                 nbunch,
                 nux,
                 nuy,
                 tuneshift_direction,
                 ncpu,
                 xlim=[0, 1],
                 ylim=[0, 1]):
        self.home = home
        self.yearMonDay = yearMonDay
        self.hourMinSec = hourMinSec
        self.particle = particle
        self.nbunch = nbunch
        self.nux = nux
        self.nuy = nuy
        self.tuneshift_direction = tuneshift_direction
        self.ncpu = ncpu
        self.xlim = xlim
        self.ylim = ylim

        self.filePath = []
        self.savePath_scatter = []
        self.savePath_hexbin = []

        for bunchid in range(self.nbunch):
            filePath = self.hourMinSec + '_' + self.particle + '_bunch' + str(
                bunchid) + '_phase_'
            if self.yearMonDay > '2021_0913':
                filePath = os.sep.join([
                    self.home, 'phase', self.yearMonDay, self.hourMinSec,
                    filePath
                ])
            else:
                filePath = os.sep.join([
                    self.home, 'statLumiPara', self.yearMonDay,
                    self.hourMinSec, filePath
                ])

            filePath = glob.glob(filePath + '*')
            # print(filePath)
            tune_turn = []

            for i in range(len(filePath)):
                if os.path.exists(filePath[i]):
                    matchObj = re.match(r'(.*)phase_(.*)turn(.*).csv',
                                        filePath[i])
                    tune_turn.append(matchObj.group(2))
                    savePath = os.sep.join([
                        self.home, 'statLumiPara', self.yearMonDay,
                        self.hourMinSec, 'figure_tuneSpread'
                    ])
                    if not os.path.exists(savePath):
                        os.makedirs(savePath)
                    savePath = os.sep.join([
                        savePath, self.hourMinSec + '_phase_' + self.particle +
                        "_bunch" + str(bunchid) + '_' + tune_turn[i]
                    ])

                    self.filePath.append(filePath[i])
                    self.savePath_scatter.append(savePath + '_scatter')
                    self.savePath_hexbin.append(savePath + '_hexbin')
        # for i in range(len(self.filePath)):
        #     print(self.filePath[i])
        #     print(self.savePath_scatter[i])
        self.nfile = len(self.filePath)
        print('{0:d} files will be drawn'.format(self.nfile))

    def get_limit(self):
        if self.xlim == [0, 1] or self.ylim == [0, 1]:
            if len(self.filePath) > 0:
                print('Cal limit by file: ', self.filePath[0])
                nuX, nuY, tag = np.loadtxt(self.filePath[0],
                                           delimiter=',',
                                           skiprows=1,
                                           usecols=(2, 3, 4),
                                           unpack=True)
                delete_list = []  # 保存需要删除的元素下标，最后统一删除
                for j in range(len(tag)):
                    if tag[j] <= 0:
                        delete_list.append(j)
                    elif np.isnan(nuX[j]) or np.isnan(nuY[j]) or np.isinf(
                            nuX[j]) or np.isinf(nuY[j]):
                        delete_list.append(j)

                nuX = np.delete(nuX, delete_list)
                nuY = np.delete(nuY, delete_list)

                xmin = min(nuX)
                ymin = min(nuY)
                xmax = max(nuX)
                ymax = max(nuY)

                if xmax == xmin:
                    xmin = xmin - (xmin - 0) * 0.2
                    xmax = xmax + (1 - xmax) * 0.2
                if ymax == ymin:
                    ymin = ymin - (ymin - 0) * 0.2
                    ymax = ymax + (1 - ymax) * 0.2

                if self.tuneshift_direction > 0:
                    xgap = abs(xmax - self.nux)
                    ygap = abs(ymax - self.nuy)
                    axmin = self.nux - xgap * 0.3
                    aymin = self.nuy - ygap * 0.3
                    axmax = xmax + xgap * 0.7
                    aymax = ymax + ygap * 0.7
                else:
                    xgap = abs(xmin - self.nux)
                    ygap = abs(ymin - self.nuy)
                    axmin = xmin - xgap * 0.3
                    aymin = ymin - ygap * 0.3
                    axmax = self.nux + xgap * 0.7
                    aymax = self.nuy + ygap * 0.7

                axmin = 0 if axmin < 0 else axmin
                aymin = 0 if aymin < 0 else aymin
                axmax = 1 if axmax > 1 else axmax
                aymax = 1 if aymax > 1 else aymax

                if self.xlim == [0, 1]:
                    self.xlim = [axmin, axmax]
                if self.ylim == [0, 1]:
                    self.ylim = [aymin, aymax]
            else:
                if self.xlim == [0, 1]:
                    if self.nux > 0.5:
                        self.xlim[0] = 0.5
                    else:
                        self.xlim[1] = 0.5
                if self.ylim == [0, 1]:
                    if self.nuy > 0.5:
                        self.ylim[0] = 0.5
                    else:
                        self.ylim[1] = 0.5

        print('xlim: ', self.xlim)
        print('ylim: ', self.ylim)

    def allocate_file(self):
        self.fileIndex = []
        for i in range(self.ncpu):
            self.fileIndex.append([])
        for i in range(self.nfile):
            self.fileIndex[i % self.ncpu].append(i)
        # print(self.fileIndex)


def load(filePath):
    nuX, nuY, tag = np.loadtxt(filePath,
                               delimiter=',',
                               skiprows=1,
                               usecols=(2, 3, 4),
                               unpack=True)

    delete_list = []  # 保存需要删除的元素下标，最后统一删除
    for j in range(len(tag)):
        if tag[j] <= 0:
            delete_list.append(j)
        elif np.isnan(nuX[j]) or np.isnan(nuY[j]) or np.isinf(
                nuX[j]) or np.isinf(nuY[j]):
            delete_list.append(j)

    nuX = np.delete(nuX, delete_list)
    nuY = np.delete(nuY, delete_list)

    return nuX, nuY


def plot_scatter(tune,
                 fig,
                 ax,
                 nuX,
                 nuY,
                 resonanceOrder,
                 myalpha,
                 mysize,
                 resonanceKind='all',
                 myfontsize=10):
    sc = ax.scatter(nuX,
                    nuY,
                    alpha=myalpha,
                    s=mysize,
                    color='red',
                    zorder=resonanceOrder)
    # cbar = fig.colorbar(sc)
    # cbar.ax.tick_params(labelsize=myfontsize)
    plot_resonanceDiagram_color(resonanceOrder, ax, tune.xlim, tune.ylim,
                                resonanceKind, myfontsize)


def plot_phase_hexbin(tune,
                      fig,
                      ax,
                      nuX,
                      nuY,
                      resonanceOrder,
                      myalpha,
                      mygridsize,
                      resonanceKind='all',
                      myfontsize=10):
    # he = ax.hexbin(self.nuX[phaseTime],
    #                self.nuY[phaseTime],
    #                gridsize=mysize,
    #                norm=matplotlib.colors.LogNorm(),
    #                cmap='coolwarm')
    he = myhexbin(ax,
                  nuX,
                  nuY,
                  gridsize=mygridsize,
                  alpha=myalpha,
                  scattersize=1,
                  norm=matplotlib.colors.LogNorm(),
                  cmap='jet')
    cbar = fig.colorbar(he)
    cbar.ax.tick_params(labelsize=myfontsize)

    plot_resonanceDiagram_color(resonanceOrder, ax, tune.xlim, tune.ylim,
                                resonanceKind, myfontsize)


def save_scatter(figure, savepath, mydpi=300):
    # print(savepath)
    figure.savefig(savepath, dpi=mydpi)


def save_hexbin(figure, savepath, mydpi=300):
    # print(savepath)
    figure.savefig(savepath, dpi=mydpi)
