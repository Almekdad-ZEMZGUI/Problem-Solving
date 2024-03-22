t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(ele) for ele in input().split()]
    count = 1
    for i in range(1, n):
        if arr[i] <= arr[i-1]:
            count += 1
        else:
            arr[i] = arr[i-1]
    print(count)
