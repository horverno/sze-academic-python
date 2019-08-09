"""
Pénzt dobálunk és nézzük, hogyan korrelál a fej értéke 0.5-höz
"""

import numpy as np
import matplotlib.pyplot as plt


# hányszor ismételjük?
db = 500

# dobások db számosságú array, 0 vagy 1 (diszkrét, egyenletes eloszlás)
dobasok = np.random.randint(2, size=db)


for i in range(1, db):
    plt.plot(i, np.sum(dobasok[0:(i+1)]) / i, "b*")
plt.grid(True)
plt.ylim(0, 1)
plt.show()