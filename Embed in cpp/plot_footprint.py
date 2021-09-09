import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import re
import PyNAFF as pnf


class FootPrint:
    '''
    Load fixed particles coord and plot frequency map analyse
    '''
    def __init__(self,
                 home,
                 yearMonDay,
                 hourMinSec,
                 particle,
                 bunchid,
                 dist='gaussian') -> None:
        self.home = home
        self.yearMonDay = yearMonDay
        self.hourMinSec = hourMinSec
        self.particle = particle
        self.bunchid = bunchid
        self.dist = dist
        self.bunchLabel = self.particle + " bunch" + str(bunchid)

        self.file = self.hourMinSec + '_' + self.dist + '_' + self.particle + '_bunch' + str(
            bunchid)
        self.file = os.sep.join([
            self.home, 'distribution', self.yearMonDay, self.hourMinSec,
            'fixPoint', self.file
        ])
        self.file = glob.glob(self.file + '*')

        self.startTurn = []
        self.endTurn = []
        self.turnUnit = ''
        self.npoint = 0
        self.isExist = []
        self.savePath_fma = []
        self.savePath_aper = []

        for i in range(len(self.file)):
            matchObj = re.match(
                r'(.*)bunch([0-9]*)_([0-9]*)points_([a-zA-Z]*)_([0-9]*)-([0-9]*).csv',
                self.file[i])
            self.npoint = int(matchObj.group(3))
            self.turnUnit = matchObj.group(4)
            self.startTurn.append(int(matchObj.group(5)))
            self.endTurn.append(int(matchObj.group(6)))

            savePath_fma = os.sep.join([
                self.home, 'statLumiPara', self.yearMonDay, self.hourMinSec,
                'figure_footprint'
            ])
            if not os.path.exists(savePath_fma):
                os.makedirs(savePath_fma)
            savePath_fma = os.sep.join([
                savePath_fma, self.hourMinSec + '_fma_' + self.particle +
                "_bunch" + str(self.bunchid) + '_' + str(self.npoint) +
                'points_' + self.turnUnit + '_' + str(self.startTurn[i]) +
                '-' + str(self.endTurn[i])
            ])
            self.savePath_fma.append(savePath_fma)

            savePath_aper = os.sep.join([
                self.home, 'statLumiPara', self.yearMonDay, self.hourMinSec,
                'figure_dynamicAperture'
            ])
            if not os.path.exists(savePath_aper):
                os.makedirs(savePath_aper)
            savePath_aper = os.sep.join([
                savePath_aper, self.hourMinSec + '_fma_' + self.particle +
                "_bunch" + str(self.bunchid) + '_' + str(self.npoint) +
                'points_' + self.turnUnit + '_' + str(self.startTurn[i]) +
                '-' + str(self.endTurn[i])
            ])
            self.savePath_aper.append(savePath_aper)

    def load_plot_save(self, para, myfigsize, myfontsize, myscattersize=1):

        isxConjugate = False if para.nux <= 0.5 else True
        isyConjugate = False if para.nuy <= 0.5 else True

        for i in range(len(self.file)):
            fig_fma, ax_fma = plt.subplots(figsize=myfigsize)
            plt.xticks(fontsize=myfontsize)
            plt.yticks(fontsize=myfontsize)
            plt.subplots_adjust(left=0.17, right=0.96, top=0.95, bottom=0.12)
            # fig_aper, ax_aper = plt.subplots(figsize=myfigsize)
            # plt.xticks(fontsize=myfontsize)
            # plt.yticks(fontsize=myfontsize)

            turn, x, px, y, py, z, pz, tag = np.loadtxt(self.file[i],
                                                        delimiter=',',
                                                        skiprows=1,
                                                        usecols=(0, 1, 2, 3, 4,
                                                                 5, 6, 7),
                                                        unpack=True)
            plot_fix_distribution_perturn(para, turn, x, px, y, py, z, pz, tag)
            nuxArray = []
            nuyArray = []
            nuzArray = []
            diffusion_xyArray = []
            # xArray = []
            # yArray = []
            # diffusion_xyzArray = []

            # diffusion_xyArray_aper = np.zeros((para.fixNy, para.fixNx))
            # diffusion_xyArray_aper = []

            for ix in range(para.fixNx):
                for iy in range(para.fixNy):
                    for iz in range(para.fixNz):
                        index = ix * para.fixNy * para.fixNz + iy * para.fixNz + iz
                        if (index > 0 and index % 100 == 0):
                            print('Reading fixPoint[{0}]'.format(index))
                        isExist, nux, nuy, nuz, diffusion_xy, diffusion_xyz, x0, y0, diffusion_aper = cal_fma_aper(
                            para, index + 1, self.npoint,
                            self.endTurn[i] - self.startTurn[i] + 1,
                            isxConjugate, isyConjugate, x, px, y, py, z, tag)
                        if isExist:
                            nuxArray.append(nux[0])
                            nuyArray.append(nuy[0])
                            nuzArray.append(nuz[0])
                            diffusion_xyArray.append(diffusion_xy)
                            # diffusion_xyzArray.append(diffusion_xyz)
                            # xArray.append(x0)
                            # yArray.append(y0)
                            # diffusion_xyArray_aper.append(diffusion_aper)
                            # diffusion_xyArray_aper[iy, ix] = diffusion_aper

            sc_fma = ax_fma.scatter(nuxArray,
                                    nuyArray,
                                    c=diffusion_xyArray,
                                    s=myscattersize,
                                    norm=matplotlib.colors.LogNorm(),
                                    cmap='rainbow')
            ax_fma.set_xlabel('Horizontal tune', fontsize=myfontsize)
            ax_fma.set_ylabel('Vertical tune', fontsize=myfontsize)
            cbar_fma = fig_fma.colorbar(sc_fma)
            cbar_fma.ax.tick_params(labelsize=myfontsize)
            # cbar_fma.set_label('Tune diffusion', fontsize=myfontsize)
            ax_fma.scatter(para.nux, para.nuy, marker='x', c='tab:red')
            fig_fma.savefig(self.savePath_fma[i], dpi=300)
            # fig_fma.show()
            plt.close(fig_fma)

            # # print(xArray)
            # # print(yArray)
            # # print(diffusion_xyArray_aper)
            # # xArray *= 1e3
            # # yArray *= 1e3
            # sc_aper = ax_aper.scatter(xArray,
            #                           yArray,
            #                           c=diffusion_xyArray_aper,
            #                           s=40,
            #                           alpha=0.6,
            #                           norm=matplotlib.colors.LogNorm(),
            #                           cmap='viridis')
            # # ax_aper.set_xlabel('x(mm)', fontsize=myfontsize)
            # # ax_aper.set_ylabel('y(mm)', fontsize=myfontsize)
            # cbar_aper = fig_aper.colorbar(sc_aper)
            # cbar_aper.ax.tick_params(labelsize=myfontsize)
            # fig_aper.savefig(self.savePath_aper[i], dpi=300)

            # x_aper = [
            #     tmp * para.fixXStep
            #     for tmp in np.arange(para.fixXStart, para.fixXEnd)
            # ]
            # y_aper = [
            #     tmp * para.fixYStep
            #     for tmp in np.arange(para.fixYStart, para.fixYEnd)
            # ]
            # pcm = ax_aper.pcolormesh(x_aper,
            #                          y_aper,
            #                          diffusion_xyArray_aper,
            #                          shading='auto',
            #                          cmap='viridis')
            # fig_aper.colorbar(pcm, ax=ax_aper)
            # plt.show()
            # plt.close(fig_aper)

            print('File has been drawn: {0}'.format(self.file[i]))


def cal_fma_aper(para, tagid, totalPoints, totalTurns, isxConjugate,
                 isyConjugate, xArray, pxArray, yArray, pyArray, zArray,
                 tagArray):
    '''
    Numerical Analysis of Fundamental Frequencies (NAFF) algorithm
    '''
    totalRows = totalPoints * totalTurns
    x = xArray[tagid - 1:totalRows:totalPoints]
    px = pxArray[tagid - 1:totalRows:totalPoints]
    y = yArray[tagid - 1:totalRows:totalPoints]
    py = pyArray[tagid - 1:totalRows:totalPoints]
    z = zArray[tagid - 1:totalRows:totalPoints]
    # print(z)
    tag = tagArray[tagid - 1:totalRows:totalPoints]

    isExist = True
    nux = [0, 0]
    nuy = [0, 0]
    nuz = [0, 0]
    diffusion_xy = 0
    diffusion_xyz = 0
    diffusion_xy_aper = 0

    x0 = 0
    y0 = 0

    for mytag in tag:
        if mytag <= 0:
            isExist = False

    half = int(totalTurns / 2)
    if isExist:
        # calculate fma
        nux[0] = pnf.naff(x[0:half], half, 1)[0][1]
        nuy[0] = pnf.naff(y[0:half], half, 1)[0][1]
        # nuz[0] = pnf.naff(z[0:half], half, 1)[0][1]
        nux[1] = pnf.naff(x[half:totalTurns], half, 1)[0][1]
        nuy[1] = pnf.naff(y[half:totalTurns], half, 1)[0][1]
        # nuz[1] = pnf.naff(z[half:totalTurns], half, 1)[0][1]

        if isxConjugate:
            nux[0] = 1 - nux[0]
            nux[1] = 1 - nux[1]
        if isyConjugate:
            nuy[0] = 1 - nuy[0]
            nuy[1] = 1 - nuy[1]

        dnux = np.abs(nux[0] - nux[1])
        dnuy = np.abs(nuy[0] - nuy[1])
        # dnuz = np.abs(nuz[0] - nuz[1])

        diffusion_xy = np.sqrt(dnux**2 + dnuy**2)
        # diffusion_xyz = np.sqrt(dnux**2 + dnuy**2 + dnuz**2)

        #calculate dynamic aperture
        # x0 = x[0]
        # y0 = y[0]
        # xmax = np.amax(x[1:])
        # xmin = np.amin(x[1:])
        # xmaxaper = xmax if xmax > abs(xmin) else xmin
        # xindex = np.argwhere(x == xmaxaper)
        # dx = (x[xindex] - x[0])

        # ymax = np.amax(y[1:])
        # ymin = np.amin(y[1:])
        # ymaxaper = ymax if ymax > abs(ymin) else ymin
        # yindex = np.argwhere(y == ymaxaper)
        # dy = (y[yindex] - y[0])
        # print(xindex, yindex)
        # diffusion_xy_aper = np.sqrt(dx**2 + dy**2)
        x0 = x[0]
        y0 = y[0]
        jx0 = cal_action_angle(x[0], px[0], para.alphax, para.betax)
        jx1 = cal_action_angle(x[-1], px[-1], para.alphax, para.betax)
        jy0 = cal_action_angle(y[0], py[0], para.alphay, para.betay)
        jy1 = cal_action_angle(y[-1], py[-1], para.alphay, para.betay)
        dx = (jx1 - jx0) / totalTurns
        dy = (jy1 - jy0) / totalTurns
        diffusion_xy_aper = np.sqrt(dx**2 + dy**2)

    return isExist, nux, nuy, nuz, diffusion_xy, diffusion_xyz, x0, y0, diffusion_xy_aper


def cal_action_angle(u, pu, alpha, beta):
    gamma = (1 + alpha**2) / beta
    J = (gamma * u**2 + 2 * alpha * u * pu + beta * pu**2)
    return J


def plot_fix_distribution_perturn(para, turnArray, xArray, pxArray, yArray,
                                  pyArray, zArray, pzArray, tagArray):
    totalPoint = para.fixNx * para.fixNy * para.fixNz
    totalTurn = int(len(turnArray) / totalPoint)

    fig_x_dist, ax_x_dist = plt.subplots()
    fig_y_dist, ax_y_dist = plt.subplots()
    fig_z_dist, ax_z_dist = plt.subplots()
    for i in range(totalTurn):
        turn = turnArray[i * totalPoint]
        x = xArray[i * totalPoint:(i + 1) * totalPoint]
        px = pxArray[i * totalPoint:(i + 1) * totalPoint]
        y = yArray[i * totalPoint:(i + 1) * totalPoint]
        py = pyArray[i * totalPoint:(i + 1) * totalPoint]
        z = zArray[i * totalPoint:(i + 1) * totalPoint]
        pz = pzArray[i * totalPoint:(i + 1) * totalPoint]

        ax_x_dist.scatter(x, px, color='tab:blue', s=1)
        ax_y_dist.scatter(y, py, color='tab:blue', s=1)

        ax_x_dist.set_xlabel('x')
        ax_x_dist.set_ylabel('px')

        ax_y_dist.set_xlabel('y')
        ax_y_dist.set_ylabel('py')

        ax_x_dist.set_title('turn' + str(int(turn)))
        ax_y_dist.set_title('turn' + str(int(turn)))

        fig_x_dist.savefig(r'D:\bb2021\distribution\tmp\\' + str(int(turn)) +
                           '_x.png')
        fig_y_dist.savefig(r'D:\bb2021\distribution\tmp\\' + str(int(turn)) +
                           '_y.png')

        ax_x_dist.cla()
        ax_y_dist.cla()


if __name__ == '__main__':
    home = 'D:\\bb2021'
    yearMonDay = '2021_0906'
    hourMinSec = '1806_01'
    # yearMonDay = '2021_0907'
    # hourMinSec = '1201_12'

    p_footprint = FootPrint(home, yearMonDay, hourMinSec, 'proton', bunchid=0)
    e_footprint = FootPrint(home,
                            yearMonDay,
                            hourMinSec,
                            'electron',
                            bunchid=0)

    p_footprint.load_plot_save(1, (8, 6), 15)
    e_footprint.load_plot_save(1, (8, 6), 15)