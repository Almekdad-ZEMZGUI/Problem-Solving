t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(e) for e in input().split()]
 
    k = 2 ** (n - 1)
 
    res = 0
    for ele in arr:
        if ele >= k:
            res += ele
            res = res % (10 ** 9 + 7)
    print(res)
