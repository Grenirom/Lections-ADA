"====================================Comprehension==============================="
# Генератор, с помощью которого мы можем создавать последовательности используя for в одну строку

"""
результат for элемент in последовательность
i for i in list1
результат for элемент in последовательность if фильтр - фильтрация
i for i in list1 if i % 2 == 0
тело1 if условие else тело2 for элемент in последовательность - условие
'четное' if i % 2 == 0 else 'нечетное' for i in range(1, 11)
"""

# comprehension = (i for i in range(1, 6)) # <generator object <genexpr> at 0x7fe657cd0ac0>
# print(comprehension)
# генератор - итерируемый объект, который не хранит в себе полностью всю последовательность данных, а создает их когда требуется

# print(next(comprehension)) # 1
# print(next(comprehension)) # 2
# print(next(comprehension)) # 3
# print(next(comprehension)) # 4
# print(next(comprehension)) # 5
# print(next(comprehension)) # StopIteration

# next() - функция, которая запрашивает у генератора текущий элемент и генератор создает следующий элемент

'===============================Синтаксический сахар=============================='
# list comprehension
# list_comprehension = list( (i**2 for i in range(1, 6)) )
# print(list_comprehension) # [1, 4, 9, 16, 25]
# list_comprehension2 = [i**2 for i in range(1, 6)]
# [1, 4, 9, 16, 25]

"Создайте список состоящий из четных чисел от 1 до 10 используя comprehension"
# list_comp = [i for i in range(1, 11) if i % 2 == 0]
# print(list_comp) # [2, 4, 6, 8, 10]
# list_comp = [i for i in range(2, 11, 2)]
# print(list_comp)

# list3 = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         list3.append(i)
# print(list3)

'Создайте список состоящий из 5 строк "hello" используя comprehension'
# list1 = []
# for i in range(5):
#     list1.append('hello')
# print(list1)

# list_ = ['hello' for _ in range(5)]
# print(list_) # ['hello', 'hello', 'hello', 'hello', 'hello']

'Создайте список состоящий из чисел от 1 до 10, но вместо чисел написать четное или нечетное'
# list_ = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         list_.append('четное')
#     else:
#         list_.append('нечетное')
# print(list_)

# list1 = ['четное' if num % 2 == 0 else 'нечетное' for num in range(1, 11)]
# print(list1)

# list2 = []
# for i in range(1, 11):
#     list2.append('четное' if i % 2 == 0 else 'нечетное')
# print(list2)

'Создайте список из существующего списка, оставив только строки'
# нужно выполнить задание 2 способами (с использованием обычного цикла, и с использованием comprehension)
# if type(i) == str:
# list1 = [1, 'hello', 2, 'a', 2.3, 1000, 'world']
# list2 = [i for i in list1 if type(i) == str]
# print(list2)
# list2 = []
# for i in list1:
#     if type(i) == str:
#         list2.append(i)
# print(list2)
"=========================================Dict comprehension======================"
# dict_ = dict( (i, i**2) for i in range(10) )
# print(dict_)
# dict_ = {i: i**2 for i in range(10)} #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# print(dict_)


"Дан словарь, создайте его копию с помощью comprehension"
# dict1 = {"a":1, "b":2, "c":3}
# dict2 = {key: value for key, value in dict1.items()}
# dict_ = {}
# for key, value in dict1.items():
#     dict_[key] = value
# print(dict_)
# print(dict1)
# print(dict2)

"Дан словарь, поменяйте ключи со значениями при помощи comprehension"
# dict1 = {"a":1, "b":2, "c":3}
# dict2 = {value: key for key, value in dict1.items()}
# print(dict2)

"Дан словарь, где значения - списки с числами, создайте словарь, где значениями будут суммы этих чисел"

# dict1 = {
#     "a":[1,2,3,4],
#     "b":[10,15,16,17],
#     "c":[1,2,54]
# }
# dict2 = {key: sum(value) for key, value in dict1.items()}
# print(dict2) # {'a': 10, 'b': 58, 'c': 57}

"Дан словарь с ключами где числа 1 до 10, а значения числа в виде строк"
# {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10'}
# str()
 
# dict2 = {i: str(i) for i in range(1, 11)}
# print(dict2)

"Даны 2 списка, создайте словарь, ключами будут элементы первого списка, а значениями - элементы второго списка"

# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c', 'd', 'e']

# # 1 способ
# dict_ = {}
# for ind in range(len(list1)):
#     key = list1[ind]
#     value = list2[ind]
#     dict_[key] = value
# print(dict_)

# # 2 способ
# dict_ = {list1[ind]: list2[ind] for ind in range(len(list1))}
# print(dict_)

# #3 способ
# dict_ = dict(zip(list1, list2))
# print(dict_)

"===============================Вложенные comprehension========================"
"Создайте словарь, где ключами будут числа от 1 до 5, а значениями - списки с числами от 1 до этого числа"
# {1:[1], 2:[1,2], 3:[1,2,3], 4:[1,2,3,4], 5:[1,2,3,4,5]}

# 1 способ

# dict1 = {}
# for i in range(1, 6):
#     key = i
#     value = [j for j in range(1, i+1)]
#     dict1[key] = value

# # 2 способ
# dict_ = {i: [j for j in range(1, i+1)] for i in range(1, 6)}
# print(dict_)

# # 3 способ
# dict_ = {i: list(range(1, i+1)) for i in range(1, 6)}
# print(dict_)

"Создать список, состоящий их 10 списков, в которых строка 'hello world' повторяется по 5 раз"

# 1 способ
# list1 = []
# for i in range(10):
#     inner_list = []
#     for j in range(5):
#         inner_list.append('hello world')
#     list1.append(inner_list)

# print(list1)

# 2 способ
# list1 = [['hello world' for j in range(5)] for i in range(10)]
# print(list1)

# 3 способ
# list1 = [['hello world']*5 for i in range(10)]
# print(list1)

# 4 способ
# list1 = [['hello world']*5]*10
# print(list1)

"Создать список состоящий из 10 списков, в которых будут числа от 1 до 5"
# [[1,2,3,4,5],
# [1,2,3,4,5],
# [1,2,3,4,5],
# [1,2,3,4,5],
# [1,2,3,4,5],
# [1,2,3,4,5],
# [1,2,3,4,5],
# [1,2,3,4,5],
# [1,2,3,4,5],
# [1,2,3,4,5]]


"Создайте словарь, где ключами будут числа от 1 до 5, а значениями словари, в которых ключами будут числа от 1 до этого числа, а значениями будут списки от 1 до этого числа"

# {
#     1:{
#         1:[1]
#     },
#     2:{
#         1:[1],
#         2:[1,2]
#     },
#     3:{
#         1:[1],
#         2:[1,2],
#         3:[1,2,3]
#     },
#     4:{
#         1:[1],
#         2:[1,2],
#         3:[1,2,3],
#         4:[1,2,3,4]
#     },
#     5:{
#         1:[1],
#         2:[1,2],
#         3:[1,2,3],
#         4:[1,2,3,4],
#         5:[1,2,3,4,5]
#     }
# }

# 1 способ
# dict_ = {}
# for i in range(1, 6):
#     inner_dict = {}
#     for j in range(1, i+1):
#         list_ = []
#         for k in range(1, j+1):
#             list_.append(k)
#         inner_dict[j] = list_
#     dict_[i] = inner_dict
# print(dict_)

# 2 способ
# dict2 = {
#     i:{
#         j:[k for k in range(1, j+1)] for j in range(1, i+1)
#     }
#     for i in range(1, 6)
# }

# Дан словарь:
dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# Создайте словарь dict2:
# - Ключи должны быть те же, что и в первом словаре, но каждый символ 'i' замените на ''
# - Значением должно быть количество повторений символа 'i' в этом ключе

# dict2 = {k.replace('i', ''): k.count('i') for k in dict1}
# print(dict2)
# print(dir(dict2))

# Используя приведенный словарь dict_, создайте список из id, 
# которые хранятся под ключом comments. Берите только те комментарии, 
# количество которых больше 3
dict_ = {
    'Dasha': {
        'likes': 15,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
        ],
        'rating': 2
    },
    'Luna': {
        'likes': 12,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
        ],
        'rating': 1
    },
    'Rena': {
        'likes': 26,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
            {'id': 4, 'text': 'some text'},
            {'id': 5, 'text': 'some text'},
            {'id': 6, 'text': 'some text'},
        ],
        'rating': 2
    }
}

# 1 способ
# ids = []

# for inner_dict in dict_.values():
#     comments = inner_dict['comments']
#     if len(comments) > 3:
#         for comment in comments:
#             ids.append(comment['id'])
# print(ids)

# 2 способ
# ids = [comment['id'] for inner_dict in dict_.values() if len(inner_dict['comments']) > 3 for comment in inner_dict['comments']]

# ids = [comment['id'] for inner_dict in dict_.values() for comment in inner_dict['comments'] if len(comments) > 3]
# print(ids)