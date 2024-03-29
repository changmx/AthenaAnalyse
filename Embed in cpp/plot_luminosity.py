import numpy as np
import matplotlib.pyplot as plt
import os
import glob


class Luminosity:
    """
    Load and plot luminisity data
    """
    def __init__(self, home, yearMonDay, hourMinSec, particle, myfontsize):
        self.home = home
        self.yearMonDay = yearMonDay
        self.hourMinSec = hourMinSec
        self.particle = particle
        self.fontsize = myfontsize

        self.lumi_file = self.hourMinSec + '_luminosity_' + self.particle
        self.lumi_file = os.sep.join([
            self.home, 'statLumiPara', self.yearMonDay, self.hourMinSec,
            self.lumi_file
        ])
        self.lumi_file = glob.glob(self.lumi_file + '*')[0]

        # print(self.lumi_file)

        self.is_lumiExist = os.path.exists(self.lumi_file)

        self.savePath = os.sep.join([
            self.home, 'statLumiPara', self.yearMonDay, self.hourMinSec,
            'figure_luminosity'
        ])
        if not os.path.exists(self.savePath):
            os.makedirs(self.savePath)

        self.save_lumiPath = os.sep.join(
            [self.savePath, self.hourMinSec + '_luminosity_' + self.particle])

        self.save_lumiTogetherPath = os.sep.join(
            [self.savePath, self.hourMinSec + '_luminosity'])

    def load_luminosity(self, skip):
        if self.is_lumiExist:
            self.lumiTurn, self.lumi, self.lumiFactor = np.loadtxt(
                self.lumi_file,
                delimiter=',',
                skiprows=skip,
                usecols=(0, 1, 2),
                unpack=True)
        else:
            print("file doesn't exist: {0}".format(self.lumi_file))

    def plot_luminosity(self, ax, isLabel, myalpha):
        mymarker = 'o'
        mymarker_size = 0.1
        mymarker_linewidth = 0.001
        if self.is_lumiExist:
            mylabel = 'super period' if self.particle == 'suPeriod' else self.particle
            if isLabel:
                ax.scatter(self.lumiTurn,
                           self.lumi,
                           label=mylabel,
                           marker=mymarker,
                           s=mymarker_size,
                           linewidth=mymarker_linewidth)
            else:
                ax.scatter(self.lumiTurn,
                           self.lumi,
                           marker=mymarker,
                           s=mymarker_size,
                           linewidth=mymarker_linewidth)

    def save_lumi(self, figure, mydpi=300):
        figure.savefig(self.save_lumiPath, dpi=mydpi)


if __name__ == '__main__':
    pass