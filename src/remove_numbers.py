import math
def remov_nb(n):
    ret = []
    for b in range(math.floor(n/(2**0.5)),n):
        a,div = divmod(n*(n+1)//2 - b, b+1)
        if div == 0:
            ret.extend([(a,b),(b,a)])
    return sorted(ret,key=lambda x:x[0])
