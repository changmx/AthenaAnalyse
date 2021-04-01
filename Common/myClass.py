import Common.commonCalculation as coc


class Beam:
    """
    particle properties
    bunch parameter
    """

    def __init__(self, name, twissBetaX, twissBetaY, emitX, emitY):
        self.name = name

        self.twiss_betax = twissBetaX
        self.twiss_betay = twissBetaY

        self.emitx = emitX
        self.emity = emitY

        self.sigmax = coc.sigma(self.twiss_betax, self.emitx)
        self.sigmay = coc.sigma(self.twiss_betay, self.emity)

        self.yokayax = coc.cal_YokoyaFactor(self.sigmax, self.sigmay)[0]
        self.yokayay = coc.cal_YokoyaFactor(self.sigmax, self.sigmay)[1]

        self.twiss_alphax = 0
        self.twiss_alphay = 0
        self.twiss_gammax = 0
        self.twiss_gammay = 0

        self.Ek = 0
        self.m0 = 0
        self.beta = 0
        self.gamma = 0
        self.radius = 0
        self.velocity = 0

        self.Np = 0
        self.Nbunch = 0
        self.Intesity = 0

    def getParticleProperty(self, kinetic_energy_ev, invariant_mass_ev, classical_radius):
        self.Ek = kinetic_energy_ev
        self.m0 = invariant_mass_ev
        self.classical_radius = classical_radius
        self.beta = coc.energy2betagamma(self.Ek, self.m0)[0]
        self.gamma = coc.energy2betagamma(self.Ek, self.m0)[1]
        self.velocity = coc.energy2velocity(self.Ek, self.m0)


test1 = Beam('proton-EicC', twissBetaX=0.2,
             twissBetaY=0.3, emitX=3e-7, emitY=6e-8)
print(test1.yokayax, test1.yokayay, test1.name)
