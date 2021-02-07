import math
from itertools import product


def prime_factors(n):
    primes = {}
    count = 0

    while n % 2 == 0 and n > 1:
        count += 1
        n /= 2
    if count > 0:
        primes.update({2: count})

    for i in range(3, math.ceil(n ** 0.5) + 1, 2):
        count = 0
        while n % i == 0:
            count += 1
            n /= i
        if count > 0:
            primes.update({i: count})
        if n == 1:
            break
    if n != 1:
        primes.update({n: 1})
    return primes


def count_Kprimes(k, start, end):
    return [x for x in range(start, end + 1) if k == sum(prime_factors(x).values())]


def puzzle(s):
    def prime_list(k):
        return set([x[0] for x in prime_count if x[1] == k])
    prime_count = [(x, sum(prime_factors(x).values())) for x in range(2, s - 3)]
    prime_sum = [1,3,7]
    prime_set = sorted([prime_list(k) for k in prime_sum], key= lambda l: len(l))
    ret = [(a,b) for a,b in product(prime_set[0],prime_set[1]) if s-a-b in prime_set[2]]
    return len(ret)

print(puzzle(490))

# count_Kprimes(2, 0, 100)
# count_Kprimes(3, 0, 100)
# , [8, 12, 18, 20, 27, 28, 30, 42, 44, 45, 50, 52, 63, 66, 68, 70, 75, 76, 78, 92, 98, 99])
# count_Kprimes(5, 1000, 1100)
# , [1020, 1026, 1032, 1044, 1050, 1053, 1064, 1072, 1092, 1100])
# count_Kprimes(5, 500, 600)
# , [500, 520, 552, 567, 588, 592, 594])

print