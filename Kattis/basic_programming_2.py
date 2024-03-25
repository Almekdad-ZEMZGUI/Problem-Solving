n, t = [int(e) for e in input().split()]
arr = [int(e) for e in input().split()]
if t == 1:
    ex = False
    for i in range(1, 7777):
        if i in arr and 7777-i in arr:
            print('Yes')
            break
    else:
        print("No")
elif t == 2:
    if len(set(arr)) == n:
        print("Unique")
    else:
        print("Contains duplicate")
elif t == 3:
    dic = {}
    for num in arr:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
[I    for k, v in dic.items():
        if v > (n // 2):
            print(k)
            break
    else:
        print(-1)
elif t == 4:
    arr.sort()
    if len(arr) % 2 == 0:
        print(arr[(n // 2) - 1], arr[n // 2])
    else:
        print(arr[n // 2])
elif t == 5:
    arr.sort()
    [print(" ".join(str(num) for num in arr if 100 <= num <= 999))]
