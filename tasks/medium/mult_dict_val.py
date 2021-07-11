"""
Написать функцию multiply_dict_values, которая принимает словарь SOME_DICT,
у которого ключи - строки, а значения - целые числа.

Необходимо, чтобы функция вернула результат умножения всех значений из словаря
"""

from typing import Optional

SOME_DICT = {str(val): val for val in range(1, 50, 3)}


def multiply_dict_values(some_dict: Optional[dict], result: int = 1) -> int:
    for key in some_dict:
        result *= int(key)
    return result
