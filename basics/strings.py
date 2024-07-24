# # "=================Строки==================="
# # # Строки - это неизменяемый тип данных, который предназначен ждя хранения текста, заключенного в одинарные или двойные кавычки

# # str_ = 'строка с одинарными кавычками'
# # str2 = "строка с двойными кавычками"
# # # error_string = 'неправильная строка"
# # str3 = """
# # Многострочный текст в двойных кавычках, 
# # можно использовать 'любые' "кавычки"
# # """

# # # str4 = 'Don\'t'
# # # str5 = "Don't"

# # # "========================Конкатенация=============="

# # # name = 'Никита'
# # # last_name = 'Гребнев'
# # # full_name = name + ' ' + last_name
# # # print(full_name)
# # # print('Никита' + ' ' + 'Гребнев')
# # # print('hello' * 10)

# # "==============Экранизация строк================="
# # # '\n' - переносит на новую строку
# # # print('hello\nworld')
# # # # print('hello')
# # # # print('world')

# # # # \t - табуляция
# # # print('hello\tworld')

# # # '\'' - отображение '
# # # "\"" - отображение "

# # # \v - перенос на новую строку со смещением вправо на длину предыдущей строки
# # # print('hello\vworld\vmy\vname')

# # # \r - перенос каретки на начало строки
# # # print('hello\rH21431')

# # "=================Форматирование строк========"

# # title = 'Iphone 15'
# # price = 1000
# # print(f'Название: {title}\nЦена: {price}')


# # format2 = 'Название: {}\nЦена: {}'
# # print(format2.format('Iphone15', '1000'))
# # print(format2.format('Iphone12', '700'))

# # format3 = 'Название: %s\nЦена: %s'
# # print(format3 % ('iphone15', 1000))

# # "=================Методы строк=================="
# # # Методы - это функции, которые относятся к определенному классу(типу данных), к ним мы обращаемся через точку

# # # print(dir(str)) # dir() - показывает все методы определенного типа данных(класса)

# # string = 'hello'
# # print(string.upper()) # переводит все символы строки в верхний регистр

# # string1 = 'HELLO'
# # # string2 = string1
# # print(string1.lower()) # переводит все символы строки в нижний регистр

# # print('HellO'.swapcase()) # переводит все символы строки в противоположный регистр

# # print('hello world'.title()) # Переводит первую букву каждого слова в верхний регистр
# # print('hello world'.capitalize()) # Переводит только первую букву первого слова в верхний регистр, остальные слова остаются неизменными
# # # print('sdljvnksdvsdjkv msd. dsv lkmsd'.capitalize())

# # # print('hello'.center(7, '=')) центрует нашу строку, по указаному ограничителю (1 значение - ограничение, 2 значение - разделитель)


# # print('world'.count('w')) # возвращает количество вхождение заданного символа

# # print('hello'.startswith('h')) # проверяет, начинается ли строка с заданного символа, возвращает True/False
# # print('Hello'.startswith('h')) # False

# # # .endswith() - проверяет, заканчивается ли строка заданным символом/символами, возвращает True/False
# # print('hello'.endswith('lo')) # True
# # print('hello'.endswith('O')) # False
# # print('hello'.endswith('hello')) # True


# # # .islower() - проверяет, находится ли строка полностью в нижнем регистре
# # print('hello world'.islower()) # True
# # print('hello wOrld'.islower()) # False

# # # .isupper() - проверяет, находится ли строка полностью в верхнем регистре
# # print('HELLO WORLD'.isupper()) # True
# # print('HeLLO WORLD'.isupper()) # False

# # # .isdigit() - проверяет, состоит ли строка полностью из чисел
# # print('123231312313'.isdigit()) # True
# # print('1авлж3231312313'.isdigit()) # False

# # # .isalpha() - проверяет, состоит ли строка только из букв
# # print('hello'.isalpha()) # True
# # print('hello324'.isalpha()) # False

# # print('hello123'.isalnum()) # True
# # print('1'.isalnum()) # True
# # print('hello'.isalnum()) # True

# # # .split() - возвращает список, который разделил по заданному разделителю на отдельные строки
# # print('hello world my name is nikita'.split())
# # # ['hello', 'world', 'my', 'name', 'is', 'nikita']

# # # .join() - соединяет список по указанному разделителю
# # print('-'.join(['hello', 'world', 'my', 'name', 'is', 'nikita']))
# # # hello-world-my-name-is-nikita

# # .strip() - убирает пробелы слева и справа
# # string = '               hello               world                                     '
# # print(string)
# # print(string.strip())

# # string = 'hello         '
# # # .lstrip() - убирает все пробелы слева
# # print(string.lstrip())
# # # .rstrip() - убирает все пробелы справа
# # print(string.rstrip())

# "===============Индексы=============="
# # Индекс - порядковый номер в последовательности (символа в строке), (индексация начинается с нуля)

# 'h e l l o w o r l d'
# #0 1 2 3 4 5 6 7 8 9
# #               -2 -1

# string1 = 'hello world'
# print(string1[10])
# print(string1[0])
# print(string1[-1])

# # срез - подстрока нашей строки
# print(string1[0:5]) # hello
# print(string1[0:4]) # hell
# print(string1[6:11]) # world
# print(string1[6:]) # world
# print(string1[6:-1]) # worl
# # print(string1[start:end:step])
# print(string1[::-1]) # dlrow olleh
# print(string1[::2]) # hlowrd
# print(string1[1:5]) # ello
# print(string1[1:5:2])

# immutable_string = 'Hello'
# print(immutable_string.upper())
# print(immutable_string)

print(dir('hello'))