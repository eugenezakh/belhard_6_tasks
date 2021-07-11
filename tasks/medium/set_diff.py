"""
Написать функцию set_diff, которая принимает 4 аргумента: 3 множества и параметр
symmetric, который по умолчанию должен быть False.

Функция должна возвращать либо разность, либо симметричную разность
в зависимости от значения параметра symmetric
"""

from typing import Optional


def set_diff(set_1, set_2, set_3: Optional[set], symmetric=False) -> set:
    if symmetric:
        set_2.symmetric_difference_update(set_3)
        set_1.symmetric_difference_update(set_2)
        return set_1
    else:
        set_1.difference_update(set_2, set_3)
        return set_1
