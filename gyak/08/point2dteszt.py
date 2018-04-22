from point2d import Point2D
p = Point2D()           # példányosítás, 0, 0 pont
p1 = Point2D(5)         # 5, 0 pont
p2 = Point2D(2, -2)     # 2 – 2 pont
print("p2 east tagváltozó értéke: ", p2.east)
print("p2 north tagváltozó értéke: ", p2.north)
print("p2 abs() függvény értéke: ", p2.abs())
print("p2.__dict__:", p2.__dict__)
print("p2:", p2)

"""
A print p2 utasítás nem azt az eredményt adja amit szeretnénk. Az egyes osztályokhoz speciális
függvényeket definiálhatunk (mint pl. az __init__), ezek jellemzője, hogy két aláhúzás karakterrel
kezdődik és végződik a nevük. Az __init__ függvény az úgynevezett konstruktor, ez fut le a példányok
létrehozásakor, itt biztosíthatjuk, hogy ne legyen inicializálatlan tagváltozónk. A destruktort a __del__
függvény implementálásával valósíthatjuk meg. A dinamikus tárfoglalás hiányában a Pythonban erre
ritkábban van szükség.
"""

print("p2.abs.__doc__: ", p2.abs.__doc__)
print("p2.__doc__: ", p2.__doc__)
#print("help(Point2D): ", help(Point2D))
"""
"""
