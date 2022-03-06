import numpy as np
import matplotlib.pyplot as plt


def plot_resonance_region(ax):
    x = np.arange(0, 200, 1)
    y1 = -1 * x + 130
    y2 = -1 * x + 100

    ax.fill_between(x, y1, y2, alpha=0.5, linewidth=0)
    # ax.plot(x, y1)


if __name__ == '__main__':

    fig, ax = plt.subplots()

    myfontsize = 12

    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    # ax.axis["x"].set_axisline_style("->", size = 1.0)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlabel(r'$\nu_e$', loc='right')
    ax.set_ylabel(r'$\nu_p^{eff}$', loc='top')

    ax.set_xticks([])
    ax.set_yticks([])

    ax.set_xlim((0, 200))
    ax.set_ylim((0, 200))

    plot_resonance_region(ax)

    plt.show()