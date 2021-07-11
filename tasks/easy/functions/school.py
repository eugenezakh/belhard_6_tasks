"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция decr_students, которая принимает SCHOOL_DATA, название класса и
    уменьшает количество учеников на 1, но не меньше 0
- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
- Функция remove_class, которая принимает SCHOOL_DATA, название класса и удаляет
    класс из словаря
- Функция calc_students, которая принимает SCHOOL_DATA и возвращает кол-во
    учеников во всей школе
"""

from typing import Optional

school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}


school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}


def incr_students(school_dict: Optional[dict], class_name: Optional[str]) -> dict:
    return school_dict.update({class_name: school_dict.get(class_name) + 1})


def dect_students(school_dict: Optional[dict], class_name: Optional[str]) -> dict:
    return school_dict.update({class_name: school_dict.get(class_name) - 1})


def add_class(school_dict: Optional[dict], class_name: Optional[str]) -> dict:
    return school_dict.update({class_name: 0})


def remove_class(school_dict: Optional[dict], class_name: Optional[str]) -> dict:
    school_dict.pop(class_name)
    return school_dict


def calc_students(school_dict: Optional[dict]) -> int:
    return sum(school_dict.values())
