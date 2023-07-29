m = input('Введите месяц: ')
d = int(input('Введите день: '))
if m == 'Январь' or m == 'Февраль':
    print('Зима')
elif m == 'Март':
    if d < 20:
        print('Зима')
    elif d >= 20:
        print('Весна')
elif m == 'Апрель' or m == 'Май':
    print('Весна')
elif m == 'Июнь':
    if d < 21:
        print('Весна')
    elif d>= 21:
        print('Лето')
elif m == 'Июль' or m == 'Август':
    print('Лето')
elif m == 'Сентябрь':
    if d < 22:
        print('Лето')
    elif d >= 22:
        print('Осень')
elif m == 'Октябрь' or m == 'Ноябрь':
    print('Осень')
elif m == 'Декабрь':
    if d < 21:
        print('Осень')
    elif d >= 21:
        print('Зима')


