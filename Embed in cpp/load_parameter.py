import json
import os
import numpy as np
import platform
from general import cal_tuneShift
from general import sigma
from constant import Const


class Parameter:
    """
    Load and save beam parameter
    """
    def __init__(self, home, yearMonDay, hourMinSec, filekind):
        self.home = home
        self.yearMonDay = yearMonDay
        self.hourMinSec = hourMinSec
        self.filekind = filekind
        self.filepath = self.hourMinSec + '_' + self.filekind + '.json'
        self.filepath = os.sep.join([
            self.home, 'statLumiPara', self.yearMonDay, self.hourMinSec,
            self.filepath
        ])
        with open(self.filepath, 'r+') as file:
            para_list = json.load(file)
            self.particle = para_list['Beam name']
            self.charge = para_list['Charge quantity']
            self.Nreal = para_list['Real particle number per bunch']
            self.Nmacro = para_list['Macro particle number per bunch']
            self.nslice = para_list['Number of slices']
            self.nbunch = para_list['Layout'][0]
            self.nux = para_list['Qx']
            self.nuy = para_list['Qy']
            self.nuz = para_list['Qz']
            self.superiod = para_list['Number of turns']
            self.betax = para_list['Beta x']
            self.betay = para_list['Beta y']
            self.alphax = para_list['Alpha x']
            self.alphay = para_list['Alpha y']
            self.emitx = para_list['Emittence x']
            self.emity = para_list['Emittence y']
            self.Ek = para_list['Kinetic energy']
            self.gridx = para_list['Grid x']
            self.gridy = para_list['Grid y']
            self.gridlenx = para_list['Grid x length']
            self.gridleny = para_list['Grid y length']
            self.chromaticity_x = para_list['Chromaticity x']
            self.chromaticity_y = para_list['Chromaticity y']
            self.sigmaz = para_list['Sigma z']
            self.sigmapz = para_list['DeltaP']

            if 'isFixAndSaveCoordinate' in para_list:
                self.fixXStart = para_list['isFixAndSaveCoordinate'][1][
                    'x_start_end_step'][0]
                self.fixXEnd = para_list['isFixAndSaveCoordinate'][1][
                    'x_start_end_step'][1]
                self.fixXStep = para_list['isFixAndSaveCoordinate'][1][
                    'x_start_end_step'][2]
                self.fixNx = self.fixXEnd - self.fixXStart

                self.fixYStart = para_list['isFixAndSaveCoordinate'][2][
                    'y_start_end_step'][0]
                self.fixYEnd = para_list['isFixAndSaveCoordinate'][2][
                    'y_start_end_step'][1]
                self.fixYStep = para_list['isFixAndSaveCoordinate'][2][
                    'y_start_end_step'][2]
                self.fixNy = self.fixYEnd - self.fixYStart

                self.fixZStart = para_list['isFixAndSaveCoordinate'][3][
                    'z_start_end_step'][0]
                self.fixZEnd = para_list['isFixAndSaveCoordinate'][3][
                    'z_start_end_step'][1]
                self.fixZStep = para_list['isFixAndSaveCoordinate'][3][
                    'z_start_end_step'][2]
                self.fixNz = self.fixZEnd - self.fixZStart

        if self.particle == 'proton':
            self.mass = Const.MASS_PROTON_EV
            self.radius = Const.RADIUS_PROTON
        elif self.particle == 'electron':
            self.mass = Const.MASS_ELECTRON_EV
            self.radius = Const.RADIUS_ELECTRON

        self.sigmax = sigma(self.betax, self.emitx)
        self.sigmay = sigma(self.betay, self.emity)
        self.gammax = (1 + self.alphax**2) / self.betax
        self.gammay = (1 + self.alphay**2) / self.betay
        self.sigmapx = np.sqrt(self.emitx * self.gammax)
        self.sigmapy = np.sqrt(self.emity * self.gammay)
        self.gridx_perSigma = self.sigmax / self.gridlenx
        self.gridy_perSigma = self.sigmay / self.gridleny

    def print(self):
        print('\n')
        print(self.particle)
        print(self.Nreal)
        print(self.Nmacro)
        print(self.nslice)
        print(self.nbunch)
        print(self.nux)
        print(self.nuy)
        # print(self.turn)
        # print(self.fixNx)
        # print(self.fixNy)
        # print(self.fixNz)

    def gen_note_withPath(self, beam2):
        self.turn = self.superiod * beam2.nbunch
        beam2.turn = self.superiod * self.nbunch

        self.tuneshift_direction = -1 * np.sign(self.charge * beam2.charge)
        self.xix, self.xiy = cal_tuneShift(beam2.Nreal, self.betax, self.betay,
                                           self.Ek, beam2.sigmax, beam2.sigmay,
                                           self.mass, self.radius)

        filename = os.sep.join(
            [self.home, 'statLumiPara', self.yearMonDay, self.hourMinSec])

        self.statnote = '{0:s}\n'.format(filename)
        self.statnote += '{0}: N = {1:.2E}, Nmacro = {2:.2E}, Nturn = {3:d}, Nbunch = {4:d}, Nslice = {5:d}\n{6}: N = {7:.2E}, Nmacro = {8:.2E}, Nturn = {9:d}, Nbunch = {10:d}, Nslice = {11:d}\n'.format(
            self.particle, self.Nreal, self.Nmacro, self.turn, self.nbunch,
            self.nslice, beam2.particle, beam2.Nreal, beam2.Nmacro, beam2.turn,
            beam2.nbunch, beam2.nslice)
        self.statnote += r'$\nu=({0:.3f},{1:.3f},{2:.3f}), \xi_x={3:.3f}, \xi_y={4:.3f}, Q^\prime_x={5:.1f}, Q^\prime_y={6:.1f}$'.format(
            self.nux, self.nuy, self.nuz, self.xix, self.xiy,
            self.chromaticity_x, self.chromaticity_x)

        self.statnote_part1 = '{0:s}\n'.format(
            filename
        ) + r'$\sigma_x^\prime={0:e}, \sigma_y^\prime={1:e}, \sigma_z={2:f}, \delta_p={3:f}$'.format(
            self.sigmapx, self.sigmapy, self.sigmaz, self.sigmapz)
        self.statnote_part1 += '\n'
        self.statnote_part1 += r'grid size = ({0:d}$\times${1:.1e}, {2:d}$\times${3:.1e}), $\sigma_x$ = {4:.1f}gridx, $\sigma_y$ = {5:.1f}gridy'.format(
            self.gridx, self.gridlenx, self.gridy, self.gridleny,
            self.gridx_perSigma, self.gridy_perSigma)

        self.statnote_part2 = '{0:s}\n'.format(
            filename
        ) + r'$\beta_x={0:f}, \beta_y={1:f}, \alpha_x={2:f}, \alpha_y={3:f}, \gamma_x={4:f}, \gamma_y={5:f}$'.format(
            self.betax, self.betay, self.alphax, self.alphay, self.gammax,
            self.gammay)

        self.luminote = '{0:s}\n'.format(filename)
        self.luminote += 'N{0} = {1:.2E}, N{2} = {3:.2E}\n'.format(
            self.particle, self.Nreal, beam2.particle, beam2.Nreal)
        self.luminote += 'Nturn superiod = {0:d}, Nturn {1} = {2:d}, Nturn {3} = {4:d}'.format(
            self.superiod, self.particle, self.turn, beam2.particle,
            beam2.turn)


if __name__ == '__main__':
    home = ''
    if platform.system() == 'Windows':
        home = os.sep.join(['D:', 'bb2021'])
    elif platform.system() == 'Linux':
        home = os.sep.join(['/home', 'changmx', 'bb2021'])
    else:
        print('We do not support {0} system now.}'.format(platform.system()))
        os.exit(1)

    yearMonDay = '2021_0908'
    hourMinSec = '1538_59'

    beam1 = Parameter(home, yearMonDay, hourMinSec, 'beam1')
    beam2 = Parameter(home, yearMonDay, hourMinSec, 'beam2')

    beam1.print()