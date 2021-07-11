"""
Написать функцию common_numbers, которая принимает 2 списка, которые содержат
целые числа.

Функция должна вернуть список общих чисел, который отсортирован по убыванию
"""

from typing import Optional


def common_numbers(list_1: Optional[list], list_2: Optional[list]) -> list:
    list_1 = set(list_1)
    list_2 = set(list_2)
    list_1.intersection_update(list_2)
    print(list_1)
    return sorted(list_1, reverse=True)


common_numbers([1, 2, 3, 4], [1, 3, 5])
