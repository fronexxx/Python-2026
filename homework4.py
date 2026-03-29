# Task 1
# try:
#     with open('email.txt') as source, open('gmail.txt', 'w') as target:
#         for line in source:
#             res = line.split()[-1]
#             if res.endswith('gmail.com'):
#                 # target.write(f'{res}\n')
#                 print(res, file=target)
# except Exception as e:
#     print(e)

# Task-2

import json
class Purchases:
    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__purchases = []
        self.__read_file()
        self.__id = self.__gen_id()

    def __show_all(self):
        for purchase in self.__purchases:
            print(f'{purchase['id']}) {purchase['name']} - {purchase['price']}')

    def __add(self):
        name = input('Name: ')

        while True:
            try:
                price = float(input('Enter price: '))
                break
            except ValueError:
                pass

        new_purchase = {'id': next(self.__id), 'name': name, 'price': price}
        self.__purchases.append(new_purchase)
        self.__write_file()

    def __write_file(self):
        try:
            with open(self.__file_name, 'w') as file:
                json.dump(self.__purchases, file)
        except Exception as e:
            print(e)

    def __read_file(self):
        try:
            with open(self.__file_name) as file:
                self.__purchases = json.load(file)
        except (Exception,):
            self.__write_file()

    def __gen_id(self):
        __id = self.__purchases[-1]['id']+1 if self.__purchases else 1
        yield __id
        __id += 1



purchases = Purchases('p1.json')
purchases.add()
