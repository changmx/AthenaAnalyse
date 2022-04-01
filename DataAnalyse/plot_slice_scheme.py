import matplotlib.pyplot as plt
import numpy as np
import matplotlib.path as mpath
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
import matplotlib as mpl

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'


def arc_patch(ax,
              xy,
              width,
              height,
              theta1=0.,
              theta2=180.,
              resolution=50,
              color='tab:blue',
              alpha=1,
              zorder=10,
              **kwargs):

    # generate the points
    theta = np.linspace(np.radians(theta1), np.radians(theta2), resolution)
    points = np.vstack((width / 2 * np.cos(theta) + xy[0],
                        height / 2 * np.sin(theta) + xy[1]))
    # build the polygon and add it to the axes
    poly = mpatches.Polygon(points.T, closed=True, **kwargs)
    poly.set_facecolor(color)
    poly.set_alpha(alpha)
    poly.set_zorder(zorder)
    ax.add_patch(poly)


def plot_text(ax,
              x,
              y,
              text,
              rotation=0,
              fontsize=12,
              color='black',
              zorder=10):
    ax.text(x,
            y,
            text,
            fontsize=fontsize,
            rotation=rotation,
            color=color,
            zorder=zorder)


def plot_array(ax, target, start, arrayColor='black', arrayAlpha=1, zorder=10):
    ax.annotate('',
                xy=target,
                xycoords='data',
                xytext=start,
                textcoords='data',
                arrowprops=dict(arrowstyle="->",
                                color=arrayColor,
                                alpha=arrayAlpha),
                zorder=zorder)


def add_ellipse(ax,
                xy,
                width,
                height,
                facecolor='tab:blue',
                edgecolor='tab:blue',
                alpha=1,
                angle=0,
                zorder=10):
    ellipse = mpatches.Ellipse(xy,
                               width,
                               height,
                               angle,
                               edgecolor=edgecolor,
                               facecolor=facecolor,
                               alpha=alpha,
                               zorder=zorder)
    ax.add_patch(ellipse)
    # label(grid[4], "Ellipse")


def add_rectangle(ax,
                  xy,
                  width,
                  height,
                  angle=0,
                  color='tab:blue',
                  alpha=1,
                  zorder=10):
    x = xy[0] - width / 2
    y = xy[1] - height / 2
    rect = mpatches.Rectangle((x, y),
                              width,
                              height,
                              angle,
                              edgecolor=None,
                              facecolor=color,
                              alpha=alpha,
                              zorder=zorder)
    ax.add_patch(rect)


def add_arrow(ax, xy, targetxy, width, color='tab:blue', alpha=1, zorder=10):
    dx = targetxy[0] - xy[0]
    dy = targetxy[1] - xy[1]
    arrow = mpatches.Arrow(xy[0],
                           xy[1],
                           dx,
                           dy,
                           width=width,
                           edgecolor=None,
                           facecolor=color,
                           alpha=alpha,
                           zorder=zorder)
    ax.add_patch(arrow)


def add_arc(ax,
            xy,
            width,
            height,
            theta1,
            theta2,
            facecolor='tab:blue',
            edgecolor='tab:blue',
            alpha=1,
            angle=0,
            zorder=50):
    arc = mpatches.Arc(xy,
                       width,
                       height,
                       angle=angle,
                       theta1=theta1,
                       theta2=theta2,
                       color=facecolor,
                       edgecolor=edgecolor,
                       facecolor=facecolor,
                       alpha=alpha,
                       zorder=zorder)
    ax.add_artist(arc)
    arc.set_facecolor(3)


if __name__ == '__main__':

    fig, ax = plt.subplots(figsize=(6.4, 2.4))
    patches = []

    add_ellipse(ax, (0, 0),
                12,
                4,
                edgecolor='tab:orange',
                facecolor='none',
                alpha=1,
                zorder=20)
    add_ellipse(ax, (0, 0),
                20,
                4,
                edgecolor='tab:blue',
                facecolor='none',
                alpha=1,
                zorder=20)

    arc_patch(ax, (0, 0),
              width=12,
              height=4,
              theta1=-90,
              theta2=90,
              color='tab:orange',
              alpha=0.6,
              zorder=10)
    arc_patch(ax, (0, 0),
              width=20,
              height=4,
              theta1=90,
              theta2=270,
              color='tab:blue',
              alpha=0.6,
              zorder=10)

    slice_color = 'w'
    add_rectangle(ax, (1, 0), 3, 5, color=slice_color, alpha=1, zorder=15)
    add_rectangle(ax, (5, 0), 3, 5, color=slice_color, alpha=1, zorder=15)

    add_rectangle(ax, (-2, 0), 4, 5, color=slice_color, alpha=1, zorder=15)
    add_rectangle(ax, (-6, 0), 1, 5, color=slice_color, alpha=1, zorder=15)
    add_rectangle(ax, (-9, 0), 6, 5, color=slice_color, alpha=1, zorder=15)

    add_arrow(ax, (9, 5.2), (1, 5.2),
              width=2,
              color='tab:orange',
              alpha=0.6,
              zorder=11)
    add_arrow(ax, (-9, 5.2), (-1, 5.2),
              width=2,
              color='tab:blue',
              alpha=0.6,
              zorder=11)
    plot_text(ax, x=1, y=3.5, text='opposite slice')
    plot_text(ax, x=-6.8, y=3.5, text='forward slice')

    ax.vlines(x=-5.5,
              ymin=-6,
              ymax=3,
              linestyles='dashed',
              colors='tab:blue',
              zorder=20)
    ax.vlines(x=-4,
              ymin=-4,
              ymax=3,
              linestyles='dashed',
              colors='tab:blue',
              zorder=20)
    
    ax.vlines(x=3,
              ymin=-6,
              ymax=3,
              linestyles='dashed',
              colors='tab:orange',
              zorder=20)

    ax.vlines(x=-1.25,
              ymin=-6,
              ymax=3,
              linestyles='solid',
              colors='black',
              zorder=20)
    ax.vlines(x=-0.5,
              ymin=-4,
              ymax=3,
              linestyles='solid',
              colors='black',
              zorder=20)

    plot_array(ax, (-0.5, -3.2), (-4, -3.2), arrayColor='tab:blue')
    plot_array(ax, (-1.25, -5.5), (-5.5, -5.5), arrayColor='tab:blue')

    plot_array(ax, (-0.5, -3.2), (3, -3.2), arrayColor='tab:orange', zorder=30)
    plot_array(ax, (-1.25, -5.5), (3, -5.5),
               arrayColor='tab:orange',
               zorder=30)

    plot_text(ax, x=-0.25, y=-2.7, text=r'$s_{head}$', zorder=40)
    plot_text(ax, x=-1, y=-5, text=r'$s_{tail}$')

    ax.set_xlim((-12, 12))
    ax.set_ylim((-6, 6))

    ax.grid()
    plt.axis('off')

    plt.savefig(r'D:\OneDrive\模拟数据2\hourglass_scheme.png', dpi=300)
    plt.show()
