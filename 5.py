#Лаб 1 - Вычисление мат. выражений
from math import *

print ('Вычисление математического выражения (вар.19)\n Введите "4"')

x = float(input('x = '))
a = 3.7
p = x**2 - sqrt(abs(x))
t = x**2 + a**2
y = x*p**2 + t**5

print ('y = ',y,'\np = ',p,'\nt= ',t)
input()
