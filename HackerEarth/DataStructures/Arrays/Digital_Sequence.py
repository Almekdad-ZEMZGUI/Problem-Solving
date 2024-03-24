n = int(input())
arr = [e for e in input().split()]
res = 0
for i in range(10):
    count = 0
    for ele in arr:
        if str(i) in ele:
            count += 1
    if count > res:
        res = count
print(res)

