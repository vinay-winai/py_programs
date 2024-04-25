# checking number of list contiguous memory discoutinuations and max chunk size
import array
arr = list(range(1,1_000_001))
arr = array.array('L', arr)
count = 0
mx = 0
prev=0
for idx,i in enumerate(arr[1:]):
    if id(i)-id(arr[idx])!=32:
        count+=1
        cidx = idx+1
        # print(idx,id(i))
        mx = max(mx, cidx-prev)
        prev = cidx
print(count,mx)

# proving numpy stores values rather than references
# import numpy as np
# import sys
# arr = np.array(list(range(1_000_000)), dtype=np.int32)
# print(len(arr) == (sys.getsizeof(arr)-112)//4)

# # showing lists store obj references and dynamic capacity increase
# s = 64
# arr = list(range(64))
# while s<165:
#     s+=1
#     arr.append(s)
#     print(sys.getsizeof(arr)-56)
#     print(len(arr) == (sys.getsizeof(arr)-56)//8)
