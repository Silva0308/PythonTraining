# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# с помощью математических формул нахождения корней квадратного уравнения
# с помощью дополнительных библиотек Python
a = int(input())
b = int(input())
c = int(input())
d = b**2-4*a*c
if d < 0:
    print("Уравнение не имеет корней")
elif d == 0:
    print("x = {}".format(-b/(2*a)))
else:
    print('x1 = {}\nx2 ={}'.format((-b+d**0.5)/(2*a),(-b-d**0.5)/(2*a)))

#второй способ
import math
if d < 0:
    print("Уравнение не имеет корней")
elif d == 0:
    print("x = {}".format(-b/(2*a)))
else:
    sol1 = (-b - math.sqrt(d)) / (2 * a)
    sol2 = (-b + math.sqrt(d)) / (2 * a)
    print('The solution are {0} and {1}'.format(sol1, sol2))