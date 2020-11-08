import numpy as np
import matplotlib.pyplot as plt
from tuneShift import cal_tuneShift
from tuneShift import cal_YokoyaFactor
from FFT import cal_freq_fft
from FFT import cal_spctrum_fft
import numpy.fft as nf
from intensity import cal_intensity

def change_x_unit(freq,Q_0,N_opp,betaX,betaY,emitX,emitY,Ek,betaX_opp,betaY_opp,emitX_opp,emitY_opp,direction,particle):
	xi = cal_tuneShift(N_opp,betaX,betaY,Ek,betaX_opp,betaY_opp,emitX_opp,emitY_opp,direction,particle)

	print(xi)
	for i in range(freq.shape[0]):
		freq[i] = (freq[i]-Q_0)/xi
	return freq

def find_mode(spectrum,freq,freq_start,freq_end):
	pi_freq = 0
	pi_amplitude = 0
	for i in range(freq.shape[0]):
		if freq[i]>freq_start and freq[i]<freq_end:
			if spectrum[i]>pi_amplitude:
				pi_amplitude=spectrum[i]
				pi_freq = freq[i]
	# print(pi_freq,pi_amplitude)
	return pi_freq

def plot_spectrum(N,N_opp,Nbunch,Nbunch_opp,axes,row,col,fftSize,sample_period,circumference,specArrayX,specArrayY,Qx_0,Qy_0,freq_start_x,freq_end_x,freq_start_y,freq_end_y,betaX,betaY,Ek,Ek_opp,emitX,emitY,betaX_opp,betaY_opp,emitX_opp,emitY_opp,particle,particle_opp,direction):
	
	specArray=specArrayX
	freq_start=0
	freq_end=0
	Q_0=0
	if direction=='x':
		specArray=specArrayX
		freq_start=freq_start_x
		freq_end=freq_end_x
		Q_0=Qx_0
	elif direction=='y':
		specArray=specArrayY
		freq_start=freq_start_y
		freq_end=freq_end_y
		Q_0=Qy_0
	else:
		print('Error: input wrong direction parameter at plot_spectrum!')
		exit(1)
	# 计算理论相干频率
	xi_theory = cal_tuneShift(N_opp,betaX,betaY,Ek,betaX_opp,betaY_opp,emitX_opp,emitY_opp,direction,particle)
	yokoya = cal_YokoyaFactor(betaX,betaY,emitX,emitY,direction)
	tuneShift_theory = xi_theory*yokoya
	
	# 做傅里叶变换，并截取指定频率范围的数据
	freq_part = cal_freq_fft(fftSize,sample_period,freq_start,freq_end)
	spectrum_part = cal_spctrum_fft(fftSize,T,freq_start,freq_end,specArray)
	
	# 在获得的指定频率范围内找sigma模和pi模对应的频率，认为sigma模是Q0附近正负0.5倍相干频移范围内的最大值，认为pi模是理论值附近-0.5到1倍相干频移范围内的最大值
	freq_sim_pi = find_mode(spectrum_part,freq_part,Q_0+tuneShift_theory*0.5,Q_0+tuneShift_theory*2)	# 如果电性相同，加号应该变为减号
	freq_sim_sigma = find_mode(spectrum_part,freq_part,Q_0-tuneShift_theory*0.5,Q_0+tuneShift_theory*0.5)
	# print(freq_sim_sigma)

	# 计算pi模与sigma模各自相对于理论值的误差
	pi_mode_error = np.abs(Q_0+tuneShift_theory-freq_sim_pi)/(tuneShift_theory+Q_0)*100
	sigma_mode_error = np.abs(Q_0-freq_sim_sigma)/Q_0*100

	# print('pi',tuneShift_theory+Q_0-freq_sim_pi,tuneShift_theory+Q_0,freq_sim_pi)
	# print('sigma',Q_0-freq_sim_sigma,Q_0,freq_sim_sigma)

	# 绘制频谱图
	axes[row,col].plot(freq_part,spectrum_part,label=r"$Simulation\ spectrum$")
	# 绘制理论sigma模和理论pi模的垂线
	axes[row,col].axvline(x=tuneShift_theory+Q_0,ymin=0,ymax=1,label=r"$Theoretical\ \pi -mode$",color="r",linestyle="--")
	axes[row,col].axvline(x=Q_0,ymin=0,ymax=1,label=r"$Theoretical\ \sigma -mode$",color="darkorchid",linestyle="--")
	# 设置横轴刻度数目
	axes[row,col].locator_params("x",tight=True,nbins=10)
	
	axes[row,col].set_title('I '+ particle +' = ' +str(format(cal_intensity(Ek,circumference,N,Nbunch,particle),".2f"))+'A, '+'I '+ particle_opp +' = ' +str(format(cal_intensity(Ek_opp,circumference,N_opp,Nbunch_opp,particle_opp),".2f"))+'A')
	axes[row,col].set_xlabel('Tune '+direction,loc="right")
	axes[row,col].set_ylabel('Amplitude',loc='center')
	
	# 添加网格
	axes[row,col].grid()
	# 添加指向sigma模和pi模理论值竖线的箭头，并显示相对误差
	axes[row,col].annotate(r'$\pi -mode\ error: $'+str(format(pi_mode_error,".3f"))+'%',xy=(Q_0+tuneShift_theory,0.6*np.max(spectrum_part)),xycoords='data',xytext=(+20,-30),textcoords='offset points', arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
	axes[row,col].annotate(r'$\sigma -mode\ error: $'+str(format(sigma_mode_error,".3f"))+'%',xy=(Q_0,0.8*np.max(spectrum_part)),xycoords='data',xytext=(+20,-30),textcoords='offset points', arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

	# 显示tune shift参数
	if direction=='x':
		axes[row,col].text(freq_start,0.9*np.max(spectrum_part),r"$\xi_x=$"+str(format(xi_theory,".4f")),bbox=dict(boxstyle="round", fc="w"))
	elif direction=='y':
		axes[row,col].text(freq_start,0.9*np.max(spectrum_part),r"$\xi_y=$"+str(format(xi_theory,".4f")),bbox=dict(boxstyle="round", fc="w"))
	
	axes[row,col].legend()

fs = 1    # 采样频率，1次/圈
T = 1/fs  # 采样间隔或采样周期，为采样频率的倒数
x_freq_start = 0.5
x_freq_end = 0.55
x_freq_start2 = 0.5
x_freq_end2 = 0.6
x_freq_start3 = 0.5
x_freq_end3 = 0.7

y_freq_start = 0.06
y_freq_end = 0.12
y_freq_start2 = 0.0
y_freq_end2 = 0.2
y_freq_start3 = 0.0
y_freq_end3 = 0.3

Qx_0 = 0.52
Qy_0 = 0.08

betaX_e = 0.33
betaY_e = 0.008
betaX_p = 0.33
betaY_p = 0.008
emitX_e = 1.8e-8
emitY_e = 3.6e-10
emitX_p = 1.8e-8
emitY_p = 3.6e-10
Ek_e = 8e9
Ek_p = 3.5e9
circumference = 3016.26
Nbunch_e = 5000
Nbunch_p = 5000

fig,axes = plt.subplots(3,3,figsize=(25,15),dpi=300)
# plt.figure(figsize=(1,1))

turn0,x0,y0 = np.loadtxt(r"E:\changmx\bb2019\statLumiPara\2020_1023\1815_positron_bunch0.csv", delimiter=',', skiprows=1, usecols=(0, 1, 3), unpack=True)
turn1,x1,y1 = np.loadtxt(r"E:\changmx\bb2019\statLumiPara\2020_1023\1814_positron_bunch0.csv", delimiter=',', skiprows=1, usecols=(0, 1, 3), unpack=True)
turn2,x2,y2 = np.loadtxt(r"E:\changmx\bb2019\statLumiPara\2020_1023\1813_positron_bunch0.csv", delimiter=',', skiprows=1, usecols=(0, 1, 3), unpack=True)
turn3,x3,y3 = np.loadtxt(r"E:\changmx\bb2019\statLumiPara\2020_1023\1812_positron_bunch0.csv", delimiter=',', skiprows=1, usecols=(0, 1, 3), unpack=True)
turn4,x4,y4 = np.loadtxt(r"E:\changmx\bb2019\statLumiPara\2020_1023\1811_positron_bunch0.csv", delimiter=',', skiprows=1, usecols=(0, 1, 3), unpack=True)
turn5,x5,y5 = np.loadtxt(r"E:\changmx\bb2019\statLumiPara\2020_1023\1810_positron_bunch0.csv", delimiter=',', skiprows=1, usecols=(0, 1, 3), unpack=True)
turn6,x6,y6 = np.loadtxt(r"E:\changmx\bb2019\statLumiPara\2020_1023\1809_positron_bunch0.csv", delimiter=',', skiprows=1, usecols=(0, 1, 3), unpack=True)
turn7,x7,y7 = np.loadtxt(r"E:\changmx\bb2019\statLumiPara\2020_1023\1808_positron_bunch0.csv", delimiter=',', skiprows=1, usecols=(0, 1, 3), unpack=True)
turn8,x8,y8 = np.loadtxt(r"E:\changmx\bb2019\statLumiPara\2020_1023\1803_positron_bunch0.csv", delimiter=',', skiprows=1, usecols=(0, 1, 3), unpack=True)

N = turn0.shape[0]

Np = [0.045e10,0.11e10,0.23e10,0.7e10,1.3e10,2.3e10,3.3e10,4.3e10,5.3e10]
Ne = [0.02e10,0.05e10,0.1e10,0.3e10,0.6e10,1.0e10,1.4e10,2.0e10,2.4e10]

direction='x'

plot_spectrum(Np[0],Ne[0],Nbunch_p,Nbunch_e,axes,0,0,N,T,circumference,x0,y0,Qx_0,Qy_0,x_freq_start,x_freq_end,y_freq_start,y_freq_end,betaX_p,betaY_p,Ek_p,Ek_e,\
	emitX_p,emitY_p,betaX_e,betaY_e,emitX_e,emitY_e,'positron','electron',direction)
plot_spectrum(Np[1],Ne[1],Nbunch_p,Nbunch_e,axes,0,1,N,T,circumference,x1,y1,Qx_0,Qy_0,x_freq_start,x_freq_end,y_freq_start,y_freq_end,betaX_p,betaY_p,Ek_p,Ek_e,\
	emitX_p,emitY_p,betaX_e,betaY_e,emitX_e,emitY_e,'positron','electron',direction)
plot_spectrum(Np[2],Ne[2],Nbunch_p,Nbunch_e,axes,0,2,N,T,circumference,x2,y2,Qx_0,Qy_0,x_freq_start,x_freq_end,y_freq_start,y_freq_end,betaX_p,betaY_p,Ek_p,Ek_e,\
	emitX_p,emitY_p,betaX_e,betaY_e,emitX_e,emitY_e,'positron','electron',direction)
plot_spectrum(Np[3],Ne[3],Nbunch_p,Nbunch_e,axes,1,0,N,T,circumference,x3,y3,Qx_0,Qy_0,x_freq_start2,x_freq_end2,y_freq_start2,y_freq_end2,betaX_p,betaY_p,Ek_p,Ek_e,\
	emitX_p,emitY_p,betaX_e,betaY_e,emitX_e,emitY_e,'positron','electron',direction)
plot_spectrum(Np[4],Ne[4],Nbunch_p,Nbunch_e,axes,1,1,N,T,circumference,x4,y4,Qx_0,Qy_0,x_freq_start2,x_freq_end2,y_freq_start2,y_freq_end2,betaX_p,betaY_p,Ek_p,Ek_e,\
	emitX_p,emitY_p,betaX_e,betaY_e,emitX_e,emitY_e,'positron','electron',direction)
plot_spectrum(Np[5],Ne[5],Nbunch_p,Nbunch_e,axes,1,2,N,T,circumference,x5,y5,Qx_0,Qy_0,x_freq_start2,x_freq_end2,y_freq_start2,y_freq_end2,betaX_p,betaY_p,Ek_p,Ek_e,\
	emitX_p,emitY_p,betaX_e,betaY_e,emitX_e,emitY_e,'positron','electron',direction)
plot_spectrum(Np[6],Ne[6],Nbunch_p,Nbunch_e,axes,2,0,N,T,circumference,x6,y6,Qx_0,Qy_0,x_freq_start3,x_freq_end3,y_freq_start3,y_freq_end3,betaX_p,betaY_p,Ek_p,Ek_e,\
	emitX_p,emitY_p,betaX_e,betaY_e,emitX_e,emitY_e,'positron','electron',direction)
plot_spectrum(Np[7],Ne[7],Nbunch_p,Nbunch_e,axes,2,1,N,T,circumference,x7,y7,Qx_0,Qy_0,x_freq_start3,x_freq_end3,y_freq_start3,y_freq_end3,betaX_p,betaY_p,Ek_p,Ek_e,\
	emitX_p,emitY_p,betaX_e,betaY_e,emitX_e,emitY_e,'positron','electron',direction)
plot_spectrum(Np[8],Ne[8],Nbunch_p,Nbunch_e,axes,2,2,N,T,circumference,x8,y8,Qx_0,Qy_0,x_freq_start3,x_freq_end3,y_freq_start3,y_freq_end3,betaX_p,betaY_p,Ek_p,Ek_e,\
	emitX_p,emitY_p,betaX_e,betaY_e,emitX_e,emitY_e,'positron','electron',direction)

fig.suptitle('Beam-beam coherent modes and incoherent spectra for the cases of two bunches colliding head-on with different intensity\n'+\
	'From a fully self-consistent simulation with KEKB parameter',y=0.96,fontsize=15)

axes[2,0].annotate('KEKB design parameter',xy=(0.05,0.6), xycoords='axes fraction',color='r')
axes[2,1].annotate(r'$\sigma_x / \sigma_y = 45,\ in\ x\ direction(0.13\sigma_x /grid), in\ y\ direction(0.47\sigma_y/grid)$',xy=(0.4,0.05), xycoords='figure fraction',fontsize=12)

# plt.savefig(r'./'+direction+'.png')
plt.show()