# Приветствие программы
name = "Первая программа на Питоне"
age = 20
print ('Доброе утро\nменя зовут '+name+' и я учу азам ЯП Python!')
print ('Моему создателю '+str(age)+' лет!')
# программа просит пользователя ввести своё имя и возраст для начала работы
name1 = input('Введите Ваше имя: ' )
age1 = input('Введите Ваш возраст: ' )
print ('Привет ' + name1 + '!')
print ('Тебе уже ' + age1 + ' лет!')
# далее учимся базовым математическим операциям
# +,-,/,*,**(возведение в степень),
# %(остаток от деления) унарный минус,округление,константа пи
#a = 5
#b = 10
#c=a+b
#print(c)
#a=5
#b=7
#c=a-b
#print(c)
#a=5
#b=10
#c=b/a
#print(c)
#a=5
#b=2
#c=a*b
#print(c)
#a=5
#b=2
#c=a**b
#print(c)
#a=10
#b=7
#c=10%7
#print(c)
#a = 10
#a =-a
#print(a)
#ELECTRORAZVEDKA = 4.88
#SEISMIC = 1.22
#print (round(ELECTRORAZVEDKA))
#import math
#print (math.floor(ELECTRORAZVEDKA))
#print(math.ceil(SEISMIC))
#a=-a
#print(math.factorial(a))
#print(math.pi)
#### К А Л Ь К У Л Я Т О Р ####
from colorama import init
from colorama import Fore, Back, Style
init()
print(Fore.BLACK)
print(Back.MAGENTA)
what = input('Что делаем, босс? Выбери операцию (+, -, *, /): ')
print(Back.CYAN)
if what == '+':
    a = float(input('Введи первое число: '))
    b = float(input('Введи второе число: '))
    c = a + b
    print(Back.GREEN)
    print ('Результат: ' + str(c))
elif what == '-':
    a = float(input('Введи первое число: '))
    b = float(input('Введи второе число: '))
    Print(Back.GREEN)
    c = a - b
    print ('Результат: ' + str(c))
elif what == '*':
    a = float(input('Введи первое число: '))
    b = float(input('Введи второе число: '))
    c = a * b
    Print(Back.GREEN)
    print ('Результат: ' + str(c))
elif what == '/':
    a = float(input('Введи первое число: '))
    b = float(input('Введи второе число: '))
    c = a / b
    Print(Back.GREEN)
    print ('Результат: ' + str(c))
else:
    Print(Back.RED)
    print('Введена неверная операция')
print('Нажмите любую клавишу, чтобы завершить работу')
input()