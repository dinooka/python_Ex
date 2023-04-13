def f():
    return 1
    return 2
    return 3

x = f()
# print(x)

def h():
    yield 11
    yield 22
    yield 33

# t = h()
# print(type(t))
# for i in h():
#     print(i)

# print lowercase letters
import string

def letters():
    for i in string.ascii_lowercase:
        yield i

# for i in letters():
#     print(i,end=' ')

# print prime numbers

def prime():
    for i in range(2,101):
        for r in range(1,101):
            if (i % r == 0):
                pass
            else:
                yield i

for i in prime():
    print(i,end=' ')











