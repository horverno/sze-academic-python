# 1. gyakorlat
Python bevezetés, Python 2 vs Python 3, IDE, egyszerű matematika, változók, szintaxis, és logika, ciklusok `I.`, string `I.`

## Feladat - Aritmetika
- Írjunk programot a fontosabb aritmetikai műveletetek szemléltetésére. 
- *Megoldás*: `01/simpleMath.py` - [link](01/simpleMath.py)

# 2. gyakorlat
String `II.` (replace, find, count, lower, stb), feltételek (if, elif, else)

## Feladat - Fizzbuzz
- Fizzbuzz: Koncentrációs játék, ahol 1-től kezdve soroljuk a számokat, és minden 3-mal osztahtó szám helyett azt kell mondani, hogy Fizz, az 5-tel oszthatók helyett, hogy Buzz. Ha 3-mal és 5-tel is osztható a szám, akkor azt kell mondani, hogy FizzBuzz. 
- Írjunk programot, ami ilyen módon számol 1-től 100-ig! 
- *Megoldás*: `02/fizzbuzz.py` - [link](02/fizzbuzz.py)

## Feladat - String szeletelés
- Írjunk programot, ami a string szeletelését szemlélteti.
- Induljunk ki a *`"@shannonturner"`* majd valósítsuk meg a következő funkciókat:
 ```
 My github handle is  @shannonturner
 My first name is  shannon
 My last name is  turner
 My last name is  turner
 My twitter handle is NOT  @shannon
 My last name is  turner
 My first name is  shannon
 ```
- *Megoldás*: `02/slicing.py` - [link](02/slicing.py) (c) Shannon Turner 

## Feladat - Palindrom
- A palindrom szűkebb értelemben olyan szó vagy szókapcsolat, amely visszafelé olvasva is ugyanaz. Pl: `Géza, kék az ég`.
- Írjunk programot, amely ellenőrzi egy stringről, hogy palindrom-e. Ehhez az kell, hogy a programunk ne vegye figyelembe a kis/nagybetű közti különbséget  illetve a szóközöket. 
- *Megoldás*: `02/palindrom.py` - [link](02/palindrom.py)

## Feladat - Piramis
- Írjon programot, amely bekér a felhasználótól egy számot _(ezt külön validálni nem kell)_ és a számnak megfelelő sorú piramis alakzatot rajzol ki `A` betűkből, például:
``` python
Kérem a sorok számát: 12
            A              1
           A A             2
          A A A            3
         A A A A           4
        A A A A A          5
       A A A A A A         6
      A A A A A A A        7
     A A A A A A A A       8
    A A A A A A A A A      9
   A A A A A A A A A A     10
  A A A A A A A A A A A    11
 A A A A A A A A A A A A   12
```
- *Megoldás*: `02/palindrom.py` - [link](02/palindrom.py)

## Feladat - Szövegpiramis
- Írjon programot, amely a `Széchenyi István Egyetem, Győr` szöveget jelzi ki, soronként bővülő karakterszámmal:
```
S
Sz
Szé
Széc
Széch
Széche
Széchen
Szécheny
Széchenyi
Széchenyi 
Széchenyi I
Széchenyi Is
Széchenyi Ist
Széchenyi Istv
Széchenyi Istvá
Széchenyi István
Széchenyi István 
Széchenyi István E
Széchenyi István Eg
Széchenyi István Egy
Széchenyi István Egye
Széchenyi István Egyet
Széchenyi István Egyete
Széchenyi István Egyetem
Széchenyi István Egyetem,
Széchenyi István Egyetem, 
Széchenyi István Egyetem, G
Széchenyi István Egyetem, Gy
Széchenyi István Egyetem, Győ
Széchenyi István Egyetem, Győr
```
- *Megoldás*: `02/szechenyi.py` - [link](02/szechenyi.py)

# 3. gyakorlat
Ciklusok `II.`, listák, join és split (string listává illetve fordítva)

# 4.  gyakorlat
Fájlok, flagek (r, w, b, +), szöveges formátumok, csv, matplotlib `I.`

# 5.  gyakorlat
Hasznos külső library-k: matplotlib `II.`, numpy

# 6.  gyakorlat
Dict, kivételkezelés (try / except) 

# 7.  gyakorlat
Függvények, pár további hasznos library (import from ... import ... as szintaktika, time, random, math, regex (regular expressions), os, sys, json)

# 8.  gyakorlat
Python: osztályok, objektum orientált programozás

# 9.  gyakorlat
Raspberry Pi: Python GPIO

# 10.  gyakorlat
OpenCV és képfeldolgozás `I.`

## _Used sources_ / Felhasznált források
- [Shannon Turner: Python lessons repository](https://github.com/shannonturner/python-lessons) MIT license (c) Shannon Turner 2013-2014
- [Siki Zoltán: Python mogyoróhéjban](http://www.agt.bme.hu/gis/python/python_oktato.pdf) GNU FDL license (c) Siki Zoltán
