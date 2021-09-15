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
                 bunchid,
                 nux,
                 nuy,
                 xlim=[0, 1],
                 ylim=[0, 1]):
        self.home = home
        self.yearMonDay = yearMonDay
        self.hourMinSec = hourMinSec
        self.particle = particle
        self.bunchid = bunchid
        self.bunchLabel = self.particle + " bunch" + str(bunchid)
        self.nux = nux
        self.nuy = nuy
        self.xlim = xlim
        self.ylim = ylim

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

        self.file = self.hourMinSec + '_' + self.particle + '_bunch' + str(
            bunchid) + '_phase_'
        if self.yearMonDay > '2021_0913':
            self.file = os.sep.join([
                self.home, 'phase', self.yearMonDay, self.hourMinSec, self.file
            ])
        else:
            self.file = os.sep.join([
                self.home, 'statLumiPara', self.yearMonDay, self.hourMinSec,
                self.file
            ])

        self.file = glob.glob(self.file + '*')
        # print(self.file)
        self.tune_turn = []

        self.isExist = []
        self.savePath_scatter = []
        self.savePath_hexbin = []

        for i in range(len(self.file)):
            matchObj = re.match(r'(.*)phase_(.*)turn(.*).csv', self.file[i])
            self.tune_turn.append(matchObj.group(2))
            self.isExist.append(os.path.exists(self.file[i]))

            savePath = os.sep.join([
                self.home, 'statLumiPara', self.yearMonDay, self.hourMinSec,
                'figure_tuneSpread'
            ])
            if not os.path.exists(savePath):
                os.makedirs(savePath)
            savePath = os.sep.join([
                savePath, self.hourMinSec + '_phase_' + self.particle +
                "_bunch" + str(self.bunchid) + '_' + self.tune_turn[i]
            ])
            self.savePath_scatter.append(savePath + '_scatter')
            self.savePath_hexbin.append(savePath + '_hexbin')

    def load(self):
        self.nuX = []
        self.nuY = []
        for i in range(len(self.file)):
            if self.isExist[i]:
                tmp_nuX, tmp_nuY, tmp_tag = np.loadtxt(self.file[i],
                                                       delimiter=',',
                                                       skiprows=1,
                                                       usecols=(2, 3, 4),
                                                       unpack=True)

                l_nuX = list(tmp_nuX)
                l_nuY = list(tmp_nuY)

                delete_number = 0  # 把数组转化为列表来删除元素时，每删除一个元素，被删除元素后面的所有元素下标都会减一，因此用这个参数来表示删除元素后其他元素下标的变化
                for j in range(len(tmp_tag)):  # 删除列表中的元素
                    if tmp_tag[j] <= 0:
                        del l_nuX[j - delete_number]
                        del l_nuY[j - delete_number]
                        delete_number += 1

                self.nuX.append(l_nuX)
                self.nuY.append(l_nuY)

    def plot_scatter(self,
                     fig,
                     ax,
                     phaseTime,
                     resonanceOrder,
                     myalpha,
                     mysize,
                     resonanceKind='all',
                     myfontsize=10):
        sc = ax.scatter(self.nuX[phaseTime],
                        self.nuY[phaseTime],
                        alpha=myalpha,
                        s=mysize,
                        color='red',
                        zorder=resonanceOrder)
        # cbar = fig.colorbar(sc)
        # cbar.ax.tick_params(labelsize=myfontsize)
        plot_resonanceDiagram_color(resonanceOrder, ax, self.xlim, self.ylim,
                                    resonanceKind, myfontsize)

    def plot_hexbin(self,
                    fig,
                    ax,
                    phaseTime,
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
                      self.nuX[phaseTime],
                      self.nuY[phaseTime],
                      gridsize=mygridsize,
                      alpha=myalpha,
                      scattersize=1,
                      norm=matplotlib.colors.LogNorm(),
                      cmap='jet')
        cbar = fig.colorbar(he)
        cbar.ax.tick_params(labelsize=myfontsize)

        plot_resonanceDiagram_color(resonanceOrder, ax, self.xlim, self.ylim,
                                    resonanceKind, myfontsize)

    def save_scatter(self, figure, phaseTime, mydpi=300):
        # print(self.savePath[phaseTime])
        figure.savefig(self.savePath_scatter[phaseTime], dpi=mydpi)

    def save_hexbin(self, figure, phaseTime, mydpi=300):
        # print(self.savePath[phaseTime])
        figure.savefig(self.savePath_hexbin[phaseTime], dpi=mydpi)
