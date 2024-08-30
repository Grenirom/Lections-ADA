# # Наследование - принцип ООП, в котором мы можем унаследовать, переопределить и использовать в дочернем классе все аттрибуты и методы родительского класа

# class A:
#     def method(self):
#         print('Метод в классе А')

# obj1 = A()
# obj1.method() # Метод в классе А

# class B(A):
#     """
#     Наследовали все методы и аттрибуты класса А
#     """

# obj2 = B()
# obj2.method() # Метод в классе А


# class C(A):
#     """
#     Наследовали все методы и аттрибуты у класса А, и переопределили метод method()
#     """

#     def method(self):
#         print('Метод в классе C')

# obj_c = C()
# obj_c.method() # Метод в классе C

# class A:
#     x = 'x in A'
#     y = 'y in A'

# class B(A):
#     x = 'x in B'

# print(A.x) #x in A
# print(B.x)x in B

"""
Виды наследований

1) одиночное наследование (когда мы наследуемся в дочернем классе от 1 класса)
2) множественное наследование (когда мы наследуемся в дочернем классе от 
нескольких классов)
3) Многоуровневое наследование (когда мы наследуемся от класса  у которого есть родитель)
4) иерархическое наследование (когда от одного родителя много дочерних классов)
5) гибридное наследование (когда используются несколько видов наследования)
"""

'==============================Множественное наследование========================'
# class A:
#     a = 'a'


# class B(A):
#     b = 'b'


# class C(A, B):
#     """
#     Наследовали все аттрибуты классов A и B
#     """
#     c = 'c'

# class D(A):
#     pass
# obj_c = C()
# print(obj_c.a)
# print(obj_c.b)
# print(obj_c.c)


# class A:
#     def method(self):
#         print('Метод в классе А')


# class B:
#     def method(self):
#         print('Метод в классе B')


# class C(A, B):
#     ...
    
# obj_c = C()
# obj_c.method()#Метод в классе А


# Создайте два класса: Class1 и Class2. Класс Class1 должен иметь методы first и second, которые ничего не делают. Класс Class2 должен наследовать Class1 и иметь дополнительные методы third и fourth, которые также ничего не делают. Создайте объект класса Class2 и вызовите все методы.

# class Class1:

#     def first(self):
#         pass

#     def second(self):
#         pass


# class Class2(Class1):

#     def third(self):
#         pass

#     def fourth(self):
#         pass


# obj_ = Class2()
# print(obj_.first())
# print(obj_.second())
# print(obj_.third())
# print(obj_.fourth())


#  Создайте два класса: A и B. Класс A должен иметь метод method1, который выводит строку "Основной функционал". Класс B должен наследовать A и переопределять метод method1, добавляя к нему вывод строки "Дополнительный функционал" после вызова метода method1 из класса A. Создайте объект класса B и вызовите метод method1.


# class A:

#     def method1(self):
#         print('Основной функционал')

    
# class B(A):

#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')

# obj1 = B()
# obj1.method1()

# Создайте класс MyDict, наследующий от встроенного класса dict. Переопределите метод get, чтобы он возвращал строку "Are you kidding?" в случае, если ключ отсутствует в словаре. Создайте объект этого класса и продемонстрируйте работу метода get.


# class MyDict(dict):

#     def get(self, *args):
#         value = super().get(*args)

#         if value:
#             return value
        
#         return 'Are you kidding?'
    

# obj_dict = MyDict({"some_title": 2})
# print(obj_dict.get('some_title'))

# Создайте класс MyString, наследующий от встроенного класса str. Добавьте методы append и pop. Метод append должен добавлять строку к экземпляру класса. Метод pop должен удалять и возвращать последний символ строки. Переопределите метод __str__, чтобы он возвращал измененную строку. Создайте объект этого класса и продемонстрируйте работу методов.


# class MyString(str):

#     def append(self, extra_string):
#         self.mutable_string = self + extra_string

#     def pop(self):
#         last_char = self.mutable_string[-1]
#         self.mutable_string = self.mutable_string[:-1]
        
#         return last_char
    
#     def __str__(self) -> str:
#         return self.mutable_string
    

# obj = MyString('hello')
# obj.append('hello')
# print(obj.pop())
# print(obj)

# Создайте класс Person с атрибутами name и age, и методом display, который выводит имя и возраст. Создайте класс Student, наследующий от Person, с дополнительным атрибутом faculty и методом display_student, который выводит имя, возраст и факультет. Создайте объект класса Student и продемонстрируйте работу методов display и display_student.


# class Person:

#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f'name: {self.name}, age: {self.age}')


# class Student(Person):

#     def __init__(self, name, age, faculty) -> None:
#         super().__init__(name, age)
#         self.faculty = faculty

#     def display_student(self):
#         print(f'name: {self.name}, age: {self.age}, faculty: {self.faculty}')

# obj1 = Student('Nikita', 21, 'computer-science')
# obj1.display() # name: Nikita, age: 21
# obj1.display_student() # name: Nikita, age: 21, faculty: computer-science


# Создайте класс ContactList, наследующий от встроенного класса list. Добавьте метод search_by_name, который принимает строку и возвращает список контактов, содержащих эту строку (без учета регистра). Создайте объект этого класса и продемонстрируйте работу метода search_by_name.


# class ContactList(list):

#     def search_by_name(self, name):
#         res = [contact for contact in self if name.lower() in contact.lower()]

#         return res
    

# list1 = ['Ivan', 'Olya', 'NiKIta', 'Vasya', 'Nikita', 'nikita']

# obj1 = ContactList(list1)

# print(obj1.search_by_name('NIKITA'))

# Создайте класс SmartPhones с атрибутами name, color, memory и battery. Добавьте метод charge, который увеличивает значение батареи на заданное количество. Создайте классы Iphone и Samsung, наследующие от SmartPhones. Класс Iphone должен иметь дополнительный атрибут ios и метод send_imessage, который отправляет сообщение. Класс Samsung должен иметь дополнительный атрибут android и метод show_time, который возвращает текущее время. Создайте объекты этих классов и продемонстрируйте их работу.

# from datetime import datetime


# class SmartPhones:

#     def __init__(self, name, color, memory) -> None:
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = 0

#     def charge(self, power):
#         self.battery += power
    
#     def __str__(self) -> str:
#         return f'{self.name}, {self.memory}, {self.color}'
    

# class Iphone(SmartPhones):

#     def __init__(self, name, color, memory, ios):
#         super().__init__(name, color, memory)
#         self.ios = ios

#     def send_imessage(self, message):
#         return f'sending {message} from {self}'
    

# class Samsung(SmartPhones):

#     def __init__(self, name, color, memory, android):
#         super().__init__(name, color, memory)
#         self.android = android

#     def show_time(self):
#         return datetime.now().time()
    

# phone = SmartPhones('nokia', 'blue', 16)
# print(phone)
# print(phone.battery)
# phone.charge(100)
# print(phone.battery)

# iphone15 = Iphone('iphone15', 'blue', 512, '17.5')

# print(iphone15)
# print(iphone15.send_imessage('hello'))

# samsungs21 = Samsung('Samsung s21', 'black', 256, 'Oreo')

# print(samsungs21.show_time())


# Создайте класс CustomError, наследующий от Exception. Создайте объект этого класса с сообщением "ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ". Напишите функцию check_letters, которая принимает строку и выбрасывает CustomError, если строка не состоит из заглавных букв. В противном случае, функция возвращает строку "ВСЕ ОТЛИЧНО!" с переданной строкой. Продемонстрируйте работу функции с примером.


# class CustomError(Exception):
#     pass

# capitals_error = CustomError("ТОЛЬКО БОЛШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ")


# def check_letters(string):
#     if not string.isupper():
#         raise capitals_error
#     return f'ВСЕ ОТЛИЧНО! {string}'

# print(check_letters('HELLO'))
