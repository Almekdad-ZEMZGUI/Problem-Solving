t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(e) for e in input().split()]
    count = 0
    max_count = 0
    all_odd = True
    for i in range(n):
        if arr[i] % 2 == 0:
            count += 1
            all_odd = False
        else:
            max_count = max(max_count, count)
            count = 0
    if all_odd:
        print(-1)
    else:
        print(max(max_count, count))
