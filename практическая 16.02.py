# 1 

a = float(input("Введите первую переменную \n >"))
b = float(input("Введите вторую переменную \n >"))
print (max(a,b), min(a,b))

# 2

a = int(input('Введите сторону квадрата: '))
b = int(input('Введите радиус круга: '))

S1 = 3.14 * (b ** 2)
S2 = a ** 4

if S2 >= S1:
    print ('впишется')
else:
    print('не впишется')
    
# 3

x = int(input('Введите y:'))

if y < 0:
    y = x ** 2
else:
    y = 1 / x ** 2
print (y)

# 4 

a = int(input('Введите сторону квадрата: '))
b = int(input('Введите радиус круга: '))

S1 = 3.14 * (b ** 2)
S2 = a ** 4

if S2 <= S1:
    print ('впишется')
else:
    print('не впишется')
    
# 5

a = float(input("Введите первую переменную \n >"))
b = float(input("Введите вторую переменную \n >"))
print (max(a,b))