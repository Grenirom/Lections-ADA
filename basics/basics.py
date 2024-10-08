"============Переменные==============="
# переменные - это ссылки на ячейки памяти, где находятся какие то данные, для дальнейшего использования этих данных, при обращении к названию переменной

name = 'Никита'
age = 21


"============Правила наименования переменных==============="
a = 10 #можно, но не понятно
# 1name = 'ybrbnf' - нельзя начинать название с символа
#my name = 'sdjvnsldv' # SymtaxError
#my-name = 'kfjnlvmsk' # так нельзя
# if = 'hsbdvksdj' - Нельзя называть переменные ключевыми словами (if, class, def, while, for)


"===========Стили написания переменных==================="
my_name = 'shfbvniskj' # разделение слов только при помощи "_" Snake case, Python способ наименования переменных

myName = 'sfkbvskjd' #Camel case - стиль наименования в других языках программирования

"=================Ввод и вывод данных (print(), input())==========="
# print - функция для вывода текста/данных в терминал
print(my_name)
print(12)
print('sfsdffdsfs')


# input - функция для ввода данных с терминала
number = input('Введите число: ')
print('Введенное число: ', number)

"============Комментарии===================="

#1) при помощи '#'
#2) при помощи 
"""
kjsnvmlkdsv;kjasns
"""
#3) при помощи ''
"================================================"
# В Python отличия между '' или "" ковычками нет

"=====================Типы данных==================="
"""
Типы данных в python делятся на 2 типа: изменяемые и неизменяемые

Изменяемые типы данных: list(список), dict(словари), set(множества)

Неизменяемые типы данных: int(числа), float/decimal(числа с плавающей точкой), str(строки), tuple(кортеж), bool(булевые значения True/False), None(Пустота)
"""
# Изменяемые
list_ = [1, 2, True, 'hello']
dict_ = {'name': 'Никита', 1: 'a', 'jk': 123}
set_ = {1, 2, 3, 3, 3, 3, 3, 0, True, False}

"""
0 - False
1 - True
"""
# Неизменяемые 
int_ = 12
float_ = 12.12
str_ = "hello"
tuple_ = (1, 2, 3, 4)
bool1 = True
bool2 = False
none = None


print('изменяемые типы данных:', list_, dict_, set_)
print('Неизменяемые типы данных: ', int_, float_, str_, tuple_, bool1, bool2, none)