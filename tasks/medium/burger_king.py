"""
С помощью декораторов реализовать конвейер сборки бургера

Написать декоратор bread, который:
 - до декорируемой функции будет печатать "</------------\\>"
 - после декорируемой функции будет печатать "<\\____________/>"


Написать декоратор tomato, который:
 - до декорируемой функции будет печатать "*** помидоры ****"

Написать декоратор salad, который:
 - до декорируемой функции будет печатать "~~~~ салат ~~~~~"

Написать декоратор cheese, который:
 - до декорируемой функции будет печатать "^^^^^ сыр ^^^^^^"

Написать декоратор onion, который:
 - до декорируемой функции будет печатать "----- лук ------"

Написать функцию beef, которая:
 - печатает "### говядина ###"

Написать функцию chicken, которая:
 - печатает "|||| курица ||||"

1) Собрать с помощью декораторов гамбургер:
    - булка
    - лук
    - помидоры
    - говядина
    - булка

2) Собрать с помощью декораторов чикенбургер:
    - булка
    - сыр
    - салат
    - курица
    - булка
"""


def bread(func):
    def wrapper():
        print("</------------\\>")
        func()
        print("<\\____________/>")
    return wrapper


def tomato(func):
    def wrapper():
        print("*** помидоры ****")
        func()
    return wrapper


def salad(func):
    def wrapper():
        print("~~~~ салат ~~~~~")
        func()
    return wrapper


def cheese(func):
    def wrapper():
        print("^^^^^ сыр ^^^^^^")
        func()
    return wrapper


def onion(func):
    def wrapper():
        print("----- лук ------")
        func()
    return wrapper


@bread
@onion
@tomato
def beef():
    print("### говядина ###")


@bread
@cheese
@salad
def chicken():
    print("|||| курица ||||")
