# https://www.codewars.com/kata/54da5a58ea159efa38000836
from itertools import groupby
def find_it(seq):
    seq_count = [num for num,group in groupby(sorted(seq)) if len(list(group))%2==1]
    return seq_count[0]

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
# test = unittest.TestCase()
# test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
# test.assert_equals(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1);
# test.assert_equals(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5);
# test.assert_equals(find_it([10]), 10);
# test.assert_equals(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10);
# test.assert_equals(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1);