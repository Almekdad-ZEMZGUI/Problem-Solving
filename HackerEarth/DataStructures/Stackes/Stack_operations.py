n, k = [int(e) for e in input().split()]
arr = [int(e) for e in input().split()]
 
if n == 1 and k % 2 == 0:
    print(max(arr))
elif n == 1 and k % 2 == 1:
    print(-1)
elif n < k:
    print(max(arr))
else:
    maxi = max(arr[:k-1])
    print(max(maxi, arr[k]))

