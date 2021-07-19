import numpy as np
import matplotlib.pyplot as plt
import os
from general import cal_freq_fft
from general import cal_spctrum_fft


class Statistic:
    """
    Load and plot bunch statistic data
    """
    def __init__(self, home, yearMonDay, hourMinSec, particle, bunchid, nux,
                 nuy):
        self.home = home
        self.yearMonDay = yearMonDay
        self.hourMinSec = hourMinSec
        self.particle = particle
        self.bunchid = bunchid
        self.bunchLabel = self.particle + " bunch" + str(bunchid)
        self.nux = nux
        self.nuy = nuy

        self.stat_file = self.hourMinSec + '_' + self.particle + '_bunch' + str(
            bunchid) + '_statistic.csv'
        self.stat_file = os.sep.join([
            self.home, 'statLumiPara', self.yearMonDay, self.hourMinSec,
            self.stat_file
        ])

        # print(self.stat_file)

        self.savePath = os.sep.join([
            self.home, 'statLumiPara', self.yearMonDay, self.hourMinSec,
            'figure'
        ])
        if not os.path.exists(self.savePath):
            os.makedirs(self.savePath)

        self.save_bunchStatisticPath = os.sep.join([
            self.savePath, self.hourMinSec + '_figure_' + self.particle +
            "_bunch" + str(self.bunchid)
        ])

        self.save_beamStatisticPath = os.sep.join([
            self.savePath,
            self.hourMinSec + '_figure_' + self.particle + "_beam"
        ])

        self.is_statExist = os.path.exists(self.stat_file)

    def load_statistic(self):
        if self.is_statExist:
            self.turn, self.xAverage, self.sigmax, self.yAverage, self.sigmay, self.xEmit, self.yEmit, self.sigmaz, self.sigmapz, self.beamloss = np.loadtxt(
                self.stat_file,
                delimiter=',',
                skiprows=1,
                usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
                unpack=True)
        else:
            print("file doesn't exist: {0}".format(self.stat_file))

    def plot_statistic(
            self,
            ax,
            myalpha,
            freqx=(0, 1),
            freqy=(0, 1),
    ):
        if self.is_statExist:
            if self.particle == 'proton':
                freqx = (0, 0.5)
                freqy = (0, 0.5)
            if self.particle == 'electron':
                freqx = (0.5, 1)
                freqy = (0.5, 1)

            ax[0, 0].plot(self.turn,
                          self.xAverage,
                          label=self.bunchLabel,
                          alpha=myalpha)
            ax[0, 0].set_ylabel(r'$\overline{\mathrm{x}}(\mathrm{m})$')

            ax[0, 1].plot(self.turn,
                          self.sigmax,
                          label=self.bunchLabel,
                          alpha=myalpha)
            ax[0, 1].set_ylabel(r'$\sigma_x (\mathrm{m})$')

            ax[0, 2].plot(self.turn,
                          self.xEmit,
                          label=self.bunchLabel,
                          alpha=myalpha)
            ax[0, 2].set_ylabel(r'$\epsilon_x (\mathrm{m}\cdot\mathrm{rad})$')

            ax[1, 0].plot(self.turn,
                          self.yAverage,
                          label=self.bunchLabel,
                          alpha=myalpha)
            ax[1, 0].set_ylabel(r'$\overline{\mathrm{y}} (\mathrm{m})$')

            ax[1, 1].plot(self.turn,
                          self.sigmay,
                          label=self.bunchLabel,
                          alpha=myalpha)
            ax[1, 1].set_ylabel(r'$\sigma_y (\mathrm{m})$')

            ax[1, 2].plot(self.turn,
                          self.yEmit,
                          label=self.bunchLabel,
                          alpha=myalpha)
            ax[1, 2].set_ylabel(r'$\epsilon_y (\mathrm{m}\cdot\mathrm{rad})$')

            freq_x = cal_freq_fft(self.turn.shape[0], 1, freqx[0], freqx[1])
            spec_x = cal_spctrum_fft(self.turn.shape[0], 1, freqx[0], freqx[1],
                                     self.xAverage)

            ax[2, 0].plot(freq_x, spec_x, label=self.bunchLabel, alpha=myalpha)
            ax[2, 0].set_ylabel('Amplitude x')
            ax[2, 0].set_yscale('log')
            ax[2, 0].axvline(x=self.nux,
                             ymin=0,
                             ymax=1,
                             color='red',
                             linestyle="--")

            freq_y = cal_freq_fft(self.turn.shape[0], 1, freqy[0], freqy[1])
            spec_y = cal_spctrum_fft(self.turn.shape[0], 1, freqy[0], freqy[1],
                                     self.yAverage)

            ax[2, 1].plot(freq_y, spec_y, label=self.bunchLabel, alpha=myalpha)
            ax[2, 1].set_ylabel('Amplitude y')
            ax[2, 1].set_yscale('log')
            ax[2, 1].axvline(x=self.nuy,
                             ymin=0,
                             ymax=1,
                             color='red',
                             linestyle="--")

            ax[2, 2].plot(self.turn,
                          self.beamloss,
                          label=self.bunchLabel,
                          alpha=myalpha)
            ax[2, 2].set_ylabel('particle loss')

            for i in range(3):
                for j in range(3):
                    ax[i, j].legend(loc='best')
            for i in range(2):
                for j in range(3):
                    ax[i, j].ticklabel_format(axis='y',
                                              style='sci',
                                              scilimits=(0, 0))

    def save_bunchStatistic(self, figure, mydpi=300):
        figure.savefig(self.save_bunchStatisticPath, dpi=mydpi)

    def save_beamStatistic(self, figure, mydpi=300):
        figure.savefig(self.save_beamStatisticPath, dpi=mydpi)

    def manage_axGrid(self, ax):
        for i in range(3):
            for j in range(3):
                ax[i, j].grid()


if __name__ == '__main__':
    pass
