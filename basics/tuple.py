"===========================Tuple=============================="
# Кортеж(tuple) - неизменяемый, индексируемый, упорядоченны, итерируемый тип данных, предназначенный для хранения любых данных в определенном порядке (в целом не отличается от списков, просто он не изменяемый, поэтому занимает меньше памяти)

# tuple1 = (1, 2, 3)
# print(type(tuple1)) # <class 'tuple'>
# tuple2 = (5) # <class 'int'>
# print(type(tuple2))

# tuple2 = tuple('hello')
# print(tuple2)
# # ('h', 'e', 'l', 'l', 'o')
# tuple3 = 1, 2, 3
# print(tuple3)

# tuple4 = (1, 2, 3, [1, 2, 3])
# tuple4[-1].append('hello')
# print(type(tuple4[-1])) # <class 'list'>

# tuple6 = tuple([1, 2, 3, 'hello', 1000, 1213123])
# print(tuple6) # <class 'tuple'>

# # print(dir(tuple6))

# '====================Методы Tuple============================='
# # .count() - считает количество принятого элемента в кортеже (tuple)

# tuple_ = (1, 1, 1, 1, 1, 1, 1, 1, 1, False, True)
# print(tuple_.count(1))

# tuple7 = ('hello', 'hello', 'hello')
# print(tuple7.count('hello'))

# # .index() - возвращает индекс первого вхождения принятого элемента
# tuple8 = (1, 2, 1, 1, 1, 1, 'hello', 100)
# print(tuple8.index(100)) # 7