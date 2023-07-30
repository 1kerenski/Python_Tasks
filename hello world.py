g = int(input('Введите год: '))
m = input('Введите месяц: ')
d = int(input('Введите день: '))
vg = g % 4
if d < 31 and m == 'Январь':
    sd = d + 1
    print(sd, m, g)
elif d == 31 and m == 'Январь':
    sd = 1
    m = 'Февраль'
    print(sd, m, g)
elif vg == 0 and m == 'Февраль':
    if d < 29:
        sd = d + 1
        print(sd, m, g)
    elif d == 29:
        sd = 1
        m = 'Март'
        print(sd, m, g)
elif vg != 0 and m == 'Февраль':
    if d < 28:
        sd = d + 1
        print(sd, m, g)
    elif d == 28:
        sd = 1
        m = 'Март'
        print(sd, m, g)
elif d < 31 and m == 'Март':
    sd = d + 1
    print(sd, m, g)
elif d == 31 and m == 'Март':
    sd = 1
    m = 'Апрель'
    print(sd, m, g)
elif d < 30 and m == 'Апрель':
    sd = d + 1
    print(sd, m, g)
elif d == 30 and m == 'Апрель':
    sd = 1
    m = 'Май'
    print(sd, m, g)
elif d < 31 and m == 'Май':
    sd = d + 1
    print(sd, m, g)
elif d == 31 and m == 'Май':
    sd = 1
    m = 'Июнь'
    print(sd, m, g)
elif d < 30 and m == 'Июнь':
    sd = d + 1
    print(sd, m, g)
elif d == 30 and m == 'Июнь':
    sd = 1
    m = 'Июль'
    print(sd, m, g)
elif d < 31 and m == 'Июль':
    sd = d + 1
    print(sd, m, g)
elif d == 31 and m == 'Июль':
    sd = 1
    m = 'Август'
    print(sd, m, g)
elif d < 31 and m == 'Август':
    sd = d + 1
    print(sd, m, g)
elif d == 31 and m == 'Август':
    sd = 1
    m = 'Сентябрь'
    print(sd, m, g)
elif d < 30 and m == 'Сентябрь':
    sd = d + 1
    print(sd, m, g)
elif d == 30 and m == 'Сентябрь':
    sd = 1
    m = 'Октябрь'
    print(sd, m, g)
elif d < 31 and m == 'Октябрь':
    sd = d + 1
    print(sd, m, g)
elif d == 31 and m == 'Октябрь':
    sd = 1
    m = 'Ноябрь'
    print(sd, m, g)
elif d < 30 and m == 'Ноябрь':
    sd = d + 1
    print(sd, m, g)
elif d == 30 and m == 'Ноябрь':
    sd = 1
    m = 'Декабрь'
    print(sd, m, g)
elif d < 31 and m == 'Декабрь':
    sd = d + 1
    print(sd, m, g)
elif d == 31 and m == 'Декабрь':
    sd = 1
    m = 'Январь'
    g = g+1
    print(sd, m, g)

