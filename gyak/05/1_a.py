import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

c = 100 # c darab véletlen pontot generálunk

x = np.random.random(c) # a generált pontok x értéke a [0;1] tartományban
y = np.random.random(c) # a generált pontok y értéke a [0;1] tartományban

d = np.sqrt(x * x + y * y) # minden pont távolsága az origótól.

d0 = np.array([d[i] for i in range(c) if d[i] <= 1.0]) # azon távolságok, melyek a kör területére esnek
d1 = np.array([d[i] for i in range(c) if d[i] > 1.0]) # azon távolságok, melyek a kör területén kívül esnek (ezt nem használjuk fel, csak a szemléltetés végett szerepel)

print(len(d0)/c * 4) # a kör területe (~PI)
