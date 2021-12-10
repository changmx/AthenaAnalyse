from typing import ChainMap
import numpy as np
import matplotlib.pyplot as plt
import sys
import time


class TimeStat:
    def __init__(self) -> None:
        self.timeDict = {
            'total': {
                'start': 0,
                'end': 0,
                'running': 0
            },
            'stat': {
                'start': 0,
                'end': 0,
                'running': 0
            },
            'lumi': {
                'start': 0,
                'end': 0,
                'running': 0
            },
            'tune': {
                'start': 0,
                'end': 0,
                'running': 0
            },
            'dist': {
                'start': 0,
                'end': 0,
                'running': 0
            },
            'fma': {
                'start': 0,
                'end': 0,
                'running': 0
            }
        }

    def start(self, mykey):
        self.timeDict[mykey]['start'] = time.time()

    def end(self, mykey):
        self.timeDict[mykey]['end'] = time.time()
        self.timeDict[mykey]['running'] += self.timeDict[mykey][
            'end'] - self.timeDict[mykey]['start']
        # print(self.timeDict[mykey]['start'], self.timeDict[mykey]['end'],
        #       self.timeDict[mykey]['running'])

    def printTimeStat(self):
        for mykey in self.timeDict:
            mymin, mysec = divmod(self.timeDict[mykey]['running'], 60)
            if mykey == 'total':
                print('\n')
                print('{0:<10s}: {1:s}'.format(
                    'start',
                    time.asctime(time.localtime(
                        self.timeDict[mykey]['start']))))
                print('{0:<10s}: {1:s}'.format(
                    'end',
                    time.asctime(time.localtime(self.timeDict[mykey]['end']))))
            print('{0:<10s}: {1:<4.0f} min {2:<4.0f} sec'.format(
                mykey, mymin, mysec))


def myhexbin(ax,
             xArray,
             yArray,
             gridsize=100,
             scattersize=10,
             norm=None,
             cmap='viridis',
             alpha=1):
    if (np.size(xArray) != np.size(yArray)):
        print(
            'Error: the x and y arrays have different numbers of elements, x: {0}, y: {1}'
            .format(np.size(xArray), np.size(yArray)))
        sys.exit(1)

    if isinstance(gridsize, int):
        '''
        格点数目比网格数目多1，否则(xArray的最大值 - xmin) / dx的值恰好等于gridsize，数组索引会超限。
        '''
        nx = gridsize + 1
        ny = gridsize + 1
    elif isinstance(gridsize, tuple):
        nx = gridsize[0] + 1
        ny = gridsize[1] + 1
    else:
        print('Error: gridsize type should be int or tuple(nx,ny)')
        sys.exit(1)

    x = np.zeros(nx**2)
    y = np.zeros(ny**2)
    z = np.zeros((nx, ny))

    xmin = np.amin(xArray)
    ymin = np.amin(yArray)
    xmax = np.amax(xArray)
    ymax = np.amax(yArray)

    if xmax == xmin:
        xmin = xmin - (xmin - 0) * 0.2
        xmax = xmax + (1 - xmax) * 0.2
    if ymax == ymin:
        ymin = ymin - (ymin - 0) * 0.2
        ymax = ymax + (1 - ymax) * 0.2

    dx = (xmax - xmin) / gridsize
    dy = (ymax - ymin) / gridsize

    for id in range(np.size(xArray)):
        xindex = int((xArray[id] - xmin) / dx)
        yindex = int((yArray[id] - ymin) / dy)
        z[yindex, xindex] += 1

    # 构造一维数组
    for iy in range(nx):
        for ix in range(ny):
            offset = iy * nx + ix
            x[offset] = xmin + ix * dx
            y[offset] = ymin + iy * dy
    c = z.flatten()  # 把二维数组展开为一维数组

    he = ax.scatter(x,
                    y,
                    c=c,
                    alpha=alpha,
                    s=scattersize,
                    norm=norm,
                    cmap=cmap,
                    marker='H')

    return he


def plot_save_single_figure(ax, x, y, xlabel, ylabel, label=None, alpha=1, fontsize=10, figsize=(8, 6), isgrid=True, yscale='linear', dpi=300, **kwargs):

    ax.plot(x, y, label=label, alpha=alpha)

    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    ax.set_yscale(yscale)
    # plt.xticks(fontsize=fontsize)
    # plt.yticks(fontsize=fontsize)

    if label is not None:
        ax.legend(fontsize=fontsize)
    if isgrid:
        ax.grid()
    if 'ystyle' in kwargs:
        if kwargs['ystyle'] == 'sci':
            ax.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
    if 'xstyle' in kwargs:
        if kwargs['xstyle'] == 'sci':
            ax.ticklabel_format(axis='x', style='sci', scilimits=(0, 0))
    if 'vline' in kwargs:
        ax.axvline(x=kwargs['vline'], ymin=0, ymax=1,
                   color='red', linestyle="--")
if __name__ == '__main__':
    pass
