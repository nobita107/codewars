def sum_squared_divisors(n):
    sq_sum_squared_divisors = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            sq_sum_squared_divisors += i**2
            if i != n//i:
                sq_sum_squared_divisors += (n//i)**2
    # print(n,sq_sum_squared_divisors)
    return sq_sum_squared_divisors


def list_squared(m, n):
    ret = []
    for i in range(m, n + 1):
        s = sum_squared_divisors(i)
        if (s**0.5).is_integer():
            ret.append([i,s])
    return ret

print(list_squared(1, 250))
print(list_squared(42, 250))
print(list_squared(250, 500))
