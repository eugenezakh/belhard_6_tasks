"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и
False, если нет

Нельзя пользоваться операцией возведения в степень
"""


def check_number(number: int) -> bool:
    if number / 2 > 1:
        check_number(number / 2)
    elif number / 2 == 1:
        return True
    else:
        return False


print(check_number(16))
