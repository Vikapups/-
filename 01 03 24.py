#1

sec_name = input("Введите фамилию \n >")
country = input("Введите страну \n >")
year = int(input("Введите год \n >"))
money = int(input("Введите стоимость \n >"))
date = int(input("Введите дату поездки \n >"))
print (f' Ваша фамилия: {sec_name} \n Страна: {country} \n Год: {year} \n Стоимость: {money} \n Дата поездки: {date}')

#2

a = int(input())
b = int(input())
c = int(input())
d = a *(b/3.14)+(c*3+5)
print (d)

#4

a = float (input())

if a >= 0:
    b = a // 1
    c = a % 1
    d = a ** 2
    f = a % 5
    print (int(b), c, d, f)
else: 
    pass

#5

a = int(input())

b = a // 60
c = a - b * 60

print ( f' {b} часов и {c} минут ')