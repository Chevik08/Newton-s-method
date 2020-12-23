"""
Модуль с примерами для модуля newtonmethod
"""

from sympy import diff, Symbol
from math import sqrt
from newtonmethod import iteration

x = Symbol('x')

print('Введена функция x**2-4')
data1 = 'x**2-4', diff(x**2-4), '2', 2, '0', '5', 0.001
iteration(data1)

print('Введена функция x**2-3')
data2 = 'x**2-3', diff(x**2-3), '2', sqrt(3), '0', '5', 0.001
iteration(data2)

print('Введена функция (x-1)**2-1')
data3 = '(x-1)**2-1', diff((x-1)**2-1), '2', 0, '0', '5', 0.001
iteration(data3)

print('Введена функция (x-16)**3-1')
data4 = '(x-16)**3-1', diff((x-16)**3-1), '2', 17, '16', '20', 0.001
iteration(data4)

print('Введена функция (x-7)**3-1')
data5 = '(x-7)**3-1', diff((x-7)**3-1), '2', 8, '7', '9', 0.001
iteration(data5)
