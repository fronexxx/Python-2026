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
# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Cinderella(Human):
#     __count = 0
#
#     def __init__(self, name, age, foot_size):
#         super().__init__(name, age)
#         self.foot_size = foot_size
#         Cinderella.__count += 1
#
#     def __str__(self):
#         return str(self.__dict__)
#
#     @classmethod
#     def get_count(cls):
#         print(cls.__count)
#
#
# class Prince(Human):
#     def __init__(self, name, age, shoe_size):
#         super().__init__(name, age)
#         self.shoe_size = shoe_size
#
#     def find_cinderella(self, cinderella_list: list[Cinderella]):
#         for cinderella in cinderella_list:
#             if cinderella.foot_size == self.shoe_size:
#                 print(cinderella)
#                 return
#
# cind_list:list[Cinderella] = [
#     Cinderella('Lola', 14, 36),
#     Cinderella('Leryn', 19, 35),
#     Cinderella('Nika', 18, 37),
#     Cinderella('Violetta', 22, 39),
#     Cinderella('Violetta', 22, 39),
# ]
# prince = Prince('Igor', 18, 35)
#
# prince.find_cinderella(cind_list)
# Cinderella.get_count()


# 1) Створити абстрактний клас Printable, який буде описувати абстрактний метод print()
#
# 2) Створити класи Book та Magazine, в кожного в конструкторі змінна name, та який наслідується від класу Printable
#
# 3) Створити клас Main, в якому буде:
#
# – змінна класу printable_list, яка буде зберігати книжки та журнали
#
# – метод add, за допомогою якого можна додавати екземпляри класів в список і робити перевірку, чи то, що передають, є класом Book або Magazine інакше ігнорувати додавання
#
# – метод show_all_magazines, який буде виводити всі журнали, викликаючи метод print абстрактного класу
#
# – метод show_all_books, який буде виводити всі книги, викликаючи метод print абстрактного класу

# Task-3

from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f'This is book: {self.name}')

class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f'This is magazine: {self.name}')

class Main:
    __printable_list: list[Printable] = []

    @classmethod
    def add(cls, item: Book | Magazine):
        if isinstance(item, (Book, Magazine)):
            cls.__printable_list.append(item)

    @classmethod
    def show_all_magazines(cls):
        for item in cls.__printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        for item in cls.__printable_list:
            if isinstance(item, Book):
                item.print()


Main.add(Book('Book1'))
Main.add(Magazine('Magazine1'))
Main.add(Book('Book2'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book3'))
Main.add(Magazine('Magazine3'))
Main.add(Book('Book4'))
Main.add(Magazine('Magazine4'))
Main.add(Book('Book5'))
Main.add(Magazine('Magazine5'))
Main.add('User')

Main.show_all_books()
print('-' * 40)
Main.show_all_magazines()
