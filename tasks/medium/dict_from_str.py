"""
Написать функцию dict_from_str, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}
"""

from typing import Optional

STR_VAL = 'python is the fastest-growing major programming language'


def dict_from_str(new_str: Optional[str]) -> dict:
    new_str = new_str.replace(' ', '')
    dict_1 = {key: new_str.count(key) for key in new_str}
    return dict_1


print(dict_from_str(STR_VAL))
