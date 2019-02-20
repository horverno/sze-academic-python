import os
import matplotlib.pyplot as plt
import numpy as np
import cv2

def ermeszamlal(fajl_nev):
    penz_kep = cv2.imread(os.path.join("data", fajl_nev))
    penz_kep = penz_kep[:,:,0].astype(np.uint8)
    plt.figure(1, figsize=(12,8))
    plt.subplot(121)
    plt.title(fajl_nev)
    plt.imshow(penz_kep, cmap = "gray")
    plt.axis("off")
    plt.colorbar()
    #plt.show()
    #plt.hist(penz_kep.ravel(), bins=256, range=(0.0, 255.0), fc='k', ec='k')
    #plt.show()

    #print("Min:", penz_kep.min(), "Max:", penz_kep.max()) # 0-255 közötti értékek
    penz_kep[penz_kep < 150] = 0
    #plt.figure(1, figsize=(12,8))
    #plt.imshow(penz_kep, cmap = "gray")
    #plt.colorbar()
    #plt.show()
    #plt.hist(penz_kep.ravel(), bins=256, range=(0.0, 255.0), fc='k', ec='k')
    #plt.show()


    penz_kep[penz_kep >= 150] = 1
    #print("Min:", penz_kep.min(), "Max:", penz_kep.max())
    #plt.figure(1, figsize=(12,8))
    #plt.imshow(penz_kep)
    #plt.colorbar()
    #plt.show()
    #plt.hist(penz_kep.ravel(), bins=256, range=(0.0, 2), fc='k', ec='k')
    #plt.show()


    penz_kitoltes = penz_kep
    h, w = penz_kep.shape[:2]
    #print(type(penz_kitoltes), penz_kitoltes.shape)
    cv2.floodFill(penz_kitoltes, None, (0, 0), 255)
    penz_kitoltes[penz_kitoltes < 150] = 1
    penz_kitoltes[penz_kitoltes >= 150] = 0
    #plt.figure(1, figsize=(12,8))
    #plt.imshow(penz_kitoltes, cmap = "gray")
    #plt.colorbar()
    #plt.show()

    # keressük meg az összekötött komponenseket, írjuk ki azok méretét
    nb_components1, output1, stats1, centroids1 = cv2.connectedComponentsWithStats(penz_kitoltes, connectivity=8)
    sizes1 = stats1[1:, -1]
    #print(sizes1)

    #szűrjük kki az 500 pixel alatti "hibákat"
    min_size = 500  
    penz_szurve = np.zeros((output1.shape))
    # csak a min_size-nál nagyobb méretűt tarsuk meg
    for i in range(0, nb_components1 - 1):
        if sizes1[i] >= min_size:
            penz_szurve[output1 == i + 1] = True

    nb_components2, output2, stats2, centroids2 = cv2.connectedComponentsWithStats(penz_szurve.astype(np.uint8), connectivity=8)
    sizes2 = stats2[1:, -1]
    #print(sizes2)

    sizes = stats1[1:, -1]
    #plt.figure(1, figsize=(12,8))
    plt.subplot(122)
    plt.imshow(output2)
    plt.axis("off")
    plt.colorbar()
    plt.plot(centroids2[1:, 0], centroids2[1:, 1], "xw", markersize=12)
    szoveg = "A " + fajl_nev + "-ben " + str(nb_components2 - 1) + " darab érme tálaható."
    plt.title(szoveg)
    print(szoveg)
    plt.show()
    #print(stats2)

ermeszamlal("penz01.jpg")
ermeszamlal("penz02.jpg")
ermeszamlal("penz03.jpg")