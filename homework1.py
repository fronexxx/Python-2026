# Task-1
# st = 'as 23fdfdg544'
#
# print(', '.join((num for num in st if num.isdigit())))

# Task-2
# st = 'as 23fdfdg544'
#
# print(', '.join(''.join(ch if ch.isdigit() else ' ' for ch in st).split()))

# Task-3
# greeting = 'Hello, world'
#
# print(str([g for g in greeting]).upper())

# Task-4

# print([num**2 for num in  range(50) if num%2])


# Task-5
# def printer (list_):
#     for i in list_:
#         print(i)
#
# printer([1, 2, 4, 5, 6, 7, 8, 9, 9])

# Task-6
# def max_number(a, b, c):
#     print(max(a, b, c))
#     return max(a, b, c)
#
# max_number(33, 44, 6)

# Task-7
# def numbers(*args):
#     print(max(args))
#     return min(args)
#
# s = numbers(44, 3, 6, 22)
# print(s)

# Task-8
# def max_from_list(list_):
#     return max(list_)
#
# def min_from_list(list_):
#     return min(list_)

# Task-9
# def sum_list(list_):
#     return sum(list_)
#
#
# i = sum_list([2, 3, 5, 2, 5])
# print(i)

# Task-10
# def avg (list_):
#     return sum(list_)/len(list_)
#
#
# res = avg([2, 3, 2, 1, 5, 7, 1])
# print(int(res))

# list = [22, 3,5,2,8,2,-23, 8,23,5]
#
#   – знайти  мін. число
#
#   – видалити усі дублікати
#
#   – замінити кожне 4-те значення на ‘X’
#
# 2) вивести на екран пустий квадрат з “*”, сторона якого вказана як аргумент функції
#
# 3) вивести табличку множення за допомогою циклу while
#
# 4) переробити це завдання під меню
#


l1 = [22, 3,5,2,8,2,-23, 8,23,5]
# copy = l1.copy()
# print(min(copy))
def min_from_list(list_):
    print(min(list_))

def duplicate ():
    copy = l1.copy()
    print(list(set(copy)))
# duplicate()

def to_x():
    copy = l1.copy()
    print(['X' if not (i + 1)%4 else num for i, num in enumerate(copy)])
# to_x()

def square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*'*n)
        else: print('*' + ' '* (n - 2) + '*')
# square(5)

def multi_table():
    size = 9
    i = 1
    while i <= size:
        j = 1
        while j <= size:
            res = i * j
            # print(' ' if res//10 else '  ', end='')
            # print(res, end='')
            print(f'{res: 3}', end='')
            j += 1
        print()
        i+=1
#
# multi_table()


while True:
    print('1) знайти  мін. число')
    print('2) видалити усі дублікати')
    print('3) замінити кожне 4-те значення на X')
    print('4) вивести на екран пустий квадрат з “*”, сторона якого вказана як аргумент функції')
    print('5) вивести табличку множення за допомогою циклу while')
    print('9) Вихід')

    choice = input('Зробіть свій вибір: ')

    if choice == '1':
        min_from_list(l1)
    elif choice == '2':
        duplicate()
    elif choice == '3':
        to_x()
    elif choice == '4':
        square(7)
    elif choice == '5':
       multi_table()
    elif choice == '9':
        break

