"======================================Функции=============================="
# функция - именнованный блок кода, который может принимать аргументы и возвращать результат

# def my_sum(x, y):
#     return x + y

# res = my_sum(5, 6)
# print(res)

# def my_len(obj):
#     count = 0
#     for element in obj:
#         count += 1
#     return count
# res = my_len(['hello', 1, 2, 3, 4, True, False, [1, 2, 3]])
# print(len(['hello', 1, 2, 3, 4, True, False, [1, 2, 3]]))
# print(res)

# a = 'skjldcmlksdc'
# count = 0
# for element in a:
#     count += 1
# print(count)

"""
DRY - (dont repeat yourself), функции соблюдают этот принцип
"""
"===============================Аргументы и параметры============================"
# параметры - переменные внутри функции, значения которым мы задаем при определении функции
# аргументы - переменные, которые мы передаем при вызове функции

# def my_len(obj, **kwargs): # оbj - параметр
#     count = 0
#     for element in obj:
#         count += 1
#     return count
# res = my_len([12]) # аргумент
# print(res)

"===========================Виды параметров==============================="
# 1) обязательные
# 2) не обязательные
# 2.1) c дефолтным значением
# 2.2) *args (все позиционные аргументы, которые не попали в обязательные, и с дефолтным значением)
# 2.3) **kwargs (все лишние именнованные аргументы)
"============================Виды аргументов====================================="
# 1) позиционные (по позиции)
# 2) именнованные (по названию (параметр=значение))

# def add_or_add_10(num1:int, num2=10) -> int:
#     """
#     Складывает 2 числа
#     Если второе число не передать, сложит первое с 10
#     """
#     return num1 + num2

# print(add_or_add_10(5))

"==============================*=================================="
# list1 = list(range(1, 11))
# list2 = [*range(1, 11)]
# print(list1)
# print(list2)

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# # dict2 = {**dict1} {'a': 1, 'b': 2, 'c': 3}
# # list1 = [*dict1] ['a', 'b', 'c']
# print(dict1)
# print(dict2)
# print(list1)

# def func(a, b=10, *args, **kwargs):
#     print('a -', a)
#     print('b - ', b)
#     print('args -', args)
#     print('kwargs -', kwargs)

# func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 123, 123,132, 13,213 ,12, 1,2,3 ,1, 3,21,1 ,312,213, k=10, d=123, v=32)
# a - 1
# b -  2
# args - (3, 4, 5, 6, 7, 8, 9, 10)
# kwargs - {'c': 10, 'd': 123, 'v': 32}
# func(b=1239123, a=8239)
# a - 8239
# b -  1239123
# args - ()
# kwargs - {}
# func(1)
# a - 1
# b -  10
# args - ()
# kwargs - {}

"================================Lambda======================================="
# lambda - анонимная функция, которая записывается в одну строку
lambda_func = lambda x: x**10
print(lambda_func(10))

"===================Калькулятор==========================================="

# calc = {
#     '+': lambda n1, n2: n1 + n2,
#     '-': lambda n1, n2: n1 - n2,
#     '*': lambda n1, n2: n1 * n2,
#     '**': lambda n1, n2: n1 ** n2,
#     '/': lambda n1, n2: n1 / n2,
#     '//': lambda n1, n2: n1 // n2,
#     '%': lambda n1, n2: n1 % n2,
# }


# def main():
#     try:
#         num1 = int(input('Введите первое число: '))
#         num2 = int(input('Введите второе число: '))
#         oper = input('Введите операцию: ')
#         func = calc[oper]
#         res = func(num1, num2)
#         print(num1, oper, num2, '=', res)
#     except ValueError:
#         print('Введите число')
#     except KeyError:
#         print('Такой операции нет')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя')

# while True:
#     main()
#     inp = input('Завершить (yes/no)? ')
#     if inp.lower() == 'yes':
#         break

db = [
    {'name': 'Nikita', 'password': hash('nikita123')},
    {'name': 'nikita2', 'password': hash('12345678')}
]

def in_database(name):
    for user in db:
        if user['name'] == name:
            return True
    return False

def register(name, password1, password2):
    if in_database(name):
        raise Exception('Пользователь с таким именем уже существует!')
    if password1 != password2:
        raise Exception('Пароли не совпали!')
    user = {'name': name, 'password': hash(password1)}
    db.append(user)
    print(db, '=================================')
    return 'Вы успешно зарегистрировались!'

def login(name, password):
    if not in_database(name):
        raise Exception('Пользователь не найден!')
    for user in db:
        if user['name'] == name:
            if user['password'] != hash(password):
                raise Exception('Пароль не верный!')
    return 'Вы успешно вошли в систему!'


def main():
    print('Добро пожаловать!')
    while True:
        try:
            action = input('Register:1, Login:2, Quit:3\n')

            if action == '3':
                break
            elif action == '1':
                name = input('Введите имя: ')
                p1 = input('Введите пароль: ')
                p2 = input('Повторите пароль: ')
                print(register(name, p1, p2))
            elif action == '2':
                name = input('Введите имя: ')
                password = input('Введите пароль: ')
                print(login(name, password))
            else:
                print('Не корректный выбор!')
        except Exception as error:
            print(error)

main()
