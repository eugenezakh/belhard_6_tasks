"""
Написать функцию triangular_sequence, которая принимает n и выводит
следующую последовательность

1
22
333
4444
55555
...

Например:

n = 3:
1
22
333

n = 6:
1
22
333
4444
55555
666666
"""


def triangular_sequence(n: int, multiply=1) -> int:
    if multiply <= n:
        print(str(multiply) * multiply)
        triangular_sequence(n, multiply=multiply + 1)


triangular_sequence(11)
