import numpy as np
import matplotlib.pyplot as plt
from Common import cal_freq_fft
from Common import cal_spctrum_fft


def plot_statistic(name_statistic,
                   path_statistic,
                   path_lumi,
                   save=False,
                   multiBunch=True,
                   freqx=(0, 1),
                   freqy=(0, 1),
                   note=''):
    row = 3
    col = 4

    if save:
        fig, ax = plt.subplots(row, col, figsize=(20, 10))
    else:
        fig, ax = plt.subplots(row, col)

    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号

    for path, particle in zip(path_statistic, name_statistic):
        turn, xAverage, sigmax, yAverage, sigmay, xEmit, yEmit, sigmaz, sigmapz, beamloss = np.loadtxt(
            path,
            delimiter=',',
            skiprows=1,
            usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
            unpack=True)

        ax[0, 0].plot(turn, xAverage, label=particle, alpha=0.5)
        ax[0, 0].set_ylabel(r'$\overline{x}$')

        ax[0, 1].plot(turn, sigmax, label=particle)
        ax[0, 1].set_ylabel(r'$\sigma_x$')

        ax[0, 2].plot(turn, xEmit, label=particle)
        ax[0, 2].set_ylabel(r'$\epsilon_x$')

        ax[1, 0].plot(turn, yAverage, label=particle, alpha=0.5)
        ax[1, 0].set_ylabel(r'$\overline{y}$')

        ax[1, 1].plot(turn, sigmay, label=particle)
        ax[1, 1].set_ylabel(r'$\sigma_y$')

        ax[1, 2].plot(turn, yEmit, label=particle)
        ax[1, 2].set_ylabel(r'$\epsilon_y$')

        ax[2, 0].plot(turn, sigmaz, label=particle)
        ax[2, 0].set_ylabel(r'$\sigma_z$')

        ax[2, 1].plot(turn, sigmapz, label=particle)
        ax[2, 1].set_ylabel(r'$\sigma_{pz}$')

        ax[2, 2].plot(turn, beamloss, label=particle)
        ax[2, 2].set_ylabel('particle loss')

        freq_x = cal_freq_fft(turn.shape[0], 1, freqx[0], freqx[1])
        spec_x = cal_spctrum_fft(turn.shape[0], 1, freqx[0], freqx[1],
                                 xAverage)
        ax[0, 3].plot(freq_x, spec_x, label=particle, alpha=0.5)
        ax[0, 3].set_ylabel('Amplitude x')
        ax[0, 3].set_yscale('log')

        freq_y = cal_freq_fft(turn.shape[0], 1, freqy[0], freqy[1])
        spec_y = cal_spctrum_fft(turn.shape[0], 1, freqy[0], freqy[1],
                                 yAverage)
        ax[1, 3].plot(freq_y, spec_y, label=particle, alpha=0.5)
        ax[1, 3].set_ylabel('Amplitude y')
        ax[1, 3].set_yscale('log')

    if multiBunch:
        name_lumi = name_statistic + ('super period', )
        for i in range(3):
            turn, lumi = np.loadtxt(path_lumi[i],
                                    delimiter=',',
                                    skiprows=1,
                                    usecols=(0, 1),
                                    unpack=True)
            ax[2, 3].plot(turn, lumi, label=name_lumi[i], alpha=0.5)
            ax[2, 3].set_ylabel('Luminosity')
    else:
        turn, lumi = np.loadtxt(path_lumi[0],
                                delimiter=',',
                                skiprows=1,
                                usecols=(0, 1),
                                unpack=True)
        ax[2, 3].plot(turn, lumi, alpha=1)
        ax[2, 3].set_ylabel('Luminosity')

    for i in range(row):
        for j in range(col):
            ax[i, j].grid()

            if (not multiBunch) and i == 2 and j == 3:
                # 单束团时只画单个亮度，不输出图例
                pass
            else:
                ax[i, j].legend()

    savename = path_statistic[0].replace('csv', 'png')
    savename = savename.replace(name_statistic[0], 'figure')
    fig.suptitle(path_statistic[0] + '\n' + path_statistic[1] + '\n' + note)

    plt.subplots_adjust(left=0.08, bottom=0.04, right=0.95, top=0.88)
    # plt.subplots_adjust(left=0.045, bottom=0.04, right=0.99, top=0.88)
    # ax[3, 3].set_visible(False)
    if save:
        plt.savefig(savename)
    plt.show()


if __name__ == '__main__':
    statistic_file = (
        r'D:\OneDrive\研究生\博二\2021_06_宏粒子数对EicC模拟结果影响比较\1021_54_proton_bunch0.csv',
        r'D:\OneDrive\研究生\博二\2021_06_宏粒子数对EicC模拟结果影响比较\1021_54_electron_bunch0.csv'
    )
    luminosity_file = (
        r'D:\OneDrive\研究生\博二\2021_06_宏粒子数对EicC模拟结果影响比较\1021_54_luminosity_proton_10000turns.csv',
        r'D:\OneDrive\研究生\博二\2021_06_宏粒子数对EicC模拟结果影响比较\1021_54_luminosity_electron_10000turns.csv',
        r'D:\OneDrive\研究生\博二\2021_06_宏粒子数对EicC模拟结果影响比较\1021_54_luminosity_suPeriod_10000turns.csv'
    )
    plot_statistic(
        ('proton', 'electron'),
        statistic_file,
        luminosity_file,
        save=True,
        multiBunch=False,
        note=
        r'$\nu_p = ({0},{1}), \nu_e = ({2},{3})$, macro particles = $5\times 10^{4}$'
        .format(0.315, 0.3, 0.58, 0.55, 7))
