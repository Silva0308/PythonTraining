#31. Задать массив из 8 элементов и вывести их на экран

from random import randint
l = [randint(0,10) for x in range(8)]
print(l)

#32 .Задать массив из 8 элементов, заполненных нулями и единицами вывести их на экран

from random import randint
array1 = [randint(0, 1) for x in range(8)]
print(array1)

#33. Задать массив из 12 элементов, заполненных числами из [0,9].
# Найти сумму положительных/отрицательных элементов массива
from random import randint
array1 = [randint(-9, 9) for x in range(12)]
print(array1)
result = 0
for i in range(len(array1)):
    if array1[i] > 0:
        result += array1[i]
print(result)