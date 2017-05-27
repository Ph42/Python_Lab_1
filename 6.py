#Вычисление выражения
from math import *

print('Введите координаты вершин треугольника')
print('A:')
aX = float(input('	x = '))
aY = float(input('	y = '))
print('B:')
bX = float(input('	x = '))
bY = float(input('	y = '))
print('C:')
cX = float(input('	x = '))
cY = float(input('	y = '))

def dlinaVectoraPoDvumTochkam(aX, aY, bX, bY):
	return (sqrt((aX - bX)**2 + (aY - bY)**2))

a = dlinaVectoraPoDvumTochkam(aX, aY, bX, bY)
b = dlinaVectoraPoDvumTochkam(bX, bY, cX, cY)
c = dlinaVectoraPoDvumTochkam(cX, cY, aX, aY)
P = a + b +c
p = P/2
S = sqrt(p*(p-a)*(p-b)*(p-c))


print ('Периметр = ',P)

