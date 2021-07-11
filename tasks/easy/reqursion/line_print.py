"""
Написать рекурсивную функцию  line_print, которая принимает 1 аргумент - список

Функция печатает каждых элемент на новой строке.

Если элемент списка - список, то его элементы должны выводиться с отступом
относительно родительского на одну табуляцию

Например:

some_list = [1, 2, [1, 2, [5, 7], 3], 8]

line_print(some_list)
1
2
    1
    2
        5
        7
    3
8
"""


def line_print(new_list: list, iteration: int = 0) -> str:
    for i in range(len(new_list)):
        if type(new_list[i]) == list:
            line_print(new_list[i], iteration=iteration + 1)
        else:
            print(f"{'    ' * iteration}{new_list[i]}")


line_print([1, 2, [1, 2, [5, 7], 3], 8])
