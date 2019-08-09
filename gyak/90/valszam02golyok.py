"""
Egy dobozban 20 fehér golyó van. Egy szabályos dobókockával dobunk, majd a következőt tesszük: 
 ha a dobott szám 1, 2 vagy 3, akkor tíz golyót cserélünk ki pirosra; 
 ha a dobott szám 4 vagy 5, akkor hat golyót cserélünk pirosra; 
 ha a dobott szám 6, akkor tizenkét golyót cserélünk pirosra. 
Ezután véletlenszerűen húzunk egy golyót a dobozból.
(a) Mi a valószínűsége annak, hogy pirosat húzunk? (0,45) 
(b) Feltéve, hogy pirosat húztunk, mi a valószínűsége, hogy hatost dobtunk? (2/9 ≈ 0,2222) 
"""

import numpy as np
import matplotlib.pyplot as plt


# hányszor ismételjük?
db = 100000

# dobások db számosságú array, 1-6 között (diszkrét, egyenletes eloszlás)
dobasok = np.random.randint(6, size=db) + 1

eredmeny_a = 0
eredmeny_b = 0
# darabszám, feltéve, hogy pirosat húztunk 
db_piros = 0

for d in dobasok:
    # False = Fehér
    # True = Piros
    golyok = np.full((20), False, dtype=bool)
    if d == 1 or d == 2 or d == 3:
        golyok[0:10] = True
    elif d == 4 or d == 5:
        golyok[0:6] = True
    else:
        golyok[0:12] = True
    huzas = golyok[np.random.randint(20)]   
    eredmeny_a += huzas
    # Ha pirosat húztunk
    if huzas == True:
        db_piros += 1
        if d == 6:
            eredmeny_b += 1

print("A válasz: %.4f (%d dobásnál, minél nagyobb szám, annál jobban közelíti a 0,45-t) " % (eredmeny_a / db, db))
print("B válasz: %.4f (%d dobásnál, minél nagyobb szám, annál jobban közelíti a 0,2222-t) " % (eredmeny_b / db_piros, db))