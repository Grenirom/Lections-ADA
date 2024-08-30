# '=======================================OOP======================================='
# # OOP - Объектно-ориентированное программирование (Парадигма)

# class Person:
#     # Переменные внутри класса (объекта) - аттрибуты класса
#     arms = 2
#     legs = 2
#     brain = 1
    
#     def __init__(self, name, age):
#         # __init__ - метод, который будет добавлять в объект те аттрибуты, которые отличаются у разных объектов
#         # self - ссылка на объект, который только что создался
#         # аттрибуты экземпляра класса
#         self.name = name
#         self.age = age

#     def walk(self):
#         print(f'{self.name} ходит')

#     def happy_birthday(self):
#         print(f'{self.name}, Happy birthday!')
#         self.age += 1
#         return 'Подарок'


# obj1 = Person('Nikita', 1)
# print(obj1.name)
# print(obj1.age)
# print(obj1.arms)
# obj1.walk()
# obj1.happy_birthday()
# print(obj1.age)
# # print(obj1.hello) # AttributeError: 'Person' object has no attribute 'hello'
# obj1.happy_birthday()
# "=======================================Объекты класса==========================="
# # объекты, экземпляр, instance класса - объект, созданный по шаблону класса (он перенимает все аттрибуты и методы класса)

# '===================================Аттрибуты и методы==========================='
# # аттрибуты - переменные
# # методы - функции

# class A:
#     var1 = 'Переменная класса'

#     def __init__(self) -> None:
#         self.var2 = 'Переменная объекта'

# print(dir(A))
# # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1']
# # нет var2
# obj2 = A()
# print(dir(obj2))
# # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1', 'var2']
# # var2 есть

# # class Calculator:
# #     def add(self, a, b):
# #         'Функция сложения'
# #         return a + b
    
# #     def sqrt(self, num, ndigits=2):
# #         'Функция нахождения квадратного корня числа с округлением'
# #         import math
# #         sqrt_num = math.sqrt(num)
# #         return round(sqrt_num, ndigits)
    
# #     def percent(self, total, percent):
# #         'функция нахождения процента от числа'
# #         return (total * percent) / 100
    
# #     def super_func(self, string):
# #         'Функция которая выполняет вычисления в строке'
# #         return eval(string)
    

# # calc = Calculator()
# # print(calc.add(10, 10))
# # print(calc.sqrt(5, 10))
# # print(calc.percent(1000, 10))
# # print(calc.super_func('(5-7)**2 - 10'))


# class Sniper:
#     health = 100

#     def __init__(self, name) -> None:
#         self.name = name

#     def shoot(self, sniper2):
#         sniper2.health -= 20
#         print(f'Атаковал {self}')
#         print(f'У {sniper2} осталось {sniper2.health}')

#     def __str__(self) -> str:
#         # когда принтим объект
#         # когда оборачиваем в строку
#         return self.name
    
# sniper1 = Sniper('Nikita', 8)
# sniper2 = Sniper('Sniper')

# import random
# while sniper1.health and sniper2.health:
#     choice = random.randint(1, 2)
#     if choice == 1:
#         sniper1.shoot(sniper2)
#     else:
#         sniper2.shoot(sniper1)

# if sniper1.health:
#     print(f'Победил {sniper1}')
# else:
#     print(f'Победил {sniper2}')

# 1) Нужно создать программу для банкомата, который принимает деньги и выдает деньги. Создайте класс Банкомат с методами: 

# Чтобы банкомат принимал деньги
# Чтобы банкомат выдавал деньги
# Чтобы банкомат показывал остаток денег

# class Bankomat:
#     # balance = 0
#     def __init__(self) -> None:
#         self.balance = 0

#     def deposit(self, sum):
#         if sum > 0:
#             self.balance += sum
#         else:
#             return 'Сумма не может быть меньше нуля'
#         return f'На вашем счету - {self.balance} сом'
    
#     def withdraw(self, amount):
#         if amount > self.balance:
#             return 'На вашем счету недостаточно средств'
#         self.balance -= amount
#         return f'На вашем счету - {self.balance} сом'

#     def show_balance(self):
#         return f'На вашем счету - {self.balance} сом'

# obj1 = Bankomat()
# print(obj1.show_balance())
# print(obj1.deposit(100000))
# print(obj1.withdraw(1000))

# 2) Создайте класс Song с атрибутами author, title и year. Напишите методы showauthor, showtitle и show_year, которые возвращают строки с информацией о песне. Создайте объект этого класса и выведите информацию о песне, используя методы.


# class Song:

#     def __init__(self, author: str, title: str, year: int) -> None:
#         self.author = author
#         self.title = title
#         self.year = year

#     def show_author(self):
#         return f'Автор этой песни: {self.author}'
    
#     def show_title(self):
#         return f'Название песни: {self.title}'
    
#     def show_year(self):
#         return f'Год выпуска песни: {self.year}'
    
# obj1 = Song('Sam Smith', 'Fire on fire', 2022)
# print(obj1.show_author())
# print(obj1.show_title())
# print(obj1.show_year())


# 4) Создайте класс Taxi с атрибутами name, cost и cost_km. Напишите метод get_total_cost, который принимает расстояние в километрах и возвращает общую стоимость поездки. Создайте несколько объектов этого класса и выведите стоимость поездки для каждого из них.


# class Taxi:
#     def __init__(self, name: str, cost: float, cost_km: float) -> None:
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km

#     def get_total_cost(self, km: float):
#         total_cost = self.cost * km * self.cost_km
#         return f'Такси: {self.name}, стоимость поездки: {total_cost} сом'
    
# taxi1 = Taxi('Yandex', 15, 7)
# taxi2 = Taxi('Namba', 10, 5)

# print(taxi1.get_total_cost(10))
# print(taxi2.get_total_cost(100))

# 5) Создайте класс Phone с атрибутами name, last_name и phone. Напишите метод get_info, который выводит информацию о контакте. Создайте объект этого класса и выведите информацию о контакте.

# class Phone:
#     def __init__(self, name, last_name, phone) -> None:
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone

#     def get_info(self):
#         return f'Имя контакта: {self.name}, фамилия: {self.last_name}, номер телефона: {self.phone}'
    
# obj1 = Phone('Никита', 'Гребнев', '+996999999999')
# print(obj1.get_info())

# 6) Создайте класс Salary с атрибутом класса percent (по умолчанию 8). Напишите метод __init, который инициализирует атрибуты экземпляра salary и experience. Напишите метод count_percent, который рассчитывает налог на зарплату за весь период работы. Создайте объект этого класса и выведите рассчитанный налог.

# class Salary:
#     percent = 8

#     def __init__(self, salary, experience) -> None:
#         self.salary = salary
#         self.experience = experience

#     def count_percent(self):
#         month_tax = self.salary / 100 * self.percent
#         res = self.experience * month_tax
#         return f'Сумма налога за весь опыт работы: {res}'
    
# obj = Salary(100000, 10)
# print(obj.count_percent())

