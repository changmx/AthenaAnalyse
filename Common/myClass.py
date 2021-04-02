import Common.commonCalculation as coc
import sys
import traceback


class Bunch:
    """
    bunch parameter
    """

    def __init__(self, name, twissBetaX, twissBetaY, emitX, emitY, sigmaz=0):
        self.name = name

        self.tbetax = twissBetaX
        self.tbetay = twissBetaY

        self.emitx = emitX
        self.emity = emitY

        self.sigmax = coc.sigma(self.tbetax, self.emitx)
        self.sigmay = coc.sigma(self.tbetay, self.emity)
        self.sigmaz = sigmaz

        self.yokoyax = coc.cal_YokoyaFactor(self.sigmax, self.sigmay)[0]
        self.yokoyay = coc.cal_YokoyaFactor(self.sigmax, self.sigmay)[1]

    def getTwissAlpha(self, twissAlphaX, twissAlphaY):
        self.talphax = twissAlphaX
        self.talphay = twissAlphaY
        self.tgammax = (1 + self.talphax ** 2) / self.tbetax
        self.tgammay = (1 + self.talphay ** 2) / self.tbetay

    def getTwissGamma(self, twissGammaX, twissGammaY):
        self.tgammax = twissGammaX
        self.tgammay = twissGammaY
        self.talphax = (self.tbetax * self.tgammax - 1) ** 0.5
        self.talphay = (self.tbetay * self.tgammay - 1) ** 0.5

    def print(self):
        print('\nBunch parameter of %s' % self.name)
        print('%-25s %-15f %-10f' %
              ('Twiss beta x/y(m):', self.tbetax, self.tbetay))
        if self.tgammax != 0 or self.tgammay != 0:
            print('%-25s %-15f %-10f' %
                  ('Twiss alpha x/y:', self.talphax, self.talphay))
            print('%-25s %-15f %-10f' %
                  ('Twiss gamma x/y:', self.tgammax, self.tgammay))
        print('%-25s %-15e %-10e' %
              ('Emittence x/y(mrad):', self.emitx, self.emity))
        print('%-25s %-15f %-10f' %
              ('Yokoya factor x/y:', self.yokoyax, self.yokoyay))


class Beam(Bunch):

    """
    bunch parameter
    particle properties
    """

    def __init__(self, name, twissBetaX, twissBetaY, emitX, emitY,
                 kinetic_energy_ev, invariant_mass_ev, classical_radius, sigmaz=0, npPerBunch=0, nbunch=0, circum=0, freq=0):
        super().__init__(name, twissBetaX, twissBetaY, emitX, emitY, sigmaz=sigmaz)

        self.Ek = kinetic_energy_ev
        self.m0 = invariant_mass_ev
        self.radius = classical_radius
        self.beta = coc.energy2betagamma(self.Ek, self.m0)[0]
        self.gamma = coc.energy2betagamma(self.Ek, self.m0)[1]
        self.velocity = coc.energy2velocity(self.Ek, self.m0)

        self.np = npPerBunch
        self.nbunch = nbunch
        self.intensity = 0
        self.circum = circum
        self.freq = freq  # rotational frequency

        self.xix = 0
        self.xiy = 0
        self.disruptionx = 0
        self.disruptiony = 0

    def print(self):
        print('\nBeam parameter of %s' % self.name)
        print('%-25s %-15f %-10f' %
              ('Twiss beta x/y(m):', self.tbetax, self.tbetay))
        print('%-25s %-15e %-10e' %
              ('Emittence x/y(mrad):', self.emitx, self.emity))
        print('%-25s %-15f %-10f' %
              ('Yokoya factor x/y:', self.yokoyax, self.yokoyay))
        print('%-25s %-15f %-10f' %
              ('Tune shift x/y:', self.xix, self.xiy))
        print('%-25s %-15f %-10f' %
              ('Disruption x/y:', self.disruptionx, self.disruptiony))
        print('Ek: %f Gev, m0: %f Mev' % (self.Ek/1e9, self.m0/1e6))
        print('beta: %f, gamma: %f' % (self.beta, self.gamma))
        if self.np != 0:
            print('NpPerBunch: %.1e' % (self.np))
        if self.nbunch != 0:
            print('Nbunch: %f' % (self.nbunch))
        if self.intensity != 0:
            print('Intensity: %f A' % (self.intensity))
        if self.circum != 0:
            print('Circumference: %f m' % (self.circum))
        if self.freq != 0:
            print('Frequency: %f MHz' % (self.freq/1e6))

    def calTuneShift(self, bunchOpp):
        try:
            if bunchOpp.np == 0:
                raise UnboundLocalError('User error: np_opp variable is 0.')
        except UnboundLocalError:
            traceback.print_exc()
            sys.exit(1)
        else:
            self.xix = coc.cal_tuneShift(bunchOpp.np, self.tbetax, self.tbetay,
                                         self.Ek, bunchOpp.sigmax, bunchOpp.sigmay, self.m0, self.radius)[0]
            self.xiy = coc.cal_tuneShift(bunchOpp.np, self.tbetax, self.tbetay,
                                         self.Ek, bunchOpp.sigmax, bunchOpp.sigmay, self.m0, self.radius)[1]

    def calDisruptionParameter(self, bunchOpp):
        try:
            if bunchOpp.np == 0:
                raise UnboundLocalError('User error: np_opp variable is 0.')
            if bunchOpp.sigmaz == 0:
                raise UnboundLocalError('User error: sigmaz_opp variable is 0.')
        except UnboundLocalError:
            traceback.print_exc()
            sys.exit(1)
        else:
            self.disruptionx = coc.cal_disruptionParameter(
                bunchOpp.np, self.Ek, bunchOpp.sigmax, bunchOpp.sigmay, bunchOpp.sigmaz, self.m0, self.radius)[0]
            self.disruptiony = coc.cal_disruptionParameter(
                bunchOpp.np, self.Ek, bunchOpp.sigmax, bunchOpp.sigmay, bunchOpp.sigmaz, self.m0, self.radius)[1]

    def calIntensity(self):
        try:
            if self.circum == 0:
                raise UnboundLocalError('User error: circum variable is 0.')
            if self.nbunch == 0:
                raise UnboundLocalError('User error: nbunch variable is 0.')
            if self.np == 0:
                raise UnboundLocalError('User error: np variable is 0.')
        except UnboundLocalError:
            traceback.print_exc()
            sys.exit(1)
        else:
            self.intensity = coc.intensity(
                self.Ek, self.m0, self.circum, self.np, self.nbunch)

    def calFrequency(self):
        try:
            if self.circum == 0:
                raise UnboundLocalError('User error: circum variable is 0.')
        except UnboundLocalError:
            traceback.print_exc()
            sys.exit(1)
        else:
            self.freq = self.velocity / self.circum


if __name__ == '__main__':

    test1 = Beam('proton-test', 0.2, 0.3, 3e-6, 5e-6,
                 20e9, 938.76767e6, 1e-15, npPerBunch=1)
    print(test1.yokoyax, test1.beta)
    test2 = Beam('electron-test', 0.4, 0.6, 5e-6, 8e-6,
                 20e9, 0.511e6, 1e-15)
    test1.calTuneShift(test2)
    test1.freq = 30e6
    test1.print()
