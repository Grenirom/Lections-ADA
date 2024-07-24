"=======================================Set====================================================="
# set(множество) - изменяемый, неупорядоченный, итерируемый, неиндексируемый тип данных, который предназзначен для хранения уникальных значений, Множества могут хранить в себе только не изменяемый типы данных. Если вы используете tuple, то в них тоже должны быть неизменяемые типы данных

"""
FIFO
LIFO
"""
# set_ = {1, 2, 3, 4}
# set2 = {1, 1, 1, 1, 2, 2, 2, 3, 3, 5, 5}
# print(set2) #{1, 2, 3, 5}

# set_ = {(1, 2, 3), 3, (4, 5, 6), (1, 2, 3)}
# print(set_) # {3, (1, 2, 3)}, {3, (4, 5, 6), (1, 2, 3)}

"=========================================Методы set=============================="
# print(dir(set_))

# .add() - Добавляет элементы в set
# set1 = {1, 2, 3, 4, 5}
# set1.add(6)
# set1.add(7)
# set1.add(True)
# print(set1) # {1, 2, 3, 4, 5, 6, 7}

# .pop() - удаляет случайный элемент из set (но есть принцип FIFO)
# set2 = {1, 2, 3}
# popped = set2.pop()
# set2.pop()
# set2.pop()
# # set2.pop() # KeyError: 'pop from an empty set'
# print(set2, popped)

# .remove() - удаляет элемент из set по значению
# set_ = {1, 2, 3}
# set_.remove(3) # KeyError: 5, если указать не существующий элемент
# print(set_) # {1, 2}
# set1 = {}
# set1.remove() #AttributeError: 'dict' object has no attribute 'remove'
# print(set1)


# .difference() (-)
# set1 = {1, 2, 6}
# set2 = {3, 4, 5}
# print(set1 - set2) # {1, 2}
# print(set2 - set1) # {4, 5}

# # .symmetric_difference() - 
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(set1.symmetric_difference(set2)) # {1, 2, 4, 5}

# .intersection() (&)
# set1 = {1, 2, 3, 4, 5, 6, 7, 8}
# set2 = { 4, 5, 6, 7, 8, 9, 10}
# print(set1.intersection(set2)) # {4, 5, 6, 7, 8}
# print(set1 & set2) # {4, 5, 6, 7, 8}

# .clear()
# set1 = {1, 2, 3, 4}
# set1.clear()
# print(set1) #set()

# .union()в - возвращает множество, которое содержит все элементы из всех переданных множеств

# set1 = {1, 2, 3}
# set2 = {True, False, (1, 2, 3)}
# set3 = {4, 5, 6, 7}

# result = set1.union(set2, set3)
# print(result) # {False, 1, 2, 3, 4, 5, 6, 7, (1, 2, 3)}
# print(set1.union(set2, set3)) # {False, 1, 2, 3, 4, 5, 6, 7, (1, 2, 3)}

# .issubset() - проверяет, является ли одно множество, подмножеством другого (если все элементы одного множества присутствуют в другом, то вернется True)

# set1 = {1, 2}
# set2 = {1, 2, 3, 4, 5}
# print(set1.issubset(set2)) # True
# print(set2.issubset(set1)) # False

# .issuperset() - проверяет, является ли множество надмножеством другого множества.

# set1 = {1, 2, 3, 6, 5}
# set2 = {1, 2, 3, 4, 5}
# print(set1.issubset(set2)) # False
# print(set2.issubset(set1)) # True

# .isdisjoint() - проверяет, не имеют ли 2 множества общих элементов, возвращает True/False

# set1 = {1, 2, 3, 4, 5}
# set2 = {6, 7, 8, 9, 10}
# print(set1.isdisjoint(set2)) # True

# .discard() - удаляет элмент по указанному значению, если элемент отсутствует, то ошибка не вызывается

# set1 = {1, 2, 3, 4}
# set1.discard(3)
# print(set1) # {1, 2, 4}

d1 = {"a": 100, "b": 200, "c":300}

d2 = {a: 300, b: 200, 'd':400}

print(d1["b"] == d2["b"])

