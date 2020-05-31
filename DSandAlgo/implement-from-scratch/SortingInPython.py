# Sort builtin function
from functools import cmp_to_key

a = [(1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5), (6, 4), (6, 3)]
a.sort(key=lambda ele: (-ele[0], -ele[1]))
print(a)


# A comparison function is any callable that accept two arguments, compares them,
# and returns a negative number for less-than, zero for equality, or a positive number for greater-than.
# A key function is a callable that accepts one argument and returns another value to be used as the sort key.

def cmp(x, y):
    if x[0] == y[0]:
        if x[1] > y[1]: return -1
        return 1
    return y[0] - x[0]


a = [(1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5), (6, 4), (6, 3)]
a.sort(key=cmp_to_key(cmp))
print(a)
