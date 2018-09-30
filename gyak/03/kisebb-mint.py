#irunk python kodot, amely a beolvasott szamnal kisebb elemeket irja csak ki az adott listabol

import sys

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(input("Choose a number: "))

new_list = []

for i in a:
    if i < num:
        new_list.append(i)

print (new_list)
