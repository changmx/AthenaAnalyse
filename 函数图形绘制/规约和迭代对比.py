import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(1,32)
y_iteration = x
y_log = np.log2(x)

fig, ax = plt.subplots()
ax.plot(x,y_iteration,label='迭代运算')
ax.plot(x,y_log,label='归约运算')
ax.set(xlabel='数组长度', ylabel='计算时间')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
ax.legend()

plt.show()
plt.close()