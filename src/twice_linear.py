# https://www.codewars.com/kata/5672682212c8ecf83e000050
def dbl_linear(n):
    x2_list = []
    x3_list = []
    x2_i = 0
    x3_i = 0
    u = [1]
    for i in range(1, n+1):
        x2_list.append(2*u[i-1]+1)
        x3_list.append(3*u[i-1]+1)
        u.append(min(x2_list[x2_i],x3_list[x3_i]))
        if u[i] == x2_list[x2_i]:
            x2_i += 1
        if u[i] == x3_list[x3_i]:
            x3_i += 1
    # print(u)
    return u[n]

# print(dbl_linear(20))

print(int('0'))