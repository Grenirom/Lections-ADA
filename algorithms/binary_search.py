def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        middle = (start + end) // 2

        # проверка 1: если искомое число находится в середине массива
        if arr[middle] == target:
            return middle
        
        # проверка 2: если число в середине больше искомого числа, ищем в левой половине
        elif arr[middle] > target:
            end = middle - 1
        
        # проверка 3: если число в середине меньше искомого числа, ищем в правой половине
        else:
            start = middle + 1

    # если искомое число не найдено
    return -1

array = [i for i in range(1, 1001)]
target = 999

res = binary_search(array, target)

if res != -1:
    print(f'Элемент найден на индексе {res}')
else:
    print('Элемент не найден')

# comparisons = 1
# for i in range(1, 1001):
#     comparisons += 1
#     if i == target:
#         print(f'Элемент {i} найден под индексом {i - 1}')
# print(comparisons)