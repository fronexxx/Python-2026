# print("Hello from Python")
#
# print(1, 2, 'HELLO', sep='-', end='')

# i = 1
# f = 1.3
# b = True
# s = 'text'
# n = None
#
# print(type(i))
# print(type(f))
# print(type(b))
# print(type(s))
# print(type(n))

# a = 7
# b = 2
# print(a**b)

# num = input('Enter number')
#
# print(num)

# res = isinstance('text', str)
# print(res)

# a = 2
# b = 4
#
# if a<b:
#     print('yes')
# elif a>b:
#     print('no')
# else:
#     print('else')

# f = True
#
# if not f and a>b or a==b:
#     print('some stuff')

# num = int(input('Enter a number:'))
# res = 'yes' if num>5 else 'no'
#
# print(res)

####################################################################
# list
####################################################################

# l = [1,2,3,4,5,6,7]
# print(l[0])
# print(l[-1])
# print(l[-3])

# l[3] = 5

# l2 = l.copy()
# l2[0] = 7777
# print(l)
# print(l2)

#
# l = [1,2,3,4,5,6]
# l.append(77)
# l.insert(1, 55)
# print(l)

# pop = l.pop()
# print(pop)
# l.remove(2)
# print(l)

# l1 = [7, 3, 4]
# l2 = [1, 2, 3, 4, 5, 6]
#
# # l1.extend(l2)
# # l3 = l1 + l2
#
# l1 += l2
# print(l1)

# l = [1, 2, 3, 2, 4, 5, 6]
#
# print(l.index(2, 2, 66))

# l = [1, 2, 3, 2, 4, 5, 6]
# l.reverse()
# l.sort()
# l.sort(reverse=True)
# print(l)
#
# print(l.count(4))
#
# l.clear()
# print(l)

# l = [1, 2, 3, 2, 4, 5, 6]
# # print(l[0:5:2])
# print(l[::-2])

##############################################################
# tuple
##############################################################

# my_tuple = (1, 2, 3)
# #
# # print(my_tuple)
# # print(my_tuple[1])
#
# new_list = list(my_tuple)
# new_list[1] = 4
# print(new_list)

##############################################################
# dictionary
##############################################################

# dictionary = {
#     'name': 'max',
#     True: 1,
#     False: 2
# }
#
# print(dictionary['name'])
# print(dictionary.get('name1', 'Karina'))
# dictionary.clear()
# dictionary.copy()

# keys = ['name', 'age', 'house']

# d = dict.fromkeys(keys, 1)
# print(d)

# print(dictionary.items())
# print(dictionary.keys())
# print(list(dictionary.values()))

# a = dictionary.pop('name')
# print(a)
# value = dictionary.popitem()
# print(dictionary)
#
# dictionary = {
#     'name':'max'
# }
#
# dictionary2 = {
#     'house':99
# }
#
#
# # dictionary['house']=55
# # # dictionary.setdefault('name', 55)
# # print(dictionary)
#
# # dictionary.update(dictionary2)
# # dictionary = dictionary|dictionary2
# dictionary |= dictionary2
# print(dictionary)


##############################################################
# SET
##############################################################

# l = [1, 2, 3, 1, 2, 4, 3, 4, 3, 2, 4, 2, 3, 2, 2, 3, 3, 6, 7]
# s = list(set(l))
# print(s)

# s = {}
# print(type(s))

# s = set()
# # print(type(s))
# s.add(5)
# s.add(3)
# s.add(6)
# s.add(6)
# s.add(5)
# s.add(3)
# print(s)

s1 = {6, 7, 8, 4, 1}
s2 = {1, 2, 3, 4}
# pop = s.pop()
# print(pop)
# print(s)

# print(s2.issuperset(s1))
# print(s1.issubset(s2))
# print(s1.isdisjoint(s2))
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))
# print(s1.update(s2))

# s1.remove(7)
# s1.discard(77)
# print(s1)


##############################################################
# Strings
##############################################################

# s = 'string'
# print(len(s))

# print('*' * 25)

name = 'Max'
age = 18
weight = 70.5

string = 'hlello my name is Max, I`m 18 y.o, and my weight is 70.5 kg'
# string = 'Hi my name is '+name+', I`m '+str(age)+' y.o, and my weight is '+str(weight)+' kg'
# string = 'Hi my name is %s, I`m %d y.o, and my weight is %f kg' % (name, age, weight)
# string = 'Hi my name is {}, I`m {} y.o, and my weight is {} kg'.format(name, age, weight)
# string = 'Hi my name is {name}, I`m {age} y.o, and my weight is {weight} kg and my friends name is also {name}'.format(age=age, name=name, weight=weight)
# string = f'Hi my name is {name}, I`m {age} y.o, and my weight is {weight} kg'
#
# print(string)

# print(string.index('ll'))
# print(string.find('lll'))
# print(string.count('l'))
# print(string.capitalize())
# print(string.upper())
# print(string.lower())
# print(string.startswith('h'))
# print(string.endswith('h'))

# print([' ssssssss   '.strip()])
# print([' ssssssss   '.lstrip()])
# print([' ssssssss   '.rstrip()])
# print(['aaa ssssssss  aaa '.strip('a ')])
#
# # print('heelo-world'.split('-'))
#
# print('hello is not good'.partition('not'))

# l1 = ['apple', 'car', 'join']
# print(', '.join(l1))

# print('hellloll'.replace('ll', 'lox'))
# string[::3]

# min(3, 4, 5, 6)
# min([3, 4, 5, 6])
#
# max()
# sum()

# print(sorted([4, 2, 5, 1, 7, 33, 11], reverse=True))

# print(pow(2, 25))
# print(2**25)


##############################################################
# Functions
##############################################################

# def fun(name2, age=4, *args, **kwargs):
#     print('hello', name2, age)
#     print(args)
#     print(kwargs)
#
# fun('Max', 455, 'Karina', 45, True, name_='Oleh', house=99)

# def func(a, b, c):
#     print(a, b, c)
#
# l = [5, 7, 2]
# func(*l)


##############################################################
# Loops
##############################################################

# i = 5
#
# while i > 0:
#     i -= 1
#     if i == 1:
#         continue
#     print(i)
# else:
#     print('finish')
#
# l1 = [1, 2, 3, 4, 5, 6]
#
# for i in range(2, 13, 2):
#     print(i)
# else:
#     print('end')


# d = {
#     'name':'max',
#     'house': 25
# }
#
# for k, v in d.items():
#     print(f'{k=}: {v=}')
# print(v)


##############################################################
# List comprehension
##############################################################

# l2 = [i for i in range(1, 101)]
# print(l2)

l2 = [4, 3, 4, 3, 2, 6]

# res = [i for i in l2 if i%2 == 0]
# res = [i*2 for i in l2]
# res = [i*2 for i in l2 if i%2 == 0]
# res = [i*2 if i%2 == 0 else i for i in l2]
# print(res)
#
# l2d = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10]
#
# ]
#
# # l = [i for j in l2d for i in j]
#
# l = []
# for i in l2d:
#     for j in i:
#         l.append(j)
#
# print(l)