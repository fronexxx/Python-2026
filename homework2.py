from typing import Callable

# def notebook() -> tuple[Callable[[str], None], Callable[[], list[str]]]:
def notebook():
    todo_list: list[str] = []

    def add_todo(todo) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> list[str]:
        nonlocal todo_list
        return todo_list.copy()

    return add_todo, get_all


add, getAll = notebook()
add1, getAll1 = notebook()

add('homework')
add('go to home')
add1('some stuff')

# print(getAll())
# print(getAll1())

def expanded_form(num: int) -> str:
    st = str(num)
    length = len(st) - 1
    res = []
    for i, ch in enumerate(st):
        if ch != '0':
            res.append(ch + '0'*(length - i))
    return ' + '.join(res) + f' = {st}'


# print(expanded_form(20523))


def count_decor(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        func(*args, **kwargs)
        print(f'{count=}')
    return inner

@count_decor
def func1():
    print('func1')
@count_decor
def func2():
    print('func2')

func1()
func1()
func2()
func1()
func2()
func1()
func1()
func2()
func1()
