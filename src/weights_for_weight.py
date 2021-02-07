from functools import cmp_to_key

def order_weight(strng):
    def comp(num1,num2):
        sum1 = sum([int(d) for d in num1])
        sum2 = sum([int(d) for d in num2])
        if sum1 == sum2:
            if str(num1) > str(num2):
                return 1
            else:
                return -1
        else:
            return sum1 - sum2
    return ' '.join(sorted(strng.split(), key=cmp_to_key(comp)))
def order_weight2(strng):
    def weight(num):
        return sum([int(d) for d in num]), strng
    return ' '.join(sorted(strng.split(), key=weight))

print(order_weight2("10003 1234000 44444444 9999 11 11 22 123 2000"))