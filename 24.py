# 24. Найти кубы чисел от 1 до N
n = int(input("Введите N: "))
for i in range(n+1):
    print(i**3, end=' ')
print()

#25. Найти сумму чисел от 1 до А
a = int(input("Введите A: "))
sum = 0
for i in range(a+1):
    sum += i
print(sum)
print()

# 26. Возведите число А в натуральную степень B используя цикл
a = int(input("Введите A: "))
b = int(input("Введите степень: "))
result = 1
for i in range(b):
    result *=a
print(result)
