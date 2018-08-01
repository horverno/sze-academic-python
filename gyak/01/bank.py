penz = 100
kamat = 1.1
for ev in range(0,6):
    print("%d: %.2f Ft van a bankban, %.1f-es kamattal" % (ev + 2018, penz * (kamat ** ev), kamat))