"=========================Циклы==================================="
# цикл - это блок кода, который отрабатывает несколько раз
# for - цикл, который работает с итерируемым объектом. Цикл заканчивает работу, когда он доходит до последнего элемента итерируемого объекта
# while - цикл, который работает до тех пор, пока условие верное


# list_ = ['hello world', 1, 2, 3, 30, None, False, True, [1, 2, 3]]

# for element in list_:
#     print(element)

# for letter in 'hello world':
#     print(letter)


# n = 1
# while n <= 10:
#     print(n)
#     # n = n + 1
#     n += 1
# # 1 2 3 4 5 6 7 8 9 10

# n = 0
# while n:
#     # n += 1
#     print(0)
    # Не запустится, потому что 0 - False

# while list_:
#     print('hello')
#     if list_:
#         print('1')
"=======================Операторы break/ continue================="
# break - полностью прерывает работу цикла (выйти из цикла)
# continue - пропускает 1 итерацию, и переходит к следующей

# for i in range(10):
#     if i == 3:
#         continue
#     print(i)
    # 0 1 2 4 5 6 7 8 9


# for i in range(10):
#     print(i)
#     if i == 3:
#         continue
    # 0 1 2 3 4 5 6 7 8 9

# for i in range(10):
#     print(i)
#     break
#     # 0

# for i in range(10):
#     print(i)
#     if i == 3:
#         break

# for i in range(10):
#     if i == 3:
#         break
#     print(i)

# for i in range(10):
#     if i < 3:
#         continue
#     print(i)
    # 3 4 5 6 7 8 9

# list1 = [1, 1, 1, 1, 2, 3, 4, 5, 1, 59, 1, 1]
# new_list = []

# # for num in list1:
# #     # if num == 1:
# #     #     continue
# #     # new_list.append(num)
# #     if num != 1:
# #         new_list.append(num)
# # print(new_list)

# list1 = [1, 1, 1, 1, 2, 3, 4, 5, 1, 59, 1, 1]

# while 1 in list1:
#     list1.remove(1)
# print(list1)

# for i in range(10):
#     for j in range(10):
#         print(i, j)

# 6) Есть строка: 
# my_string = "Ботнет IPStorm, в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем" 
# num_list = []
# Пройтись по всем элементам строки, если элемент(символ) строки является цифрой, то перевести его в тип int, далее умножить его на 2 и вывести результат

# for letter in my_string:
#     if letter.isdigit():
#         # num_list.append(letter)
#         # num_str = ''.join(num_list)
#         print(int(letter) * 2)
# print(num_list)

# 0) Вывести числа от 1 до 10.(решить с помощью while и for) 
# for i in range(1, 11):
#     print(i)
num = 1
while True:
    print(num)
    num += 1
    if num > 10:
        break

# 1) Вывести все четные числа от 1 до 20. (решить с помощью while и for) 

# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)
n = 1

while n <= 20:
    
    if n % 2 == 0:
        print(n)

# 2) Есть числа от 1 до 100. Если при делении числа на 3, остаток равен 0, то вывести само число, иначе вывести остаток от деления .(решить с помощью while и for)
    
# for i in range(1, 100):
#     if i % 3 == 0:
#         print(i)
#     else:
#         print(f'остаток от деления: {i % 3}')

# while True:
#     for i in range(1, 100):
#         if i % 3 == 0:
#             print(i)
#         else:
#             print(f'остаток от деления: {i % 3}')
#     break
# n = 1

# while n <= 100:
#     if n % 3 == 0:
#         print(f'целое число: {n}')
#     else:
#         print(f'остаток от деления: {n % 3}')
#     n += 1

# 4) Найти числа в диапазоне (1, 100), которые четные и кратны 3 и 9. (решить с помощью while и for)
# new_list = []

# for num in range(1, 101):
#     if num % 2 == 0 and num % 3 == 0 and num % 9 == 0:
#         new_list.append(num)

# print(new_list)
# n = 1

# while n <= 100:
#     if n % 2 == 0 and n % 3 == 0 and n % 9 == 0:
#         new_list.append(n)
#     n += 1
# print(new_list)

# 5) Напишите программу, которая выводит чётные числа из диапазона (1, 300) и останавливается, если встречает число 237.
# for i in range(1, 301):
#     if i % 2 == 0:
#         print(i)
#     elif i == 237:
#         break
    

    