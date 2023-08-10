s = 0
x = int(input("Введите целое число (0 для выхода): "))

if x == 0:
    print('Ошибка')

s = s + x
y = 1

while x != 0:
    x = int(input("Введите целое число (0 для выхода): "))
    if x == 0:
        sr = s/y
        print(sr)
    else:
        s = s + x
        y = y + 1
