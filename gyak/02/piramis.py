n = int(input('Kérem a sorok számát: '))
 
for i in range(1, n+1):
    # emlékezzünk: az i * "A" i darab A betűt ír ki
    print((n-i) * " ", i * "A ", (n-i) * " ", i)