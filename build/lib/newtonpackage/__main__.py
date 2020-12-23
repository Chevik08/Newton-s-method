"""
Модуль для взаимодействия программы с командной строкой,
тестирование и вызова примеров

Запуск с помощью команды: python newtonpackage\\__main__.py [y, a, b, e] [-h, -ex, -t]
Запуск теста вручную: pytest pytest newtonpackage\\tests\\tests.py -v

Автор: Черных Никита Сергеевич, КИ20-17/2б
"""

import argparse
import newtonmethod
import os

parser = argparse.ArgumentParser()

parser.add_argument("y", help='Your function')
parser.add_argument("a", type=int, help='Beginning of the interval')
parser.add_argument("b", type=int, help='Ending of the interval')
parser.add_argument("e", type=float, help='Accuracy')

parser.add_argument('-ex', '--example', action='store_true', required=False,
                    help='Six examples')
parser.add_argument('-t', '--testing', action='store_true', required=False,
                    help='Testing program with PyTest')

args = parser.parse_args()
if args.example:
    import examples
    print('Вводим функцию (x-1)**2-1 на интервале от 1 до 5 с точность 0.001')
    print('Таким образом, y=x**2-4, a=0, b=5, e=0.001')
    data = newtonmethod.check('(x-1)**2-1', 1, 5, 0.001)
    newtonmethod.iteration(data)
elif args.testing:
    print('Запускаем тестирование')
    os.system('pytest newtonpackage\\tests\\tests.py -v')
else:
    try:
        data = newtonmethod.check(args.y, args.a, args.b, args.e)
        newtonmethod.iteration(data)
    except ValueError:
        print('Данные введены неверно, введите -ex для запуска примера')
