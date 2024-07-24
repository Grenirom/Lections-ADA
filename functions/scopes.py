"===================================Области видимости============================="
# LEGB - local enclosed global built-in

"==========================Built-in============================================"
# Встроенное пространство имен (list, sum, dict, print, input)

"===========================Global================================"
# Все переменные которые мы создали внутри одного файла
# чтобы посмотреть все глобальные переменные, можно использовать globals()

# a = 5
# b = 'hello'
# print(globals())
"=============================Local=========================================="
# локальное пространство имен - переменные, созданные внутри функции

# abc = 10

# def func(a, b):
#     print('GLOBALS', globals())
#     hello = 'hello'
#     print("LOCALS", locals())
#     print(a, b, hello)
#     print(abc)

# func(5, 7)
# print(hello)

"===================================Enclosed=============================="
#  замкнутое пространство имен - локальное пространство, у которого есть внутреннее локальное пространство

# var = 'global'

# def func():
#     #Локальное пространство для глобального пространства
#     # замкнутое пространство(потому что есть более локальное пространство)
#     var = 'enclosed'
#     def inner_func():
#         # локальное пространство для пространства func
#         var = 'local'
#         print(var) # 3) local
#     print(var) # 2) enclosed
#     inner_func()

# print(var) # 1) global
# func()

# count = 1

# def increase_count():
#     global count
#     print(count)
#     count += 1


# increase_count()
# increase_count()
# increase_count()
# increase_count()
# increase_count(

# def count(i):
#     counter = 0

#     def increase_counter():
#         nonlocal counter
#         # доступ на изменение переменной замкнутого пространства
#         print(counter)
#         counter += 1
    
#     for _ in range(i):
#         increase_counter()

# count(10)

