# найти площадь и периметр треугольника
import math
a = input("длина первого катета:")
b = input("длина второго катета:")
a = float(a)
b = float(b)
area = (a*b)/2
c = math.sqrt(a**2*b**2)
p = a + b + c
print('area:', area)
print ('p:', p)
