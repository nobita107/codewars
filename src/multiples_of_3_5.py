def solution(number):
  multi_3 = set(range(0,number,3))
  multi_5 = set(range(0,number,5))
  num_array = multi_3.union(multi_5)
  return sum(num_array)

print(solution(10))