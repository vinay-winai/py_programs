arr = [i for i in range(10000)]
count = 0
mx,mn = 0,float('inf')
prev=0
for idx,i in enumerate(arr[1:]):
    if id(i)-id(arr[idx])!=32:
        count+=1
        cidx = idx+1
        print(idx,id(i))
        mx = max(mx, cidx-prev)
        mn = min(mn, cidx-prev)
        prev = cidx
print(count,mx,mn)