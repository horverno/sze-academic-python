#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Képrészlet keresés.
# Ezen a képen keresünk mintát
I = cv2.imread("waldo.png")
# A keresett minta
T = cv2.imread("waldo_minta.png")

print("A minta mérete: ", T.shape)
print("A kép mérete: ", I.shape)


# A visszaadott térképen az intenzitás jelzi az egyezés mértékét (legnagyobb intenzitás -> legjobban illeszkedő pont)
M = cv2.matchTemplate(I, T, cv2.TM_CCOEFF)
# A minMaxLoc megadja a legkisebb és legnagyobb intenzitás értékét, illetve ezek helyét. Itt most csak az utolsó érték fontos.(_, _, _, maxloc) = cv2.minMaxLoc(M)
(_, _, _, maxloc) = cv2.minMaxLoc(M)

# Körrel jelöljük a legjobban illeszkedő pontot
cv2.circle(I, (maxloc[0] + T.shape[1] // 2, maxloc[1] + T.shape[0] // 2), 20, (0, 255, 0), 3)

plt.figure()
plt.subplot(121)
plt.title("Egyezes terkep")
plt.imshow(M)
plt.axis("off")
plt.colorbar()
plt.subplot(122)
plt.title("Waldo")
plt.imshow(I[:, :, ::-1])
plt.axis("off")

plt.show()


