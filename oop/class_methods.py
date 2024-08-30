# # class methods - методы, которые принимает первым аргументом cls (ссылка на класс). Нужны они для создания объектов, или изменения аттрибутов класса. для создания метода класса нужно задекорировать его в classmethod


# class B:
#     @classmethod
#     def class_method(cls):
#         print('класс метод')
#         print('первый аргумент', cls)

# obj1 = B()
# B.class_method()
# obj1.class_method()


# class A:
#     def hello(self):
#         print('hello')

# obj2 = A()
# # A.hello()


# # class C:
# #     counter = 0

# #     def __init__(self):
# #         self._inc_counter()

# #     def __del__(self):
# #         self._dec_counter()
# #         del self

# #     @classmethod
# #     def _inc_counter(cls):
# #         cls.counter += 1

# #     @classmethod
# #     def _dec_counter(cls):
# #         cls.counter -= 1


# # obj1 = C()
# # obj2 = C()
# # obj3 = C()
# # print(C.counter)
# # del obj2
# # print(C.counter)


# # static methods - просто функции внутри класса, которые не взаимодействуют ни с классом, ни с объектом. Находятся они внутри класса лишь потому, что они используются только внутри класса, и вне они в целом бесполезны.Чтобы создать static метод, нужно его задекорировать staticmethod

# class D:

#     @staticmethod
#     def hello(string):
#         print(string)
        
# obj_d = D()
# obj_d.hello('hello world')
# D.hello('hello world')


# class Cylinder:
#     def __init__(self, diameter, height) -> None:
#         self.di = diameter
#         self.h = height
#         self.area = self.get_area(diameter, height)

#     def a(sfjv):
#         ...

#     @staticmethod
#     def get_area(di, h):
#         from math import pi
#         circle = pi * di ** 2 / 4
#         side = pi * di * h
#         area = circle * 2 + side
#         return round(area, 2)
    
# cylinder1 = Cylinder(4, 10)
# print(cylinder1.area) # 150.8

# area2 = Cylinder.get_area(2, 5)
# print(area2) # 37.7

# KISS - keep it simple stupid
# YAGNI - you aint gonna need it
# SOLID - 

# Создайте класс MathOperations, который будет иметь статический метод add для сложения двух чисел. Вызовите этот метод без создания объекта класса.

# class MathOperation:
#     @staticmethod
#     def add(a, b):
#         return a + b
    
# print(MathOperation.add(5, 5))
# res = MathOperation.add(5, 5)
# print(res)


# Создайте класс Person, в котором будет метод from_birth_year, который принимает год рождения и вычисляет возраст. Реализуйте этот метод как метод класса.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_birth_year(cls, name, birth_year):
#         current_year = 2024
#         age = current_year - birth_year
#         return cls(name, age)
    
# person = Person.from_birth_year('John', 1998)
# print(person.name, person.age)
