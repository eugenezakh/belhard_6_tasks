"""
Написать функцию to_set, которая принимает список, а возвращает множество,
созданное из этого списка и длину этого множества
"""


def to_set(new_list: list):
    new_list = set(new_list)
    return new_list, len(new_list)
