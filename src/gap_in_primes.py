import math


def is_prime(n):
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3, math.ceil(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
def gap(g, m, n):
    # g is odd?
    if g%2 and is_prime(2+g):
        return [2,2+g]
    # g is even
    for i in range(m-m%2+1,n+n%2-g,2):
        print(i)
        if is_prime(i) and is_prime(i+g):
            if all([not is_prime(j) for j in range(i+2,i+g)]):
                return [i,i+g]
    return None

print(gap(6,100,110))