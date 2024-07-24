"=======================================Декораторы============================="
# функция высшего порядка - функция, которая принимает в аргументы другую функцию, создает внутри себя функцию, вызывает функцию, возвращает функцию
# Декоратор - функция высшего порядка, которая нужна чтобы расширять функционал функции, не изменяя ее (функция обертка)

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         from datetime import datetime
#         print('start:', datetime.now())
        #   start = datetime.now()
#         func(*args, **kwargs)
#         print('finish:', datetime.now())
#     return wrapper

# @decorator
# def hello():
#     print('Hello world')

# hello()

# @decorator
# def my_sqrt(x):
#     print(x ** 0.5)

# my_sqrt(25)

# def func_start_time(func):
#     def wrapper(*a, **k):
#         from datetime import datetime
#         now = datetime.now()
#         correct_format = now.strftime('%d.%m.%Y %H:%M')
#         print('фукнция запущена', correct_format)
#         func(*a, **k)
#     return wrapper

# @func_start_time
# def func1():
#     print('Hello')

# func1()


# def decorator(num):
#     def inner_decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(num):
#                 func(*args, **kwargs)
#         return wrapper
#     return inner_decorator


# @decorator(100)
# def hello():
#     print('hello world')

# hello()

#Напишите декоратор benchmark, который измеряет и выводит время выполнения декорированной функции в формате Время выполнения: {время} секунд..

import requests
from time import time

def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time()
        func()
        end = time()
        time_exec = end - start
        print(f"Время выполнения: {time_exec} секунд")
    return wrapper

@benchmark
def fetch_webpage() -> None:
    webpage = requests.get('https://google.com')

fetch_webpage()

