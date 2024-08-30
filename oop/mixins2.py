# "================================Миксины==============================="
# # Миксины - классы, которые будут использоваться для наследования. Но от миксинов не создаются объекты


# class FlyMixin:
#     def fly(self):
#         print('я могу летать')


# class WalkMixin:
#     def walk(self):
#         print('я могу ходить')
    

# class SwimMixin:
#     def swim(self):
#         print('я могу плыть')


# class Human(SwimMixin, WalkMixin):
#     name = 'человек'

#     def talk(self):
#         print('я могу говорить')

# # obj = Human()
# # obj.swim()
# # obj.talk()
# # obj.walk()

# class Fish(SwimMixin):
#     name = 'рыба'


# class Duck(WalkMixin, FlyMixin, SwimMixin):
#     name = 'утка'

# objects = [Human(), Fish(), Duck()]

# for obj in objects:
#     print(obj.name)

#     attrs = ['fly', 'swim', 'walk', 'talk']
#     for attr in attrs:
#         if hasattr(obj, attr):
#             method = getattr(obj, attr)
#             method()

# obj1 = Human()
# setattr(obj1, 'new_attr', 'hello world')

# print(obj1.new_attr)
# print(dir(obj1))
# print(obj1.new_attr)

# # hasattr() - функция, которая принимает объект и название аттрибута. Возвращает True, если у объекта есть такой аттрибут(метод)

# # getattr() - фукнция, которая принимает объект, и название аттрибута. Возвращает значение аттрибута

# # setattr() - функция, которая принимает объект, название аттрибута и значение. Добавляет в объект новый аттрибут, или перезапишет одноименный аттрибут

