a = int(input('Введите длину стороны: '))
b = int(input('Введите длину стороны: '))
c = int(input('Введите длину стороны: '))
if a == b and b == c:
    print('Равносторонний')
elif a == b or b == c or c == b:
    print('Равнобедренный')
else:
    print('Разносторонний')






