#1
a = input("Какое сейчас время суток?")
if a == 'утро':
    print("Пора вставать")
elif a == 'день':
    print("Пора учиться")
elif a == 'ночь':
    print("Пора спать")

#2
par = str (input('Введите пароль:'))
par1 = str (input('Для проверки, повторно введите пароль:'))

if par == par1:
    print('пароль правильный')
else:
    print('пароль не подходит')

#3
otpravka = str (input("отправиться сейчас?"))
da = 'да'
if otpravka  == da:
    pri = str (input( "Все ли припасы загружены в лодку?") )
    if pri == da:
        print( ' В путь!')
    else:
     print ("Стоит подготовиться лучше")
else:
    print('Скажи, как будешь готов.')
