import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

c = 1

for i in range(6): # 10, 100, 1000, 10000, 100000 és 1000000 darab pont esetén közelítjük a PI értékét.
    c = c * 10
    print(c)
    for j in range(10): # minden c darabszám melett 10 mérést végzünk
        print("\t", j)
        x = np.random.random(c)
        y = np.random.random(c)
        d = np.sqrt(x * x + y * y)
        d0 = np.array([d[i] for i in range(c) if d[i] <= 1.0])
        plt.plot(i, len(d0)/c*4, "rx")
plt.grid(True)
plt.show()