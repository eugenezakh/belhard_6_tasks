"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.

Номер значения нужно проверить

Пример:

fibonacci(0) -> 'Введите значение больше 1'
fibonacci(5)
1
2
3
5
8
Traceback (most recent call last):
File «C:/Python/Python3/python_generator.py», line 29, in
print(next(fib))
StopIteration
"""

from typing import Optional


def fibonacci(num_count: Optional[int], first_num=0, second_num=1) -> int:
    for i in range(num_count):
        if num_count <= 1:
            print('Введите значение больше 1')
        else:
            first_num, second_num = second_num, second_num + first_num
            print(second_num)


fibonacci(7)
