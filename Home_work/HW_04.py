import functools
import time
import random as rand

from my_calc import *

"""4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
     периметр квадрата, площадь квадрата и диагональ квадрата."""


# -1
def square(s):
    return s * 4, \
           s * s, \
        round(s * 1.414, 2)


print(f'Периметр квадрата; Площадь квадрата; Диагональ квадрата = {square(12)}')


# -2
def perimeter(a):
    return a * a


def area(a):
    return a * 4


def diagonal(a):
    return a * 1.414


def square(a):
    return perimeter(a), area(a), diagonal(a)


print(square(5))

# - 1
x = lambda s: ((s * 4), (s * s), (round(s * 1.414, 2)))
print(f'S square = {x(5)}')


# -2
def square(a):
    perimeter = lambda a: a * a
    s_area = lambda a: a * 4
    diagonal = lambda a: round(a * 1.414, 2)
    return perimeter(a), s_area(a), diagonal(a)


print(square(5))

""" 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
     в формате аргумент: значение. Например:"""


@calculate_time
def about(name, last_name, age, position):
    return f'Name: {name},\nLast_Name: {last_name},\nAge: {age},\nPosition: {position}\n'


print(about('Katya', 'M', 35, 'student'))


def argum(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


print(argum(name='Max', age='19', position='Student'))

"""4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
     положительные числа"""

my_list = [20, -3, 15, 2, -1, -21]
l = list(filter(lambda x: x >= 0, my_list))
print(l)

'''4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке '''
su_m = functools.reduce(lambda x, y: x * y, l)
print(su_m)

'''4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра '''
# look my_calc.py
"""4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления. 
     Примените эти функции в качестве методов в другом файле. """

print(plus(3, 44))
print(minus(2, 3))
print(divide(23, 3))
print(multi(2, 3))
print(exp(2, 3))
print(r_of_dev(2, 3))
