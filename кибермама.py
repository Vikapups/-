#1
a = int(input("Введите число"))
b = int(input("Введите число"))
if a == 0 or b == 0:
    print (' ты идиот ноль писать ?')
elif a % 2 == 0 and b % 2 == 0:
    print(' сумма чисел равна ', a + b)
elif b % 2 != 0 and a % 2 != 0 :
    print('произведенние чисел', a * b)
elif a % 2 == 0 and b % 2 != 0 or a % 2 != 0 and b % 2 == 0:
    if a < b:
        print ('разность чисел', b - a)
    else:
        print ('разность чисел',a - b)

#2
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > 0 and num2 > 0:
    print( num1 + num2)
elif num1 < 0 and num2 < 0:
    print(num1 * num2)
elif num1 == 0 or num2 == 0:
    print("Cannot perform calculations with 0")
else:
    l_num = max ( num2, num1)
    s_num = min ( num1, num2)
    print ( l_num - s_num , ' разница ')

#3
a = int(input())

f = 1
if a == 0:
    print ('1')
else:
    while a > 1:
        f *= a
        a -= 1
    print ( f )

#доп
a = int(input("Сколько у вас писем?"))

if a > 100:
     print("Получите рассылку")
else:
     print("Сегодня без рассылки:(")
