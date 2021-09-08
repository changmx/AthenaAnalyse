import PyNAFF as pnf
import numpy as np

N = 512
t = np.arange(N)
Q = 0.123456789
signal = np.sin(2.0 * np.pi * Q * t)

freq_NAFF = pnf.naff(signal, N, 1, 0, False, 1)[0][1]

sp = np.fft.fft(signal)
freq = np.fft.fftfreq(t.shape[-1])
i = np.argmax(sp)

freq_FFT = freq[i]

print(Q)
print(freq_NAFF)
print(freq_FFT)