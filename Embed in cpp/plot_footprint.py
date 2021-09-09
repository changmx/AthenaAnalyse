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
        self.savePath_dist_xpx = []
        self.savePath_dist_ypy = []
        self.savePath_dist_xy = []

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
                'figure_frequencyMap'
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

            savePath_dist_xpx = os.sep.join([
                self.home, 'statLumiPara', self.yearMonDay, self.hourMinSec,
                'figure_distribution', 'fixPoint',
                self.particle + '_bunch' + str(self.bunchid) + '_xpx'
            ])
            if not os.path.exists(savePath_dist_xpx):
                os.makedirs(savePath_dist_xpx)
            savePath_dist_xpx = os.sep.join([
                savePath_dist_xpx, self.hourMinSec + '_' + self.particle +
                '_bunch' + str(self.bunchid)
            ])
            self.savePath_dist_xpx.append(savePath_dist_xpx)

            savePath_dist_ypy = os.sep.join([
                self.home, 'statLumiPara', self.yearMonDay, self.hourMinSec,
                'figure_distribution', 'fixPoint',
                self.particle + '_bunch' + str(self.bunchid) + '_ypy'
            ])
            if not os.path.exists(savePath_dist_ypy):
                os.makedirs(savePath_dist_ypy)
            savePath_dist_ypy = os.sep.join([
                savePath_dist_ypy, self.hourMinSec + '_' + self.particle +
                '_bunch' + str(self.bunchid)
            ])
            self.savePath_dist_ypy.append(savePath_dist_ypy)

            savePath_dist_xy = os.sep.join([
                self.home, 'statLumiPara', self.yearMonDay, self.hourMinSec,
                'figure_distribution', 'fixPoint',
                self.particle + '_bunch' + str(self.bunchid) + '_xy'
            ])
            if not os.path.exists(savePath_dist_xy):
                os.makedirs(savePath_dist_xy)
            savePath_dist_xy = os.sep.join([
                savePath_dist_xy, self.hourMinSec + '_' + self.particle +
                '_bunch' + str(self.bunchid)
            ])
            self.savePath_dist_xy.append(savePath_dist_xy)

            # savePath_aper = os.sep.join([
            #     self.home, 'statLumiPara', self.yearMonDay, self.hourMinSec,
            #     'figure_dynamicAperture'
            # ])
            # if not os.path.exists(savePath_aper):
            #     os.makedirs(savePath_aper)
            # savePath_aper = os.sep.join([
            #     savePath_aper, self.hourMinSec + '_fma_' + self.particle +
            #     "_bunch" + str(self.bunchid) + '_' + str(self.npoint) +
            #     'points_' + self.turnUnit + '_' + str(self.startTurn[i]) +
            #     '-' + str(self.endTurn[i])
            # ])
            # self.savePath_aper.append(savePath_aper)

    def load_plot_save(self, para, myfigsize, myfontsize, myscattersize=1):

        self.isxConjugate = False if para.nux <= 0.5 else True
        self.isyConjugate = False if para.nuy <= 0.5 else True

        for i in range(len(self.file)):

            turn, x, px, y, py, z, pz, tag = np.loadtxt(self.file[i],
                                                        delimiter=',',
                                                        skiprows=1,
                                                        usecols=(0, 1, 2, 3, 4,
                                                                 5, 6, 7),
                                                        unpack=True)
            self.plot_fix_distribution_perturn(i, para, turn, x, px, y, py, z,
                                               pz, tag)
            self.plot_fma(i, para, x, px, y, py, z, tag, myfigsize, myfontsize,
                          myscattersize)

            print('File has been drawn: {0}'.format(self.file[i]))

    def plot_fma(self,
                 i,
                 para,
                 x,
                 px,
                 y,
                 py,
                 z,
                 tag,
                 myfigsize,
                 myfontsize,
                 myscattersize=1):
        fig_fma, ax_fma = plt.subplots(figsize=myfigsize)
        plt.xticks(fontsize=myfontsize)
        plt.yticks(fontsize=myfontsize)
        plt.subplots_adjust(left=0.17, right=0.96, top=0.95, bottom=0.12)
        nuxArray = []
        nuyArray = []
        nuzArray = []
        diffusion_xyArray = []

        xArray = []
        yArray = []

        for ix in range(para.fixNx):
            for iy in range(para.fixNy):
                for iz in range(para.fixNz):
                    index = ix * para.fixNy * para.fixNz + iy * para.fixNz + iz
                    # if (index > 0 and index % 100 == 0):
                    #     print('Reading fixPoint[{0}]'.format(index))
                    isExist, nux, nuy, nuz, diffusion_xy, diffusion_xyz, x0, y0, diffusion_aper = cal_fma_aper(
                        para, index + 1, self.npoint,
                        self.endTurn[i] - self.startTurn[i] + 1,
                        self.isxConjugate, self.isyConjugate, x, px, y, py, z,
                        tag)
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

    def plot_fix_distribution_perturn(self, fileid, para, turnArray, xArray,
                                      pxArray, yArray, pyArray, zArray,
                                      pzArray, tagArray):
        totalPoint = para.fixNx * para.fixNy * para.fixNz
        totalTurn = int(len(turnArray) / totalPoint)

        fig_xpx_dist, ax_xpx_dist = plt.subplots()
        plt.subplots_adjust(left=0.15)
        fig_ypy_dist, ax_ypy_dist = plt.subplots()
        plt.subplots_adjust(left=0.15)
        fig_xy_dist, ax_xy_dist = plt.subplots()
        plt.subplots_adjust(left=0.15)
        fig_z_dist, ax_z_dist = plt.subplots()
        plt.subplots_adjust(left=0.15)

        unitConvert = 1e3

        # xmin = para.fixXStart * para.fixXStep * para.sigmax * 1.2 * unitConvert
        # xmax = para.fixXEnd * para.fixXStep * para.sigmax * 1.2 * unitConvert
        # ymin = para.fixYStart * para.fixYStep * para.sigmay * 1.2 * unitConvert
        # ymax = para.fixYEnd * para.fixYStep * para.sigmay * 1.2 * unitConvert
        # pxmin = -1 * para.sigmapx * 5 * unitConvert
        # pxmax = para.sigmapx * 5 * unitConvert
        # pymin = -1 * para.sigmapy * 5 * unitConvert
        # pymax = para.sigmapy * 5 * unitConvert
        xmax = np.amax(xArray) * 1.2 * unitConvert
        xmin = np.amin(xArray) * 1.2 * unitConvert
        ymax = np.amax(yArray) * 1.2 * unitConvert
        ymin = np.amin(yArray) * 1.2 * unitConvert
        pxmin = np.amax(pxArray) * 1.2 * unitConvert
        pxmax = np.amin(pxArray) * 1.2 * unitConvert
        pymin = np.amax(pyArray) * 1.2 * unitConvert
        pymax = np.amin(pyArray) * 1.2 * unitConvert

        for i in range(totalTurn):
            turn = turnArray[i * totalPoint]
            x = xArray[i * totalPoint:(i + 1) * totalPoint]
            px = pxArray[i * totalPoint:(i + 1) * totalPoint]
            y = yArray[i * totalPoint:(i + 1) * totalPoint]
            py = pyArray[i * totalPoint:(i + 1) * totalPoint]
            z = zArray[i * totalPoint:(i + 1) * totalPoint]
            pz = pzArray[i * totalPoint:(i + 1) * totalPoint]

            ax_xpx_dist.scatter(x * unitConvert,
                                px * unitConvert,
                                color='tab:blue',
                                s=1)
            ax_ypy_dist.scatter(y * unitConvert,
                                py * unitConvert,
                                color='tab:blue',
                                s=1)
            ax_xy_dist.scatter(x * unitConvert,
                               y * unitConvert,
                               color='tab:blue',
                               s=1)

            ax_xpx_dist.set_xlabel('x(mm)')
            ax_xpx_dist.set_ylabel(r'$\rm x^{\prime}$(mrad)')
            ax_xpx_dist.set_xlim(xmin, xmax)
            ax_xpx_dist.set_ylim(pxmin, pxmax)

            ax_ypy_dist.set_xlabel('y(mm)')
            ax_ypy_dist.set_ylabel(r'$\rm y^{\prime}$(mrad)')
            ax_ypy_dist.set_xlim(ymin, ymax)
            ax_ypy_dist.set_ylim(pymin, pymax)

            ax_xy_dist.set_xlabel('x(mm)')
            ax_xy_dist.set_ylabel('y(mm)')
            ax_xy_dist.set_xlim(xmin, xmax)
            ax_xy_dist.set_ylim(ymin, ymax)

            ax_xpx_dist.set_title('turn ' + str(int(turn)))
            ax_ypy_dist.set_title('turn ' + str(int(turn)))
            ax_xy_dist.set_title('turn ' + str(int(turn)))

            fig_xpx_dist.savefig(self.savePath_dist_xpx[fileid] + "_xpx_" +
                                 str(int(turn)) + '.png',
                                 dpi=150)
            fig_ypy_dist.savefig(self.savePath_dist_ypy[fileid] + "_ypy_" +
                                 str(int(turn)) + '.png',
                                 dpi=150)
            fig_xy_dist.savefig(self.savePath_dist_xy[fileid] + "_xy_" +
                                str(int(turn)) + '.png',
                                dpi=150)

            ax_xpx_dist.cla()
            ax_ypy_dist.cla()
            ax_xy_dist.cla()

    def plot_DA(self,
                para,
                turn,
                x,
                px,
                y,
                py,
                z,
                pz,
                tag,
                myfigsize,
                myfontsize,
                myscattersize=1):
        abc = 'abc'
        # fig_aper, ax_aper = plt.subplots(figsize=myfigsize)
        # plt.xticks(fontsize=myfontsize)
        # plt.yticks(fontsize=myfontsize)

        # xArray = []
        # yArray = []
        # diffusion_xyzArray = []

        # diffusion_xyArray_aper = np.zeros((para.fixNy, para.fixNx))
        # diffusion_xyArray_aper = []

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


if __name__ == '__main__':
    home = 'D:\\bb2021'
    yearMonDay = '2021_0906'
    hourMinSec = '1806_01'
    # yearMonDay = '2021_0907'
    # hourMinSec = '1201_12'
