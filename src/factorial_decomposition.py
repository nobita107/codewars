import math

from datetime import datetime

prime_facts = {}


def prime_factors(n):
    primes = {}
    count = 0
    global prime_facts
    while n % 2 == 0 and n > 1:
        count += 1
        n /= 2
        primes.update({2: count})
        if n in prime_facts.keys():
            # print('Got something 1')
            return dict_sum([primes, prime_facts.get(n)])

    for i in range(3, math.ceil(n ** 0.5) + 1, 2):
        count = 0
        while n % i == 0:
            count += 1
            n /= i
            primes.update({i: count})
            if n in prime_facts.keys():
                # print('Got something 2')
                return dict_sum([primes, prime_facts.get(n)])
        if n == 1:
            break
    if n != 1:
        primes.update({n: 1})
    return primes


def dict_sum(dicts):
    output = {}
    for d in dicts:
        for key, value in d.items():
            if key in output:
                output[key] += value
            else:
                output[key] = value
    return output


def decomp(n):
    primes = []
    for i in range(2, n + 1):
        p = prime_factors(i)
        primes.append(p)
        prime_facts.update({i: p})

    return ' * '.join([str(p[0]) +  '^' + str(p[1]) if p[1] > 1 else str(p[0]) for p in sorted(dict_sum(primes).items(),key=lambda x:x[0])])
    # return dict_sum(primes)


start = datetime.now()
for _ in range(10):
    decomp(4000)
end = datetime.now()
print(f'Time:{end-start}')

# print(decomp(5))
