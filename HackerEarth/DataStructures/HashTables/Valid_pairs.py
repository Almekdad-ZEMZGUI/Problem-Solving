import math
n = int(input())
arr = [int(e) for e in input().split()]
count = 0
dic = {}
for ele in arr:
    if ele in dic:
        dic[ele] += 1
    else:
        dic[ele] = 1
for i in range(21):
    pwr = pow(3, i)
    for j in range(n):
        if pwr - arr[j] in dic:
            count += dic[arr[j]]
print(count // 2)
