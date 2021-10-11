import PyNAFF as pnf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

    
N = 1500
fe = 0.2
fp = 0.37
xe = np.arange(N)
xe1 = np.sin(2*np.pi*fe*xe)
xe2 = np.sin(2*np.pi*fe*xe)

xp = np.arange(2*N)
xp1 = 1*np.sin(2*np.pi*fp*xp)
xp2 = 1*np.sin(2*np.pi*fp*xp)
xp3 = 1*np.sin(2*np.pi*fp*xp)

for i in range(N):
    id = int(i/5)
    if i%5 == 0:
        xe1[i]+=xp1[id*3+0]

x = xe1

sp = np.fft.fft(x)
freq = np.fft.fftfreq(x.shape[-1])
# plt.plot(freq, sp.real, freq, sp.imag)
plt.plot(freq, np.abs(sp))
plt.grid()
plt.show()

# fig, ax = plt.subplots()


# def f(x, y):
#     return np.sin(x) + np.cos(y)


# x = np.linspace(0, 2 * np.pi, 120)
# y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)

# # ims is a list of lists, each row is a list of artists to draw in the
# # current frame; here we are just animating one artist, the image, in
# # each frame
# ims = []
# for i in range(60):
#     x += np.pi / 15.
#     y += np.pi / 20.
#     im = ax.imshow(f(x, y), animated=True)
#     if i == 0:
#         ax.imshow(f(x, y))  # show an initial one first
#     ims.append([im])

# ani = animation.ArtistAnimation(fig,
#                                 ims,
#                                 interval=50,
#                                 blit=True,
#                                 repeat_delay=1000)

# # To save the animation, use e.g.
# #
# ani.save("movie.gif", writer='pillow')
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()

# for i in range(3):
#     print('i', i)
#     for i in range(5):
#         print(i)
#     print(i)

# test NAFF
# N = 512
# t = np.arange(N)
# Q = 0.123456789
# signal = np.sin(2.0 * np.pi * Q * t)

# freq_NAFF = pnf.naff(signal, N, 1, 0, False, 1)[0][1]

# sp = np.fft.fft(signal)
# freq = np.fft.fftfreq(t.shape[-1])
# i = np.argmax(sp)

# freq_FFT = freq[i]

# print(Q)
# print(freq_NAFF)
# print(freq_FFT)