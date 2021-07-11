"""
Написать функцию bang, которая печатает "Boom"
Написать декоратор repeat_n_times, у которого есть параметр n.
Декоратор должен выполнить функцию bang n раз
"""


def repeat_n_times(n: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat_n_times(6)
def bang():
    print("Boom")


bang()
