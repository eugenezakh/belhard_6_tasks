"""
Написать функцию get_dict_from_lists, которая принимает 2 значения - 2 списка
одинаковой длины: LIST_1 и LIST_2.

Необходимо, чтобы функция составляла и возвращала словарь, у которого ключи -
элементы LIST_1, а значения - элементы LIST_2
"""

from typing import Optional

LIST_1 = [str(i) for i in range(20)]
LIST_2 = [i ** 2 for i in range(20)]


def get_dict_from_lists(list_1, list_2: Optional[list], new_dict: dict = {}) -> dict:
    for i in range(len(list_1)):
        new_dict.update({list_1[i]: list_2[i]})
    print(new_dict)
    return new_dict


print(get_dict_from_lists(LIST_1, LIST_2))
