"=======================================Полиморфизм==============================="
# Полиморфизм - принцип ООП, в котором в разных классах методы называются, но реализация разная (один интерфейс - много реализаций)

# class Dog:
#     def speak(self):
#         print('Гав-гав')


# class Cat:
#     def speak(self):
#         print('Мяу')


# class Frog:
#     def speak(self):
#         print('ква-ква')


# obj = [Frog(), Cat(), Dog(), Cat(), Frog(), Dog()]
# for obj in obj:
#     obj.speak()


# # __add__ (+)
# print(5 + 5) # 10 int
# print('5' + '5') # 55 str
# print([1,2,3] + [4,5,6]) #list
# a = [1,2,3,4]
# b = [5,6,7]

# print(a.__add__(b)) # [1, 2, 3, 4, 5, 6, 7]

# # __len__

# print(len('abc'))
# print(len(['abc']))
# print(len([[1,2,3],[4,5,6]]))


# Создайте классы Person, Employee и Student. Класс Employee и Student должны наследоваться от Person и переопределять метод get_info, добавляя специфическую информацию. Напишите функцию, которая принимает объект и вызывает его метод get_info.

# class Person:
#     def __init__(self, name, last_name) -> None:
#         self.name = name
#         self.last_name = last_name

#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}'
    

# class Employee(Person):
#     def __init__(self, name, last_name, work, experience) -> None:
#         super().__init__(name, last_name)
#         self.work = work
#         self.experience = experience

#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work}, и мой опыт работы {self.experience}'
    

# class Student(Person):
#     def __init__(self, name, last_name, university, course) -> None:
#         super().__init__(name, last_name)
#         self.university = university
#         self.course = course

#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university}, на {self.course} курсе'
    
# def get_human_info(human):
#     print(human.get_info())


# person = Person('Nikita', 'Grebnev')
# employee = Employee('nikita', 'grebnev', 'mdigital', '10')
# student = Student('nikita', 'grebnev', 'MIT', '4')


# get_human_info(person)
# get_human_info(employee)
# get_human_info(student)

    