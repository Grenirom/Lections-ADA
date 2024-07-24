"========================================Модули и пакеты=========================="
# любой файл с расширением .py - модуль
# пакет - набор модулей (обязательно должен быть файл __init__.py)

"============================Работа с файлами=================================="
# open() - функция, которая открывает файл в определенном режиме
'Режимы'
# r - read (только для чтения)
# w - write (только для записи, если такого файла нет, то он его создаст. Каждый раз файл очищается)
# a - append (только для дозаписи, данные добавляются в конец)
# x - создает файл, но если файл существует выйдет ошибка
# b - binary (в бинарном виде)

"============================Read========================================"
# file = open('tesjnt.txt', 'r')
# print(dir(file))
# print(file.writable()) # False (проверяет, можно ли записывать что-то в файл)
# print(file.readable()) # True
# print(file.read())
# """
# hello
# world
# ADA
# """
# print(file.read()) # '' (потому что каретка находится в конце)
# file.seek(0) (метод переносит каретку на самое начало) 
# print(file.read())
# print(file.read(50))
# print(file.read(3))
# print(file.read(3))
# print(file.read(3))
# file.seek(0)
# print(file.readline()) # hello (читает одну строку)
# print(file.readline())
# print(file.readline())
# file.seek(0)
# print(file.readlines())
# # ['hello\n', 'world\n', 'ADA\n', 'komstlgfdc,;adsjnm;kflav\n', "afvm'sdfjlv\n", 'ldsfvkms\n', "dfvlmsdfvkjnsdf;kvjavsmdf;kvja'sdfjlvfsvkjsfv\n"]

# file.close()

# print(file.readlines())

"======================================Write============================="
# file = open('test2.txt', 'w')
# Если такого файла нет, то он его создаст
# print(file.readable()) # False
# print(file.writable()) # True

# file2 = open('test.txt', 'w')
# стирает данные существующего файла, если они там есть

# file.write('hello\n') # принимает строку, и записывает ее в файл
# file.write('World\n')
# file.writelines(['hello', 'world\n']) # принимает список строк

# file.close()

"=============================Append============================================="
# file = open('test23.txt', 'a')

# print(file.readable()) # False
# file.write('hello')
# file.seek(0)
# file.writelines(['hello', 'hello'])

# file.close()
"============================Контекстный менеджер============================="
# конструкция with ... as ...

# try:
#     file = open('sjfdvkml', 'w')
#     file.read() # ошибка
# finally:
#     file.close()

# with open('test23.txt', 'r') as f:
#     print(f.read()) # hellohellohello

# print(f.closed) # True
# 1) Создайте файл, внесите туда небольшой текст. В программе откройте этот файл и выведите содержимое на экран. 

# with open('test23.txt', 'r') as file:
#     content = file.read()
#     print(content)

# 2) Создайте файл users.txt. Напишите программу которая спрашивает у пользователя его Логин и Пароль и записывает в файл users.txt
# login = input('Введите логин: ')
# password = input('Введите пароль: ')

# with open('users.txt', 'w') as file:
#     file.write(f'Логин: {login},\nПароль: {password}')

#  Создайте программу, которая считает из файла текст, и если в тексте содержится буква “w”, то выведет на экран “Да, в тексте есть w”, иначе - “Нет, в тексте нет w”. Подсказка: используйте ключевое слово in.

# with open('test.txt', 'r') as file:
#     content = file.read()

# if 'hello' in content:
#     print('Да, в тексте есть w')
# else:
#     print('Нет, в тексте нет w')
# 4) Создайте текстовый файл python.txt и запишите в него текст #1 из github: Затем, считайте его. Найдите слова которые содержат букву  "o" и запишите в список o_words=[] и 
#   выведите на экран все полученные слова.
# text = """
# Next, install the Python 3 interpreter on your computer. This is the program that reads Python programs and carries out their instructions;
# you need it before you can do any Python programming. Mac and Linux distributions may include an outdated version of Python (Python 2),
# but you should install an updated one (Python 3). See BeginnersGuide/Download for instructions to download the correct version of Python.
# """

# with open('python.txt', 'w') as file:
#     file.write(text)

# with open('python.txt', 'r') as file:
#     content = file.read()

# o_words = [word for word in content.split() if 'o' in word]
# print(o_words)

# 5)  Возьмите текст №2(GitHub), запишите его в файл. Далее считайте этот текст с файла и выведите в обратном порядке.

# text = """
# .detacilpmoc naht retteb si xelpmoC
# .xelpmoc naht retteb si elpmiS
# .ticilpmi naht retteb si ticilpxE
# .ylgu naht retteb si lufituaeB

# """

# with open('task5.txt', 'w') as file:
#     file.write(text)

# with open('task5.txt', 'r') as file:
#     content = file.read()
#     reversed_content = content[::-1]
#     print(reversed_content)

# 6) Создайте файл и запишите туда текст №3(github). В каждой строчке есть цифры, которые вместе дадут число. Посчитайте сумму всех чисел.

text = """
123
aaa456
fxdya 5 0 0
"""
import csv

with open('task6.txt', 'w') as file:
    file.write(text)

total_sum = 0
with open('task6.txt', 'r') as file:
    for line in file:
        for word in line.split():
            number = ''.join(filter(str.isdigit, word))
            if number:
                total_sum += int(number)

print(f'Сумма чисел: {total_sum}')
