"=============================Встроенные функции============================="
# map, filter, reduce, zip, enumerate

# zip - соединяет несколько последовательностей (получаем генератор, в котором элементы - tuple)

# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c']
# list3 = [10.5, 20.6, 100.54]

# zipped = zip(list1, list2, list3) #<zip object at 0x7f5848ae2e80>
# # print(zipped)
# for el in zipped:
#     print(el)

# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c', 'd', 'e']
# dict_ = dict(zip(list1, list2)) # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
# print(dict_)

"=============================Enumerate================================"
# enumerate - нумерует последовательность (по дефолту с 0) (так-же получаем генератор)

# enumerated = enumerate('hello') # <enumerate object at 0x7ff6f6bcb8d0>
# # print(enumerated)

# for el in enumerated:
#     print(el)
# (0, 'h')
# (1, 'e')
# (2, 'l')
# (3, 'l')
# (4, 'o')

# string = 'hello world'
# print(list(enumerate(string[5:]))) #[(0, ' '), (1, 'w'), (2, 'o'), (3, 'r'), (4, 'l'), (5, 'd')]

"===================================Map======================================"
# map - принимает функцию и последовательность (записывает в новую последовательность результат функции, в которую передаются элементы последовательности)

# list_ = ['1', '2', '3', '4', '5']
# mapped_list = list(map(int, list_))
# print(mapped_list) # [1, 2, 3, 4, 5]

# string = 'hello world'
# res = ''.join(map(lambda x: x.upper(), string))
# print(res)
# list_ = [1, 2, 3, 4, 5]
# print(list(map(lambda x: x**2, list_)))
# print(list2) #[1, 4, 9, 16, 25]

# list_ = [1, 2, 3, 4, 5]
# def to_2_degree(x):
#     return x ** 2
# print(list(map(to_2_degree, list_))) # [1, 4, 9, 16, 25]


"===============================Filter==========================================="
# filter - Возвращает генератор, с элементами, прошедшими филтр(какое-то условие), принимает в себя функци. и последовательность
# list1 = [1, 0, -2, -3, -4, 5, 10]
# filtered  = list(filter(lambda x: x > 0, list1)) # [1, 5, 10]
# print(filtered)

# users = [
#     {'name': 'nikita', 'age': 12},
#     {'name': 'nastya', 'age': 20},
#     {'name': 'artem', 'age': 19}
# ]
# for user in users:
#     print(user)

# оставить пользователей, которые старше 18

# res = list(filter(lambda user: user['age'] > 18, users))
# print(res)

"""
вывести только имена пользователей которые младше 15
"""

# filtered = filter(lambda user: user['age'] < 15, users)
# result = list(map(lambda x: x['name'], filtered))
# print(result)

"==============================Reduce================================"
from functools import reduce
# reduce - принимает функцию и последовательность, возвращает 1 результат (передаваемая функция должна принимать 2 аргумента)

# list_ = [1, 2, 3, 4, 5]
# res = reduce(lambda x, y: x*y, list_)
# print(res) # 120

# string = 'hello'
# res = reduce(lambda x, y: x + '$' + y, string)
# print(res)
# x = 'h', y = 'e' -> h$e
# x = 'h$e', y = 'l' -> h$e$l


# string = 'hello world'
# print(reduce(lambda x, y: string.replace(x, y), string)) # heddo wordd

# list_ = [1, 2, 4, 6, 7, 654, 3, 2, 3, 456, 5432, 1]
# # выведите самое маленькое число, с помощью reduce
# res = reduce(lambda x, y: x if x<y else y, list_)
# print(res)

# users = [
#     {'name': 'nikita', 'age': 12},
#     {'name': 'nastya', 'age': 20},
#     {'name': 'artem', 'age': 19},
# ]
# выведите самого младшего пользователя, с помощью reduce

# def min_dict(dict1, dict2):
#     if dict1['age'] < dict2['age']:
#         return dict1
#     return dict2

# res = reduce(min_dict, users)
# print(res)

# result = reduce(lambda x, y: x if x['age'] < y['age'] else y, users)
# print(result) # {'name': 'nikita', 'age': 12}


# 1) напишите программу, которая суммирует все элементы в списке используя какую-то встроенную функцию
from functools import reduce

# list1 = [1, 12000, 134, 12431, 43542]

# new_list = reduce(lambda x, y: x + y, list1)
# print(new_list) # 68108
# print(sum(list1))

# напишите программу которая возводит в квадрат каждый элемент списка

# list1 = [1, 12000, 134, 12431, 43542]

# res = list(map(lambda x: x**2, list1))
# print(res) # 1895905764


# напишите программу которая отбирает только четные числа из исходного списка

# list1 = [1, 12000, 134, 12431, 43542]

# result = list(filter(lambda x: x % 2 == 0, list1))
# print(result) # [12000, 134, 43542]

# напишите программу которая отбирает слова длина которых больше 7 из исходного списка

# list_ = ["inheritance", "solid", "polymorphism", "dry", "yagni"]

# res = list(filter(lambda word: len(word) > 7, list_))
# print(res)
a = 6
b = 7
a > b


# напишите программу которая считает количество четных и нечетных чисел в списке и выводит их количество в формате строки "четные: {колич'ество}, нечетные: {количество}"


# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list2 = len(list(filter(lambda x: x % 2 != 0, list1)))
# list3 = len(list(filter(lambda x: x % 2 == 0, list1)))
# result = F'четные: {list3}, нечетные: {list2}'
# print(result)

# напишите программу которая находит самое длинное имя в списке

# list1 = ["Paul", "George", "Ringo", "John"]
# res = reduce(lambda x, y: x if len(x) > len(y) else y, list1)
# print(res)

# Напишите програму которая меняет число на 'fizz' если оно делится на 3, и на строку 'buzz' если не делится, в диапазоне чисел от 1 до 50 включительно

# res = list(map(lambda x:'Fizz' if x % 3 == 0 else 'Buzz', range(1, 51)))
# print(res)

# напишите программу которая находит минимальное значение у элемента в списке

# list1 = [1, 2, 3, 4, 234, 534, 123, -123, 342, 654]

# res = reduce(lambda x, y: x if x < y else y, list1)
# print(res)
