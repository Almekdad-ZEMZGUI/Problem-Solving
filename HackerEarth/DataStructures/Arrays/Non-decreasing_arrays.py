t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(e) for e in input().split()]
    res = [arr[0]]
    for i in range(n-1):
        if res[i] <= arr[i+1]:
            res.append(arr[i + 1])
        else:
            k = res[i] / arr[i+1]
            new_k = int(k) if int(k) == k else int(k) + 1
            new_ai = arr[i+1] * new_k
            res.append(new_ai)
    print(" ".join(map(str,res)))

