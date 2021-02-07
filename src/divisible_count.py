# def divisor(x,y,k):
    # s,e=x,y
    # mid = (x+y)//2
    # div, mod = divmod(mid,k)
    # if
def divisible_count(x,y,k):
    div, mod = divmod(x, k)
    start = div * k
    if start < x:
        start +=k
    return len(range(start,y,k))

print(divisible_count(20,20,2))