def func(x):
    yield x*x
    x += x*x
    yield x*x
    x += x*x
    yield x*x
    x += x*x
    yield x*x


value = func(2)
print(next(value))
print(next(value))
print(next(value))
print(next(value))


# example 1

def func2(range_number):
    for i in range(range_number):
        yield i*1


set_number = 30
value2 = func2(set_number)
for i in range(set_number):
    print(next(value2))


# example for Generator

_list = [12, 22, 35, 47, 5, 76, 72]

for i, j in enumerate(_list):
    print(f'index:{i} value:{j}')

# to Generator


def my_enumerate(list, start=0):
    c = start
    for i in list:
        yield c, i
        c += i


for i, j in my_enumerate(_list):
    print(f"gen index: {i}, gen_nunmber: {j}")


# ___________exam 2 -------------------

def gen_fibonachy():
    f1 = 0
    f2 = 1
    while True:
        f3 = f1 + f2
        yield f3
        f1 = f2
        f2 = f3


febo = gen_fibonachy()
for _ in range(30):
    print(next(febo))


# ___________exam 3 -------------------
print("-"*30)

_llist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def count_list(li):
    for i in li:
        f1 = li[i]
        f2 = i + f1
        yield f2


count = count_list(_llist)
for _ in range(len(_llist)-1):
    print(next(count))


# ==========================
# ==========================
# ==========================
# ==========================
# ==========================
print('---===--' * 20)
# coroutine in Generator


def show_name():
    while True:
        name = yield
        print(f'you name is : {name}')


g = show_name()
next(g)
g.send('reza')
g.send('amir')
g.send('sina')
g.send('ali')
g.send('jafar')


# examp for coroutine

def cen_gen(words):
    print('start !')
    w = None
    while True:
        word = yield w
        w = word if word not in words else '*' * len(word)


gen = cen_gen(['badddd', 'you', 'ali'])

next(gen)
print(gen.send('you'))
print(gen.send('reza'))
print(gen.send('badddd'))
print(gen.send('reza'))
print(gen.send('ali'))
print(gen.send('reza'))
