import cProfile
import pstats
import numpy as np
from numba import njit
from collections import OrderedDict
from array import array

@njit
def dseek(ds):
    for i in ds:
        if i == 89_988_999:
            print(i)
            break
@njit
def lseek(ls):
    for i in ls:
        if i == 89_988_999:
            print(i)
            break

@njit
def dcalc(ds):
    sum = 0
    for k in ds:
        sum += k
    print(sum)

@njit
def lcalc(ls):
    sum = 0
    for k in ls:
        sum += k
    print(sum)

@njit
def dcreate():
    return {i:i for i in range(100_000_000)}

if __name__ == '__main__':
    with cProfile.Profile() as pr:
        # my_list = np.arange(100_000_000)
        # od = OrderedDict({i:i for i in range(10_000_000)})
        my_list = array('i', range(100_000_000))
        ds = dcreate()
        dcalc(ds)
        lcalc(my_list)
        for i in range(5):
            lseek(my_list)
            dseek(ds)
            # dseek(od)
    results = pstats.Stats(pr)
    results.sort_stats(pstats.SortKey.TIME)
    results.print_stats(12)
    
# Results 100M:

# Dict seek: ~ 300ms
# Dict sum: ~ 400ms
# Ordered Dict not supported by Numba.
# In normal mode it's around 10x slower than Dict .
# For 10mil and for 100mil it doesn't fit in my 16 GB system.

# Array seek: ~ 50ms
# Array sum: ~ 25ms
# Np Array seek: ~ 50ms
# Np Array sum: ~ 25ms
# Np Array 2x slower than Array plus sum overflow. (NoJit)