n = int(input())
arr = [int(e) for e in input().split()]
arr.sort()
res = []
sec = [arr[0]]
for i in range(1, n):
    if arr[i] - 1 == arr[i-1]:
        sec.append(arr[i])
    else:
        res.append(sec)
        sec = [arr[i]]
res.append(sec)
res2 = ""
for ele in res:
    if len(ele) >= 3:
        res2 += str(ele[0]) + "-" + str(ele[-1]) + " "
    elif len(ele) == 2:
        res2 += str(ele[0]) + " " + str(ele[1]) + " "
    else:
        res2 += str(*ele) + " "
print(res2)
