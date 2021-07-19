import numpy
from Common import sigma

emitx_p = 300e-9
emity_p = 180e-9
betax_p = 0.04
betay_p = 0.02

emitx_e = 60e-9
emity_e = 60e-9
betax_e = 0.2
betay_e = 0.06

simgax_p = sigma(betax_p, emitx_p)
simgay_p = sigma(betay_p, emity_p)
simgax_e = sigma(betax_e, emitx_e)
simgay_e = sigma(betay_e, emity_e)

Nx = 512
Ny = 512
gridxLen = 2e-5
gridyLen = 1e-5

scalex_p = Nx / 2 * gridxLen / simgax_p
scaley_p = Ny / 2 * gridyLen / simgay_p
scalex_e = Nx / 2 * gridxLen / simgax_e
scaley_e = Ny / 2 * gridyLen / simgay_e

print(
    'Proton,   grid area / simga is: x {0:.2f}, y {1:.2f}; simga / gridLen is: x {2:.2f}, y {3:.2f}'
    .format(scalex_p, scaley_p, simgax_p / gridxLen, simgay_p / gridyLen))
print(
    'Electron, grid area / simga is: x {0:.2f}, y {1:.2f}; simga / gridLen is: x {2:.2f}, y {3:.2f}'
    .format(scalex_e, scaley_e, simgax_e / gridxLen, simgay_e / gridyLen))
