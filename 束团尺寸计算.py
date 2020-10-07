import numpy as np

# x, px, y, py = np.loadtxt(r"E:\changmx\bb2019\distribution\2020_0817_kv_proton\1444\proton_bunch0_10000_turn0.csv", delimiter=',', usecols=(0, 1, 2, 3), unpack=True)
x, px, y, py = np.loadtxt(r"E:\changmx\bb2019\distribution\2020_0908_gaussian_electron\1608\electron_bunch0_20000_turn0.csv", delimiter=',', usecols=(0, 1, 2, 3), unpack=True)

x_sigma_11 = np.mean(np.square(x))
x_sigma_22 = np.mean(np.square(px))
x_sigma_12 = np.mean(np.multiply(x,px))
y_sigma_11 = np.mean(np.square(y))
y_sigma_22 = np.mean(np.square(py))
y_sigma_12 = np.mean(np.multiply(y, py))

x_sigma = abs(x_sigma_11 * x_sigma_22 - x_sigma_12 ** 2)
y_sigma = abs(y_sigma_11 * y_sigma_22 - y_sigma_12 ** 2)
# sigma1 = np.std(x, ddof=1)  #calculate the standard deviation
# print(sigma1)
# print(x_sigma_11 ** 0.5)
print(x_sigma_11**0.5)
print(y_sigma_11**0.5)
emit_x = np.sqrt(x_sigma_11 * x_sigma_22 - x_sigma_12 *x_sigma_12)
emit_y = np.sqrt(y_sigma_11 * y_sigma_22 - y_sigma_12 *y_sigma_12)
print(emit_x,emit_y)