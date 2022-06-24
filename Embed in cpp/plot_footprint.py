import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import re
import PyNAFF as pnf
import zipfile


class FootPrint:
    '''
    Load fixed particles coord and plot frequency map analyse
    '''

    def __init__(self,
                 home,
                 yearMonDay,
                 hourMinSec,
                 particle,
                 bunchidList,
                 nux,
                 nuy,
                 tuneshift_direction,
                 ncpu,
                 xlim=[0, 1],
                 ylim=[0, 1],
                 vmin=None,
                 vmax=None,
                 dist='gaussian') -> None:
        self.home = home
        self.yearMonDay = yearMonDay
        self.hourMinSec = hourMinSec
        self.particle = particle
        self.bunchidList = bunchidList
        self.nux = nux
        self.nuy = nuy
        self.tuneshift_direction = tuneshift_direction
        self.ncpu = ncpu
        self.xlim = xlim
        self.ylim = ylim
        self.vmin = vmin
        self.vmax = vmax
        self.dist = dist

        self.filePath = []
        self.savePath_fma = []
        self.savePath_dist_xpx = []
        self.savePath_dist_ypy = []
        self.savePath_dist_xy = []

        self.startTurn = []
        self.endTurn = []
        self.turnUnit = []
        self.npoint = []
        self.isExist = []

        for bunchid in self.bunchidList:
            filePath = self.hourMinSec + '_' + self.dist + '_' + self.particle + '_bunch' + str(
                bunchid)
            filePath = os.sep.join([
                self.home, 'distribution', self.yearMonDay, self.hourMinSec,
                'fixPoint', filePath
            ])
            filePath = glob.glob(filePath + '*')

            filePath.sort()

            for i in range(len(filePath)):
                if os.path.exists(filePath[i]):
                    matchObj = re.match(
                        r'(.*)bunch([0-9]*)_([0-9]*)points_([a-zA-Z]*)_([0-9]*)-([0-9]*).csv',
                        filePath[i])
                    npoint = int(matchObj.group(3))
                    turnUnit = matchObj.group(4)
                    startTurn = int(matchObj.group(5))
                    endTurn = int(matchObj.group(6))
                    self.npoint.append(npoint)
                    self.turnUnit.append(turnUnit)
                    self.startTurn.append(startTurn)
                    self.endTurn.append(endTurn)

                    self.filePath.append(filePath[i])

                    savePath_fma = os.sep.join([
                        self.home, 'statLumiPara', self.yearMonDay,
                        self.hourMinSec, 'figure_frequencyMap'
                    ])
                    if not os.path.exists(savePath_fma):
                        os.makedirs(savePath_fma)
                    savePath_fma = os.sep.join([
                        savePath_fma,
                        self.hourMinSec + '_fma_' + self.particle + "_bunch" +
                        str(bunchid) + '_' + str(npoint) + 'points_' +
                        turnUnit + '_' + str(startTurn) + '-' + str(endTurn)
                    ])
                    self.savePath_fma.append(savePath_fma)

                    savePath_dist_xpx = os.sep.join([
                        self.home, 'statLumiPara', self.yearMonDay,
                        self.hourMinSec, 'figure_distribution',
                        self.particle + '_bunch' + str(bunchid) + '_xpx'
                    ])
                    if not os.path.exists(savePath_dist_xpx):
                        os.makedirs(savePath_dist_xpx)
                    savePath_dist_xpx = os.sep.join([
                        savePath_dist_xpx, self.hourMinSec + '_' +
                        self.particle + '_bunch' + str(bunchid)
                    ])
                    self.savePath_dist_xpx.append(savePath_dist_xpx)

                    savePath_dist_ypy = os.sep.join([
                        self.home, 'statLumiPara', self.yearMonDay,
                        self.hourMinSec, 'figure_distribution',
                        self.particle + '_bunch' + str(bunchid) + '_ypy'
                    ])
                    if not os.path.exists(savePath_dist_ypy):
                        os.makedirs(savePath_dist_ypy)
                    savePath_dist_ypy = os.sep.join([
                        savePath_dist_ypy, self.hourMinSec + '_' +
                        self.particle + '_bunch' + str(bunchid)
                    ])
                    self.savePath_dist_ypy.append(savePath_dist_ypy)

                    savePath_dist_xy = os.sep.join([
                        self.home, 'statLumiPara', self.yearMonDay,
                        self.hourMinSec, 'figure_distribution',
                        self.particle + '_bunch' + str(bunchid) + '_xy'
                    ])
                    if not os.path.exists(savePath_dist_xy):
                        os.makedirs(savePath_dist_xy)
                    savePath_dist_xy = os.sep.join([
                        savePath_dist_xy, self.hourMinSec + '_' +
                        self.particle + '_bunch' + str(bunchid)
                    ])
                    self.savePath_dist_xy.append(savePath_dist_xy)

        # print(self.filePath)
        self.nfile = len(self.filePath)
        self.ntask = self.nfile if self.nfile < self.ncpu else self.ncpu
        print('{0:d} files will be drawn'.format(self.nfile))

    def get_phase_limit(self, para):

        self.isxConjugate = False if para.nux <= 0.5 else True
        self.isyConjugate = False if para.nuy <= 0.5 else True

        if self.xlim == [0, 1] or self.ylim == [
                0, 1
        ] or self.vmax == None or self.vmin == None:
            if len(self.filePath) > 0:

                print('Cal limit by file: ', self.filePath[0])

                nuxArray = []
                nuyArray = []
                diffusion_xyArray = []

                turn, x, px, y, py, z, pz, tag = np.loadtxt(self.filePath[0],
                                                            delimiter=',',
                                                            skiprows=1,
                                                            usecols=(0, 1, 2,
                                                                     3, 4, 5,
                                                                     6, 7),
                                                            unpack=True)
                for ix in range(para.fixNx):
                    for iy in range(para.fixNy):
                        for iz in range(para.fixNz):
                            index = ix * para.fixNy * para.fixNz + iy * para.fixNz + iz
                            # if (index > 0 and index % 100 == 0):
                            #     print('Reading fixPoint[{0}]'.format(index))
                            isExist, nux, nuy, diffusion_xy = cal_fma(
                                para, index + 1, self.npoint[0],
                                self.endTurn[0] - self.startTurn[0] + 1,
                                self.isxConjugate, self.isyConjugate, x, y,
                                tag)
                            if isExist:
                                nuxArray.append(nux)
                                nuyArray.append(nuy)
                                diffusion_xyArray.append(diffusion_xy)

                xmin = min(nuxArray)
                ymin = min(nuyArray)
                xmax = max(nuxArray)
                ymax = max(nuyArray)
                vmin = min(diffusion_xyArray)
                vmax = max(diffusion_xyArray)

                if xmax == xmin:
                    xmin = xmin - (xmin - 0) * 0.2
                    xmax = xmax + (1 - xmax) * 0.2
                if ymax == ymin:
                    ymin = ymin - (ymin - 0) * 0.2
                    ymax = ymax + (1 - ymax) * 0.2
                if vmax == vmin:
                    vmin = vmin * 0.5
                    vmax = vmax * 1.5

                if self.tuneshift_direction > 0:
                    xgap = abs(xmax - self.nux)
                    ygap = abs(ymax - self.nuy)
                    axmin = self.nux - xgap * 0.3
                    aymin = self.nuy - ygap * 0.3
                    axmax = xmax + xgap * 0.7
                    aymax = ymax + ygap * 0.7
                else:
                    xgap = abs(xmin - self.nux)
                    ygap = abs(ymin - self.nuy)
                    axmin = xmin - xgap * 0.3
                    aymin = ymin - ygap * 0.3
                    axmax = self.nux + xgap * 0.7
                    aymax = self.nuy + ygap * 0.7

                vgap = abs(vmax - vmin)
                avmin = vmin - vgap * 0.2
                avmax = vmax + vgap * 0.2

                axmin = np.floor(axmin * 1000) / 1000
                aymin = np.floor(aymin * 1000) / 1000
                axmax = np.ceil(axmax * 1000) / 1000
                aymax = np.ceil(aymax * 1000) / 1000
                avmin = np.floor(avmin * 10) / 10
                avmax = np.ceil(avmax * 10) / 10

                axmin = 0 if axmin < 0 else axmin
                aymin = 0 if aymin < 0 else aymin
                axmax = 1 if axmax > 1 else axmax
                aymax = 1 if aymax > 1 else aymax

                if self.xlim == [0, 1]:
                    self.xlim = [axmin, axmax]
                if self.ylim == [0, 1]:
                    self.ylim = [aymin, aymax]
                if self.vmin == None:
                    self.vmin = avmin
                if self.vmax == None:
                    self.vmax = avmax

        else:
            if self.xlim == [0, 1]:
                if self.nux > 0.5:
                    self.xlim[0] = 0.5
                else:
                    self.xlim[1] = 0.5
            if self.ylim == [0, 1]:
                if self.nuy > 0.5:
                    self.ylim[0] = 0.5
                else:
                    self.ylim[1] = 0.5

        print('xlim: ', self.xlim)
        print('ylim: ', self.ylim)
        print('vlim: ', self.vmin, self.vmax)

    def allocate_phase_file(self):
        self.fileIndex = []
        for i in range(self.ncpu):
            self.fileIndex.append([])
        for i in range(self.nfile):
            self.fileIndex[i % self.ncpu].append(i)
        # print(self.fileIndex)

    def load_plot_save(self,
                       fileIndex,
                       para,
                       myfigsize,
                       myfontsize,
                       myscattersize=1,
                       myDistTurnStep=20,
                       isDistZip=False,
                       plotkind='all'):

        turn, x, px, y, py, z, pz, tag = np.loadtxt(self.filePath[fileIndex],
                                                    delimiter=',',
                                                    skiprows=1,
                                                    usecols=(0, 1, 2, 3, 4, 5,
                                                             6, 7),
                                                    unpack=True)
        if plotkind == 'all' or plotkind == 'fma' or plotkind == 'fma-dist':
            self.plot_fix_distribution_perturn(fileIndex, para, turn, x, px, y,
                                               py, z, pz, tag, myDistTurnStep,
                                               isDistZip)
        if plotkind == 'all' or plotkind == 'fma' or plotkind == 'fma-fma':
            self.plot_fma(fileIndex, para, x, y, tag, myfigsize, myfontsize,
                          myscattersize)

        print('File has been drawn: {0}'.format(self.filePath[fileIndex]))

    def plot_fma(self,
                 i,
                 para,
                 x,
                 y,
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
        diffusion_xyArray = []

        for ix in range(para.fixNx):
            for iy in range(para.fixNy):
                for iz in range(para.fixNz):
                    index = ix * para.fixNy * para.fixNz + iy * para.fixNz + iz
                    # if (index > 0 and index % 100 == 0):
                    #     print('Reading fixPoint[{0}]'.format(index))
                    isExist, nux, nuy, diffusion_xy = cal_fma(
                        para, index + 1, self.npoint[i],
                        self.endTurn[i] - self.startTurn[i] + 1,
                        self.isxConjugate, self.isyConjugate, x, y, tag)
                    if isExist:
                        nuxArray.append(nux)
                        nuyArray.append(nuy)
                        diffusion_xyArray.append(diffusion_xy)

        sc_fma = ax_fma.scatter(nuxArray,
                                nuyArray,
                                c=diffusion_xyArray,
                                s=myscattersize,
                                norm=matplotlib.colors.Normalize(
                                    vmin=self.vmin, vmax=self.vmax),
                                cmap='rainbow')
        ax_fma.set_xlabel('Horizontal tune', fontsize=myfontsize)
        ax_fma.set_ylabel('Vertical tune', fontsize=myfontsize)
        cbar_fma = fig_fma.colorbar(sc_fma)
        cbar_fma.ax.tick_params(labelsize=myfontsize)
        cbar_fma.set_label('Diffusion index', fontsize=myfontsize)
        ax_fma.set_xlim(self.xlim[0], self.xlim[1])
        ax_fma.set_ylim(self.ylim[0], self.ylim[1])

        ax_fma.scatter(para.nux, para.nuy, marker='x', c='tab:red')
        fig_fma.savefig(self.savePath_fma[i], dpi=300)
        # fig_fma.show()
        plt.close(fig_fma)

    def plot_fix_distribution_perturn(self,
                                      fileid,
                                      para,
                                      turnArray,
                                      xArray,
                                      pxArray,
                                      yArray,
                                      pyArray,
                                      zArray,
                                      pzArray,
                                      tagArray,
                                      turnStep=20,
                                      isZip=False):
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

        xlim = [-6 * para.sigmax, 6 * para.sigmax]
        ylim = [-6 * para.sigmay, 6 * para.sigmay]
        pxlim = [-6 * para.sigmapx, 6 * para.sigmapx]
        pxlim = [-6 * para.sigmapy, 6 * para.sigmapy]

        if isZip:
            zip_xpx = zipfile.ZipFile(
                self.savePath_dist_xpx[fileid] + '_xpx.zip', 'a')
            zip_ypy = zipfile.ZipFile(
                self.savePath_dist_ypy[fileid] + '_ypy.zip', 'a')
            zip_xy = zipfile.ZipFile(self.savePath_dist_xy[fileid] + '_xy.zip',
                                     'a')

        plotTurn = int(totalTurn / turnStep)
        if plotTurn * turnStep < totalTurn:
            plotTurn += 1
        for i in range(plotTurn):
            iturn = i * turnStep

            turn = turnArray[iturn * totalPoint]
            x = xArray[iturn * totalPoint:(iturn + 1) * totalPoint]
            px = pxArray[iturn * totalPoint:(iturn + 1) * totalPoint]
            y = yArray[iturn * totalPoint:(iturn + 1) * totalPoint]
            py = pyArray[iturn * totalPoint:(iturn + 1) * totalPoint]
            z = zArray[iturn * totalPoint:(iturn + 1) * totalPoint]
            pz = pzArray[iturn * totalPoint:(iturn + 1) * totalPoint]
            tag = tagArray[iturn * totalPoint:(iturn + 1) * totalPoint]

            xexit = []
            pxexit = []
            yexit = []
            pyexit = []
            zexit = []
            pzexit = []

            for id in range(np.size(tag)):
                if tag[id] > 0:
                    xexit.append(x[id] * unitConvert)
                    pxexit.append(px[id] * unitConvert)
                    yexit.append(y[id] * unitConvert)
                    pyexit.append(py[id] * unitConvert)
                    zexit.append(z[id] * unitConvert)
                    pzexit.append(pz[id] * unitConvert)

            ax_xpx_dist.scatter(xexit, pxexit, color='tab:blue', s=1)
            ax_ypy_dist.scatter(yexit, pyexit, color='tab:blue', s=1)
            ax_xy_dist.scatter(xexit, yexit, color='tab:blue', s=1)

            ax_xpx_dist.set_xlabel('x(mm)')
            ax_xpx_dist.set_ylabel(r'$\rm x^{\prime}$(mrad)')
            ax_xpx_dist.set_xlim(xlim[0], xlim[1])
            ax_xpx_dist.set_ylim(pxlim[0], pxlim[1])

            ax_ypy_dist.set_xlabel('y(mm)')
            ax_ypy_dist.set_ylabel(r'$\rm y^{\prime}$(mrad)')
            ax_ypy_dist.set_xlim(ylim[0], ylim[1])
            ax_ypy_dist.set_ylim(pylim[0], pylim[1])

            ax_xy_dist.set_xlabel('x(mm)')
            ax_xy_dist.set_ylabel('y(mm)')
            ax_xy_dist.set_xlim(xlim[0], xlim[1])
            ax_xy_dist.set_ylim(ylim[0], ylim[1])

            ax_xpx_dist.set_title('turn ' + str(int(turn)))
            ax_ypy_dist.set_title('turn ' + str(int(turn)))
            ax_xy_dist.set_title('turn ' + str(int(turn)))

            file_xpx = self.savePath_dist_xpx[fileid] + "_xpx_" + str(
                int(turn)) + '.png'
            file_ypy = self.savePath_dist_ypy[fileid] + "_ypy_" + str(
                int(turn)) + '.png'
            file_xy = self.savePath_dist_xy[fileid] + "_xy_" + str(
                int(turn)) + '.png'
            fig_xpx_dist.savefig(file_xpx, dpi=150)
            fig_ypy_dist.savefig(file_ypy, dpi=150)
            fig_xy_dist.savefig(file_xy, dpi=150)

            if isZip:
                zip_xpx.write(file_xpx, os.path.split(file_xpx)[1])
                zip_ypy.write(file_ypy, os.path.split(file_ypy)[1])
                zip_xy.write(file_xy, os.path.split(file_xy)[1])

                os.remove(file_xpx)
                os.remove(file_ypy)
                os.remove(file_xy)

            ax_xpx_dist.cla()
            ax_ypy_dist.cla()
            ax_xy_dist.cla()

        if isZip:
            zip_xpx.close()
            zip_ypy.close()
            zip_xy.close()

        plt.close(fig_xpx_dist)
        plt.close(fig_ypy_dist)
        plt.close(fig_xy_dist)
        plt.close(fig_z_dist)

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


def cal_fma(para, tagid, totalPoints, totalTurns, isxConjugate, isyConjugate,
            xArray, yArray, tagArray):
    '''
    Numerical Analysis of Fundamental Frequencies (NAFF) algorithm

    选择前一半圈数频率作为FMA的x轴与y轴坐标，是否正确未知。或许试试后一半圈数？或者所有圈数的频率？或者最大频率？或者最小频率？
    '''
    totalRows = totalPoints * totalTurns
    x = xArray[tagid - 1:totalRows:totalPoints]
    y = yArray[tagid - 1:totalRows:totalPoints]
    tag = tagArray[tagid - 1:totalRows:totalPoints]

    isExist = True

    half = int(totalTurns / 2)

    nux = 0
    nuy = 0
    nux_tmp = np.zeros(half + 1)
    nuy_tmp = np.zeros(half + 1)

    diffusion_xy = 0

    for mytag in tag:
        if mytag <= 0:
            isExist = False
    turn_step = int(totalTurns / 10)
    # if isExist:
    #     nux = pnf.naff(x[0:half], half, 1)[0][1]
    #     nuy = pnf.naff(y[0:half], half, 1)[0][1]
    #     for turn_offset in range(0, half + 1, turn_step):
    #         nux_tmp[turn_offset] = abs(
    #             nux -
    #             pnf.naff(x[turn_offset:half + turn_offset], half, 1)[0][1])
    #         nuy_tmp[turn_offset] = abs(
    #             nuy -
    #             pnf.naff(y[turn_offset:half + turn_offset], half, 1)[0][1])

    #     if isxConjugate:
    #         nux = 1 - nux
    #     if isyConjugate:
    #         nuy = 1 - nuy

    #     dnux = np.amax(nux_tmp)
    #     dnuy = np.amax(nuy_tmp)

    #     diffusion_xy = np.sqrt(dnux**2 + dnuy**2)
    if isExist:
        nux = pnf.naff(x[0:totalTurns], totalTurns, 1)[0][1]
        nuy = pnf.naff(y[0:totalTurns], totalTurns, 1)[0][1]
        nux_1st_window = pnf.naff(x[0:half], half, 1)[0][1]
        nuy_1st_window = pnf.naff(y[0:half], half, 1)[0][1]

        for turn_offset in range(1, half + 1, turn_step):
            nux_2nd_window = pnf.naff(x[turn_offset:half + turn_offset], half,
                                      1)[0][1]
            nuy_2nd_window = pnf.naff(y[turn_offset:half + turn_offset], half,
                                      1)[0][1]
            nux_tmp[turn_offset] = abs(nux_1st_window - nux_2nd_window)
            nuy_tmp[turn_offset] = abs(nuy_1st_window - nuy_2nd_window)

        if isxConjugate:
            nux = 1 - nux
        if isyConjugate:
            nuy = 1 - nuy

        # dnux = np.sqrt(np.mean(nux_tmp**2))
        # dnuy = np.sqrt(np.mean(nuy_tmp**2))
        # dnux = np.std(nux_tmp)
        # dnuy = np.std(nuy_tmp)
        dnux = np.amax(nux_tmp)
        dnuy = np.amax(nuy_tmp)

        diffusion_xy = np.log10(np.sqrt(dnux**2 + dnuy**2))

    return isExist, nux, nuy, diffusion_xy


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
