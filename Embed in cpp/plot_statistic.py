from pickle import NEXT_BUFFER
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os
from general import cal_freq_fft
from general import cal_spctrum_fft
from plot_general import plot_save_single_figure
from plot_general import plot_save_single_line_figure


class Statistic:
    """
    Load and plot bunch statistic data
    """

    def __init__(self, home, yearMonDay, hourMinSec, particle, bunchid, nux,
                 nuy, sigmax, sigmay, sigmapx, sigmapy, nbunch_opp):
        self.marker = 'o'
        self.marker_size = 0.1
        self.marker_linewidth = 0.001
        self.home = home
        self.yearMonDay = yearMonDay
        self.hourMinSec = hourMinSec
        self.particle = particle
        self.bunchid = bunchid
        self.bunchLabel = self.particle + " bunch" + str(bunchid)
        self.nux = nux
        self.nuy = nuy
        self.inisigmax = sigmax
        self.inisigmay = sigmay
        self.inisigmapx = sigmapx
        self.inisigmapy = sigmapy
        self.nbunch_opp = nbunch_opp
        self.version = 'new' if self.yearMonDay > '2021_0816' else 'old'

        self.stat_file = self.hourMinSec + '_' + self.particle + '_bunch' + str(
            bunchid) + '_statistic.csv'
        self.stat_file = os.sep.join([
            self.home, 'statLumiPara', self.yearMonDay, self.hourMinSec,
            self.stat_file
        ])
        self.turn_unit = 'Super period' if self.nbunch_opp > 1 else 'Turn'

        # print(self.stat_file)

        self.savePath = os.sep.join([
            self.home, 'statLumiPara', self.yearMonDay, self.hourMinSec,
            'figure_statistic'
        ])
        if not os.path.exists(self.savePath):
            os.makedirs(self.savePath)

        self.savePath_single = os.sep.join([self.savePath, 'single'])
        if not os.path.exists(self.savePath_single):
            os.makedirs(self.savePath_single)

        self.save_bunchStatisticPath = []
        self.save_beamStatisticPath = []
        self.save_bunchStatisticPath_single = os.sep.join([
            self.savePath_single, self.hourMinSec + '_' + self.particle +
            "_bunch" + str(self.bunchid)
        ])
        self.save_beamStatisticPath_single = os.sep.join(
            [self.savePath_single, self.hourMinSec + '_' + self.particle])

        for i in range(5):
            self.save_bunchStatisticPath.append(
                os.sep.join([
                    self.savePath, self.hourMinSec + '_' + self.particle +
                    "_bunch" + str(self.bunchid) + '_part' + str(i)
                ]))

            self.save_beamStatisticPath.append(
                os.sep.join([
                    self.savePath, self.hourMinSec + '_' + self.particle +
                    '_beam_part' + str(i)
                ]))

        self.is_statExist = os.path.exists(self.stat_file)

    def load_statistic(self):
        if self.is_statExist:
            self.turn, self.xAverage, self.pxAverage, self.sigmax, self.sigmapx, self.yAverage, self.pyAverage, self.sigmay, self.sigmapy, self.zAverage, self.pzAverage, self.sigmaz, self.sigmapz, self.xEmit, self.yEmit, self.betax, self.betay, self.alphax, self.alphay, self.gammax, self.gammay, self.invariantx, self.invarianty, self.xzAverage, self.xyAverage, self.yzAverage, self.xzDevideSigmaxSigmaZ, self.beamloss, self.lossPercent = np.loadtxt(
                self.stat_file,
                delimiter=',',
                skiprows=1,
                usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                         16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
                unpack=True)
            self.turn /= self.nbunch_opp
            self.xAverage /= self.inisigmax
            self.yAverage /= self.inisigmay
            self.pxAverage /= self.inisigmapx
            self.pyAverage /= self.inisigmapy
            try:
                self.xSkewness, self.xKurtosis, self.ySkewness, self.yKurtosis = np.loadtxt(
                    self.stat_file,
                    delimiter=',',
                    skiprows=1,
                    usecols=(29, 30, 31, 32),
                    unpack=True)
            except:
                pass
        else:
            print("file doesn't exist: {0}".format(self.stat_file))

    def plot_statistic_part0(
            self,
            ax,
            ax_single,
            myalpha,
            myfontsize,
            freqx=(0, 1),
            freqy=(0, 1),
    ):
        matplotlib.rcParams['agg.path.chunksize'] = 10000
        if self.is_statExist:
            if self.nux > 0.5:
                freqx = (0.5, 1)
            else:
                freqx = (0, 0.5)
            if self.nuy > 0.5:
                freqy = (0.5, 1)
            else:
                freqy = (0, 0.5)

            ax[0, 0].scatter(self.turn,
                             self.xAverage,
                             label=self.bunchLabel,
                             alpha=myalpha,
                             marker=self.marker,
                             s=self.marker_size,
                             linewidth=self.marker_linewidth)
            ax[0, 0].set_ylabel(r'$\overline{\mathrm{x}}/\sigma_x$',
                                fontsize=myfontsize)
            plot_save_single_figure(ax_single[0],
                                    self.turn,
                                    self.xAverage,
                                    self.turn_unit,
                                    r'$\overline{\mathrm{x}}/\sigma_x$',
                                    label=self.bunchLabel,
                                    xstyle='sci',
                                    ystyle='sci',
                                    fontsize=15,
                                    alpha=myalpha)

            ax[0, 1].scatter(self.turn,
                             self.sigmax,
                             label=self.bunchLabel,
                             alpha=myalpha,
                             marker=self.marker,
                             s=self.marker_size,
                             linewidth=self.marker_linewidth)
            ax[0, 1].set_ylabel(r'$\sigma_x\ (\mathrm{m})$',
                                fontsize=myfontsize)
            plot_save_single_figure(ax_single[1],
                                    self.turn,
                                    self.sigmax,
                                    self.turn_unit,
                                    r'$\sigma_x\ (\mathrm{m})$',
                                    label=self.bunchLabel,
                                    ystyle='sci',
                                    xstyle='sci',
                                    fontsize=15,
                                    alpha=myalpha)

            ax[0, 2].scatter(self.turn,
                             self.xEmit,
                             label=self.bunchLabel,
                             alpha=myalpha,
                             marker=self.marker,
                             s=self.marker_size,
                             linewidth=self.marker_linewidth)
            ax[0, 2].set_ylabel(r'$\epsilon_x\ (\mathrm{m}\cdot\mathrm{rad})$',
                                fontsize=myfontsize)
            plot_save_single_figure(
                ax_single[2],
                self.turn,
                self.xEmit,
                self.turn_unit,
                r'$\epsilon_x\ (\mathrm{m}\cdot\mathrm{rad})$',
                label=self.bunchLabel,
                ystyle='sci',
                xstyle='sci',
                fontsize=15,
                alpha=myalpha)

            ax[1, 0].scatter(self.turn,
                             self.yAverage,
                             label=self.bunchLabel,
                             alpha=myalpha,
                             marker=self.marker,
                             s=self.marker_size,
                             linewidth=self.marker_linewidth)
            ax[1, 0].set_ylabel(r'$\overline{\mathrm{y}}/\sigma_y$',
                                fontsize=myfontsize)
            plot_save_single_figure(ax_single[3],
                                    self.turn,
                                    self.yAverage,
                                    self.turn_unit,
                                    r'$\overline{\mathrm{y}}/\sigma_y$',
                                    label=self.bunchLabel,
                                    xstyle='sci',
                                    ystyle='sci',
                                    fontsize=15,
                                    alpha=myalpha)

            ax[1, 1].scatter(self.turn,
                             self.sigmay,
                             label=self.bunchLabel,
                             alpha=myalpha,
                             marker=self.marker,
                             s=self.marker_size,
                             linewidth=self.marker_linewidth)
            ax[1, 1].set_ylabel(r'$\sigma_y\ (\mathrm{m})$',
                                fontsize=myfontsize)
            plot_save_single_figure(ax_single[4],
                                    self.turn,
                                    self.sigmay,
                                    self.turn_unit,
                                    r'$\sigma_y\ (\mathrm{m})$',
                                    label=self.bunchLabel,
                                    ystyle='sci',
                                    xstyle='sci',
                                    fontsize=15,
                                    alpha=myalpha)

            ax[1, 2].scatter(self.turn,
                             self.yEmit,
                             label=self.bunchLabel,
                             alpha=myalpha,
                             marker=self.marker,
                             s=self.marker_size,
                             linewidth=self.marker_linewidth)
            ax[1, 2].set_ylabel(r'$\epsilon_y\ (\mathrm{m}\cdot\mathrm{rad})$',
                                fontsize=myfontsize)
            plot_save_single_figure(
                ax_single[5],
                self.turn,
                self.yEmit,
                self.turn_unit,
                r'$\epsilon_y\ (\mathrm{m}\cdot\mathrm{rad})$',
                label=self.bunchLabel,
                ystyle='sci',
                xstyle='sci',
                fontsize=15,
                alpha=myalpha)

            freq_x = cal_freq_fft(self.turn.shape[0], 1, freqx[0], freqx[1])
            spec_x = cal_spctrum_fft(self.turn.shape[0], 1, freqx[0], freqx[1],
                                     self.xAverage)
            ax[2, 0].plot(freq_x,
                          spec_x,
                          label=self.bunchLabel,
                          alpha=myalpha,
                          linewidth=0.2)
            ax[2, 0].set_ylabel('Amplitude x', fontsize=myfontsize)
            ax[2, 0].set_yscale('log')
            ax[2, 0].axvline(x=self.nux,
                             ymin=0,
                             ymax=1,
                             color='red',
                             linestyle="--")
            plot_save_single_line_figure(ax_single[6],
                                         freq_x,
                                         spec_x,
                                         r'$\nu_x$',
                                         'Amplitude x',
                                         label=self.bunchLabel,
                                         fontsize=15,
                                         yscale='log',
                                         vline=self.nux,
                                         alpha=myalpha)

            freq_y = cal_freq_fft(self.turn.shape[0], 1, freqy[0], freqy[1])
            spec_y = cal_spctrum_fft(self.turn.shape[0], 1, freqy[0], freqy[1],
                                     self.yAverage)

            ax[2, 1].plot(freq_y,
                          spec_y,
                          label=self.bunchLabel,
                          alpha=myalpha,
                          linewidth=0.2)
            ax[2, 1].set_ylabel('Amplitude y', fontsize=myfontsize)
            ax[2, 1].set_yscale('log')
            ax[2, 1].axvline(x=self.nuy,
                             ymin=0,
                             ymax=1,
                             color='red',
                             linestyle="--")
            plot_save_single_line_figure(ax_single[7],
                                         freq_y,
                                         spec_y,
                                         r'$\nu_y$',
                                         'Amplitude y',
                                         label=self.bunchLabel,
                                         fontsize=15,
                                         yscale='log',
                                         vline=self.nuy,
                                         alpha=myalpha)

            ax[2, 2].plot(self.turn,
                          self.beamloss,
                          label=self.bunchLabel,
                          alpha=myalpha)
            ax[2, 2].set_ylabel('particle loss', fontsize=myfontsize)
            plot_save_single_line_figure(ax_single[8],
                                         self.turn,
                                         self.beamloss,
                                         self.turn_unit,
                                         'Particle loss',
                                         label=self.bunchLabel,
                                         fontsize=15,
                                         xstyle='sci',
                                         alpha=myalpha)

            for i in range(3):
                for j in range(3):
                    leg = ax[i, j].legend(loc='best',
                                          fontsize=myfontsize,
                                          markerscale=1 / self.marker_size)
                    for legobj in leg.legendHandles:
                        legobj.set_linewidth(1)
            for i in range(2):
                for j in range(3):
                    ax[i, j].ticklabel_format(axis='y',
                                              style='sci',
                                              scilimits=(0, 0))

    def plot_statistic_part1(self, ax, ax_single, myalpha, myfontsize):
        matplotlib.rcParams['agg.path.chunksize'] = 10000
        if self.version == 'new':
            if self.is_statExist:
                ax[0, 0].scatter(self.turn,
                                 self.pxAverage,
                                 label=self.bunchLabel,
                                 alpha=myalpha,
                                 marker=self.marker,
                                 s=self.marker_size,
                                 linewidth=self.marker_linewidth)
                ax[0, 0].set_ylabel(
                    r'$\overline{\mathrm{x^{\prime}}}/\sigma_{\mathrm{x^{\prime}}}$',
                    fontsize=myfontsize)
                plot_save_single_figure(
                    ax_single[9],
                    self.turn,
                    self.pxAverage,
                    self.turn_unit,
                    r'$\overline{\mathrm{x^{\prime}}}/\sigma_{\mathrm{x^{\prime}}}$',
                    label=self.bunchLabel,
                    xstyle='sci',
                    ystyle='sci',
                    fontsize=15,
                    alpha=myalpha)

                ax[0, 1].scatter(self.turn,
                                 self.sigmapx,
                                 label=self.bunchLabel,
                                 alpha=myalpha,
                                 marker=self.marker,
                                 s=self.marker_size,
                                 linewidth=self.marker_linewidth)
                ax[0, 1].set_ylabel(r'$\sigma_{x^{\prime}}\ (\mathrm{rad})$',
                                    fontsize=myfontsize)
                plot_save_single_figure(
                    ax_single[10],
                    self.turn,
                    self.sigmapx,
                    self.turn_unit,
                    r'$\sigma_{x^{\prime}}\ (\mathrm{rad})$',
                    label=self.bunchLabel,
                    ystyle='sci',
                    xstyle='sci',
                    fontsize=15,
                    alpha=myalpha)

                ax[0, 2].scatter(self.turn,
                                 self.zAverage,
                                 label=self.bunchLabel,
                                 alpha=myalpha,
                                 marker=self.marker,
                                 s=self.marker_size,
                                 linewidth=self.marker_linewidth)
                ax[0, 2].set_ylabel(r'$\overline{\mathrm{z}}\ (\mathrm{m})$',
                                    fontsize=myfontsize)
                plot_save_single_figure(
                    ax_single[11],
                    self.turn,
                    self.zAverage,
                    self.turn_unit,
                    r'$\overline{\mathrm{z}}\ (\mathrm{m})$',
                    label=self.bunchLabel,
                    ystyle='sci',
                    xstyle='sci',
                    fontsize=15,
                    alpha=myalpha)

                ax[1, 0].scatter(self.turn,
                                 self.pyAverage,
                                 label=self.bunchLabel,
                                 alpha=myalpha,
                                 marker=self.marker,
                                 s=self.marker_size,
                                 linewidth=self.marker_linewidth)
                ax[1, 0].set_ylabel(
                    r'$\overline{\mathrm{y^{\prime}}}/\sigma_{\mathrm{y^{\prime}}}$',
                    fontsize=myfontsize)
                plot_save_single_figure(
                    ax_single[12],
                    self.turn,
                    self.pyAverage,
                    self.turn_unit,
                    r'$\overline{\mathrm{y^{\prime}}}/\sigma_{\mathrm{y^{\prime}}}$',
                    label=self.bunchLabel,
                    xstyle='sci',
                    ystyle='sci',
                    fontsize=15,
                    alpha=myalpha)

                ax[1, 1].scatter(self.turn,
                                 self.sigmapy,
                                 label=self.bunchLabel,
                                 alpha=myalpha,
                                 marker=self.marker,
                                 s=self.marker_size,
                                 linewidth=self.marker_linewidth)
                ax[1, 1].set_ylabel(r'$\sigma_{y^{\prime}}\ (\mathrm{rad})$',
                                    fontsize=myfontsize)
                plot_save_single_figure(
                    ax_single[13],
                    self.turn,
                    self.sigmapy,
                    self.turn_unit,
                    r'$\sigma_{y^{\prime}}\ (\mathrm{rad})$',
                    label=self.bunchLabel,
                    ystyle='sci',
                    xstyle='sci',
                    fontsize=15,
                    alpha=myalpha)

                ax[1, 2].scatter(self.turn,
                                 self.sigmaz,
                                 label=self.bunchLabel,
                                 alpha=myalpha,
                                 marker=self.marker,
                                 s=self.marker_size,
                                 linewidth=self.marker_linewidth)
                ax[1, 2].set_ylabel(r'$\sigma_z\ (\mathrm{m})$',
                                    fontsize=myfontsize)
                plot_save_single_figure(ax_single[14],
                                        self.turn,
                                        self.sigmaz,
                                        self.turn_unit,
                                        r'$\sigma_z\ (\mathrm{m})$',
                                        label=self.bunchLabel,
                                        ystyle='sci',
                                        xstyle='sci',
                                        fontsize=15,
                                        alpha=myalpha)

                ax[2, 0].scatter(self.turn,
                                 self.pzAverage,
                                 label=self.bunchLabel,
                                 alpha=myalpha,
                                 marker=self.marker,
                                 s=self.marker_size,
                                 linewidth=self.marker_linewidth)
                ax[2, 0].set_ylabel(r'$\overline{\mathrm{dp}}$',
                                    fontsize=myfontsize)
                plot_save_single_figure(ax_single[15],
                                        self.turn,
                                        self.pzAverage,
                                        self.turn_unit,
                                        r'$\overline{\mathrm{dp}}$',
                                        label=self.bunchLabel,
                                        ystyle='sci',
                                        xstyle='sci',
                                        fontsize=15,
                                        alpha=myalpha)

                ax[2, 1].scatter(self.turn,
                                 self.sigmapz,
                                 label=self.bunchLabel,
                                 alpha=myalpha,
                                 marker=self.marker,
                                 s=self.marker_size,
                                 linewidth=self.marker_linewidth)
                ax[2, 1].set_ylabel(r'$\delta_p$', fontsize=myfontsize)
                plot_save_single_figure(ax_single[16],
                                        self.turn,
                                        self.sigmapz,
                                        self.turn_unit,
                                        r'$\delta_p$',
                                        label=self.bunchLabel,
                                        ystyle='sci',
                                        xstyle='sci',
                                        fontsize=15,
                                        alpha=myalpha)

                ax[2, 2].plot(self.turn,
                              self.lossPercent,
                              label=self.bunchLabel,
                              alpha=myalpha)
                ax[2, 2].set_ylabel('Percentage of particle loss (%)',
                                    fontsize=myfontsize)
                plot_save_single_figure(ax_single[17],
                                        self.turn,
                                        self.lossPercent,
                                        self.turn_unit,
                                        'Percentage of particle loss (%)',
                                        label=self.bunchLabel,
                                        fontsize=15,
                                        xstyle='sci',
                                        alpha=myalpha)

                for i in range(3):
                    for j in range(3):
                        ax[i, j].legend(loc='best',
                                        fontsize=myfontsize,
                                        markerscale=1 / self.marker_size)
                for i in range(3):
                    for j in range(3):
                        ax[i, j].ticklabel_format(axis='y',
                                                  style='sci',
                                                  scilimits=(0, 0))

    def plot_statistic_part2(self, ax, ax_single, myalpha, myfontsize):
        matplotlib.rcParams['agg.path.chunksize'] = 10000
        if self.version == 'new':
            if self.is_statExist:
                ax[0, 0].scatter(self.turn,
                                 self.betax,
                                 label=self.bunchLabel,
                                 alpha=myalpha,
                                 marker=self.marker,
                                 s=self.marker_size,
                                 linewidth=self.marker_linewidth)
                ax[0, 0].set_ylabel(r'$\mathrm{\beta_x}\ (\mathrm{m})$',
                                    fontsize=myfontsize)
                plot_save_single_figure(ax_single[18],
                                        self.turn,
                                        self.betax,
                                        self.turn_unit,
                                        r'$\mathrm{\beta_x}\ (\mathrm{m})$',
                                        label=self.bunchLabel,
                                        ystyle='sci',
                                        xstyle='sci',
                                        fontsize=15,
                                        alpha=myalpha)

                ax[0, 1].scatter(self.turn,
                                 self.betay,
                                 label=self.bunchLabel,
                                 alpha=myalpha,
                                 marker=self.marker,
                                 s=self.marker_size,
                                 linewidth=self.marker_linewidth)
                ax[0, 1].set_ylabel(r'$\mathrm{\beta_y}\ (\mathrm{m})$',
                                    fontsize=myfontsize)
                plot_save_single_figure(ax_single[19],
                                        self.turn,
                                        self.betay,
                                        self.turn_unit,
                                        r'$\mathrm{\beta_y}\ (\mathrm{m})$',
                                        label=self.bunchLabel,
                                        ystyle='sci',
                                        xstyle='sci',
                                        fontsize=15,
                                        alpha=myalpha)

                ax[0, 2].plot(self.turn,
                              self.invariantx,
                              label=self.bunchLabel,
                              alpha=myalpha)
                ax[0, 2].set_ylabel(r'$\mathrm{\gamma_x\beta_x}-{\alpha_x}^2$',
                                    fontsize=myfontsize)
                plot_save_single_line_figure(
                    ax_single[20],
                    self.turn,
                    self.invariantx,
                    self.turn_unit,
                    r'$\mathrm{\gamma_x\beta_x}-{\alpha_x}^2$',
                    label=self.bunchLabel,
                    fontsize=15,
                    xstyle='sci',
                    alpha=myalpha)

                ax[1, 0].scatter(self.turn,
                                 self.alphax,
                                 label=self.bunchLabel,
                                 alpha=myalpha,
                                 marker=self.marker,
                                 s=self.marker_size,
                                 linewidth=self.marker_linewidth)
                ax[1, 0].set_ylabel(r'$\mathrm{\alpha_x}$',
                                    fontsize=myfontsize)
                plot_save_single_figure(ax_single[21],
                                        self.turn,
                                        self.alphax,
                                        self.turn_unit,
                                        r'$\mathrm{\alpha_x}$',
                                        label=self.bunchLabel,
                                        ystyle='sci',
                                        xstyle='sci',
                                        fontsize=15,
                                        alpha=myalpha)

                ax[1, 1].scatter(self.turn,
                                 self.alphay,
                                 label=self.bunchLabel,
                                 alpha=myalpha,
                                 marker=self.marker,
                                 s=self.marker_size,
                                 linewidth=self.marker_linewidth)
                ax[1, 1].set_ylabel(r'$\mathrm{\alpha_y}$',
                                    fontsize=myfontsize)
                plot_save_single_figure(ax_single[22],
                                        self.turn,
                                        self.alphay,
                                        self.turn_unit,
                                        r'$\mathrm{\alpha_y}$',
                                        label=self.bunchLabel,
                                        ystyle='sci',
                                        xstyle='sci',
                                        fontsize=15,
                                        alpha=myalpha)

                ax[1, 2].plot(self.turn,
                              self.invarianty,
                              label=self.bunchLabel,
                              alpha=myalpha)
                ax[1, 2].set_ylabel(r'$\mathrm{\gamma_y\beta_y}-{\alpha_y}^2$',
                                    fontsize=myfontsize)
                plot_save_single_line_figure(
                    ax_single[23],
                    self.turn,
                    self.invarianty,
                    self.turn_unit,
                    r'$\mathrm{\gamma_y\beta_y}-{\alpha_y}^2$',
                    label=self.bunchLabel,
                    fontsize=15,
                    xstyle='sci',
                    alpha=myalpha)

                ax[2, 0].scatter(self.turn,
                                 self.gammax,
                                 label=self.bunchLabel,
                                 alpha=myalpha,
                                 marker=self.marker,
                                 s=self.marker_size,
                                 linewidth=self.marker_linewidth)
                ax[2, 0].set_ylabel(r'$\mathrm{\gamma_x}\ (\mathrm{m^{-1}})$',
                                    fontsize=myfontsize)
                plot_save_single_figure(
                    ax_single[24],
                    self.turn,
                    self.gammax,
                    self.turn_unit,
                    r'$\mathrm{\gamma_x}\ (\mathrm{m^{-1}})$',
                    label=self.bunchLabel,
                    fontsize=15,
                    xstyle='sci',
                    alpha=myalpha)

                ax[2, 1].scatter(self.turn,
                                 self.gammay,
                                 label=self.bunchLabel,
                                 alpha=myalpha,
                                 marker=self.marker,
                                 s=self.marker_size,
                                 linewidth=self.marker_linewidth)
                ax[2, 1].set_ylabel(r'$\mathrm{\gamma_y}\ (\mathrm{m^{-1}})$',
                                    fontsize=myfontsize)
                plot_save_single_figure(
                    ax_single[25],
                    self.turn,
                    self.gammay,
                    self.turn_unit,
                    r'$\mathrm{\gamma_y}\ (\mathrm{m^{-1}})$',
                    label=self.bunchLabel,
                    fontsize=15,
                    xstyle='sci',
                    alpha=myalpha)

                ax[2, 2].plot(self.turn,
                              self.beamloss,
                              label=self.bunchLabel,
                              alpha=myalpha)
                ax[2, 2].set_ylabel('particle loss', fontsize=myfontsize)

                for i in range(3):
                    for j in range(3):
                        leg = ax[i, j].legend(loc='best',
                                              fontsize=myfontsize,
                                              markerscale=1 / self.marker_size)
                        for legobj in leg.legendHandles:
                            legobj.set_linewidth(1)
                # for i in range(3):
                #     for j in range(3):
                #         ax[i, j].ticklabel_format(axis='y',
                #                                   style='sci',
                #                                   scilimits=(0, 0))

    def plot_statistic_part3(self, ax, ax_single, myalpha, myfontsize):
        matplotlib.rcParams['agg.path.chunksize'] = 10000
        if self.version == 'new':
            if self.is_statExist:
                ax[0, 0].scatter(self.turn,
                                 self.xzAverage,
                                 label=self.bunchLabel,
                                 alpha=myalpha,
                                 marker=self.marker,
                                 s=self.marker_size,
                                 linewidth=self.marker_linewidth)
                ax[0,
                   0].set_ylabel(r'$\overline{\mathrm{xz}}\ (\mathrm{m^2})$',
                                 fontsize=myfontsize)
                plot_save_single_figure(
                    ax_single[26],
                    self.turn,
                    self.xzAverage,
                    self.turn_unit,
                    r'$\overline{\mathrm{xz}}\ (\mathrm{m^2})$',
                    label=self.bunchLabel,
                    ystyle='sci',
                    xstyle='sci',
                    fontsize=15,
                    alpha=myalpha)

                ax[0, 1].scatter(self.turn,
                                 self.xyAverage,
                                 label=self.bunchLabel,
                                 alpha=myalpha,
                                 marker=self.marker,
                                 s=self.marker_size,
                                 linewidth=self.marker_linewidth)
                ax[0,
                   1].set_ylabel(r'$\overline{\mathrm{xy}}\ (\mathrm{m^2})$',
                                 fontsize=myfontsize)
                plot_save_single_figure(
                    ax_single[27],
                    self.turn,
                    self.xyAverage,
                    self.turn_unit,
                    r'$\overline{\mathrm{xy}}\ (\mathrm{m^2})$',
                    label=self.bunchLabel,
                    ystyle='sci',
                    xstyle='sci',
                    fontsize=15,
                    alpha=myalpha)

                ax[1, 0].scatter(self.turn,
                                 self.yzAverage,
                                 label=self.bunchLabel,
                                 alpha=myalpha,
                                 marker=self.marker,
                                 s=self.marker_size,
                                 linewidth=self.marker_linewidth)
                ax[1,
                   0].set_ylabel(r'$\overline{\mathrm{yz}}\ (\mathrm{m^2})$',
                                 fontsize=myfontsize)
                plot_save_single_figure(
                    ax_single[28],
                    self.turn,
                    self.yzAverage,
                    self.turn_unit,
                    r'$\overline{\mathrm{yz}}\ (\mathrm{m^2})$',
                    label=self.bunchLabel,
                    ystyle='sci',
                    xstyle='sci',
                    fontsize=15,
                    alpha=myalpha)

                ax[1, 1].scatter(self.turn,
                                 self.xzDevideSigmaxSigmaZ,
                                 label=self.bunchLabel,
                                 alpha=myalpha,
                                 marker=self.marker,
                                 s=self.marker_size,
                                 linewidth=self.marker_linewidth)
                ax[1, 1].set_ylabel(
                    r'$\overline{\mathrm{xz}}/\mathrm{\sigma_x\sigma_z}$',
                    fontsize=myfontsize)
                plot_save_single_figure(
                    ax_single[29],
                    self.turn,
                    self.xzDevideSigmaxSigmaZ,
                    self.turn_unit,
                    r'$\overline{\mathrm{xz/\sigma_x\sigma_z}}$',
                    label=self.bunchLabel,
                    ystyle='sci',
                    xstyle='sci',
                    fontsize=15,
                    alpha=myalpha)

                for i in range(2):
                    for j in range(2):
                        ax[i, j].legend(loc='best',
                                        fontsize=myfontsize,
                                        markerscale=1 / self.marker_size)
                # for i in range(2):
                #     for j in range(2):
                #         ax[i, j].ticklabel_format(axis='y',
                #                                   style='sci',
                #                                   scilimits=(0, 0))

    def plot_statistic_part4(self, ax, ax_single, myalpha, myfontsize):
        matplotlib.rcParams['agg.path.chunksize'] = 10000
        if self.version == 'new':
            if self.is_statExist:
                if hasattr(self, 'xSkewness'):
                    ax[0, 0].scatter(self.turn,
                                     self.xSkewness,
                                     label=self.bunchLabel,
                                     alpha=myalpha,
                                     marker=self.marker,
                                     s=self.marker_size,
                                     linewidth=self.marker_linewidth)
                    ax[0, 0].set_ylabel('x skewness', fontsize=myfontsize)
                    plot_save_single_figure(ax_single[30],
                                            self.turn,
                                            self.xSkewness,
                                            self.turn_unit,
                                            'x skewness',
                                            label=self.bunchLabel,
                                            ystyle='sci',
                                            xstyle='sci',
                                            fontsize=15,
                                            alpha=myalpha)

                    ax[0, 1].scatter(self.turn,
                                     self.xKurtosis,
                                     label=self.bunchLabel,
                                     alpha=myalpha,
                                     marker=self.marker,
                                     s=self.marker_size,
                                     linewidth=self.marker_linewidth)
                    ax[0, 1].set_ylabel('x kurtosis', fontsize=myfontsize)
                    plot_save_single_figure(ax_single[31],
                                            self.turn,
                                            self.xKurtosis,
                                            self.turn_unit,
                                            'x kurtosis',
                                            label=self.bunchLabel,
                                            fontsize=15,
                                            xstyle='sci',
                                            alpha=myalpha)

                    ax[1, 0].scatter(self.turn,
                                     self.ySkewness,
                                     label=self.bunchLabel,
                                     alpha=myalpha,
                                     marker=self.marker,
                                     s=self.marker_size,
                                     linewidth=self.marker_linewidth)
                    ax[1, 0].set_ylabel('y skewness', fontsize=myfontsize)
                    plot_save_single_figure(ax_single[32],
                                            self.turn,
                                            self.ySkewness,
                                            self.turn_unit,
                                            'y skewness',
                                            label=self.bunchLabel,
                                            ystyle='sci',
                                            xstyle='sci',
                                            fontsize=15,
                                            alpha=myalpha)

                    ax[1, 1].scatter(self.turn,
                                     self.yKurtosis,
                                     label=self.bunchLabel,
                                     alpha=myalpha,
                                     marker=self.marker,
                                     s=self.marker_size,
                                     linewidth=self.marker_linewidth)
                    ax[1, 1].set_ylabel('y kurtosis', fontsize=myfontsize)
                    plot_save_single_figure(ax_single[33],
                                            self.turn,
                                            self.yKurtosis,
                                            self.turn_unit,
                                            'y kurtosis',
                                            label=self.bunchLabel,
                                            xstyle='sci',
                                            fontsize=15,
                                            alpha=myalpha)

                    for i in range(2):
                        for j in range(2):
                            ax[i, j].legend(loc='best',
                                            fontsize=myfontsize,
                                            markerscale=1 / self.marker_size)
                    # for i in range(2):
                    #     for j in range(2):
                    #         ax[i, j].ticklabel_format(axis='y',
                    #                                   style='sci',
                    #                                   scilimits=(0, 0))

    def save_bunchStatistic(self, figure, part, mydpi=300):
        # print(self.save_bunchStatisticPath[part])
        figure.savefig(self.save_bunchStatisticPath[part], dpi=mydpi)

    def save_beamStatistic(self, figure, part, mydpi=300):
        figure.savefig(self.save_beamStatisticPath[part], dpi=mydpi)

    def manage_axGrid(self, ax, row, col):
        for i in range(row):
            for j in range(col):
                ax[i, j].grid()


if __name__ == '__main__':
    pass
