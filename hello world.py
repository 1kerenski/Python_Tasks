x = int(input('Введите номинал банкноты: '))
if x == 1:
    print('Портрет Джоржда Вашингтона')
elif x == 2:
    print('Портрет Томаса Джефферсона')
elif x == 5:
    print('Портрет Авраама Линкольна')
elif x == 10:
    print('Портрет Александра Гамильтона')
elif x == 20:
    print('Портрет Эндрю Джексона')
elif x == 50:
    print('Портрет Улисса Гранта')
elif x == 100:
    print('Портрет Бенджамина Франклина')
else:
    print('Ошибка')
