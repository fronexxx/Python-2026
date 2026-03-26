#############################################
# Генератор
#############################################

# l = [i for i in range(50_000_000)]
# g = (i for i in range(50_000_000))
# # input()
# #
# # print('Hello')
#
# # print(type(g)
# print(next(g))
# print('some')
# print(next(g))
#
# for i in g:
#     print(i)

# g = (i for i in range(7))
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# def gen(name):
#     for ch in name:
#         yield ch
#
#
# g = gen('max')
# print(next(g))
# print(next(g))
# print(next(g))

# def gen():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     return 'my return'
#
# g = gen()
#
# try:
#
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
# except StopIteration as e:
#     print(e)

# def gen1(n):
#     for i in range(1, n + 1):
#         yield f'{i} - Team1'
#
# def gen2(n):
#     for i in range(1, n + 1):
#         yield f'{i} - Team2'
#
# teams = [gen1(5), gen2(7)]
#
# while teams:
#     team = teams.pop(0)
#
#     try:
#         print(next(team))
#         teams.append(team)
#     except StopIteration:
#         pass


import uuid

from lesson1 import age


def gen_jpg_file():
    pattern = '{}.jpg'
    while True:
        yield pattern.format(uuid.uuid1())


#
# file_gen = gen_jpg_file()
#
# print(next(file_gen))
# print(next(file_gen))
# print(next(file_gen))

# Range за допомогою ітератора
# class MyRange:
#     def __init__(self, length):
#         self.__length = length
#         self.__counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.__counter < self.__length:
#             res = self.__counter
#             self.__counter += 1
#             return res
#         raise StopIteration
#
# for i in MyRange(5):
#     print(i)

# Range за допомогою генератора

# def my_range(length):
#     count = 0
#     while count < length:
#         yield count
#         count += 1
#
# for i in my_range(10):
#     print(i)


# file = open('1.txt', mode='r')
# print(file.read())
# file.close()

# try:
#     file = open('1.txt')
#     try:
#         print(file.read())
#     finally:
#         file.close()
#
# except Exception as e:
#     print(e)


# try:
#     with open('1.txt') as file:
#         # print(file.read())
#         # print(file.readline())
#         # print(file.readline())
#         # print(file.readline())
#         # for line in file:
#         #     print(line)
#
# except Exception as e:
#     print(e)

# try:
#     with open('1.txt', 'w') as file:
#         file.write('hello from write\nHI')
# except Exception as e:
#     print(e)

# try:
#     with open('1.txt', 'a') as file:
#         file.write('\nAppend')
# except Exception as e:
#     print(e)

# try:
#     with open('2.txt', 'x') as file:
#         pass
# except Exception as e:
#     print(e)

# try:
#     with open('1.txt', 'w+') as file:
#         file.write('Hello')
#         file.seek(0) # Ставимо курсор там звідки хочемо щоб файл починав читатися // в дужках прописуємо байти, 0 байт = початок файлу
#         print(file.read())
# except Exception as e:
#     print(e)

# try:
#     with open('1.txt', 'r+') as file:
#         file.write('Hello')
#         file.seek(0) # Ставимо курсор там звідки хочемо щоб файл починав читатися // в дужках прописуємо байти, 0 байт = початок файлу
#         print(file.read())
# except Exception as e:
#     print(e)
#

########################################
# Бінарні дані
########################################

# try:
#     with open('download.jpeg', 'rb') as file, open(next(gen_jpg_file()), 'wb') as file2 :
#         file2.write(file.read())
# except Exception as e:
#     print(e)


import json
import pickle
from typing import TypedDict

User = TypedDict('User', {'name': str, 'age': int})

users: list[User] = [
    {'name': 'Max', 'age': 15},
    {'name': 'Karina', 'age': 18},
    {'name': 'Makar', 'age': 16},
]

# try:
#     with open('users.json', 'w') as file:
#         json.dump(users, file)
# except Exception as e:
#     print(e)
#
# try:
#     with open('users.json', 'r') as file:
#         users: list[User] = json.load(file)
#         print(users)
# except Exception as e:
#     print(e)

# try:
#     with open('users.data', 'wb') as file:
#         pickle.dump(users, file)
# except Exception as e:
#     print(e)

# try:
#     with open('users.data', 'rb') as file:
#         users: list[User] = pickle.load(file)
#         print(users)
# except Exception as e:
#     print(e)
#


#####################################################
# pattern match
#####################################################


# any = input('enter any: ')
# match any:
#     case 'hi':
#         print('hello')
#
#     case 'no':
#         print('nope')
#
#     case _:
#         print('default')

# a = ['left', '20']
# # a = ['right', '200', '5555']
#
# match a:
#     case 'left' as k, '200' as value:
#         print('left1', k, value)
#     case 'right', value:
#         print('right1', value)
#     case a, w, d:
#         print('three', a, w, d)
#     case _:
#         print('default')

user = {'name': 'Max', 'age': 15}


class User:
    __match_args__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


user_class = User('Karina', 18)


# def matcher(source: User | dict):
#     if isinstance(source, dict):
#         print(source['name'], source['age'])
#     elif isinstance(source, User):
#         print(source.name, source.age)
#
# matcher(user)

def matcher(source:User | dict):
    match source:
        case User(name, age):
            print(name, age)
        case {'name': name, 'age': age}:
            print(name, age)


matcher(user_class)
