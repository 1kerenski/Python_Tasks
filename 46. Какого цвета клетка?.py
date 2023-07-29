x = input('Введите координаты: ')
bkv = x[0]
cfr = int(x[1])
if bkv == 'a':
    bkv = 1
elif bkv == 'b':
    bkv = 2
elif bkv == 'c':
    bkv = 3
elif bkv == 'd':
    bkv = 4
elif bkv == 'e':
    bkv = 5
elif bkv == 'f':
    bkv = 6
elif bkv == 'g':
    bkv = 7
elif bkv == 'h':
    bkv = 8
s = bkv + cfr
z = s % 2
if z == 0:
    print('Клетка черная')
else:
     print('Клетка белая')

