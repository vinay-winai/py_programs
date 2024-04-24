import cProfile
import pstats
import numpy as np
from numba import njit
from collections import OrderedDict

@njit
def lseek(ls):
    for i in ls:
        if i == 8889999:
            print(i)
            break

def dseek(ds):
    for k in ds:
        if k == 8889999:
            print(k)
            break


if __name__ == '__main__':
    with cProfile.Profile() as pr:
        my_dictionary = {i:i for i in range(10_000_000)}
        # o_d = OrderedDict({i:i for i in range(10_000_000)})
        my_list = np.arange(10_000_000)
        # my_list = [i for i in range(100_000_000)]
        
        for i in range(2):
            lseek(my_list)
            dseek(my_dictionary)
            # dseek(o_d)
    results = pstats.Stats(pr)
    results.sort_stats(pstats.SortKey.TIME)
    results.print_stats(10)
    