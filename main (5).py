a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

print(max(a, b))

#2

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if a + b > c:
    print('YES')
else:
    print('NO')

#3

a = int(input('Введите год: '))

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('YES')
else:
    print('NO')