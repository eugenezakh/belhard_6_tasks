"""
Написать функцию reverse_dict, которая принимает словарь ключ-значение и
возвращает новый словарь, у которого ключи - значения первого, а значения -
ключи первого

Тело функции может состоять из одной строки!
"""

from typing import Optional


def reverse_dict(dict_1: Optional[dict], dict_2={}) -> dict:
    key, value = list(dict_1.keys()), list(dict_1.values())
    for i in range(len(key)):
        dict_2.update({value[i]: key[i]})
    return dict_2
