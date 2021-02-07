import re
def find_num(word):
    return int(re.findall(r'[1-9]',word)[0])
def order(sentence):
  return sorted(sentence.split(),key=lambda x:find_num(x))

print(order("is2 Thi1s T4est 3a"))
# print('a'.)