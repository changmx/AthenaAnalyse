import numpy as np
from matplotlib import pyplot as plt
import math

x = np.linspace(0,10,1000)
y = (1+x)*(np.exp(1-x))

plt.figure(1)
plt.xlabel("x")
plt.ylabel("y")
plt.title(r"$f(x) = (1+x)e^{1-x}$")
plt.plot(x,y)
plt.savefig('gaussian generate function.png',dpi = 300)
plt.show()