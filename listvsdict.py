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
@njit
def dseek(ds):
    for k in ds:
        if k == 8889999:
            print(k)
            break
@njit
def dcreate():
    return {i:i for i in range(10_000_000)}

if __name__ == '__main__':
    with cProfile.Profile() as pr:
        # my_list = np.arange(10_000_000)
        # od = OrderedDict({i:i for i in range(10_000_000)})
        ds = dcreate()

        for i in range(10):
            # lseek(my_list)
            dseek(ds)
            # dseek(od)
    results = pstats.Stats(pr)
    results.sort_stats(pstats.SortKey.TIME)
    results.print_stats(10)
    