"""
Написать рекурсивную функцию, которая будет вычислять сумму цифр целого числа

Можно пользоваться только функциями, операторами и условиями
"""


def num_sum(num, result=[], i=0) -> int:
    if i < len(str(num)):
        result.append(int(str(num)[i]))
        num_sum(num, result, i=i + 1)
    else:
        return sum(result)


print(num_sum(511215))
