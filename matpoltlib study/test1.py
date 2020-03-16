import matplotlib.pyplot as plt
import numpy as np

# fig = plt.figure()
# fig.suptitle('No axes on this figure')
# plt.subplot(2,2,1)

# fig, (ax1, ax2, ax3) = plt.subplots(3,1)
x = np.arange(0, 10, 0.2)
y = np.sin(x)
plt.plot(x,y)
# ax1 = plt.subplot(2,2,1)
# ax1.plot(x, y)

# ax2 = plt.subplot(2,2,2)
# z = x
# ax2.plot(x,z)

# ax3 = plt.subplot(2,2,3)
# m = x+10
# ax3.plot(x,m)


plt.show()