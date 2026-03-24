# Task-1
# from typing import Self
#
# class Rectangle:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.area = self.x * self.y
#
#     def __add__(self, other: Self):
#         return self.area + other.area
#
#     def __sub__(self, other:Self):
#         return self.area - other.area
#
#     def __eq__(self, other: Self):
#         return self.area == other.area
#
#     def __ne__(self, other):
#         return self.area != other.area
#
#     def __lt__(self, other: Self):
#         return self.area < other.area
#
#     def __gt__(self, other: Self):
#         return self.area > other.area
#
#     def __len__(self):
#         return (self.x + self.y) * 2


# Task-2
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    __count = 0

    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size
        Cinderella.__count += 1

    def __str__(self):
        return str(self.__dict__)

    @classmethod
    def get_count(cls):
        print(cls.__count)


class Prince(Human):
    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size

    def find_cinderella(self, cinderella_list: list[Cinderella]):
        for cinderella in cinderella_list:
            if cinderella.foot_size == self.shoe_size:
                print(cinderella)
                return

cind_list:list[Cinderella] = [
    Cinderella('Lola', 14, 36),
    Cinderella('Leryn', 19, 35),
    Cinderella('Nika', 18, 37),
    Cinderella('Violetta', 22, 39),
    Cinderella('Violetta', 22, 39),
]
prince = Prince('Igor', 18, 35)

prince.find_cinderella(cind_list)
Cinderella.get_count()
