import numpy as np
import matplotlib.pyplot as plt
from math import sin, pi

s = 50 # a vizsgált diszkrét függvény mérete

t = np.array([sin((2*pi)/(s-1)*i) for i in range(s)])

k = np.array([-1, 0, 1])

dt = np.array([None] + [np.sum(t[i:i+len(k)] * k) for i in range(len(t) - len(k) + 1)] + [None]) # a függvény első és utolsó elemét nem tudjuk számítani, ezért az elejét és a végét kitöltjük egy üres elemmel

plt.plot(t)
plt.plot(dt)
plt.grid(True)
plt.show()