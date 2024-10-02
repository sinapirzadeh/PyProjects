# this is Walrus
print(word := 5)

# ---------------------
# example

x = []
while (s := input('Enter your name (q for quit) : ').lower()) != 'q':
    x.append(s)

print('Names : \n', x)

# ----------- end ------

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if (n := input('Enter You Number:') not in a or (l := len(a)) <= 20):
    a.append(n)

print(a)

# ----------- end ------


def func(x):
    print(x ** 2)


func(z := 12)
print(z)
