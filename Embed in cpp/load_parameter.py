import json
import os
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
            self.emitx = para_list['Emittence x']
            self.emity = para_list['Emittence y']
            self.Ek = para_list['Kinetic energy']
            self.gridx = para_list['Grid x']
            self.gridy = para_list['Grid y']
            self.gridlenx = para_list['Grid x length']
            self.gridleny = para_list['Grid y length']
            self.chromaticity_x = para_list['Chromaticity x']
            self.chromaticity_y = para_list['Chromaticity y']

        if self.particle == 'proton':
            self.mass = Const.MASS_PROTON_EV
            self.radius = Const.RADIUS_PROTON
        elif self.particle == 'electron':
            self.mass = Const.MASS_ELECTRON_EV
            self.radius = Const.RADIUS_ELECTRON

        self.sigmax = sigma(self.betax, self.emitx)
        self.sigmay = sigma(self.betay, self.emity)
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
        print(self.turn)

    def gen_note_withPath(self, beam2):
        self.turn = self.superiod * beam2.nbunch
        beam2.turn = self.superiod * self.nbunch

        self.xix, self.xiy = cal_tuneShift(beam2.Nreal, self.betax, self.betay,
                                           self.Ek, beam2.sigmax, beam2.sigmay,
                                           self.mass, self.radius)

        filename = os.sep.join(
            [self.home, 'statLumiPara', self.yearMonDay, self.hourMinSec])

        self.statnote = '{0:s}\n'.format(filename)
        self.statnote += 'N{0} = {1:.2E}, Nmacro = {2:.2E}, Nturn = {3:d}, Nbunch = {4:d}, Nslice = {5:d}\n'.format(
            self.particle, self.Nreal, self.Nmacro, self.turn, self.nbunch,
            self.nslice)
        self.statnote += r'$\nu=({0:.3f},{1:.3f},{2:.3f}), \xi_x={3:.3f}, \xi_y={4:.3f}, Q^\prime_x={5:.1f}, Q^\prime_y={6:.1f}$'.format(
            self.nux, self.nuy, self.nuz, self.xix, self.xiy,
            self.chromaticity_x, self.chromaticity_x)
        self.statnote += '\n'
        self.statnote += r'grid size = ({0:d}$\times${1:.1e}, {2:d}$\times${3:.1e}), $\sigma_x$ = {4:.1f}gridx, $\sigma_y$ = {5:.1f}gridy'.format(
            self.gridx, self.gridlenx, self.gridy, self.gridleny,
            self.gridx_perSigma, self.gridy_perSigma)

        self.luminote = '{0:s}\n'.format(filename)
        self.luminote += 'N{0} = {1:.2E}, N{2} = {3:.2E}\n'.format(
            self.particle, self.Nreal, beam2.particle, beam2.Nreal)
        self.luminote += 'Nturn superiod = {0:d}, Nturn {1} = {2:d}, Nturn {3} = {4:d}'.format(
            self.superiod, self.particle, self.turn, beam2.particle,
            beam2.turn)
