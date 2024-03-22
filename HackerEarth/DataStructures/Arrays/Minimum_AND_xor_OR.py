t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(e) for e in input().split()]
    arr.sort()
    minn = (arr[0] & arr[1]) ^ (arr[0] | arr[1])
    for i in range(n-1):
        minn = min((arr[i] & arr[i + 1]) ^ (arr[i] | arr[i + 1]), minn)
    print(minn)
