arr = list(range(10000))
count = 0
mx = 0
prev=0
for idx,i in enumerate(arr[1:]):
    if id(i)-id(arr[idx])!=32:
        count+=1
        cidx = idx+1
        print(idx,id(i))
        mx = max(mx, cidx-prev)
        prev = cidx
print(count,mx)

import numpy as np
import sys
arr = np.array(list(range(10000000)), dtype=np.int32)
print(len(arr) == (sys.getsizeof(arr)-112)//4)

s = 64
arr = list(range(64))
while s<165:
    s+=1
    arr.append(s)
    print(sys.getsizeof(arr)-56)
    print(len(arr) == (sys.getsizeof(arr)-56)//8)
