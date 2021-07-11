"""
Написать 2 генератора:
1) Генератор simple_number первый идет по всем простым числам
(число делится только на 1 и на само себя)
2) Генератор odd_simple, который используется значения первого и возвращает
из них нечетные
"""


def simple_number(n: int = 2) -> int:
    while True:
        counter = 1
        for i in range(1, n):
            if n % i == 0:
                counter += 1
        else:
            if counter == 2:
                yield n
        n += 1


def odd_simple() -> int:
    result = simple_number()
    while True:
        odd_number = next(result)
        if odd_number % 2 != 0:
            yield odd_number
