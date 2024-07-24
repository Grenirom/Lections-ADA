"=============Числа=================="
# integers(int) - целые числа (1, 3, 6)

# age = 10
# print(type(age)) # <class 'int'>
# type() - возвращает  класс/тип данных к которому относится переменная или значение

# b = int('10j') # ValueError: invalid literal for int() with base 10: '10j'
# print(type(b))
# b = int('10')
# print(type(b)) #<class 'int'>


"=============float============="
#float - вещественные числа/числа с плавающей точкой/десятичные

# price = 105.5
# print(type(price)) # <class 'float'>

# price2 = float(1) # 1.0
# print(price2)

# price3 = float('10.64')
# print(price3) # 10.64
# print(type(price3)) # <class 'float'>
# print(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1) # 0.9999999999999999

# import decimal
# from decimal import Decimal

# a = Decimal('0.1')
# print(a) # 0.1
# print(type(a)) # <class 'decimal.Decimal'>
# print(a + a + a + a + a + a + a + a + a + a)

"==================binary================="

# a = bin(10) 
# print(a) # 0b1010
# print(int(a, 2)) # 10

"====================Операции над числами==========="

5 + 7 # сложение
7 - 3 # вычитание
10 * 4 # умножение
10 / 3 # деление
10 // 2 # целочисленное деление
5 % 2 # нахождение остатка от деления
2 ** 3 # возведение числа в степень(квадрат/куб и тд.)
25 ** 0.5 # 5, нахождение квадратного корня

# модуль числа - из отрицательного числа в положительное |-5| = 5
# abs() - для получения положительного числа

# print(abs(-5))
# print(abs(-1000.213))
# print(abs(-585839435))


# round() - округление числа
# print(round(1.3))
# print(round(1.6))
# print(round(13.49))
# print(round(1.5))
# print(round(1.51))

"""
python3 <название файла> - запуск файла через терминал

python3 - вход в python shell
ctrl + d - выход из shell
"""


# sqrt - функция для нахождения квадратного корня числа. sqrt обязательно нужно импортировать
# import math
# from math import sqrt

# print(sqrt(25))
# print(sqrt(36))
# print(sqrt(34))

"""
чтобы закоментировать выделенную область, нужно нажать сочетание клавиш ctrl + /
"""


# pow
# 1) возводит число в степень
# 2) находит остаток от деления на 3 число

# print(pow(2, 3)) # 2 ** 3 = 8
# print(pow(2, 3, 3)) # 2 ** 3 % 3 = 2


# divmod() - функция, которая возвращает 2 числа, где 1 число - целая часть от деления, 2 число - остаток от деления

# print(divmod(8, 4)) # (2, 2)
# print(divmod(5, 2)) # (2, 1)
# print(divmod(17, 3)) # (5, 2)

# number1 = input('Введи число: ')
# number2 = input('Введи второе число: ')
# print(int(number1) + int(number2))
# print(number1)
# print(type(number1))