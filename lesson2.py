##########################################
# Деструктиризація
##########################################

# tuple1 = (1, 2)
#
# a, b = tuple1
#
# print(a, b)

# a = 5
# b = 7
#
# a, b = b, a
#
# print(a)
# print(b)

# l1 = [1, 2, 3, 4, 5, 6, 7, 8]
#
# # _, b, *_, y, z = l1
# *_, x, y, z = l1
# print(x)
# print(y)
# print(z)

# args = [2, 3, 5]
# dict_args = {
#     'arg1': 8,
#     'arg2': 9,
#     'arg3': 10,
# }
# def func(arg1, arg2, arg3):
#     print(arg1, arg2, arg3)
#
# func(**dict_args)

##########################################
# Декоратори
##########################################

# def decor(func):
#     def inner(*args, **kwargs):
#         print('****************************')
#         func(*args, **kwargs)
#         print('****************************')
#     return inner
#
# def decor2(func):
#     def inner(*args, **kwargs):
#         print('----------------------------')
#         func(*args, **kwargs)
#         print('----------------------------')
#     return inner
#
# @decor
# @decor2
# def greeting(name):
#     print(f'Hello {name}')
#
#
#
# greeting('Max')

##########################################
# Скоупи
##########################################

# name = 'Max'
#
# def func():
#     pass
#
# for i in range(5):
#     print(i)
#
# print(i)
#
# print(globals())

# name = 'Oleh'
#
# def a():
#     name = 'Max'
#     print(locals())
#
#
# print(globals())
# a()

# Як працювати зі скоупами

# name = 'Max'
#
# def a():
#     # name = 'Vasya'
#
#     def b():
#         # nonlocal name
#         global name
#         name = 'Petya'
#         print(name)
#     b()
#     print(name)
# a()
# print(name)

# def counter():
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#     return inner
#
#
# counter1 = counter()
# counter2 = counter()
#
# print(counter1())
# print(counter2())
# print(counter1())
# print(counter1())
# print(counter2())


##########################################
# Лямбда вирази ( як call back ф-ія в js )
##########################################

# func = lambda a, b: a + b
#
# print(func(5, 6))

# l = [1, 2, 3, 4, 5]
#
# m = map(lambda item: item ** 2, l)
# f = filter(lambda x: x % 2 == 0, l)
#
# # for i in m:
# #     print(i)
#
# for i in f:
#     print(i)

# users = [
#     {'name': 'Max', 'age': 15},
#     {'name': 'olha', 'age': 17},
#     {'name': 'kamila', 'age': 19},
#     {'name': 'lox', 'age': 1}
# ]
#
# users.sort(key=lambda x: len(x['name']))
#
# print(users)

##########################################
# Type hitting (анотація типів)
##########################################

# def func(name:list[str]) -> dict:
#     name = '333'
#     return {'name': name}

# import typing

from typing import Any, TypedDict, Callable

# a: int = 'sd'
#
# print(a)

# my_type = bool|str|int
# def func() -> my_type:
#     return 43
#
# def func2() -> None:
#     return


# User = TypedDict('User', {'name': str, 'age': int, 'house': int})
#
# users: list[User] = [
#     {'name': 'Max', 'age': 65, 'house': 55},
#     {'name': 'Max', 'age': 65, 'house': 55},
# ]

def counter(a: str, b: int) -> Callable[[bool, list[str]], int]:
    count = 0

    def inner(f: bool, y: list[str]) -> int:
        nonlocal count
        count += 1
        return count
    return inner
