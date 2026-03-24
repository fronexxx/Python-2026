# class User:
#     __slots__ = ('name', 'age')
#     count = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def __str__(self):
#         # return  f'{self.name}, {self.age}'
#         return str(self.__dict__)
#
#     def __repr__(self):
#         return self.__str__()
#
# User.count = 880
# print(User.count)
#
# user = User('Max', 15)
# print(user)
# print(user.name)
# print(user.count)
#
# users = [user, User('Olha', 15)]
# print(users)
#
# print(user.get_name())
#
# user.age = 99
# # user.house = 55
# print(user)


# class User:
#     count = 0
#     def __init__(self, name, age):
#         self.__name = name
#         self._age = age
#
#     def get_name(self):
#         return self.__name


# user = User('Max', 16)
# # print(user.get_name())
# # print(user._age)
#
# # print(user._User__name)
# # print(User._User__count)

# user2 = User('Olha', 32)
# user = User('Max', 16)
# User.count = 88
# print(user.count)
# print(user2.count)

# class Tools:
#     def greeting(self):
#         print('Hello')
#
#     def go_to_home(self):
#         print('Welcome to home')
#
# class Car:
#     def start(self):
#         print('Welcome to car')
#
# class Parent(User, Tools, Car):
#     def __init__(self, name, age, status):
#         super().__init__(name, age)
#         self.status = status
#
#     def get_status(self):
#         return self.status
#
# parent = Parent('Oleh', 20, True)
# parent.go_to_home()
# parent.greeting()
# parent.start()
# print(parent.get_status())


# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     # name = property(fget=__get_name, fset=__set_name, fdel=__del_name)
#
# user = User('Max')
# print(user.name)
# user.name = 'Albina'
# print(user.name)
# del user.name
# print(user.name)
# user.set_name('Karina')
# user.del_name()
# print(user.get_name(1111))


###############################################
# Поліморфізм
###############################################

# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         # print('Area', end=': ')
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         # print('Perimeter', end=': ')
#         pass
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def area(self):
#         # super().area()
#         # print(self.a*self.b*self.c)
#         return self.a*self.b*self.c
#
#     def perimeter(self):
#         # super().perimeter()
#         # print(self.a+self.b+self.c)
#         return self.a+self.b+self.c
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         # super().area()
#         # print(self.a * self.b)
#         return self.a * self.b
#
#     def perimeter(self):
#         return self.a + self.b
#
# triangle = Triangle(4, 5, 6)
# triangle.area()
# triangle.perimeter()
#
# rectangle = Rectangle(3, 4)
# rectangle.area()
# rectangle.perimeter()
#
#
# shapes: list[Shape] = [
#     triangle,
#     rectangle,
#     Triangle(10, 45, 3)
# ]
#
# for shape in shapes:
#     print('-------------------------------------')
#     # shape.area()
#     # shape.perimeter()
#
#     print(shape.area())
#     print(shape.perimeter())
#
#
#     print('-------------------------------------')

#
# class User:
#     __count = 0
#
#     def __init__(self, name, age):
#         self.__name = name
#         self._age = age
#
#     @classmethod
#     def get_count(cls):
#         return cls.__count
#
#         # return User.__count
#
#     @staticmethod
#     def greeting():
#         print('Hello world')
#
# user = User('Max', 32)
#
# print(User.get_count())
#
# User.greeting()
# user.greeting()


###############################################
# Перегрузка методів
###############################################

# from typing import Self
# class User:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return str(self.__dict__)
#
#     def __repr__(self):
#         return self.__str__()
#
#     def __add__(self, other: Self):
#         return self.age + other.age
#
#     def __sub__(self, other: Self):
#         return self.age - other.age
#
#     def __len__(self):
#         return len(self.name)
#
#
#
# user = User('Max', 15)
# user1 = User('Olha', 35)
#
# print(user + user1)
# print(user - user1)
#
# print(len(user))


# class User:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not isinstance(cls.__instance, cls):
#             cls.__instance = super().__new__(cls)
#
#         return cls.__instance
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# user1 = User('name', 16)
#
# print(user1.name)
# print(user2.name)
# print(id(user1))
# print(id(user2))

# class User:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not isinstance(cls.__instance, cls):
#             cls.__instance = super().__new__(cls)
#
#         return cls.__instance
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#     def __call__(self, value):
#         self.age += value
#
# user1 = User('name', 16)
# user1(15)
# print(user1.age)

class Array:
    def __init__(self, *args):
        self.__arr = [*args]

    def __str__(self):
        return str(self.__arr)

    def __len__(self):
        return len(self.__arr)

    def __setitem__(self, key, value):
        self.__arr[key] = value

    def __getitem__(self, key):
        return self.__arr[key]

    def __delitem__(self, key):
        del self.__arr[key]

    def push(self, item):
        self.__arr.append(item)

    def map(self, cb):
        return Array(*[cb(item) for item in self.__arr])

    def filter(self, cb):
        return Array(*[item for item in self.__arr if cb(item)])

# arr = Array()
#
# arr.push(5)
# arr.push(10)
#
# arr[1] = 666
# print(arr)
#
# del arr[0]
# print(arr)

arr = Array(2, 3, 5, 1, 5, 6)


arr_map = arr.map(lambda x: x * 2)
print(arr_map)

arr_filter = arr.filter(lambda x: x < 5)
print(arr_filter)