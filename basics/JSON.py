"===============================JSON=================================="
# Javascript object notation - Универсальный формат, в котором мы можем хранить данные в типах данных, понятных почти для всех языков программирования

# import json

# json_list = "[1, 2, 3, 4, 5]"
# print(type(json_list)) # <class 'str'>

# python_list = json.loads(json_list)
# print(type(python_list)) # <class 'list'>


# Десериализация - перевод с JSON строки в python объекты
# .loads() - метод для десериализации с json строки
# .load() - метод для десериализации с json файла

# сериализация - перевод python объектов в json строку
# .dumps() - метод для сериализации в json строку
# .dump() - метод для сериализации в json файл

# with open('test.json', 'r') as file:
#     list_ = json.load(file)

# print(list_)
# list_.append((1, 2, 3))
# print(list_)
# list_.append((1, 2, 3))
# list_.append((1, 2, 3))
# list_.append((1, 2, 3))
# list_.append((1, 2, 3))
# list_.append((1, 2, 3))
# list_.append((1, 2, 3))
# print(list_)

# with open('test.json', 'w') as file:
#     json.dump(list_, file)
