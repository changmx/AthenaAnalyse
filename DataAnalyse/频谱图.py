import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as nf
import Common as co

# def change_x_unit(freq,Q_0,N_opp,betaX,betaY,emitX,emitY,Ek,betaX_opp,betaY_opp,emitX_opp,emitY_opp,direction,particle):
# 	xi = cal_tuneShift(N_opp,betaX,betaY,Ek,betaX_opp,betaY_opp,emitX_opp,emitY_opp,direction,particle)


# 	print(xi)
# 	for i in range(freq.shape[0]):
# 		freq[i] = (freq[i]-Q_0)/xi
# 	return freq
class fft:
    """
	读取文件中的数据对x与y方向分别做fft，并得到指定范围内的频谱数据
	"""
    def __init__(self, beam, beam_opp, sample_period, Qx, Qy, freq_start_x,
                 freq_end_x, freq_start_y, freq_end_y, filepath):
        beam.calTuneShift(beam_opp)
        beam_opp.calTuneShift(beam)
        beam.calIntensity()
        beam_opp.calIntensity()

        self.name = beam.name
        self.name_opp = beam_opp.name
        self.Qx = Qx
        self.Qy = Qy
        self.sample_period = sample_period
        self.freq_start_x = freq_start_x
        self.freq_start_y = freq_start_y
        self.freq_end_x = freq_end_x
        self.freq_end_y = freq_end_y
        self.tuneshiftx = beam.tuneshiftx
        self.tuneshifty = beam.tuneshifty
        self.xix = beam.xix
        self.xiy = beam.xiy
        self.xix_opp = beam_opp.xix
        self.xiy_opp = beam_opp.xiy
        self.turn, self.x0, self.y0 = np.loadtxt(filepath,
                                                 delimiter=',',
                                                 skiprows=1,
                                                 usecols=(0, 1, 3),
                                                 unpack=True)
        # print(self.x0)

        self.Intensity = beam.intensity
        self.Intensity_opp = beam_opp.intensity

        self.fftSize = self.turn.shape[0]

        # 做傅里叶变换，并截取指定频率范围的数据
        self.freqx = co.cal_freq_fft(self.fftSize, self.sample_period,
                                     self.freq_start_x, self.freq_end_x)
        self.freqy = co.cal_freq_fft(self.fftSize, self.sample_period,
                                     self.freq_start_y, self.freq_end_y)
        self.spectrumx = co.cal_spctrum_fft(self.fftSize, self.sample_period,
                                            self.freq_start_x, self.freq_end_x,
                                            self.x0)
        self.spectrumy = co.cal_spctrum_fft(self.fftSize, self.sample_period,
                                            self.freq_start_y, self.freq_end_y,
                                            self.y0)

        # 在获得的指定频率范围内找sigma模和pi模对应的频率，认为sigma模是Q0附近正负0.5倍相干频移范围内的最大值，认为pi模是理论值附近-0.5到1倍相干频移范围内的最大值
        self.sigma_x = find_mode(self.spectrumx, self.freqx,
                                 self.Qx - beam.tuneshiftx * 0.5,
                                 self.Qx + beam.tuneshiftx * 0.5)
        self.pi_x = find_mode(self.spectrumx, self.freqx,
                              self.Qx + beam.tuneshiftx * 0.9,
                              self.Qx + 1)  # 如果电性相同，加号应该变为减号
        # print(self.pi_x)
        # print(self.tuneshiftx)
        self.sigma_y = find_mode(self.spectrumy, self.freqy,
                                 self.Qy - beam.tuneshifty * 0.5,
                                 self.Qy + beam.tuneshifty * 0.5)
        self.pi_y = find_mode(self.spectrumy, self.freqy,
                              self.Qy + beam.tuneshifty * 0.9,
                              self.Qy + 1)  # 如果电性相同，加号应该变为减号

        # 计算pi模与sigma模各自相对于理论值的误差
        self.sigma_x_error = np.abs(self.Qx - self.sigma_x) / (self.Qx) * 100
        self.pi_x_error = np.abs(self.Qx + beam.tuneshiftx -
                                 self.pi_x) / (self.Qx + beam.tuneshiftx) * 100
        self.sigma_y_error = np.abs(self.Qy - self.sigma_y) / (self.Qy) * 100
        self.pi_y_error = np.abs(self.Qy + beam.tuneshifty -
                                 self.pi_y) / (self.Qy + beam.tuneshifty) * 100

    def plot_mode(self, ax, direction):
        freq = self.freqx if direction == "x" else self.freqy
        spec = self.spectrumx if direction == "x" else self.spectrumy
        xi = self.xix if direction == "x" else self.xiy
        xi_opp = self.xix_opp if direction == "x" else self.xiy_opp
        xi_str = r"$\xi_x$ " + self.name if direction == "x" else r"$\xi_y$ " + self.name
        xi_str_opp = r"$\xi_x$ " + self.name_opp if direction == "x" else r"$\xi_y$ " + self.name_opp

        sigma = self.Qx if direction == "x" else self.Qy
        pi = self.Qx + self.tuneshiftx if direction == "x" else self.Qy + self.tuneshifty
        sigma_err = self.sigma_x_error if direction == "x" else self.sigma_y_error
        pi_err = self.pi_x_error if direction == "x" else self.pi_y_error

        # 绘制频谱图
        ax.plot(freq, spec, label="Simulated spectrum")
        # print(self.freqx, self.spectrumx)

        # 绘制sigma模与pi模理论值对应的垂线
        ax.axvline(x=sigma,
                   ymin=0,
                   ymax=1,
                   label=r"Theoretical $\sigma$ mode",
                   color="darkorchid",
                   linestyle="--")
        ax.axvline(x=pi,
                   ymin=0,
                   ymax=1,
                   label=r"Theoretical $\pi$ mode",
                   color="r",
                   linestyle="--")

        # 设置横轴刻度数目
        ax.locator_params("x", tight=True, nbins=10)

        ax.set_xlabel("Tune {0} ".format(direction), loc="right")
        ax.set_ylabel("Amplitude({})".format(self.name), loc="center")
        # ax.set_title("I {0} = {1:.1f}A, I {2} = {3:.1f}A".format(
        #     self.name, self.Intensity, self.name_opp, self.Intensity_opp))
        ax.grid()

        # 添加指向sigma模和pi模的箭头，并显示相对误差
        ax.annotate(r"$\pi$ mode error: {0:.2f}%".format(pi_err),
                    xy=(pi, 0.4 * np.max(spec)),
                    xycoords="data",
                    xytext=(+100, -30),
                    textcoords="offset points",
                    arrowprops=dict(arrowstyle="->",
                                    connectionstyle="arc3,rad=.2"))
        ax.annotate(r"$\sigma$ mode error: {0:.2f}%".format(sigma_err),
                    xy=(sigma, 0.8 * np.max(spec)),
                    xycoords="data",
                    xytext=(+100, -30),
                    textcoords="offset points",
                    arrowprops=dict(arrowstyle="->",
                                    connectionstyle="arc3,rad=.2"))

        # 显示beambeam parameter参数
        ax.text(
            freq[0],
            0.6 * np.max(spec),
            "{0} = {1:.4f}\n{2} = {3:.4f}\nI {4} = {5:.1f}A\nI {6} = {7:.1f}A".
            format(xi_str, xi, xi_str_opp, xi_opp, self.name, self.Intensity,
                   self.name_opp, self.Intensity_opp),
            bbox=dict(boxstyle="round", fc="w"))
        ax.legend()


def find_mode(spectrum, freq, freq_start, freq_end):
    pi_freq = 0
    pi_amplitude = 0
    for i in range(freq.shape[0]):
        if freq[i] > freq_start and freq[i] < freq_end:
            if spectrum[i] > pi_amplitude:
                pi_amplitude = spectrum[i]
                pi_freq = freq[i]
    # print(pi_freq, pi_amplitude)
    return pi_freq


Qx_0 = 0.52
Qy_0 = 0.08

betaX_e = 0.33
betaY_e = 0.01
betaX_p = 0.33
betaY_p = 0.01
emitX_e = 1.8e-8
emitY_e = 3.6e-10
emitX_p = 1.8e-8
emitY_p = 3.6e-10

sigmaZ_e = 0.004
sigmaZ_p = 0.004

Ek_e = 8e9
Ek_p = 3.5e9
circumference_e = 3016.26
circumference_p = 3016.26
Nbunch_e = 5000
Nbunch_p = 5000

fs = 1  # 采样频率，1次/圈
T = 1 / fs  # 采样间隔或采样周期，为采样频率的倒数
x_freq_start = 0.5
x_freq_end = 0.55

y_freq_start = 0.06
y_freq_end = 0.12

Np_e = 1.4e9
Np_p = 3.3e9

electron = co.Beam('electron', betaX_e, betaY_e, emitX_e, emitY_e, Ek_e,
                   co.Const.MASS_ELECTRON_EV, co.Const.RADIUS_ELECTRON,
                   sigmaZ_e, Np_e, Nbunch_e, circumference_e)
positron = co.Beam('positron', betaX_p, betaY_p, emitX_p, emitY_p, Ek_p,
                   co.Const.MASS_ELECTRON_EV, co.Const.RADIUS_ELECTRON,
                   sigmaZ_p, Np_p, Nbunch_p, circumference_p)

freq_e = []
freq_p = []
freq_e.append(
    fft(
        electron, positron, T, Qx_0, Qy_0, x_freq_start, x_freq_end,
        y_freq_start, y_freq_end,
        r"E:\changmx\bb2021\linux\2021_0428\KEKB yokoya\1456_35_electron_bunch0.csv"
    ))
freq_e.append(
    fft(
        electron, positron, T, Qx_0, Qy_0, x_freq_start, x_freq_end,
        y_freq_start, y_freq_end,
        r"E:\changmx\bb2021\linux\2021_0428\KEKB yokoya\1457_19_electron_bunch0.csv"
    ))
freq_e.append(
    fft(
        electron, positron, T, Qx_0, Qy_0, x_freq_start, x_freq_end,
        y_freq_start, y_freq_end,
        r"E:\changmx\bb2021\linux\2021_0428\KEKB yokoya\1459_27_electron_bunch0.csv"
    ))
freq_e.append(
    fft(
        electron, positron, T, Qx_0, Qy_0, x_freq_start, x_freq_end,
        y_freq_start, y_freq_end,
        r"E:\changmx\bb2021\linux\2021_0428\KEKB yokoya\1500_16_electron_bunch0.csv"
    ))

e_direction = "y"

fig_e, ax_e = plt.subplots(2, 2, sharex='col', sharey='all')

freq_e[0].plot_mode(ax_e[0, 0], e_direction)
freq_e[1].plot_mode(ax_e[0, 1], e_direction)
freq_e[2].plot_mode(ax_e[1, 0], e_direction)
freq_e[3].plot_mode(ax_e[1, 1], e_direction)

ax_e[0, 0].set_title(
    r'1 slice $\times$ 1 slice, without hourglass effect, without damping')
ax_e[0, 1].set_title(
    r'1 slice $\times$ 1 slice, without hourglass effect, with damping')
ax_e[1, 0].set_title(
    r'10 slice $\times$ 10 slice, with hourglass effect, without damping')
ax_e[1, 1].set_title(
    r'10 slice $\times$ 10 slice, with hourglass effect, with damping')

fig_e.suptitle(
    r'The influence of hourglass effect and damping on yokoya factor in {0}-direction'
    .format(e_direction))

freq_p.append(
    fft(
        positron, electron, T, Qx_0, Qy_0, x_freq_start, x_freq_end,
        y_freq_start, y_freq_end,
        r"E:\changmx\bb2021\linux\2021_0428\KEKB yokoya\1456_35_electron_bunch0.csv"
    ))
freq_p.append(
    fft(
        positron, electron, T, Qx_0, Qy_0, x_freq_start, x_freq_end,
        y_freq_start, y_freq_end,
        r"E:\changmx\bb2021\linux\2021_0428\KEKB yokoya\1457_19_electron_bunch0.csv"
    ))
freq_p.append(
    fft(
        positron, electron, T, Qx_0, Qy_0, x_freq_start, x_freq_end,
        y_freq_start, y_freq_end,
        r"E:\changmx\bb2021\linux\2021_0428\KEKB yokoya\1459_27_electron_bunch0.csv"
    ))
freq_p.append(
    fft(
        positron, electron, T, Qx_0, Qy_0, x_freq_start, x_freq_end,
        y_freq_start, y_freq_end,
        r"E:\changmx\bb2021\linux\2021_0428\KEKB yokoya\1500_16_electron_bunch0.csv"
    ))

p_direction = "x"

fig_p, ax_p = plt.subplots(2, 2, sharex='col', sharey='all')

freq_p[0].plot_mode(ax_p[0, 0], p_direction)
freq_p[1].plot_mode(ax_p[0, 1], p_direction)
freq_p[2].plot_mode(ax_p[1, 0], p_direction)
freq_p[3].plot_mode(ax_p[1, 1], p_direction)

ax_p[0, 0].set_title(
    r'1 slice $\times$ 1 slice, without hourglass effect, without damping')
ax_p[0, 1].set_title(
    r'1 slice $\times$ 1 slice, without hourglass effect, with damping')
ax_p[1, 0].set_title(
    r'10 slice $\times$ 10 slice, with hourglass effect, without damping')
ax_p[1, 1].set_title(
    r'10 slice $\times$ 10 slice, with hourglass effect, with damping')

fig_p.suptitle(
    r'The influence of hourglass effect and damping on yokoya factor in {0}-direction'
    .format(p_direction))
# ax_e[-1, -1].axis('off')
plt.show()

# Qx_e = 0.58
# Qy_e = 0.55
# Qx_p = 0.315
# Qy_p = 0.3

# betaX_e = 0.2
# betaY_e = 0.06
# betaX_p = 0.04
# betaY_p = 0.02
# emitX_e = 60e-9
# emitY_e = 60e-9
# emitX_p = 300e-9
# emitY_p = 180e-9

# sigmaZ_e = 0.02
# sigmaZ_p = 0.04

# Ek_e = 3.5e9
# Ek_p = 19.08e9
# circumference_e = 809.44
# circumference_p = 1341.58
# Nbunch_e = 1
# Nbunch_p = 1

# fs = 1  # 采样频率，1次/圈
# T = 1 / fs  # 采样间隔或采样周期，为采样频率的倒数
# e_x_freq_start = 0.5
# e_x_freq_end = 0.6
# p_x_freq_start = 0.25
# p_x_freq_end = 0.35

# e_y_freq_start = 0.5
# e_y_freq_end = 0.6
# p_y_freq_start = 0.25
# p_y_freq_end = 0.35

# Np_e = 1.7e11
# Np_p = 1.25e10

# Nbunch_e = 270
# Nbunch_p = 448

# electron = co.Beam('electron', betaX_e, betaY_e, emitX_e, emitY_e, Ek_e,
#                    co.Const.MASS_ELECTRON_EV, co.Const.RADIUS_ELECTRON,
#                    sigmaZ_e, Np_e, Nbunch_e, circumference_e)
# proton = co.Beam('proton', betaX_p, betaY_p, emitX_p, emitY_p, Ek_p,
#                  co.Const.MASS_PROTON_EV, co.Const.RADIUS_PROTON, sigmaZ_p,
#                  Np_p, Nbunch_p, circumference_p)

# freq_e = []
# freq_p = []

# freq_e.append(
#     fft(
#         electron, proton, T, Qx_e, Qy_e, e_x_freq_start, e_x_freq_end,
#         e_y_freq_start, e_y_freq_end,
#         r"E:\changmx\bb2021\linux\2021_0428\寻找网格宽度EicC\1959_26_electron_bunch0.csv"
#     ))
# freq_e.append(
#     fft(
#         electron, proton, T, Qx_e, Qy_e, e_x_freq_start, e_x_freq_end,
#         e_y_freq_start, e_y_freq_end,
#         r"E:\changmx\bb2021\linux\2021_0428\寻找网格宽度EicC\2001_52_electron_bunch0.csv"
#     ))
# freq_e.append(
#     fft(
#         electron, proton, T, Qx_e, Qy_e, e_x_freq_start, e_x_freq_end,
#         e_y_freq_start, e_y_freq_end,
#         r"E:\changmx\bb2021\linux\2021_0428\寻找网格宽度EicC\2003_08_electron_bunch0.csv"
#     ))
# freq_e.append(
#     fft(
#         electron, proton, T, Qx_e, Qy_e, e_x_freq_start, e_x_freq_end,
#         e_y_freq_start, e_y_freq_end,
#         r"E:\changmx\bb2021\linux\2021_0428\寻找网格宽度EicC\2004_22_electron_bunch0.csv"
#     ))

# e_direction = "y"

# fig_e, ax_e = plt.subplots(2, 2, sharex='col', sharey='all')

# freq_e[0].plot_mode(ax_e[0, 0], e_direction)
# freq_e[1].plot_mode(ax_e[0, 1], e_direction)
# freq_e[2].plot_mode(ax_e[1, 0], e_direction)
# freq_e[3].plot_mode(ax_e[1, 1], e_direction)

# freq_p.append(
#     fft(
#         proton, electron, T, Qx_p, Qy_p, p_x_freq_start, p_x_freq_end,
#         p_y_freq_start, p_y_freq_end,
#         r"E:\changmx\bb2021\linux\2021_0428\寻找网格宽度EicC\1959_26_proton_bunch0.csv"
#     ))
# freq_p.append(
#     fft(
#         proton, electron, T, Qx_p, Qy_p, p_x_freq_start, p_x_freq_end,
#         p_y_freq_start, p_y_freq_end,
#         r"E:\changmx\bb2021\linux\2021_0428\寻找网格宽度EicC\2001_52_proton_bunch0.csv"
#     ))
# freq_p.append(
#     fft(
#         proton, electron, T, Qx_p, Qy_p, p_x_freq_start, p_x_freq_end,
#         p_y_freq_start, p_y_freq_end,
#         r"E:\changmx\bb2021\linux\2021_0428\寻找网格宽度EicC\2003_08_proton_bunch0.csv"
#     ))
# freq_p.append(
#     fft(
#         proton, electron, T, Qx_p, Qy_p, p_x_freq_start, p_x_freq_end,
#         p_y_freq_start, p_y_freq_end,
#         r"E:\changmx\bb2021\linux\2021_0428\寻找网格宽度EicC\2004_22_proton_bunch0.csv"
#     ))

# p_direction = "x"

# fig_p, ax_p = plt.subplots(2, 2, sharex='col', sharey='all')

# freq_p[0].plot_mode(ax_p[0, 0], p_direction)
# freq_p[1].plot_mode(ax_p[0, 1], p_direction)
# freq_p[2].plot_mode(ax_p[1, 0], p_direction)
# freq_p[3].plot_mode(ax_p[1, 1], p_direction)
# plt.show()