# Decorator

import functools
from functools import wraps
from time import perf_counter


def dec(func):
    def inner():
        print('----------')
        func()
        print('----------')
    inner()


@dec
def ali():
    print('sian')


def dec2(func):
    def inner(*x, **y):
        if x == 0:
            return 'Warning!!!!'
        return func(*x, **y)
    return inner


@dec2
def sum_number(x, y):
    return x ** y


x = sum_number(0, 0)
print(x)


# ================================================================


def star(mark, count):
    def inner1(func):
        # wraps for show Doc string __doc__ and show __name__ of function
        @wraps(func)
        def inner2(*x, **y):
            print(mark * count)
            func(*x, **y)
            print(mark * count)
        return inner2
    return inner1


@star("#-#:", 20)
def print_str_name(name):
    """print a name star """
    print(name)


print_str_name('sina pirzadeh')


# ================================================================


# Exampels for Decorator

users = {"Class_S":
         {
             "sina": "1331",
             "amir": '4023'
         },
         "Class_A":
         {
             "gtr": "443",
             "ffgf": '4066823'
         },
         "Class_B":
         {
             "ggf": "54",
             "dssg": '7676'
         }
         }


def showPass(user, set_class):
    get_user = users[set_class][user]
    return get_user


print(showPass("sina", 'Class_S'))


# Exampels for Decorator - 2


def countTime(func):
    @functools.wraps(func)
    def inner(*x, **y):
        get_time = perf_counter()
        value = func(*x, **y)
        end_time = perf_counter()
        print(end_time - get_time)
        return value
    return inner


@countTime
def func11(number_for_count):
    for i in number_for_count:
        i += i
    print(i)


func11([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
       111, 9, 10, 222, 333, 444, 555, 666, 777, 888, 999, 10000, 1000, 2000, 3000, 400, 500, 6, 7, 8])
