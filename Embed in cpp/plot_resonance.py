import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib import rcParams, cycler
from matplotlib.patches import Patch


def Farey(n):
    # Return the nth Farey sequence, ascending.
    seq = [[0, 1]]
    a, b, c, d = 0, 1, 1, n
    while c <= n:
        k = int((n + b) / d)
        a, b, c, d = c, d, k * c - a, k * d - b
        # seq.append([a,b])
        seq.append([a, b])

    return seq


def plot_resonanceDiagram_all(order, col='b', kind='all'):

    fig, ax = plt.subplots()
    ax.set_ylim(0, 1)
    ax.set_xlim(0, 1)
    x = np.linspace(0, 1, 2)
    FN = Farey(order)
    # print(FN)
    for f in FN:
        h, k = f  # Node h/k on the axes
        for sf in FN:
            p, q = sf
            c = float(p * h)
            a = float(k * p)  # Resonance line a Qx + bQy = c linked to p/q
            b = float(q - k * p)
            if a > 0:
                if kind == 'all' or kind == 'sum':
                    ax.plot(x, c / a - x * b / a, color=col)
                    ax.plot(c / a - x * b / a, x, color=col)
                    ax.plot(c / a + x * b / a, 1 - x, color=col)
                if kind == 'all' or kind == 'diff':
                    ax.plot(x, c / a + x * b / a, color=col)
                    ax.plot(c / a + x * b / a, x, color=col)
                    ax.plot(c / a - x * b / a, 1 - x, color=col)

            if q == k and p == 1:  # FN elements below 1/k
                break

    # ax.scatter(0.315,0.3,c='r')
    plt.show()


def plot_resonanceDiagram_one(ax, order, col, repeatLine, legend, kind='all'):
    # 绘制某一阶数的共振线
    FN = Farey(order)
    # print(FN)
    for f in FN:
        h, k = f  # Node h/k on the axes
        for sf in FN:
            p, q = sf
            c = float(p * h)
            a = float(k * p)  # # Resonance line a Qx + bQy = c linked to p/q
            b = float(q - k * p)
            if a > 0:
                if kind == 'all' or kind == 'sum':
                    coord = [[0, 1],
                             [c / a - 0 * b / a,
                              c / a - 1 * b / a]]  # 两点确定一条直线，确定两个点的横纵坐标
                    # print('one',coord)
                    if coord not in repeatLine:  # 如果这条线的数据在列表中不存在，说明之前没有画过这条线
                        ax.plot(coord[0], coord[1], color=col)
                        repeatLine.append(coord)  # 画之，并添加到列表中，下次不再画这条线

                    coord = [[c / a - 0 * b / a, c / a - 1 * b / a], [0, 1]]
                    if coord not in repeatLine:
                        ax.plot(coord[0], coord[1], color=col)
                        repeatLine.append(coord)

                    coord = [[c / a + 0 * b / a, c / a + 1 * b / a], [1, 0]]
                    if coord not in repeatLine:
                        ax.plot(coord[0], coord[1], color=col)
                        repeatLine.append(coord)

                if kind == 'all' or kind == 'diff':
                    coord = [[0, 1], [c / a + 0 * b / a, c / a + 1 * b / a]]
                    if coord not in repeatLine:
                        ax.plot(coord[0], coord[1], color=col)
                        repeatLine.append(coord)

                    coord = [[c / a + 0 * b / a, c / a + 1 * b / a], [0, 1]]
                    if coord not in repeatLine:
                        ax.plot(coord[0], coord[1], color=col)
                        repeatLine.append(coord)

                    coord = [[c / a - 0 * b / a, c / a - 1 * b / a], [1, 0]]
                    if coord not in repeatLine:
                        ax.plot(coord[0], coord[1], color=col)
                        repeatLine.append(coord)

            if q == k and p == 1:  # FN elements below 1/k
                break
    legend.append(
        Line2D([0], [0], color=col, lw=4,
               label=str(order) + '-order'))  # 添加这条线的图例


def plot_resonanceDiagram_oneByOne(order,
                                   xlim=[0, 1],
                                   ylim=[0, 1],
                                   kind='all'):

    fig, ax = plt.subplots()
    ax.set_xlim(xlim[0], xlim[1])
    ax.set_ylim(ylim[0], ylim[1])
    x = [0, 1]
    repeatLine = []  # 保存已经画过的线的列表
    legend_elements = []  # 保存各个阶数图例的列表
    col = [
        'midnightblue', 'mediumblue', 'crimson', 'darkorange', 'violet',
        'skyblue', 'deepskyblue', 'steelblue', 'lightblue', 'aliceblue'
    ]  # 各个阶数共振线的颜色
    # col = ['b','b','b','b','b','b','b','b','b','b']

    for i in range(1, order + 1, 1):
        plot_resonanceDiagram_one(ax, i, col[i - 1], repeatLine,
                                  legend_elements, kind)

    ax.scatter(0.315, 0.3, marker='x', c='r')
    ax.scatter(0.58, 0.55, marker='x', c='r')
    ax.legend(handles=legend_elements, loc='upper right')
    plt.show()


def plot_resonanceDiagram_color(order,
                                ax,
                                xlim=[0, 1],
                                ylim=[0, 1],
                                kind='all'):

    ax.set_xlim(xlim[0], xlim[1])
    ax.set_ylim(ylim[0], ylim[1])
    x = [0, 1]
    repeatLine = []  # 保存已经画过的线的列表
    legend_elements = []  # 保存各个阶数图例的列表

    # 各个阶数共振线的颜色
    col = [
        'midnightblue', 'black', 'tab:orange', 'tab:green', 'tab:red',
        'tab:purple', 'tab:blue', 'tab:pink', 'tab:gray', 'tab:cyan'
    ]
    # col = [
    #     'midnightblue', 'black', 'gold', 'crimson', 'darkorange', 'mediumblue',
    #     'violet', 'deepskyblue', 'darkgreen', 'maroon'
    # ]
    # col = ['b','b','b','b','b','b','b','b','b','b']

    for i in range(1, order + 1, 1):
        plot_resonanceDiagram_one(ax, i, col[i - 1], repeatLine,
                                  legend_elements, kind)

    # ax.scatter(0.315,0.3,marker='x',c='r')
    # ax.scatter(0.58,0.55,marker='x',c='r')
    ax.legend(handles=legend_elements, loc='upper right')


if __name__ == '__main__':

    plot_resonanceDiagram_all(order=12, col='royalblue', kind='all')
    plot_resonanceDiagram_oneByOne(order=8,
                                   xlim=[0, 1],
                                   ylim=[0, 1],
                                   kind='all')
    # plot_resonanceDiagram_oneByOne(order=10,xlim=[0.27,0.35],ylim=[0.27,0.35])
