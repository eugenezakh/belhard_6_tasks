"""
Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и
возвращает словарь, в котором каждый элемент списка является и ключом и
значением. Предполагается, что элементы списка будут соответствовать
правилам задания ключей в словарях.
"""

from typing import Optional


def to_dict(list_1: Optional[list]) -> dict:
    return {key_value: key_value for key_value in list_1}
