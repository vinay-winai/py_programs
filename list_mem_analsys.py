# checking number of list contiguous memory discoutinuations and max chunk size
import array
from itertools import tee
from functools import reduce
import numpy as np

# arr = list(range(1, 1_000_001))
# arr = np.arange(1, 1_000_001)
arr = array.array('L', list(range(1,1_000_001)))
ids = [id(i) for i in arr]

discons = []
def make_contiguous_test():
    curr_chunk = 0

    def inner(acc, pair):
        nonlocal curr_chunk
        a, b = pair
        diff = b - a
        if diff == 32:
            curr_chunk+=1
            return acc + 1
        discons.append(curr_chunk)
        curr_chunk = 0
        return acc
    return inner

continuity_test = make_contiguous_test()

iter1, iter2 = tee(ids)
next(iter2, None)
pairs = zip(iter1, iter2)
result = reduce(continuity_test, pairs, 0)
print(f"Number of pairs with a difference of 32: {result}")
print(sorted(discons)[:20])
