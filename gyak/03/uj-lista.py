my_list = ['p', 'q']

n = 0

while(n<2 or n>9):
    n = int(input("Adjon meg egy szamot 2-9 kozott! "))

new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]

print(new_list)
