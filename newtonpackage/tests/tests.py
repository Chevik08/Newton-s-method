"""
Модуль для тестироание программы
"""

import pytest
from sympy import Symbol
from ..newtonmethod import check, iteration, switching

x = Symbol('x')


# Тест на нормальную работу функции
def test_working():
    assert check('x**2-4', 0, 5, 0.001) == ('x**2-4', 2*x, 2, 2, 0, 5, 0.001)


# Тест на непредвиденные типы данных
def test_type():
    assert check([2, 3, 4], {2, 3, 4}, (2, 3, 4), '2, 3, 4')\
           == 'False'


# Тест на отрицательную точность
def test_negative_e():
    assert check('x**2-4', 0, 5, -0.001) == 'False'


# Тест на наличие решения в интервале
def test_out_of_range():
    assert check('x**2-4', 0, 1, 0.001) == 'False lit'


# Тест на некорректные данные
def test_bad_data():
    data = 'x-4', 1, 0, 4, 0, 5, 0.001
    assert iteration(data) == 'False'


# Тест на нормальную работу
def test_good_data():
    data = 'x**2-4', 2*x, 2, 2, 0, 5, 0.001
    assert iteration(data) is None


# Тест на нормальную работу
def test_switching_function():
    assert switching('x**2', 0) == 0


# Тест на отрицательное число
def test_switching_negative():
    assert switching('x**2', -95) == 9025
