import math


def prime_factors(n):
    primes = {}
    count = 0
    while n % 2 == 0:
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
    return ''.join([f'({i}**{count})' if count > 1 else f'({i})'for i,count in sorted(primes.items(),key=lambda x:x[0])])

print(prime_factors(18))
# print('0'==0)