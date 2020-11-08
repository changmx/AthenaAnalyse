import numpy as np
import numpy.fft as nf

def cal_freq_fft(N,T,freq_start,freq_end):
	freq = np.arange(0,1,1/N)
	for i in range(freq.shape[0]):
		freq[i]=freq[i]/T
	freq_part = freq[range(int(freq_start*T*N),int(freq_end*T*N))]
	return freq_part

def cal_spctrum_fft(N,T,freq_start,freq_end,sequence):
	spectrum = np.abs(nf.fft(sequence))
	spectrum_part = spectrum[range(int(freq_start*T*N),int(freq_end*T*N))]
	return spectrum_part