import Common.commonCalculation as coc


class Bunch:
    """
    bunch parameter
    """

    def __init__(self, name, twissBetaX, twissBetaY, emitX, emitY):
        self.name = name

        self.tbetax = twissBetaX
        self.tbetay = twissBetaY

        self.emitx = emitX
        self.emity = emitY

        self.sigmax = coc.sigma(self.tbetax, self.emitx)
        self.sigmay = coc.sigma(self.tbetay, self.emity)
        self.sigamz = -1

        self.yokayax = coc.cal_YokoyaFactor(self.sigmax, self.sigmay)[0]
        self.yokayay = coc.cal_YokoyaFactor(self.sigmax, self.sigmay)[1]

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


class Beam(Bunch):

    """
    bunch parameter
    particle properties
    """

    def __init__(self, name, twissBetaX, twissBetaY, emitX, emitY,
                 kinetic_energy_ev, npPerBunch, invariant_mass_ev, classical_radius):
        super().__init__(name, twissBetaX, twissBetaY, emitX, emitY)

        self.Ek = kinetic_energy_ev
        self.m0 = invariant_mass_ev
        self.radius = classical_radius
        self.beta = coc.energy2betagamma(self.Ek, self.m0)[0]
        self.gamma = coc.energy2betagamma(self.Ek, self.m0)[1]
        self.velocity = coc.energy2velocity(self.Ek, self.m0)

        self.np = npPerBunch
        self.nbunch = -1
        self.intesity = -1
        self.circum = -1
        self.freq = -1  # rotational frequency

    def calTuneShift(self, bunchOpp):
        self.xix = coc.cal_tuneShift(bunchOpp.np, self.tbetax, self.tbetay,
                                     self.Ek, bunchOpp.sigamx, bunchOpp.sigmay, self.m0, self.radius)[0]
        self.xiy = coc.cal_tuneShift(bunchOpp.np, self.tbetax, self.tbetay,
                                     self.Ek, bunchOpp.sigamx, bunchOpp.sigmay, self.m0, self.radius)[1]

    def calDisruptionParameter(self, bunchOpp):
        if bunchOpp.sigamz == -1:
            print('\nError: sigmaz variable is not initialized!')
        else:
            self.disruptionx = coc.cal_disruptionParameter(
                bunchOpp.np, self.Ek, bunchOpp.sigamx, bunchOpp.sigmay, bunchOpp.sigamz, self.m0, self.radius)[0]
            self.disruptiony = coc.cal_disruptionParameter(
                bunchOpp.np, self.Ek, bunchOpp.sigamx, bunchOpp.sigmay, bunchOpp.sigamz, self.m0, self.radius)[1]

    def calIntensity(self):
        if self.circum == -1:
            print('\nError: circum variable is not initialized!')
        elif self.nbunch == -1:
            print('\nError: nbunch variable is not initialized!')
        else:
            self.intesity = coc.intensity(
                self.Ek, self.m0, self.circum, self.np, self.nbunch)


test1 = Bunch('proton-EicC', 0.2, 0.3, emitX=3e-7, emitY=6e-8)
test1.getTwissAlpha(0.3, 0.4)
print(test1.talphax)
