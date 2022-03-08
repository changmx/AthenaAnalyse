'''
Author: your name
Date: 2022-03-07 08:45:46
LastEditTime: 2022-03-07 19:23:41
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \AthenaAnalyse\DataAnalyse\plot_bblimit_compensate.py
'''
from cProfile import label
from turtle import color
import numpy as np
import matplotlib.pyplot as plt


def plot_resonance_region(ax):
    x = np.arange(0, 200, 1)
    y1 = -1.4 * x + 150
    y2 = -1.4 * x + 120

    ax.fill_between(x, y1, y2, alpha=0.5, linewidth=0)
    # ax.plot(x, y1)


def plot_axis(ax):
    # 给x和y轴加箭头
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

    # 隐藏图的上x轴和右y轴
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # 隐藏坐标轴的刻度
    ax.set_xticks([])
    ax.set_yticks([])


def plot_text(ax, x, y, text, rotation=0, fontsize=12, color='black'):
    ax.text(x, y, text, fontsize=fontsize, rotation=rotation, color=color)


def plot_array(ax, target, start, arrayColor='black', arrayAlpha=1):
    ax.annotate('',
                xy=target,
                xycoords='data',
                xytext=start,
                textcoords='data',
                arrowprops=dict(arrowstyle="->",
                                color=arrayColor,
                                alpha=arrayAlpha))


if __name__ == '__main__':

    myfontsize = 12
    fig, ax = plt.subplots()

    ax.set_xlabel(r'$\nu_e$', loc='right', fontsize=myfontsize)
    ax.set_ylabel(r'$\nu_p^{eff}$', loc='top', fontsize=myfontsize)

    ax.set_xlim((0, 200))
    ax.set_ylim((0, 200))

    # ax.scatter(126, 65, c='black', marker='x', label='(0.58, 0.315)')
    # ax.scatter(198, 65, c='tab:red', marker='x')
    # ax.scatter(126, 155, c='tab:green', marker='x')
    plot_text(ax, 124, 63, r'$\nu_1$', fontsize=10, color='black')
    plot_text(ax, 49, 63, r'$\nu_2$', fontsize=10, color='black')
    plot_text(ax, 196, 63, r'$\nu_3$', fontsize=10, color='tab:red')
    plot_text(ax, 124, 153, r'$\nu_4$', fontsize=10, color='tab:green')
    plot_text(ax, 49, 153, r'$\nu_5$', fontsize=10, color='black')
    # plot_text(ax, 110, 50, r'(0.58, 0.315)', color='tab:orange')

    plot_resonance_region(ax)
    plot_axis(ax)

    plot_text(ax, x=15, y=20, text='resonance region', rotation=-47)

    plot_array(ax, (55, 65), (123, 65), arrayColor='tab:blue', arrayAlpha=1)
    plot_text(ax, x=59, y=70, text='intensity decrease', color='black')

    plot_array(ax, (129, 68), (195, 68), arrayColor='tab:red')
    plot_array(ax, (195, 62), (129.8, 62), arrayColor='tab:red')

    plot_text(ax, x=132, y=73, text='intensity decrease')
    plot_text(ax, x=135, y=52, text=r'compensating $\nu_e$')

    plot_array(ax, (126.3, 151), (126.3, 70), arrayColor='tab:green')
    plot_array(ax, (55, 154), (123, 154), arrayColor='tab:green')

    plot_text(ax, x=59, y=159, text='intensity decrease')
    plot_text(ax, x=132, y=120, text=r'compensating $\nu_p^{eff}$')

    # plt.legend(fontsize=myfontsize, framealpha=0)
    plt.savefig(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\bblimit_compensate.png',
        dpi=300)

    # plt.show()