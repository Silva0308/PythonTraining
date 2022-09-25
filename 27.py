# 27. Определить количество цифр в числе
x = input("Введите число: ")
print(len(x))

#28. Подсчитать сумму цифр в числе
x = input("Введите число: ")
n = len(x)
sum = 0
for i in range(n):
   sum += int(x[i])
print(sum)

# 29. Написать программу вычисления произведения чисел от 1 до N
n = int(input("Введите число: "))
result = 1
for i in range(n):
    result *= i+1
print(result)



