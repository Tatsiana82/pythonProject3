# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.
"""from math import sqrt
def square(side):
    return (side**2, side*4, round(sqrt(side**2*2), 2))"""


# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#    в формате аргумент: значение. Например:
#	name: John
#	last_name: Smith
#	age: 35
#	position: web developer

"""def employee(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}: {v}')
employee(last_name = 'Ivanov', name = 'Ivan', age = 40, position = 'tester')"""


# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#     положительные числа
#my_list = [20, -3, 15, 2, -1, -21]
#print(list(filter(lambda x: x > 0, my_list)))

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке

"""from functools import reduce
my_list = [20, -3, 15, 2, -1, -21]
print(reduce(lambda x, y: x*y, my_list))"""
# Чтобы получить результат перемножения только положительных значений
#print(reduce(lambda x, y: x*y, [x for x in my_list if x > 0]))

# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
"""import time

def count_execution_time(func):
    def wrapper(*args):
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()
        exec_time = end - start
        print(f'{func.__name__} execution time is: {exec_time}')
        return result
    return wrapper

@count_execution_time
def greeting(name):
    return f'Hello {name}!'"""

# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#     Примените эти функции в качестве методов в другом файле.
#my_calc.py


"""from my_file import *

prod_res = prod(10, 2)
print(prod_res)

div_res1 = divide(40, 5)
print(div_res1)

div_res2 = divide(3, 0)
print(div_res2)

add_res = add(585, 1987)
print(add_res)

remain_res = remain(541, 6)
print(remain_res)

sub_res = subtract(23, 13)
print(sub_res)"""

# def my_decorator(my_func):
#     from time import time
#     def wrapper():
#         start_time = time()
#         print(f'Начало отсчета: {start_time}')
#         result = my_func()
#         end_time = time()
#         print(f'Конец отсчета: {end_time}')
#         print(f'Время работы функции {my_func.__name__}: {end_time - start_time}')
#         return result
#     return wrapper
#
# @my_decorator
# def my_func():
#     from time import sleep
#     sleep(5)
#     return 'End'
#
# print(my_func())

"""def my_decorator(my_exponent):
    from time import time
    def wrapper(*args):
        start_time = time()
        print(f'Начало отсчета: {start_time}')
        result = my_exponent(*args)
        end_time = time()
        print(f'Конец отсчета: {end_time}')
        print(f'Время работы функции {my_exponent.__name__}: {end_time - start_time}')
        return result
    return wrapper

@my_decorator
def my_exponent(a, b):
    from time import sleep
    sleep(2)
    return a ** b

print(my_exponent(3, 3))"""
