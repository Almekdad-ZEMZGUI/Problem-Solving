t = int(input())
for i in range(t):
    n, k = [int(e) for e in input().split()]
    arr = [int(e) for e in input().split()]
    if min(arr) >= k:
        print(0)
    else:
        print(k-min(arr))
