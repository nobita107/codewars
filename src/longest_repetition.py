import re


def longest_repetition(chars):
    c = ''
    l = 0
    for s in re.finditer(r'((.)\2*)', chars):
        if len(s.group()) > l:
            c, l = s.groups()[0], len(s.group())
    return c, l


print(longest_repetition(r""))
