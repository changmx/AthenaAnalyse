from typing import ChainMap
import numpy as np
import matplotlib.pyplot as plt
import sys


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
    c = z.flatten() # 把二维数组展开为一维数组

    he = ax.scatter(x,
                    y,
                    c=c,
                    alpha=alpha,
                    s=scattersize,
                    norm=norm,
                    cmap=cmap,
                    marker='H')

    return he


if __name__ == '__main__':
    pass