# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def Prime_num(n):
    num_list=[]
    for number in range(2, n + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                num_list.append(number)
    return num_list
def prime_fact(n,my_list ):
    result=[]
    for i in my_list:
        if n% i==0:
            result.append(i)
            n/=i
    return result



my_num = int(input('введите число: '))
list_num = Prime_num(my_num)
print(prime_fact(my_num, list_num))
