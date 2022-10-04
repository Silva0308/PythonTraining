# # 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import math
def prime_factors(num):
    if n == 1:
        result = 1
    else:
        result = []
        while num % 2 == 0:
            result.append(2)
            num = num / 2
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            while num % i == 0:
                result.append(i)
                num = num / i
        if num > 2:
            result.append(num)
    return result

n = int(input('введите число: '))
print(prime_factors(n))
