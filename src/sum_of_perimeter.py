import operator
from functools import reduce
import numpy
from datetime import datetime


def perimeter(n):
    a = [1, 1]
    for i in range(2, n + 1):
        a.append(a[i - 1] + a[i - 2])
    # return 4*reduce(operator.add,a)


def perimeter2(n):
    a = [1, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        a[i] = a[i - 1] + a[i - 2]
        # a.append(a[i - 1] + a[i - 2])


def perimeter3(n):
    # print(numpy.ones(2))
    a = numpy.zeros(n + 1,dtype='int64')
    # print(a.dtype)

    a[0] = a[1] = 1
    for i in range(2, n + 1):
        a[i] = a[i - 1] + a[i - 2]
        # a.append(a[i - 1] + a[i - 2])


start = datetime.now()
for _ in range(1000):
    perimeter(1000)
print(f'Time:{datetime.now()-start}')
start = datetime.now()
for _ in range(1000):
    perimeter2(1000)
print(f'Time:{datetime.now()-start}')
start = datetime.now()
for _ in range(1000):
    perimeter3(1000)
print(f'Time:{datetime.now()-start}')
