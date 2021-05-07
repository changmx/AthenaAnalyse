from plot_resonance import plot_resonanceDiagram_color
import matplotlib.pyplot as plt
import numpy as np


def plot_tuneSpread(path,
                    ax,
                    resonanceOrder,
                    xlim=[0, 1],
                    ylim=[0, 1],
                    resonanceKind='all'):

    phaseX, phaseY, nuX, nuY, tag = np.loadtxt(path,
                                               delimiter=',',
                                               skiprows=1,
                                               usecols=(0, 1, 2, 3, 4),
                                               unpack=True)
    l_nuX = list(nuX)
    l_nuY = list(nuY)

    delete_number = 0  # 把数组转化为列表来删除元素时，每删除一个元素，被删除元素后面的所有元素下标都会减一，因此用这个参数来表示删除元素后其他元素下标的变化
    for i in range(len(tag)):  # 删除列表中的元素
        if tag[i] < 0:
            # print(i, len((tag)))
            del l_nuX[i - delete_number]
            del l_nuY[i - delete_number]
            delete_number += 1

    ax.scatter(l_nuX, l_nuY, alpha=0.2, s=2, color='red')

    plot_resonanceDiagram_color(resonanceOrder, ax, xlim, ylim, resonanceKind)


if __name__ == '__main__':

    fig, ax = plt.subplots()

    # path = r'E:\changmx\bb2019\statLumiPara\2020_1210\2133_01_electron_phase_2-10turn_10000'+'.csv'
    # path = r'E:\changmx\bb2021\linux\2021_0506\1e-1p-1slice-nohourglass\1100_29_electron_bunch0_phase_9000-10000turn_50000' + '.csv'
    # ax.scatter(0.67, 0.55, marker='+')
    # path = r'E:\changmx\bb2021\linux\2021_0506\1e-1p-1slice-nohourglass\1101_04_electron_bunch0_phase_9000-10000turn_50000' + '.csv'
    # ax.scatter(0.693, 0.55, marker='+')
    path = r'E:\changmx\bb2021\linux\2021_0506\1e-1p-1slice-nohourglass\1101_26_electron_bunch0_phase_9000-10000turn_50000' + '.csv'
    ax.scatter(0.74, 0.55, marker='+')

    plot_tuneSpread(path, ax, 3, resonanceKind='all')
    # ax.scatter(0.58, 0.55, marker='+')

    plt.show()
