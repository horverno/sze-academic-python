class Haromszog(object):
    
    def __init__(self, a = 1, b = 1, c = 1):
        self.setA(a)
        self.setB(b)
        self.setC(c)
        
    def setA(self, a):
        self._a = a
        
    def setB(self, b):
        self._b = b
        
    def setC(self, c):
        self._c = c
        
    def __str__(self):
        return "(a: %f, b: %f, c: %f)" % (self._a, self._b, self._c)
    
    def kerulet(self):
        return self._a + self._b + self._c
    
    def terulet(self):
        s = self.kerulet() / 2
        return (s * ((s - self._a) * (s - self._b) * (s - self._c))) ** 0.5
    
    def szerkesztheto_e(self):
        if (self._a + self._b > self._c) and (self._a + self._c > self._b) and (self._c + self._b > self._a):
            return True
        else:
            return False
        
    def beirt_kor_sugara(self):
        return 2 * self.terulet() / self.kerulet()
    
h = Haromszog(4, 5, 6)

if h.szerkesztheto_e():
    print("A megadott", h, "haromszog szerkesztheto!")
    
print("A haromszog kerulete:", h.kerulet())
print("A haromszog terulete:", h.terulet())
print("A haromszogbe irhato kor sugara:", h.beirt_kor_sugara())