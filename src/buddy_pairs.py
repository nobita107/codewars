# https://www.codewars.com/kata/59ccf051dcc4050f7800008f
from datetime import datetime
import time
import cProfile

import math
from functools import reduce
from itertools import accumulate, product, groupby, chain
from operator import mul

class Buddy:
    least_primes = None
    def least_prime_factor(self,n):
        least_prime = [0]*(n+1)
        for i in range(2,n+1,2):
            least_prime[i] = 2
        for i in range(3,n+1,2):
            # print(i)
            if least_prime[i] == 0:
                for j in range (i,n + 1,i):
                    if least_prime[j] == 0:
                        least_prime[j] = i
        return least_prime
    def timeit(f):
        def timed(*args, **kw):
            start = time.time()
            result = f(*args, **kw)
            end = time.time()
            print(f'Timed:{end-start}')
            return result
        return timed
    # def primeFactors(n):
    #     ret = []
    #     i = 2
    #     nn = n
    #     while i <= math.sqrt(n):
    #         l = []
    #         # print(i)
    #         while nn % i == 0:
    #             l.append(i)
    #             nn //= i
    #         # i += 1 if i==2 else 2
    #         if i == 2:
    #             step = 1
    #         else:
    #             step = 2
    #         i += step
    #         # print(i)
    #         ret.append(l)
    #     if nn > 1:
    #         ret.append([nn])
    #     return ret

    def primeFactors(self,n):
        ret = []
        if n> len(self.least_primes):
            self.least_primes = self.least_prime_factor(n)
            print(f'Recalculating, n = {n}')
            #print(f'Out of range:{n}>{len(self.least_primes)}')
        l_prime = self.least_primes[n]
        # print(l_prime,n//l_prime if l_prime > 0 else 0)
        if l_prime == 0:
            return ret
        # elif l_prime == n:
        #     return [n]

        ret.append(l_prime)
        ret.extend(self.primeFactors(n//l_prime))
        return ret

    def prod(self,a, b):
        return [x * y for x, y in product(a, accumulate(chain([1], b), mul))]
    # def primeFactors(n):
    #     i = 2
    #     nn = n
    #     while i <= math.sqrt(n):
    #         while nn % i == 0:
    #             yield i
    #             nn //= i
    #         if i == 2:
    #             step = 1
    #         else:
    #             step = 2
    #         i += step
    #     if nn > 1:
    #         yield nn
    #

    def sum_divisors(self,n):
        return self.naive_sum_divisors(n)

        if n > len(self.least_primes):
            # print('Going to naive...')
            return self.naive_sum_divisors(n)
        s = sorted(reduce(self.prod, [list(y) for _, y in groupby(self.primeFactors(n))], [1])
                   )[:-1]
        return sum(s)
    def naive_sum_divisors(self,n):
        sum_ = 1
        # if n%2==0:
        #     sum_ += 2
        for i in range(2,math.ceil(math.sqrt(n)),1):
            if n%i==0:
                sum_ += (i+n//i)
        return sum_


    def buddy(self,start, limit):
        print(f'Finding buddy of {start}:{limit}')
        count=0
        for n in range(start, limit + 1):
            count+=1
            sum_divs_n = self.sum_divisors(n)
            m = sum_divs_n - 1
            if m > n:
                if self.sum_divisors(m) == n + 1:
                    return n, m
        return "Nothing"

    @timeit
    def test(self):
        print('Testing...')
        start = 1071625
        limit = 1103735
        # start = 57345
        # limit = 90061
        # self.least_primes = self.least_prime_factor(limit)
        print(self.buddy(start,limit))

        # print(self.primeFactors(62744))
        print(self.sum_divisors(62744))
        print(self.sum_divisors(75495))
        # for i in range(1071625,limit):
        #     self.primeFactors(i)

        # l = [y for y in primeFactors(i)]
# print(primeFactors(102))
b = Buddy()
b.test()
#
# limit = 1071625 + 100
# b.least_primes = b.least_prime_factor(limit)
# print(b.primeFactors(1071625))
# test()
# cProfile.run("")
start = datetime.now()
# print(buddy(1071625, 1103735))
# for i in range(10000):
#     primeFactors(1e7)
# end = datetime.now()
# print(f'Time1:{end-start}')
# start = datetime.now()
# print(buddy(1071625, 1103735))
#
#
# # for i in range(100000):
# #     primeFactors2(1e7)
# end = datetime.now()
# print(f'Time2:{end-start}')
# TestCase.assertEqual(buddy(10, 50), [48, 75])
# Test.assert_equals(buddy(2177, 4357), "Nothing")
# Test.assert_equals(buddy(57345, 90061), [62744, 75495])
# Test.assert_equals(buddy(1071625, 1103735), [1081184, 1331967])
