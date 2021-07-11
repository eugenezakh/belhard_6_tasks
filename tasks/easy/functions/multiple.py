"""
Написать функцию multiply, которая принимает аргумент n.
и возвращает функцию closure, которая принимает аргумент x и возвращает x * n
"""


def multiply(n: int):
    def closure(x: int) -> int:
        return x * n
    return closure
