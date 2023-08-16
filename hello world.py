x = 0
a = 0
s = 0

while x != "":
    x = input('Введите оценку (Enter для выхода): ')
    if x == "A+":
        s = s + 4.0
        a = a + 1
    elif x == "A":
        s = s + 4.0
        a = a + 1
    elif x == "A-":
        s = s + 3.7 
        a = a + 1
    elif x =="B+":
        s = s + 3.
        a = a + 1
    elif x == "B":
        s = s + 3.0
        a = a + 1
    elif x == "B-":
        s = s + 2.7
        a = a + 1
    elif x == "C+":
        s = s + 2.3
        a = a + 1
    elif x == "C":
        s = s + 2.
        a = a + 1
    elif x == "C-":
        s = s + 1.7
        a = a + 1
    elif x == "D+":
        s = s + 1.3
        a = a + 1
    elif x == "D":
        s = s + 1.0
        a = a + 1
    elif x == "A":
        s = s + 0
        a = a + 1

z = s / a
print('Средняя оценка: ', z)



















