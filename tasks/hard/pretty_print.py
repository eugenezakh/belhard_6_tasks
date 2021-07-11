"""
Написать рекурсивную функцию, которая будет красиво выводить данные в консоль.
Если строчный тип данных, то выводить в кавычках


например:

data = {'a': 123, 123: [1, 2, 3], 'asd': {'c': 654.54}}

{
    'a': 123,
    123: [1, 2, 3],
    'asd': {
        'c': 654.54,
    },
}
"""


def pretty_print(dict_1: dict, counter=0) -> dict:
    dict_1 = tuple(dict_1.items())
    for counter in range(len(dict_1)):
        if dict_1[counter] == dict:
            pretty_print(dict_1, counter + 1)
        else:
            print(dict_1[counter])


pretty_print({'a': 123, 123: [1, 2, 3], 'asd': {'c': 654.54}})


def pretty_print(dict_1: dict, id_1=0, value=[], keys=[], id_2=0) -> dict:
    if 6 > id_2:
        keys = list(dict_1.keys())[id_1]
        value = list(dict_1.values())[id_1]
        if type(value) == dict:
            print(f"{'    '}{keys}")
            pretty_print(dict_1=value, id_1=0, id_2=id_2 + 1)
        else:
            print(f"{'    '}{keys}: {value},")
            pretty_print(dict_1, id_1=id_1 + 1, id_2=id_2 + 1)


data = {'a': 123, 123: [1, 2, 3], 'asd': {'c': 654.54}}
pretty_print(data)
