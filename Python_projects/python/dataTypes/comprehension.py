_list = [i ** 2 for i in range(20)]
print(_list)

# ----------------------

_list2 = [i ** 2 for i in range(10) if i % 2 == 0]
print(_list2)


# ----------------------

names = ['sina', 'reza', 'amir', 'mamad']
_dict = {name: [0 for _ in range(len(names))] for name in names}
print(_dict)