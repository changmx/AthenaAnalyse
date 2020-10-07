import numpy as np
import numpy.fft as nf
import matplotlib.pyplot as plt

turn,x,y,xEmit,yEmit,sigmaz,sigmapz = np.loadtxt(r"E:\changmx\bb2019\statistic\2020_0925\0836_electron_bunch0.csv", delimiter=',', skiprows=1, usecols=(0, 1, 2, 3, 4, 5, 6), unpack=True)
sp_x = nf.fft(x)
sp_y = nf.fft(y)
sp_xEmit = nf.fft(xEmit)
sp_yEmit = nf.fft(yEmit)
sp_sigmaz = nf.fft(sigmaz)
sp_sigmapz = nf.fft(sigmapz)
freq = nf.fftfreq(turn.shape[0])

plt.plot(freq,sp_x.real)
# plt.plot(freq,sp.real,freq,sp.imag)
plt.show()