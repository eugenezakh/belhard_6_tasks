"""
Написать рекурсивную функцию, которая будет красиво выводить данные в консоль.
Если строчный тип данных, то выводить в кавычках


например:

data = {'a': 123, 123: [1, 2, 3], 'asd': {'c': 654.54}}

{
    'a': 123,
    123: [1, 2, 3],
    'asd': {
        'c': 654.54,
    },
}
"""
from typing import Any


def string_or_not(some_value: Any) -> str:
    if isinstance(some_value, str):
        return f"'{some_value}'"
    else:
        return some_value


def pretty_print(some_dict: dict, indent: int = 0):
    flag = False
    if indent == 0:
        flag = True
        print("{")
    indent += 1
    for key, value in some_dict.items():
        if isinstance(value, dict):
            print("\t" * indent + string_or_not(key) + ': {')
            pretty_print(value, indent + 1)
            print("\t" * indent + "},")
        else:
            print("\t" * indent + f"{string_or_not(key)}: {string_or_not(value)},")
    if flag:
        print("}")


data = {'a': 123, 123: [1, 2, 3], 'asd': {'c': 654.54}}
pretty_print(data)
