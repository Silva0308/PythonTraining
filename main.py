# Дано число. Проверить кратно ли оно 7 и 23
n = int(input())
if n%7==0 and n%23==0:
    print("yes")
else:
    print("no")

#Показать таблицу квадратов чисел от 1 до N
n = int(input("Введите N"))
for i in range(n+1):
    print(i**2, end=' ')

