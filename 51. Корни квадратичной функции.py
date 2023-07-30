import math
a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))
d = (b**b) - 4*a*c
if d < 0:
    print('Корней нет')
elif d == 0:
    x1 = int(-(b/(2*a)))
    print('Один корень')
    print(x1)
elif d > 0:
    x1 = int((-b + math.sqrt(d))/(2*a))
    x2 = int((-b - math.sqrt(d))/(2*a))
    print('Два корня')
    print(x1, x2)

