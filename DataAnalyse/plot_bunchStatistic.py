import numpy as np
import matplotlib.pyplot as plt


def plot_statistic(name_statistic,
                   path_statistic,
                   path_lumi,
                   save=False,
                   note=''):
    row = 4
    col = 4
    fig, ax = plt.subplots(row, col, figsize=(20, 10))

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

    name_lumi = name_statistic + ('super period', )
    for i in range(3):
        turn, lumi = np.loadtxt(path_lumi[i],
                                delimiter=',',
                                skiprows=1,
                                usecols=(0, 1),
                                unpack=True)
        ax[3, i].plot(turn, lumi, label=name_lumi[i])
        ax[3, i].set_ylabel('Luminosity')

    for i in range(row):
        for j in range(col):
            ax[i, j].grid()
            ax[i, j].legend()

    savename = path_statistic[0].replace('csv', 'png')
    savename = savename.replace(name_statistic[0], 'figure')
    fig.suptitle(path_statistic[0] + '\n' + path_statistic[1] + '\n' + note)

    plt.subplots_adjust(left=0.045, bottom=0.04, right=0.99, top=0.88)
    # ax[3, 3].set_visible(False)
    if save:
        plt.savefig(savename)
    plt.show()


if __name__ == '__main__':
    plot_statistic(('proton', 'electron'), (
        r'E:\changmx\bb2021\linux\2021_0508\1e-1p-1slice\1740_38_proton_bunch0.csv',
        r'E:\changmx\bb2021\linux\2021_0508\1e-1p-1slice\1740_38_electron_bunch0.csv'
    ), (r'E:\changmx\bb2021\linux\2021_0508\1e-1p-1slice\1740_38_luminosity_electron_10000turns.csv',
        r'E:\changmx\bb2021\linux\2021_0508\1e-1p-1slice\1740_38_luminosity_proton_10000turns.csv',
        r'E:\changmx\bb2021\linux\2021_0508\1e-1p-1slice\1740_38_luminosity_suPeriod_10000turns.csv'
        ),
                   save=True,
                   note=r'$(nu_x^e,nu_x^p)=({0},{1})$'.format(0.74, 0.25))
