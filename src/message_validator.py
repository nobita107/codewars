#https://www.codewars.com/kata/5fc7d2d2682ff3000e1a3fbc
import re
def is_valid_message(message):
    print(re.findall("(\d{1,})(\D*)",message))
    return all(n and int(n) == len(s) for n, s in re.findall("(\d{1,})(\D*)", message))
    # if len(message) == 0:
    #     return True
    # str_split = list(re.findall("(\d{1,})(\D*)",message))
    # print(str_split)
    # for i in range(len(str_split)):
    #     try:
    #         n = int(str_split[i])
    #     except:
    #         continue
    #     if i == len(str_split)-1:
    #         return False
    #     if n != len(str_split[i+1]):
    #         return False
    # return True
print(is_valid_message('4code13hellocodewars'))
print(is_valid_message('2hi2'))
print(is_valid_message('hello5'))