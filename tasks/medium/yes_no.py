"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""

from typing import Optional


def yes_or_no(list_1: Optional[list]):
    for i in range(len(list_1)):
        first = list_1[i]
        second = list_1[:i]
        if first in second:
            print('Yes')
        else:
            print('No')


a = [1, 5, 5, 3, 6, 3]
print(yes_or_no(a))
