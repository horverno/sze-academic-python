import csv
import os
import matplotlib.pyplot as plt

helys = "mohely.csv"
nepes = {}
with open("monepesseg.csv") as f:
    for line in f:
        (key, val) = line.split(";")
        nepes[key] = int(val)

with open(helys, 'rt') as csvhelys:
    readerhelys = csv.DictReader(csvhelys, delimiter=';', quotechar='"')
    i = 0
    for row in readerhelys:
        i += 1
        if row["Név"] in nepes: #row["Név"] == "Budapest":
            # fok:perc.századperc szétbontása
            xF = float(row["KeletiHossz"].split(":")[0])
            xP = float(row["KeletiHossz"].split(":")[1].split(".")[0])
            xS = float(row["KeletiHossz"].split(".")[1])
            # fok:perc.századperc szétbontása
            yF = float(row["ÉszakiSzél"].split(":")[0])
            yP = float(row["ÉszakiSzél"].split(":")[1].split(".")[0])
            yS = float(row["ÉszakiSzél"].split(".")[1])
            # fok + (perc + (század / 60)) / 60 
            x = xF + (xP + (xS / 60)) / 60
            y = yF + (yP + (yS / 60)) / 60
            area = int(nepes[row["Név"]]) / 100
            plt.scatter(x, y, s= int(area), c='blue', alpha=0.2)
            plt.annotate(row["Név"], (x, y))
plt.show()
