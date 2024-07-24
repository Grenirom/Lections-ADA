# "=======================List=========================="

# # Списки - это изменяемый, индексируемый, упорядоченный, итерируемый тип данных, который прелназначен для хранения любых данных в определенном порядке


# list_ = [1, 2, 3, 'hello', [1, 2, 3], [[[1,2,3]]], None, цTrue, False, (1, 2, 3), {1: '1'}]

# print(list_[1])
# print(list_[3][-1])
# print(list_[-1])
# print(list_[4][2])


# new_list = list('hello world')
# print(new_list)

# # range() - задает диапозон чисел, принимает 3 аргумента, 1 - начало диапозона, 2 - конец, 3 - шаг

# list2 = list(range(1, 11))
# print(list2)

# list3 = [1] * 10
# print(list3)

"===============Методы списков======================="
# print(dir(list3))

# .append() - добавляет элемент в конец списка

list_ = []
list_.append(1)
print(list_)
list_.append(1)
list_.append(1)
list_.append(1)
print(list_)
list_.append('hello')
print(list_)

# .pop() - удаляет элемент из списка по индексу, и результатом метода будет удаленный элемент (метод возвращает удаленный элемент), если не указать индекс - удалит с конца

popped_el = list_.pop(4)
print(popped_el)
print(list_)
popped_el = list_.pop()
print(popped_el)

# list2 = [1, 2, 3]
# list2.pop(3)

# .remove() - удаляет элемент из списка по значению 
list2 = [1, 2, 3, 4, True, 'hello']
list2.remove(2)
list2.remove('hello')
print(list2)
# [1, 3, 4, True]


# .count() - считает количество принятого элемента в списке
print(list2.count(1))

list3 = ['hello', 'hello', 'hello']
print(list3.count('hello'))
print(list3.count(100))


# .index() - возвращает индекс первого вхождения принятого элемента

# list3 = ['hello', 'hello', 'hello', 1, 4, 100, None]

# print(list3.index(1))
# print(list3.index(11029190))

# .insert() - добавляет элемент в список по индексу
# list3 = ['hello', 'hello', 'hello', 1, 4, 100, None]

# list3.insert(0, 'world')
# print(list3)
# list3.insert(0, 'hello')
# print(list3)
# list3.insert(5, False)
# print(list3)

# .extend() - добавляет элементы принятого списка в первый список, изменяя его

list3 = ['hello', 'hello', 'hello', 1, 4, 100, None]
list4 = [1, 2, 3, 4, {'a': 123}]
list3.extend(list4)
# print(list3 + list4)
print(list3)

# .reverse() - изменяет список, расставляя его элементы в обратном порядке

list3.reverse()
print(list3)
# [{'a': 123}, 4, 3, 2, 1, None, 100, 4, 1, 'hello', 'hello', 'hello']

# .sort() - сортирует список, состоящий из элементов одного типа данных
# list3.sort()
# print(list3)
# TypeError: '<' not supported between instances of 'int' and 'dict'

list5 = [1, 2, 3, 100, 1223, 211, 2000, 8923490123285]

list5.sort()
print(list5)

list5.sort(reverse=True)
print(list5)
# list5 = ['a', 'b', 'c', 'A', 'B', 'hello']
# list5.sort()
# print(list5)

# .clear() - очищает список
list5.clear()
print(list5)

# len() - считает количество элементов в последовательности
list1 = [1, 2, 3, 4, 5, 6, 7, 8, [1, 2, 3]]
print(len(list1))
len(list1)

# множественное присваивание
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

a, b = [1, 22]
print(a)
print(b)

name, age, city = ['Nikita', 5, 'Bishkek']
print(name)
print(age)
print(city)
