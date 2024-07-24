# '====================================Exceptions==============================='
# # Исключения (ошибки) - объекты, которые прерывают работу кода, если не были обработаны

# SyntaxError
# # Исключение, которое выходит когда в коде допущена синтаксическая ошибка
# """
# (
# SyntaxError: unexpected EOF while parsing
# (когда мы не закрыли скобочку или кавычку)
# """

# """
# a = 
# SyntaxError: invalid syntax
# (когда мы сделали что-то не правильно в синтаксисе)
# """

# # print(00000000000000)
# # print(9 / 0

# NameError
# # Исключение, которое выходит, когда мы обращаемся к несуществующей переменной
# # print(alknsfdlkmads)
# """
# NameError: name 'alknsfdlkmads' is not defined
# """

# IndexError
# # Исключение, которое выходит, когда мы обращаемся по несуществующему индексу
# # list_ = [1, 2, 3]
# # print(list_[1000])
# """
# IndexError: list index out of range
# """
# # [1, 2, 3].pop(1000)
# # IndexError: pop index out of range

# # [].pop()
# # IndexError: pop from empty list

# KeyError
# # исключение, которое выходит, когда обращаемся по несуществующему ключу
# # dict_ = {1: 1}
# # dict_['b'] # KeyError: 'b'
# # dict_.pop('b') # KeyError: 'b'

# ValueError
# # когда мы передаем в функцию не корректный для нее тип данных
# # когда мы распаковываем итерируемый объект на несколько переменных и кол-во переменных не совпадает с кол-вом элементов в итерируемом объекте
# # int('dsflj') # ValueError: invalid literal for int() with base 10: 'dsflj'

# # a, b, c = [1, 2] # ValueError: not enough values to unpack (expected 3, got 2)

# IndentationError
# # выходит, когда мы не правильно используем отступы

#     # a = 5 # IndentationError: unexpected indent

# # for i in range(10):
# # print(i) # IndentationError: expected an indented block after 'for' statement on line 59


# TypeError
# """
# когда мы пытаемся использовать методы не свойственные какому-то типу данных
# или когда мы пытаемся передать функции больше или меньше аргументов, чем  принимает функция
# """
# # for i in 123: # TypeError: 'int' object is not iterable
#     # ...

# # '5' + 5 TypeError: can only concatenate str (not "int") to str

# # 5 + '5' # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# # {[1, 2, 3]: 'hello'} # TypeError: unhashable type: 'list'

# # input('hello', 1) TypeError: input expected at most 1 argument, got 2


# Exception
# # исключение, которое создали, чтобы его вызвали

# "================================Вызов исключений=============================="

# # raise NameError('my exception') # NameError: my exception


# "=============================Обработка исключений==========================="
# # чтобы код не прекращал свою работу, мы можем использовать конструкцию try-except, и обрабатывать вызванное исключение

# try:
#     # код который возможно вызовет ошибку
#     num = int(input('Введите число'))
# except ValueError: # ошибка, которая может возникнуть
#     print('Вы ввели не число')
# else:
#     #код который отработает, только если ошибка не вышла
#     print('Введенное число', num)
# finally:
#     # Код, которвый отработает в любом случае
#     print('до свидания')


# try:
#     raise ValueError
# except (SyntaxError, NameError):
#     print('Вышла одна из ошибок: SyntaxError, NameError')

# try:
#     raise Exception
# except:
#     print('Отловленна любая ошибка')

# from math import sqrt as kvadratnyi_koren


# try:
#     raise TypeError('Type error')
# except Exception as error:
#     print('Ошибка', type(error).__name__)


# 1) напишите полный синтаксис конструкции try-except

# try:
#     pass
# except:
#     pass
# else:
#     pass
# finally:
#     pass

# 2)Напишите код, который пытается вывести значение переменной, не определенной ранее, и обрабатывает исключение, выводя сообщение "Такой переменной не существует!".

# b = 10
# c = 11

# try:
#     print(a)
# except NameError:
#     print('Такой переменной не существует')

# 3) Напишите код, который принимает два числа от пользователя и выводит результат их деления. Обработайте исключение, которое выйдет при делении на ноль, выводя сообщение "На ноль делить нельзя"

# num1 = int(input())
# num2 = int(input())

# try:
#     num1 = int(input())
#     num2 = int(input())
#     print(num1 / num2)
# except (ZeroDivisionError, ValueError):
#     print('На ноль делить нельзя')

#4)Напишите код, который принимает две строки от пользователя, преобразует их в целые числа и выводит их сумму. Обработайте исключение которое выйдет в случае если пользователь передал не число а строку, выводя сообщение "Введите число!"

# num1 = input()
# num2 = input()

# try:
    # print(int(num1) + int(num2))
# except ValueError:
#     print('Введите число')

# 5)  Напишите код, который пытается получить значение по ключу из словаря. Обработайте исключение, которое выйдет если такого ключа нет, выводя сообщение "Нет такого ключа!".

# dict_ = {'a': 1, 'b': 2, 'c': 3}

# try:
#     print(dict_['g'])
# except KeyError:
#     print('Такого ключа не существует')


# 6)напишите код, который пытается получить элемент списка по индексу. Обработайте исключение которое выйдет если такого индекса нет, выводя сообщение "Нет такого элемента!"

# list_ = [1, 2, 3, 4, 5]

# try:
#     print(list_[100])
# except IndexError:
#     print('Нет такого элемента')

# 7)Напишите код, который принимает возраст от пользователя и выбрасывает исключение ValueError с сообщением "Доступ запрещён", если возраст меньше 18. Обработайте это исключение, выводя сообщение "Введён некорректный возраст". Используйте блоки else и finally для вывода сообщений "Спасибо" и "До свидания!" соответственно.

# try:
#     age = int(input('Введи возраст'))
#     if age < 18:
#         raise ValueError('Доступ запрещен')
# except ValueError:
#     print('Введен некорректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания')

# 8) Напишите код, который принимает два числа от пользователя и выводит результат их деления. Обработайте исключения ValueError и ZeroDivisionError, выводя сообщение "Произошла ошибка!".

# try:
#     num1 = int(input())
#     num2 = int(input())
#     print(num1 / num2)
# except (ValueError, ZeroDivisionError):
#     print('Произошла ошибка')

# 9) Напишите код, который принимает сумму денег от пользователя и выбрасывает исключение ValueError с сообщением "Сумма не может быть отрицательной!", если сумма меньше 0. Обработайте это исключение и выведите сообщение ошибки. Если исключение не возникло, выведите сумму.

# try:
#     summa = float(input())
#     if summa < 0:
#         raise ValueError('Сумма не может быть отрицательной')
# except ValueError:
#     print('Введи корректное число')
# else:
#     print(summa)


# 11) Напишите код, который пытается сложить строку и число. Обработайте исключение TypeError, выводя сообщение "Unsupported option"

# num = 2
# str_ = 'hello'

# try:
#     print(num + str_)
# except TypeError:
#     print('Unsupporter Option')

# 12) Напишите код, который пытается расширить список, который не был создан. Обработайте исключение NameError, и выведите сообщение 'list does not exist'.

# try:
#     list_.extend([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# except NameError:
#     print('list does not exist')

# 13) Напишите код, который перебирает элементы списка, превышая его длину. Обработайте исключение IndexError, не выполняя никаких действий при возникновении ошибки.
# list_ = [1, 2, 3, 4, 5, 6, 7]

# try:
#     for i in range(0, len(list_) + 1):
#         print(list_[i])
# except IndexError:
#     print('Ошибка')

#  14)Напишите код, который проверяет длину пароля и выбрасывает исключение ValueError, если длина меньше 6 символов. (можно без try-except, просто через raise выкидывать ошибку)

# password = '12345'
# if len(password) < 6:
#     raise ValueError('Длина пароля не должна быть меньше 6 символов')


# try:
#     password = int(input('Введи пароль: '))
#     if len(str(password)) < 6:
#         raise ValueError('Длина пароля не должна быть меньше 6 символов')
# except ValueError:
#     print('Пароль должен состоять только из чисел')

# 15)
warehouse = [
    [[1, 2, 3], [1, 2, 3, 4, 5], {'hello': 'world'}],
    ['1', '2', '3'],
    [1, 2, 3, 4 , 5, 6],
    [[1], [2], [3]],
    [[1, 2, 3], [1, 2, 3, 4, 5], {'hello': 'world'}],
]
# Напишите код, который проверяет длину хранилища и выбрасывает исключение ValueError, если длина больше 10. Также выбрасывайте исключение ValueError, если какой-либо вложенный список внутри хранилища имеет длину больше 3.

# if len(warehouse) > 10:
#     raise ValueError("На складе не должно быть более 10 коробок")

# for box in warehouse:
#     if len(box) > 3:
#         raise ValueError('В коробке не должно быть более 3-х элементов')
    
# 16) Напишите код, который пытается импортировать несуществующий модуль lamabimgo. Обработайте исключение ImportError, выводя сообщение "Такого модуля нет".

# try:
#     import lamabimgo
# except ImportError:
#     print('Такого модуля не существует')

# 17) Напишите код, который уменьшает значение переменной в цикле while. Обработайте исключение KeyboardInterrupt, выводя сообщение "Nope".

# n = 100000000000000

# try:
#     while n > 1:
#         n -= 1
# except KeyboardInterrupt:
#     print('nope')

# 18) Напишите код, который принимает строку, разделяет её на элементы и пытается преобразовать каждый элемент в целое число, добавляя его в список. Если элемент не является числом, выбрасывайте исключение ValueError с сообщением "Данный элемент не является числом!".

# inp1 = input().split()
# print(inp1)
# list_ = []

# for element in inp1:
#     try:
#         list_.append(int(element))
#     except ValueError:
#         print('Данный элемент не является числом')

# print(list_)
