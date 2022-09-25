# 31. Задать массив из 8 элементов и вывести их на экран

from random import randint

l = [randint(0, 10) for x in range(8)]
print(l)

# 32 .Задать массив из 8 элементов, заполненных нулями и единицами вывести их на экран

from random import randint

array1 = [randint(0, 1) for x in range(8)]
print(array1)

# 33. Задать массив из 12 элементов, заполненных числами из [0,9].
# Найти сумму положительных/отрицательных элементов массива
from random import randint

array1 = [randint(-9, 9) for x in range(12)]
print(array1)
result = 0
for i in range(len(array1)):
    if array1[i] > 0:
        result += array1[i]
print(result)


# 34. Написать программу замену элементов массива на противоположные
def listprint(a, b, n):
    from random import randint
    array_1 = [randint(a, b) for x in range(n)]
    return array_1


def listinversion(list):
    for i in range(len(list)):
        list[i] *= -1
    return list


min_num = int(input("Put minimal number: "))
max_num = int(input("Put maximal number: "))
a = int(input("Put the number of elements: "))
numbers = listprint(min_num, max_num, a)
print(numbers)
inv_numbers = listinversion(numbers)
print(inv_numbers)
