# iterate


# Iteration -> for, while


# iterable


# iterator


print("__iter__" in dir([1, 2, 3, 4, 5]))

li = [1, 2, 3, 4, 5]
li = iter(li)
print(next(li))
print(next(li))
print(next(li))
print(next(li))
print(next(li))

print("__iter__" in dir([1, 2, 3, 4, 5]))
