# "===============================Словари======================================="
# # dict - изменяемый, итерируемый, неупорядоченный, неиндексируемый тип данных, для хранения данных в паре {ключ: значение}

# user = {
#     'name': 'Nikita',
#     "city": 'Bishkek',
#     'country': 'Kyrgyzstan',
# }

# print(user['name'])
# print(user['city'])

# # Ключами в словаре могут быть только не изменяемые типы данных


# dict1 = {'a': 1, 'b': 2, 'c': 3, 'a': 4}

# print(dict1['a']) # 4, Если ключи одинаковые, то сохранится только последнее значение
# # print(dict1['d']) # KeyError: 'd'

# dict1 = {'a': 1, 'b': 2}
# dict2 = dict( [ ('a', 1), ('b', 2) ] )
# # print(dict2) # {'a': 1, 'b': 2}
# dict3 = dict( ["ab", "cd", "ef"] )
# # print(dict3) # {'a': 'b', 'c': 'd', 'e': 'f'}

# dict4 = {'name': 'Nikita', 'city': 'Bishkek'}
# dict4['name'] = 1
# print(dict4) # {'name': 'Nikita', 'city': 'Bishkek'}

# "======================================Методы словарей============================"
# # print(dir(dict4))
# # .get() - метод, который возвращает значение по ключу, если такого ключа нет, то возвращает None, или дефолтное значение
 
# user = {
#     'name': 'Nikita',
#     "city": 'Bishkek',
#     'country': 'Kyrgyzstan',
# }

# print(user.get('id'))
# print(user.get('name'))
# print(user.get('city'))
# print(user.get('country'))


# # .pop() - Метод, который удаляет пару по ключу и возвращает значение
# dict_ = {'a': 1, 'b': 2, 'c': 3}
# popped = dict_.pop("a")
# print(dict_)
# print(popped)
# # {'b': 2, 'c': 3}
# # 1
# # dict_.pop('a') KeyError: 'a'


# # .popitem() - метод, который удаляет последнюю пару и возвращает ее
# dict5 = {'a': 1, 'b': 2, 'c': 3}
# popped = dict5.popitem()
# print(dict5)
# print(popped)
# # {'a': 1, 'b': 2}
# # ('c', 3)

# dict0 = {}
# # print(dict0.popitem()) #KeyError: 'popitem(): dictionary is empty'


# .update() - расширяет словарь парами из второго словаря

# dict1 = {1: 'a', 2: 'b', 3: 'c'}
# dict2 = {2: 'c', 4: 'd'}
# dict1.update(dict2)
# print(dict1) #{1: 'a', 2: 'c', 3: 'c', 4: 'd'}

# # .clear() - удаляет все пары в словаре
# dict1.clear()
# print(dict1) # {}

# .fromkeys() - Метод для создания нового словаря, используя список ключей

# dict1 = dict.fromkeys('hi')
# print(dict1) # {'h': None, 'i': None}

# dict2 = dict.fromkeys([1, 2, 3])
# print(dict2) # {1: None, 2: None, 3: None}

# dict3 = dict.fromkeys([1, 2, 3], "hello") 
# print(dict3) #{1: 'hello', 2: 'hello', 3: 'hello'}


# print(dir(dict3))
"=========================================================================="

#keys, values, items
# keys - метод, который возвращает ключи
# values - метод, который возвращает значения
# items - метод, который возвращает пары ключ - значение, в виде tuple

# user = {
#     'name': 'Nikita',
#     "city": 'Bishkek',
#     'country': 'Kyrgyzstan',
# }

# print(user.keys()) # dict_keys(['name', 'city', 'country'])
# print(user.values()) # dict_values(['Nikita', 'Bishkek', 'Kyrgyzstan'])
# print(user.items()) # # dict_items([('name', 'Nikita'), ('city', 'Bishkek'), ('country', 'Kyrgyzstan')])

"==========================Итерирование словарей============================="

# user = {
#     'name': 'Nikita',
#     "city": 'Bishkek',
#     'country': 'Kyrgyzstan',
# }

# for key in user:
#     print(key)
#     # name
#     # city
#     # country
#     # при итерации словаря будут приходить ключи

# for key in user.keys():
#     print(key)
#     # name
#     # city
#     # country
#     # при итерации dict_keys тоже приходят ключи

# for value in user.values():
#     print(value)
#     # Nikita
#     # Bishkek
#     # Kyrgyzstan
#     # при итерации dict_values приходят значения

# for items in user.items():
#     print(items)
#     # ('name', 'Nikita')
#     # ('city', 'Bishkek')
#     # ('country', 'Kyrgyzstan')
#     # при итерации doct_items приходят пары (ключ - значение) в  tuple

# for key, value in user.items():
#     print(key, value)

"""
Ваи дан словарь 
"""
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# # Создайте новый словарь dict2, поменяв местами ключи со значениями
# # dict2 = {1: 'a', 2: 'b', 3: 'c'}

# dict2 = {}
# for key, value in dict1.items():
#     dict2[value] = key

# print(dict2)
# {1: 'a', 2: 'b', 3: 'c'}
