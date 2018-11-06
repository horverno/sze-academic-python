class Romaiszam(object):
    
    def __init__(self, szam):
        self._arab_szamok = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
        self._romai_szamok = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
        self._szam = szam
        self._result = ""
        for i in range(len(self._arab_szamok)):
            db = int(szam / self._arab_szamok[i])
            self._result += self._romai_szamok[i] * db
            szam -= self._arab_szamok[i] * db
            
    def __str__(self):
        return self._result
    
    def __add__(self, rszam):
        return Romaiszam(self._szam + rszam._szam)
    
    def __sub__(self, rszam):
        return Romaiszam(self._szam - rszam._szam)
    
    def __mul__(self, rszam):
        return Romaiszam(self._szam * rszam._szam)
    
    def __truediv__(self, rszam):
        return Romaiszam(int(self._szam / rszam._szam))
    
a = Romaiszam(12)
b = Romaiszam(4)

print(a, "+", b, "=", a + b)
print(a, "-", b, "=", a - b)
print(a, "*", b, "=", a * b)
print(a, "/", b, "=", a / b)